import adsk.core, adsk.fusion, adsk.drawing
import os
from ...lib import fusion360utils as futil
from ... import config
app = adsk.core.Application.get()
ui = app.userInterface
#Design e Parâmetros
design = adsk.fusion.Design.cast(app.activeProduct)
userParams = design.userParameters


# TODO *** Specify the command identity information. ***
CMD_ID = f'{config.COMPANY_NAME}_{config.ADDIN_NAME}_cmdDialog'
CMD_NAME = 'Personaliza as dimensões e padrão do vaso'
CMD_Description = 'A Fusion 360 Add-in Command with a dialog'

# Specify that the command will be promoted to the panel.
IS_PROMOTED = True

# TODO *** Define the location where the command button will be created. ***
# This is done by specifying the workspace, the tab, and the panel, and the 
# command it will be inserted beside. Not providing the command to position it
# will insert it at the end.
WORKSPACE_ID = 'FusionSolidEnvironment'
PANEL_ID = 'SolidScriptsAddinsPanel'
COMMAND_BESIDE_ID = 'ScriptsManagerCommand'

# Resource location for command icons, here we assume a sub folder in this directory named "resources".
ICON_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', '')

# Local list of event handlers used to maintain a reference so
# they are not released and garbage collected.
local_handlers = []


#Pârametros de Utilizador
DiaBaseParam = design.userParameters.itemByName('Diametro_Base')
DiaPriParam = design.userParameters.itemByName('Diametro_Intermedio1')
DiaSegParam = design.userParameters.itemByName('Diametro_Intermedio2')
DiaTerParam = design.userParameters.itemByName('Diametro_Intermedio3')
DiaTopoParam = design.userParameters.itemByName('Diametro_Topo')

AltBaseParam = design.userParameters.itemByName('Altura_Base')
AltPriParam = design.userParameters.itemByName('Altura_Intermedia1')
AltSegParam = design.userParameters.itemByName('Altura_Intermedia2')
AltTerParam = design.userParameters.itemByName('Altura_Intermedia3')
AltTopoParam = design.userParameters.itemByName('Altura_Topo')

DispBaseParam = design.userParameters.itemByName('Dispersao_Base')
DispPriParam = design.userParameters.itemByName('Dispersao_Intermedia1')
DispSegParam = design.userParameters.itemByName('Dispersao_Intermedia2')
DispTerParam = design.userParameters.itemByName('Dispersao_Intermedia3')
DispTopoParam = design.userParameters.itemByName('Dispersao_Topo')

# Executed when add-in is run.
def start():
    # Create a command Definition.
    cmd_def = ui.commandDefinitions.addButtonDefinition(CMD_ID, CMD_NAME, CMD_Description, ICON_FOLDER)

    # Define an event handler for the command created event. It will be called when the button is clicked.
    futil.add_handler(cmd_def.commandCreated, command_created)

    # ******** Add a button into the UI so the user can run the command. ********
    # Get the target workspace the button will be created in.
    workspace = ui.workspaces.itemById(WORKSPACE_ID)

    # Get the panel the button will be created in.
    panel = workspace.toolbarPanels.itemById(PANEL_ID)

    # Create the button command control in the UI after the specified existing command.
    control = panel.controls.addCommand(cmd_def, COMMAND_BESIDE_ID, False)

    # Specify if the command is promoted to the main toolbar. 
    control.isPromoted = IS_PROMOTED


# Executed when add-in is stopped.
def stop():
    # Get the various UI elements for this command
    workspace = ui.workspaces.itemById(WORKSPACE_ID)
    panel = workspace.toolbarPanels.itemById(PANEL_ID)
    command_control = panel.controls.itemById(CMD_ID)
    command_definition = ui.commandDefinitions.itemById(CMD_ID)

    # Delete the button command control
    if command_control:
        command_control.deleteMe()

    # Delete the command definition
    if command_definition:
        command_definition.deleteMe()


