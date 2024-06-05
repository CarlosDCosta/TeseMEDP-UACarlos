#Author- Carlos Costa
#Description- Criação de CAM de FFF (original obtido do Fusion alterado para os objetivos da dissertação)

import adsk.core, adsk.fusion, adsk.cam, traceback, tempfile, time

app = adsk.core.Application.get()
ui  = app.userInterface

def run(context):
    try:
        # Make sure the TEXT COMMAND palette is visible.
        textPalette = ui.palettes.itemById('TextCommands')
        if not textPalette.isVisible:
            textPalette.isVisible = True
            adsk.doEvents()

        doc = app.activeDocument
        products = doc.products

        # Make
        camWS = ui.workspaces.itemById('CAMEnvironment') 
        camWS.activate()
        cam = adsk.cam.CAM.cast(products.itemByProductType("CAMProductType"))

        # Design creation
        designWS = ui.workspaces.itemById('FusionSolidEnvironment') 
        designWS.activate()
        design = adsk.fusion.Design.cast(products.itemByProductType("DesignProductType"))
        camWS.activate()

        showMessage('=============================================')
        showMessage('Creating Manufacturing Model...')
        manufacturingModels = cam.manufacturingModels
        mmInput = manufacturingModels.createInput()
        mmInput.name = "Modelo de Fabrico - CE2 - FFF"
        manufacturingModel = manufacturingModels.add(mmInput)

        showMessage('Getting occurrences...')
        occs = getValidOccurrences(manufacturingModel.occurrence)
        if len(occs) == 0:
            ui.messageBox('No component has been added to the scene.')
            return 

        showMessage('Creating arrange operation...')
        setup = createAdditiveSetup(occs, cam)

        # Define and create the arrange operation.
        operationInput = setup.operations.createInput('additive_arrange')
        arrange = setup.operations.add(operationInput)

        parameter: adsk.cam.StringParameterValue = arrange.parameters.itemByName("arrange_arrangement_type").value
        parameter.value = 'Pack2D'

        # Specify the values to control the arrangement. All length units are centimeters.
        parameter: adsk.cam.FloatParameterValue = arrange.parameters.itemByName("arrange_platform_clearance").value
        parameter.value = 0
        
        parameter: adsk.cam.FloatParameterValue = arrange.parameters.itemByName("arrange_frame_width").value
        parameter.value = 0.5
        
        parameter: adsk.cam.FloatParameterValue = arrange.parameters.itemByName("arrange_ceiling_clearance").value
        parameter.value = 0.5              

        parameter: adsk.cam.FloatParameterValue = arrange.parameters.itemByName("arrange_object_spacing").value
        parameter.value = 1

        future = cam.generateToolpath(arrange)
        while (future.isGenerationCompleted == False):
            time.sleep(0.5)

        # Create the automatic orientation operations for each occurrence.
        for occ in occs:
            showMessage(f'Defining orientation for occurrence "{occ.name}" ...')
            operationInput = setup.operations.createInput('automatic_orientation')
            operationInput.isAutoCalculating = False
            orientationTarget = operationInput.parameters.itemByName('optimizeOrientationTarget')
            orientationTarget.value.value = [occ]
            operationInput.displayName = 'Automatic Orientation: ' + occ.name
            #global orientation
            orientation = setup.operations.add(operationInput)

            parameter: adsk.cam.FloatParameterValue = orientation.parameters.itemByName("optimizeOrientationSmallestRotation").value
            parameter.value = 180 #angle units are always degrees
        
            parameter: adsk.cam.BooleanParameterValue = orientation.parameters.itemByName("optimizeOrientationUsePreciseCalculation").value
            parameter.value = True #capitilize
            
            parameter: adsk.cam.FloatParameterValue = orientation.parameters.itemByName("optimizeOrientationCriticalAngle").value
            parameter.value = 45 #angle units are always degrees
            
            parameter: adsk.cam.FloatParameterValue = orientation.parameters.itemByName("optimizeOrientationDistanceToPlatform").value
            parameter.value = 0 #units are always cm
            
            parameter: adsk.cam.BooleanParameterValue = orientation.parameters.itemByName("optimizeOrientationMoveToCenter").value
            parameter.value = True #capitilize
            
            parameter: adsk.cam.FloatParameterValue = orientation.parameters.itemByName("optimizeOrientationFrameWidth").value
            parameter.value = 0.5 #units are always cm
            
            parameter: adsk.cam.FloatParameterValue = orientation.parameters.itemByName("optimizeOrientationCeilingClearance").value
            parameter.value = 0.5 #units are always cm
            
            parameter: adsk.cam.ChoiceParameterValue = orientation.parameters.itemByName("optimizeOrientationRankingSupportVolume").value
            parameter.value = '10' #take the number from dialog with its quotes

            parameter: adsk.cam.ChoiceParameterValue = orientation.parameters.itemByName("optimizeOrientationRankingSupportArea").value
            parameter.value = '0' #take the number from dialog with its quotes
            
            parameter: adsk.cam.ChoiceParameterValue = orientation.parameters.itemByName("optimizeOrientationRankingBoundingBoxVolume").value
            parameter.value = '2' #take the number from dialog with its quotes

            parameter: adsk.cam.ChoiceParameterValue = orientation.parameters.itemByName("optimizeOrientationRankingPartHeight").value
            parameter.value = '6' #take the number from dialog with its quotes

            parameter: adsk.cam.ChoiceParameterValue = orientation.parameters.itemByName("optimizeOrientationRankingCOGHeight").value
            parameter.value = '6' #take the number from dialog with its quotes

            showMessage('Generating orientation...')
            future = cam.generateToolpath(orientation)
            while (future.isGenerationCompleted == False):
                time.sleep(0.5)

            generatedResults = orientation.generatedDataCollection
            castPref = None
            firstResult = None
            primary = generatedResults.itemByIdentifier(adsk.cam.GeneratedDataType.OptimizedOrientationGeneratedDataType)

            if isinstance(primary, adsk.cam.OptimizedOrientationResults):
                castPref: adsk.cam.OptimizedOrientationResults = primary
                firstResult = castPref.item(0)

            castPref.currentOrientationResult = firstResult

        showMessage('Generating arrange...')
        future = cam.generateToolpath(arrange)
        while (future.isGenerationCompleted == False):
            time.sleep(0.5)
            
        showMessage('Generating supports...')
        supportInput1 = setup.operations.createInput('solid_bar_support')  # Change operation type to solid bar support
        solidBarSupport = setup.operations.add(supportInput1)
        supportParam1 = solidBarSupport.parameters.itemByName('supportTarget')
        supportParam1.value.value = occs
        future1 = cam.generateToolpath(solidBarSupport)
        while (future1.isGenerationCompleted == False):
            time.sleep(0.5)

        if solidBarSupport.hasError:
            solidBarSupport.deleteMe()
            
            showMessage('Generating supports...')
            supportInput2 = setup.operations.createInput('solid_volume_support')
            volumeSupport = setup.operations.add(supportInput2)
            supportParam2 = volumeSupport.parameters.itemByName('supportTarget')
            supportParam2.value.value = occs
            future2 = cam.generateToolpath(volumeSupport)
            while (future2.isGenerationCompleted == False):
                time.sleep(0.5)

            if volumeSupport.hasError:
                volumeSupport.deleteMe()

        showMessage('Generating toolpath...')
        toolpath = None
        i = 0
        for i in range(setup.operations.count):
            op = setup.operations.item(i)
            if (op.strategy == 'additive_buildstyle'):
                toolpath = op
                break
        if (toolpath == None): 
            return

        future = cam.generateToolpath(toolpath)
        while (future.isGenerationCompleted == False):
           time.sleep(1.0)

        app.activeViewport.fit()

        # Start the toolpath simulation command.
        app.executeTextCommand('NaNeuCAMUI.AdditiveSimulateCmd')  

        showMessage('Finished.')
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
        adsk.terminate()