# Function that is called when a user clicks the corresponding button in the UI.
# This defines the contents of the command dialog and connects to the command related events.
def command_created(args: adsk.core.CommandCreatedEventArgs):
    # General logging for debug.
    futil.log(f'{CMD_NAME} Command Created Event')

    # https://help.autodesk.com/view/fusion360/ENU/?contextId=CommandInputs
    inputs = args.command.commandInputs

    # TODO Define the dialog for your command by adding different inputs to the command.

    # Create a simple text box input.
    #inputs.addTextBoxCommandInput('text_box', 'Some Text', 'Enter some text.', 1, False)

    # Create a value input field and set the default using 1 unit of the default length unit.
    defaultLengthUnits = app.activeProduct.unitsManager.defaultLengthUnits
    default_value = adsk.core.ValueInput.createByString('1')
    #inputs.addValueInput('value_input', 'Some Value', defaultLengthUnits, default_value)

    # Criar Input para mostar os valores atuais
    inputs.addTextBoxCommandInput('text_box', 'Diâmetro da Base Anterior', DiaBaseParam.expression, 1, True)
    inputs.addTextBoxCommandInput('text_box2', 'Diâmetro da Base-Centro Anterior', DiaPriParam.expression, 1, True)
    inputs.addTextBoxCommandInput('text_box3', 'Diametro do Centro  Anterior', DiaSegParam.expression, 1, True)
    inputs.addTextBoxCommandInput('text_box4', 'Diâmetro do Centro-Topo Anterior', DiaTerParam.expression, 1, True)
    inputs.addTextBoxCommandInput('text_box5', 'Diâmetro do Topo Anterior', DiaTopoParam.expression, 1, True)

    inputs.addTextBoxCommandInput('text_box6', 'Altura da Base Anterior', AltBaseParam.expression, 1, True)
    inputs.addTextBoxCommandInput('text_box7', 'Altura da Base-Centro Anterior', AltPriParam.expression, 1, True)
    inputs.addTextBoxCommandInput('text_box8', 'Altura do Centro Anterior', AltSegParam.expression, 1, True)
    inputs.addTextBoxCommandInput('text_box9', 'Altura do Centro-Topo Anterior', AltTerParam.expression, 1, True)
    inputs.addTextBoxCommandInput('text_box10', 'Altura do Topo Anterior', AltTopoParam.expression, 1, True)
    
    inputs.addTextBoxCommandInput('text_box11', 'Dispersão da Base Anterior', DispBaseParam.expression, 1, True)
    inputs.addTextBoxCommandInput('text_box12', 'Dispersão da Base-Centro Anterior', DispPriParam.expression, 1, True)
    inputs.addTextBoxCommandInput('text_box13', 'Dispersão do Centro Anterior', DispSegParam.expression, 1, True)
    inputs.addTextBoxCommandInput('text_box14', 'Dispersão do Centro-Topo Anterior', DispTerParam.expression, 1, True)
    inputs.addTextBoxCommandInput('text_box15', 'Dispersão do Topo Anterior', DispTopoParam.expression, 1, True)

    #Criar Input Slider
    DiaBaseSlider = inputs.addFloatSliderCommandInput('slider_diametro_base', 'Slider para diâmetro da base', 'mm', 5,40,False)
    DiaBaseSlider.valueOne = DiaBaseParam.value
    DiaPriSlider = inputs.addFloatSliderCommandInput('slider_primeiro_diametro', 'Slider para o diâmetro da base-centro','mm', 5, 40, False)
    DiaPriSlider.valueOne = DiaPriParam.value
    DiaSegSlider = inputs.addFloatSliderCommandInput('slider_segundo_diametro', 'Slider para o diâmetro do centro', 'mm', 5, 40, False)
    DiaSegSlider.valueOne = DiaSegParam.value
    DiaTerSlider = inputs.addFloatSliderCommandInput('slider_terceiro_diametro', 'Slider para o diâmetro do centro-topo', 'mm', 5, 40, False)
    DiaTerSlider.valueOne = DiaTerParam.value
    DiaTopoSlider = inputs.addFloatSliderCommandInput('slider_diametro_topo', 'Slider para diâmetro do topo', 'mm', 5, 40, False)
    DiaTopoSlider.valueOne = DiaTopoParam.value



    AltBaseSlider = inputs.addFloatSliderCommandInput('slider_altura_base', 'Slider para a altura da base', 'mm', 0,100,False)
    AltBaseSlider.valueOne = AltBaseParam.value
    AltPriSlider = inputs.addFloatSliderCommandInput('slider_primeira_altura', 'Slider para a altura da base-centro','mm', 0, 100, False)
    AltPriSlider.valueOne = AltPriParam.value
    AltSegSlider = inputs.addFloatSliderCommandInput('slider_segunda_altura', 'Slider para a altura do centro', 'mm', 0, 100, False)
    AltSegSlider.valueOne = AltSegParam.value
    AltTerSlider = inputs.addFloatSliderCommandInput('slider_terceira_altura', 'Slider para a altura do centro-topo', 'mm', 0, 100, False)
    AltTerSlider.valueOne = AltTerParam.value
    AltTopoSlider = inputs.addFloatSliderCommandInput('slider_altura_topo', 'Slider para a altura do topo', 'mm', 0, 100, False)
    AltTopoSlider.valueOne = AltTopoParam.value

    DispBaseSlider = inputs.addFloatSliderCommandInput('slider_dispersao_base', 'Slider para a dispersão da base', 'mm', 14,39, False)
    DispBaseSlider.valueOne = DispBaseParam.value
    DispPriSlider = inputs.addFloatSliderCommandInput('slider_primeira_dispersao', 'Slider para a dispersão da base-centro','mm', 14, 39, False)
    DispPriSlider.valueOne = DispPriParam.value
    DispSegSlider = inputs.addFloatSliderCommandInput('slider_segunda_dispersao', 'Slider para a dispersão do centro', 'mm', 14, 39, False)
    DispSegSlider.valueOne = DispSegParam.value
    DispTerSlider = inputs.addFloatSliderCommandInput('slider_terceira_dispersao', 'Slider para a dispersão do centro-topo', 'mm', 14, 39, False)
    DispTerSlider.valueOne = DispTerParam.value
    DispTopoSlider = inputs.addFloatSliderCommandInput('slider_dispersao_topo', 'Slider para a dispersão do topo', 'mm', 14, 39, False)
    DispTopoSlider.valueOne = DispTopoParam.value



    # TODO Connect to the events that are needed by this command.
    futil.add_handler(args.command.execute, command_execute, local_handlers=local_handlers)
    futil.add_handler(args.command.inputChanged, command_input_changed, local_handlers=local_handlers)
    futil.add_handler(args.command.executePreview, command_preview, local_handlers=local_handlers)
    futil.add_handler(args.command.validateInputs, command_validate_input, local_handlers=local_handlers)
    futil.add_handler(args.command.destroy, command_destroy, local_handlers=local_handlers)