# Create an additive setup.
def createAdditiveSetup(models: list[adsk.fusion.Occurrence], cam: adsk.cam.CAM):
    setups = cam.setups
    input = setups.createInput(adsk.cam.OperationTypes.AdditiveOperation)
    input.models = models
    input.name = 'AdditiveSetup'

    camManager = adsk.cam.CAMManager.get()
    libraryManager = camManager.libraryManager
    printSettingLibrary = libraryManager.printSettingLibrary
    machineLibrary = libraryManager.machineLibrary
    printSetting = None
    machine = None
    if True:
        # URL-structure browsing
        printSettingUrl = printSettingLibrary.urlByLocation(adsk.cam.LibraryLocations.Fusion360LibraryLocation) ## .Fusion360LibraryLocation (Settings from Fusion) vs .LocalLibraryLocation (Custom Settings)
        printSettings = printSettingLibrary.childPrintSettings(printSettingUrl)

        machineUrl = machineLibrary.urlByLocation(adsk.cam.LibraryLocations.Fusion360LibraryLocation) 
        machines = machineLibrary.childMachines(machineUrl)
        for ps in printSettings:
            if ps.name ==  "ABS (Direct Drive)": #print setting name from fusions library alter to the 
                printSetting = ps
                break
            
#Selecção da máquina
        for machine in machines: #model name from fusions library -- Example: "Generic FFF Machine"
            if machine.model ==  "CR-10":
                machine = machine
                break
    input.machine = machine
    input.printSetting= printSetting
    setup = setups.add(input)
    return setup


# Given an occurrence, this finds all child occurrences that contain either a
# B-Rep or Mesh body. It is recursive, so it will find all occurrences at all levels.
def getValidOccurrences(occurrence: adsk.fusion.Occurrence) -> list[adsk.fusion.Occurrence]:
    result = []
    for childOcc in occurrence.childOccurrences:
        if (childOcc.bRepBodies.count + childOcc.component.meshBodies.count  > 0):
            result.append(childOcc)

        result.extend(getValidOccurrences(childOcc))

    return result


def showMessage(message):
    app.log(message)

    # Give control back to Fusion, so it can update the UI.
    adsk.doEvents()