# This event handler is called when the user clicks the OK button in the command dialog or 
# is immediately called after the created event not command inputs were created for the dialog.
def command_execute(args: adsk.core.CommandEventArgs):
    # General logging for debug.
    futil.log(f'{CMD_NAME} Command Execute Event')

    # TODO ******************************** Your code here ********************************

    # Get a reference to your command's inputs.
    inputs = args.command.commandInputs
    #text_box: adsk.core.TextBoxCommandInput = inputs.itemById('text_box')
    #value_input: adsk.core.ValueCommandInput = inputs.itemById('value_input')

    # Do something interesting
    #text = text_box.text
    #expression = value_input.expression
    #msg = f'Your text: {text}<br>Your value: {expression}'
    #ui.messageBox(msg)


    # Manipular UP
    DiaBaseParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_diametro_base')
    DiaPriParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_primeiro_diametro')
    DiaSegParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_segundo_diametro')
    DiaTerParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_terceiro_diametro')
    DiaTopoParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_diametro_topo')

    AltBaseParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_altura_base')
    AltPriParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_primeira_altura')
    AltSegParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_segunda_altura')
    AltTerParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_terceira_altura')
    AltTopoParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_altura_topo')
    
    DispBaseParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_dispersao_base')
    DispPriParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_primeira_dispersao')
    DispSegParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_segunda_dispersao')
    DispTerParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_terceira_dispersao')
    DispTopoParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_dispersao_topo')
    
    userParams.itemByName('Diametro_Base').expression = DiaBaseParamNovo.expressionOne
    userParams.itemByName('Diametro_Intermedio1').expression = DiaPriParamNovo.expressionOne
    userParams.itemByName('Diametro_Intermedio2').expression = DiaSegParamNovo.expressionOne
    userParams.itemByName('Diametro_Intermedio3').expression = DiaTerParamNovo.expressionOne
    userParams.itemByName('Diametro_Topo').expression = DiaTopoParamNovo.expressionOne

    userParams.itemByName('Altura_Base').expression = AltBaseParamNovo.expressionOne
    userParams.itemByName('Altura_Intermedia1').expression = AltPriParamNovo.expressionOne
    userParams.itemByName('Altura_Intermedia2').expression = AltSegParamNovo.expressionOne
    userParams.itemByName('Altura_Intermedia3').expression = AltTerParamNovo.expressionOne
    userParams.itemByName('Altura_Topo').expression = AltTopoParamNovo.expressionOne

    userParams.itemByName('Dispersao_Base').expression = DispBaseParamNovo.expressionOne
    userParams.itemByName('Dispersao_Intermedia1').expression = DispPriParamNovo.expressionOne
    userParams.itemByName('Dispersao_Intermedia2').expression = DispSegParamNovo.expressionOne
    userParams.itemByName('Dispersao_Intermedia3').expression = DispTerParamNovo.expressionOne
    userParams.itemByName('Dispersao_Topo').expression = DispTopoParamNovo.expressionOne

# This event handler is called when the command needs to compute a new preview in the graphics window.
def command_preview(args: adsk.core.CommandEventArgs):
    # General logging for debug.
    futil.log(f'{CMD_NAME} Command Preview Event')
    inputs = args.command.commandInputs

    DiaBaseParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_diametro_base')
    DiaPriParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_primeiro_diametro')
    DiaSegParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_segundo_diametro')
    DiaTerParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_terceiro_diametro')
    DiaTopoParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_diametro_topo')

    AltBaseParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_altura_base')
    AltPriParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_primeira_altura')
    AltSegParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_segunda_altura')
    AltTerParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_terceira_altura')
    AltTopoParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_altura_topo')
    
    DispBaseParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_dispersao_base')
    DispPriParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_primeira_dispersao')
    DispSegParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_segunda_dispersao')
    DispTerParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_terceira_dispersao')
    DispTopoParamNovo: adsk.core.FloatSliderCommandInput = inputs.itemById('slider_dispersao_topo')

    userParams.itemByName('Diametro_Base').expression = DiaBaseParamNovo.expressionOne
    userParams.itemByName('Diametro_Intermedio1').expression = DiaPriParamNovo.expressionOne
    userParams.itemByName('Diametro_Intermedio2').expression = DiaSegParamNovo.expressionOne
    userParams.itemByName('Diametro_Intermedio3').expression = DiaTerParamNovo.expressionOne
    userParams.itemByName('Diametro_Topo').expression = DiaTopoParamNovo.expressionOne

    userParams.itemByName('Altura_Base').expression = AltBaseParamNovo.expressionOne
    userParams.itemByName('Altura_Intermedia1').expression = AltPriParamNovo.expressionOne
    userParams.itemByName('Altura_Intermedia2').expression = AltSegParamNovo.expressionOne
    userParams.itemByName('Altura_Intermedia3').expression = AltTerParamNovo.expressionOne
    userParams.itemByName('Altura_Topo').expression = AltTopoParamNovo.expressionOne

    userParams.itemByName('Dispersao_Base').expression = DispBaseParamNovo.expressionOne
    userParams.itemByName('Dispersao_Intermedia1').expression = DispPriParamNovo.expressionOne
    userParams.itemByName('Dispersao_Intermedia2').expression = DispSegParamNovo.expressionOne
    userParams.itemByName('Dispersao_Intermedia3').expression = DispTerParamNovo.expressionOne
    userParams.itemByName('Dispersao_Topo').expression = DispTopoParamNovo.expressionOne


# This event handler is called when the user changes anything in the command dialog
# allowing you to modify values of other inputs based on that change.
def command_input_changed(args: adsk.core.InputChangedEventArgs):
    changed_input = args.input
    inputs = args.inputs

    # General logging for debug.
    futil.log(f'{CMD_NAME} Input Changed Event fired from a change to {changed_input.id}')


# This event handler is called when the user interacts with any of the inputs in the dialog
# which allows you to verify that all of the inputs are valid and enables the OK button.
def command_validate_input(args: adsk.core.ValidateInputsEventArgs):
    # General logging for debug.
    futil.log(f'{CMD_NAME} Validate Input Event')

    inputs = args.inputs
    
    # Verify the validity of the input values. This controls if the OK button is enabled or not.
    valueInput = inputs.itemById('value_input')
    if valueInput.value >= 0:
        args.areInputsValid = True
    else:
        args.areInputsValid = False
        

# This event handler is called when the command terminates.
def command_destroy(args: adsk.core.CommandEventArgs):
    # General logging for debug.
    futil.log(f'{CMD_NAME} Command Destroy Event')

    global local_handlers
    local_handlers = []
