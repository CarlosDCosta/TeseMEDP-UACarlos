#Author- Carlos Costa
#Description- Aplicação

import adsk.core, adsk.fusion, traceback
import math

defaultPlateName = 'Prato'
defaultDiameter1 = 5
defaultDiameter2 = 15
defaultDiameter3 = 5
defaultDiameter4 = 10
defaultDiameter5 = 20
defaultHeight1 = 0
defaultHeight2 = 100
defaultHeight3 = 200
defaultHeight4 = 300
defaultHeight5 = 400
defaultOffset1 = 10
defaultOffset2 = 10
defaultOffset3 = 10
defaultOffset4 = 10
defaultOffset5 = 10
defaultPoints = 20

# global set of event handlers to keep them referenced for the duration of the command
handlers = []
app = adsk.core.Application.get()
if app:
    ui = app.userInterface

newComp = None

def createNewComponent():
    # Get the active design.
    product = app.activeProduct
    design = adsk.fusion.Design.cast(product)
    rootComp = design.rootComponent
    allOccs = rootComp.occurrences
    newOcc = allOccs.addNewComponent(adsk.core.Matrix3D.create())
    return newOcc.component

class PratoCommandExecuteHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            unitsMgr = app.activeProduct.unitsManager
            command = args.firingEvent.sender
            inputs = command.commandInputs

            prato = Prato()
            for input in inputs:
                if input.id == 'pratoName':
                    prato.pratoName = input.value
                    
                elif input.id == 'slider_diametro_base':
                    prato.Diameter1 = input.valueOne
                elif input.id == 'slider_primeiro_diametro':
                    prato.Diameter2 = input.valueOne
                elif input.id == 'slider_segundo_diametro':
                    prato.Diameter3 = input.valueOne
                elif input.id == 'slider_terceiro_diametro':
                    prato.Diameter4 = input.valueOne
                elif input.id == 'slider_diametro_topo':
                    prato.Diameter5 = input.valueOne
                    
                elif input.id == 'slider_altura_base':
                    prato.Height1 = input.valueOne
                elif input.id == 'slider_primeira_altura':
                    prato.Height2 = input.valueOne
                elif input.id == 'slider_segunda_altura':
                    prato.Height3 = input.valueOne
                elif input.id == 'slider_terceira_altura':
                    prato.Height4 = input.valueOne
                elif input.id == 'slider_altura_topo':
                    prato.Height5 = input.valueOne
                
                elif input.id == 'slider_dispersao_base':
                    prato.Offset1 = input.valueOne
                elif input.id == 'slider_primeira_dispersao':
                    prato.Offset2 = input.valueOne
                elif input.id == 'slider_segunda_dispersao':
                    prato.Offset3 = input.valueOne
                elif input.id == 'slider_terceira_dispersao':
                    prato.Offset4 = input.valueOne
                elif input.id == 'slider_dispersao_topo':
                    prato.Offset5 = input.valueOne    
                elif input.id == 'slider_numero_pontos':
                    prato.Points = input.valueOne              


            prato.Tese_Forma();
            args.isValidResult = True

        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

class PratoCommandDestroyHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # when the command is done, terminate the script
            # this will release all globals which will remove all event handlers
            adsk.terminate()
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

class PratoCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):    
    def __init__(self):
        super().__init__()        
    def notify(self, args):
        try:
            cmd = args.command
            cmd.isRepeatable = False
            onExecute = PratoCommandExecuteHandler()
            cmd.execute.add(onExecute)
            onExecutePreview = PratoCommandExecuteHandler()
            cmd.executePreview.add(onExecutePreview)
            onDestroy = PratoCommandDestroyHandler()
            cmd.destroy.add(onDestroy)
            # keep the handler referenced beyond this function
            handlers.append(onExecute)
            handlers.append(onExecutePreview)
            handlers.append(onDestroy)

            #define the inputs
            inputs = cmd.commandInputs
            inputs.addStringValueInput('vaseName', 'Nome do Vaso', defaultPlateName)
            
            inputs.addFloatSliderCommandInput('slider_diametro_base', 'Slider para diâmetro da base', 'mm', 5,29,False)
            inputs.addFloatSliderCommandInput('slider_primeiro_diametro', 'Slider para o diâmetro da base-centro','mm', 5, 29, False)
            inputs.addFloatSliderCommandInput('slider_segundo_diametro', 'Slider para o diâmetro do centro', 'mm', 5, 29, False)
            inputs.addFloatSliderCommandInput('slider_terceiro_diametro', 'Slider para o diâmetro do centro-topo', 'mm', 5, 29, False)
            inputs.addFloatSliderCommandInput('slider_diametro_topo', 'Slider para diâmetro do topo', 'mm', 5, 29, False)
     

            inputs.addFloatSliderCommandInput('slider_altura_base', 'Slider para a altura da base', 'mm', 0,39,False)
            inputs.addFloatSliderCommandInput('slider_primeira_altura', 'Slider para a altura da base-centro','mm', 0, 39, False)
            inputs.addFloatSliderCommandInput('slider_segunda_altura', 'Slider para a altura do centro', 'mm', 0, 39, False)
            inputs.addFloatSliderCommandInput('slider_terceira_altura', 'Slider para a altura do centro-topo', 'mm', 0, 39, False)
            inputs.addFloatSliderCommandInput('slider_altura_topo', 'Slider para a altura do topo', 'mm', 0, 39, False)


            inputs.addFloatSliderCommandInput('slider_dispersao_base', 'Slider para a dispersão da base', 'mm', 0.01,5, False)
            inputs.addFloatSliderCommandInput('slider_primeira_dispersao', 'Slider para a dispersão da base-centro','mm', 0.01, 5, False)
            inputs.addFloatSliderCommandInput('slider_segunda_dispersao', 'Slider para a dispersão do centro', 'mm', 0.01, 5, False)
            inputs.addFloatSliderCommandInput('slider_terceira_dispersao', 'Slider para a dispersão do centro-topo', 'mm', 0.01, 5, False)
            inputs.addFloatSliderCommandInput('slider_dispersao_topo', 'Slider para a dispersão do topo', 'mm', 0.01, 5, False)


            inputs.addIntegerSliderCommandInput('slider_numero_pontos', 'Slider para numero de pontos', 4, 24, False)

        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

class Prato:
    def __init__(self):
        self._vaseName = defaultPlateName
        self._Diameter1 = defaultDiameter1
        self._Diameter2 = defaultDiameter2
        self._Diameter3 = defaultDiameter3
        self._Diameter4 = defaultDiameter4
        self._Diameter5 = defaultDiameter5
        self._Height1 = defaultHeight1
        self._Height2 = defaultHeight2
        self._Height3 = defaultHeight3
        self._Height4 = defaultHeight4
        self._Height5 = defaultHeight5
        self._Offset1 = defaultOffset1
        self._Offset2 = defaultOffset2
        self._Offset3 = defaultOffset3
        self._Offset4 = defaultOffset4
        self._Offset5 = defaultOffset5
        self._Points = defaultPoints

    #properties
    @property
    def vaseName(self):
        return self._vaseName
    @vaseName.setter
    def vaseName(self, value):
        self._vaseName = value

    @property
    def Diameter1(self):
        return self._Diameter1
    @Diameter1.setter
    def Diameter1(self, value):
        self._Diameter1 = value
        
    @property
    def Diameter2(self):
        return self._Diameter2
    @Diameter2.setter
    def Diameter2(self, value):
        self._Diameter2 = value 
    
    @property
    def Diameter3(self):
        return self._Diameter3
    @Diameter3.setter
    def Diameter3(self, value):
        self._Diameter3 = value  
    
    @property
    def Diameter4(self):
        return self._Diameter4
    @Diameter4.setter
    def Diameter4(self, value):
        self._Diameter4 = value
    
    @property
    def Diameter5(self):
        return self._Diameter5
    @Diameter5.setter
    def Diameter5(self, value):
        self._Diameter5 = value
    
    
    @property
    def Height1(self):
        return self._Height1
    @Height1.setter
    def Height1(self, value):
        self._Height1 = value
        
    @property
    def Height2(self):
        return self._Height2
    @Height2.setter
    def Height2(self, value):
        self._Height2 = value
        
    @property
    def Height3(self):
        return self._Height3
    @Height3.setter
    def Height3(self, value):
        self._Height3 = value
    
    @property
    def Height4(self):
        return self._Height4
    @Height4.setter
    def Height4(self, value):
        self._Height4 = value
    
    @property
    def Height5(self):
        return self._Height5
    @Height5.setter
    def Height5(self, value):
        self._Height5 = value
        


    @property
    def Offset1(self):
        return self._Offset1
    @Offset1.setter
    def Offset1(self, value):
        self._Offset1 = value
        
    @property
    def Offset2(self):
        return self._Offset2
    @Offset2.setter
    def Offset2(self, value):
        self._Offset2 = value
    
    @property
    def Offset3(self):
        return self._Offset3
    @Offset3.setter
    def Offset3(self, value):
        self._Offset3 = value
    
    @property
    def Offset4(self):
        return self._Offset1
    @Offset4.setter
    def Offset4(self, value):
        self._Offset4 = value
    
    @property
    def Offset5(self):
        return self._Offset5
    @Offset5.setter
    def Offset5(self, value):
        self._Offset5 = value
    
    @property
    def Points(self):
        return self._Points
    @Points.setter
    def Points(self, value):
        self._Points = value


    # Função principal para criar o vaso
    def Tese_Forma(self):
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)

        # Criar um novo componente
        root_comp = design.rootComponent
        occurence = root_comp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        component = occurence.component
        newComp = component  
        unitsMgr = design.unitsManager


        # Inputs
        # 1º Sketch
        # Diâmetro 
        parameterName1 = 'Diametro_Base'
        realValueInputDB = adsk.core.ValueInput.createByReal(self._Diameter1)

        # Altura
        defaultInputAB = '0 cm'
        parameterNameA1 = 'Altura_Base'
        realValueInputAB = adsk.core.ValueInput.createByReal(self._Height1)
        Altura1 = (0, 0, realValueInputAB.realValue)
        # Dispersão
        parameterNameDisp1 = 'Dispersao_Base'
        realValueInputDispB = adsk.core.ValueInput.createByReal(self._Offset1)

        # 2º Sketch
        # Diâmetro
        parameterName2 = 'Diametro_Intermedio1'
        realValueInputDI1 = adsk.core.ValueInput.createByReal(self._Diameter2)
        # Altura
        parameterNameA2 = 'Altura_Intermedia1'
        realValueInputAI1 = adsk.core.ValueInput.createByReal(self._Height2)
        Altura2 = (0, 0, realValueInputAI1.realValue)
        # Dispersão
        parameterNameDisp2 = 'Dispersao_Intermedia1'
        realValueInputDispI1 = adsk.core.ValueInput.createByReal(self._Offset2)

        # 3º Sketch
        # Diâmetro
        parameterName3 = 'Diametro_Intermedio2'
        realValueInputDI2 = adsk.core.ValueInput.createByReal(self._Diameter3)
        # Altura
        parameterNameA3 = 'Altura_Intermedia2'
        realValueInputAI2 = adsk.core.ValueInput.createByReal(self._Height3)
        Altura3 = (0, 0, realValueInputAI2.realValue)
        
        # Dispersão
        parameterNameDisp3 = 'Dispersao_Intermedia2'
        realValueInputDispI2 = adsk.core.ValueInput.createByReal(self._Offset3)

        # 4º Sketch
        # Diâmetro
        parameterName4 = 'Diametro_Intermedio3'
        realValueInputDI3 = adsk.core.ValueInput.createByReal(self._Diameter4)
        # Altura
        parameterNameA4 = 'Altura_Intermedia3'
        realValueInputAI3 = adsk.core.ValueInput.createByReal(self._Height4)
        Altura4 = (0, 0, realValueInputAI3.realValue)
        # Dispersão
        parameterNameDisp4 = 'Dispersao_Intermedia3'
        realValueInputDispI3 = adsk.core.ValueInput.createByReal(self._Offset4)

        # 5º Sketch
        # Diâmetro
        parameterName5 = 'Diametro_Topo'
        realValueInputDT = adsk.core.ValueInput.createByReal(self._Diameter5)
        # Altura
        parameterNameA5 = 'Altura_Topo'
        realValueInputAT = adsk.core.ValueInput.createByReal(self._Height5)
        Altura5 = (0, 0, realValueInputAT.realValue)
        # Dispersão
        parameterNameDisp5 = 'Dispersao_Topo'
        realValueInputDispT = adsk.core.ValueInput.createByReal(self._Offset5)
        
        realValueP = adsk.core.ValueInput.createByReal(self._Points)

        # Parâmetros
        userParam1 = design.userParameters.add(parameterName1, realValueInputDB, unitsMgr.defaultLengthUnits, '')
        userParam2 = design.userParameters.add(parameterName2, realValueInputDI1, unitsMgr.defaultLengthUnits, '')
        userParam3 = design.userParameters.add(parameterName3, realValueInputDI2, unitsMgr.defaultLengthUnits, '')
        userParam4 = design.userParameters.add(parameterName4, realValueInputDI3, unitsMgr.defaultLengthUnits, '')
        userParam5 = design.userParameters.add(parameterName5, realValueInputDT, unitsMgr.defaultLengthUnits, '')

        userParamA1 = design.userParameters.add(parameterNameA1, realValueInputAB, unitsMgr.defaultLengthUnits, '')
        userParamA2 = design.userParameters.add(parameterNameA2, realValueInputAI1, unitsMgr.defaultLengthUnits, '')
        userParamA3 = design.userParameters.add(parameterNameA3, realValueInputAI2, unitsMgr.defaultLengthUnits, '')
        userParamA4 = design.userParameters.add(parameterNameA4, realValueInputAI3, unitsMgr.defaultLengthUnits, '')
        userParamA5 = design.userParameters.add(parameterNameA5, realValueInputAT, unitsMgr.defaultLengthUnits, '')
        
        userParamDisp1 = design.userParameters.add(parameterNameDisp1, realValueInputDispB, unitsMgr.defaultLengthUnits, '')
        userParamDisp2 = design.userParameters.add(parameterNameDisp2, realValueInputDispI1, unitsMgr.defaultLengthUnits, '')
        userParamDisp3 = design.userParameters.add(parameterNameDisp3, realValueInputDispI2, unitsMgr.defaultLengthUnits, '')
        userParamDisp4 = design.userParameters.add(parameterNameDisp4, realValueInputDispI3, unitsMgr.defaultLengthUnits, '')
        userParamDisp5 = design.userParameters.add(parameterNameDisp5, realValueInputDispT, unitsMgr.defaultLengthUnits, '')


    # Criar os esboços
        sketches = root_comp.sketches
        xz_plane = root_comp.xZConstructionPlane
        num_points = self._Points
        
        # Esboço 1
        sketch1 = sketches.add(xz_plane)

        # Adicionar círculos
        center_point1 = adsk.core.Point3D.create(Altura1[0], Altura1[1], Altura1[2])
        circle1 = sketch1.sketchCurves.sketchCircles.addByCenterRadius(center_point1, realValueInputDB.realValue)
        circle1.isConstruction = True


        inwardcircle1 = sketch1.sketchCurves.sketchCircles.addByCenterRadius(center_point1, ((realValueInputDB.realValue-realValueInputDispB.realValue)/2))
        inwardcircle1.isConstruction = True
        
        # Adicionando as dimensões
        dim1 = sketch1.sketchDimensions.addDiameterDimension(circle1, adsk.core.Point3D.create(Altura1[0], Altura1[1], Altura1[2] + realValueInputDB.realValue))
        dim1.parameter.expression = userParam1.name
        dimOffset1 = sketch1.sketchDimensions.addConcentricCircleDimension(circle1, inwardcircle1, adsk.core.Point3D.create(Altura1[0], Altura1[1], Altura1[2] + realValueInputDispB.realValue))
        dimOffset1.parameter.expression = userParamDisp1.name


        # Adicionando dimensão de altura
        height_dim1 = sketch1.sketchDimensions.addDistanceDimension(sketch1.originPoint, circle1.centerSketchPoint, adsk.fusion.DimensionOrientations.AlignedDimensionOrientation, adsk.core.Point3D.create(Altura1[0], Altura1[1], Altura1[2]))
        height_dim1.parameter.expression = userParamA1.name


        # Ângulo entre cada ponto
        angle_increment1 = 2 * math.pi / num_points

        # Raio dos círculos
        radius_outward1 = circle1.radius
        radius_inward1 = inwardcircle1.radius

        # Centro dos círculos
        center_point_outward1 = circle1.centerSketchPoint
        center_point_inward1 = inwardcircle1.centerSketchPoint

        # Listas para armazenar os pontos
        points_outward1 = []
        points_inward1 = []

        # Loop para criar as linhas radiais e pontos intercalados
        for i in range(num_points):
            # Calcular os ângulos para os pontos
            angle_outward1 = i * angle_increment1
            angle_inward1 = (i + 0.5) * angle_increment1

            # Calcular as coordenadas dos pontos
            x_outward1 = center_point_outward1.geometry.x + radius_outward1 * math.cos(angle_outward1)
            y_outward1 = center_point_outward1.geometry.y + radius_outward1 * math.sin(angle_outward1)
            point_outward1 = adsk.core.Point3D.create(x_outward1, y_outward1, Altura1[2])

            x_inward1 = center_point_inward1.geometry.x + radius_inward1 * math.cos(angle_inward1)
            y_inward1 = center_point_inward1.geometry.y + radius_inward1 * math.sin(angle_inward1)
            point_inward1 = adsk.core.Point3D.create(x_inward1, y_inward1, Altura1[2])

            # Adicionar os pontos às listas
            points_outward1.append(point_outward1)
            points_inward1.append(point_inward1)

            # Criar as linhas radiais
            line_outward1 = sketch1.sketchCurves.sketchLines.addByTwoPoints(point_outward1, circle1.centerSketchPoint)
            line_inward1 = sketch1.sketchCurves.sketchLines.addByTwoPoints(point_inward1, inwardcircle1.centerSketchPoint)
            line_outward1.isConstruction = True
            line_inward1.isConstruction = True

            # Adicionar restrições de coincidência entre as linhas radiais e os círculos
            sketch1.geometricConstraints.addCoincident(line_outward1.startSketchPoint, circle1)
            sketch1.geometricConstraints.addCoincident(line_inward1.startSketchPoint, inwardcircle1)


        # Criar spline usando os pontos intercalados
        combined_points1 = adsk.core.ObjectCollection.create()
        for i in range(num_points):
            combined_points1.add(points_outward1[i])
            combined_points1.add(points_inward1[i])
        combined_points1.add(points_outward1[0])
        combined_spline1 = sketch1.sketchCurves.sketchFittedSplines.add(combined_points1)
        combined_spline1.isClosed = True
        


        # Esboço 2
        sketch2 = sketches.add(xz_plane)

        # Adicionar círculos
        center_point2 = adsk.core.Point3D.create(Altura2[0], Altura2[1], Altura2[2])
        circle2 = sketch2.sketchCurves.sketchCircles.addByCenterRadius(center_point2, realValueInputDI1.realValue)
        circle2.isConstruction = True

        inwardcircle2 = sketch2.sketchCurves.sketchCircles.addByCenterRadius(center_point2, ((realValueInputDI1.realValue-realValueInputDispI1.realValue)/2))
        inwardcircle2.isConstruction = True
        sketch2.geometricConstraints.addConcentric(circle2,inwardcircle2)
        
        constructionline2 = sketch2.sketchCurves.sketchLines.addByTwoPoints(center_point1,center_point2)
        constructionline2.isConstruction=True
        sketch2.geometricConstraints.addPerpendicularToSurface(constructionline2, xz_plane)
        sketch2.geometricConstraints.addCoincident(constructionline2.startSketchPoint, sketch2.originPoint)
        sketch2.geometricConstraints.addCoincident(constructionline2.endSketchPoint, circle2.centerSketchPoint)

        # Adicionando as dimensões
        dim2 = sketch2.sketchDimensions.addDiameterDimension(circle2, adsk.core.Point3D.create(Altura2[0], Altura2[1], Altura2[2] + realValueInputDI1.realValue))
        dim2.parameter.expression = userParam2.name
        dimOffset2 = sketch2.sketchDimensions.addConcentricCircleDimension(circle2, inwardcircle2, adsk.core.Point3D.create(Altura2[0], Altura2[1], Altura2[2] + realValueInputDispI1.realValue))
        dimOffset2.parameter.expression = userParamDisp2.name

        # Adicionando dimensão de altura
        height_dim2 = sketch2.sketchDimensions.addDistanceDimension(sketch2.originPoint, circle2.centerSketchPoint, adsk.fusion.DimensionOrientations.AlignedDimensionOrientation, adsk.core.Point3D.create(Altura2[0], Altura2[1], Altura2[2]))
        height_dim2.parameter.expression = userParamA2.name
    
        # Ângulo entre cada ponto
        angle_increment2 = 2 * math.pi / num_points

        # Raio dos círculos
        radius_outward2 = circle2.radius
        radius_inward2 = inwardcircle2.radius

        # Centro dos círculos
        center_point_outward2 = circle2.centerSketchPoint
        center_point_inward2 = inwardcircle2.centerSketchPoint

        # Listas para armazenar os pontos
        points_outward2 = []
        points_inward2 = []

        # Loop para criar as linhas radiais e pontos intercalados
        for i in range(num_points):
            # Calcular os ângulos para os pontos
            angle_outward2 = i * angle_increment2
            angle_inward2 = (i + 0.5) * angle_increment2

            # Calcular as coordenadas dos pontos
            x_outward2 = center_point_outward2.geometry.x + radius_outward2 * math.cos(angle_outward2)
            y_outward2 = center_point_outward2.geometry.y + radius_outward2 * math.sin(angle_outward2)
            point_outward2 = adsk.core.Point3D.create(x_outward2, y_outward2, Altura2[2])

            x_inward2 = center_point_inward2.geometry.x + radius_inward2 * math.cos(angle_inward2)
            y_inward2 = center_point_inward2.geometry.y + radius_inward2 * math.sin(angle_inward2)
            point_inward2 = adsk.core.Point3D.create(x_inward2, y_inward2, Altura2[2])

            # Adicionar os pontos às listas
            points_outward2.append(point_outward2)
            points_inward2.append(point_inward2)

            # Criar as linhas radiais
            line_outward2 = sketch2.sketchCurves.sketchLines.addByTwoPoints(point_outward2, circle2.centerSketchPoint)
            line_inward2 = sketch2.sketchCurves.sketchLines.addByTwoPoints(point_inward2, inwardcircle2.centerSketchPoint)
            line_outward2.isConstruction = True
            line_inward2.isConstruction = True
            sketch2.geometricConstraints.addPerpendicular(constructionline2,line_outward2)
            sketch2.geometricConstraints.addPerpendicular(constructionline2,line_inward2)


            # Adicionar restrições de coincidência entre as linhas radiais e os círculos
            sketch2.geometricConstraints.addCoincident(line_outward2.startSketchPoint, circle2)
            sketch2.geometricConstraints.addCoincident(line_inward2.startSketchPoint, inwardcircle2)


        # Criar spline usando os pontos intercalados
        combined_points2 = adsk.core.ObjectCollection.create()
        for i in range(num_points):
            combined_points2.add(points_outward2[i])
            combined_points2.add(points_inward2[i])
        combined_points2.add(points_outward2[0])
        combined_spline2 = sketch2.sketchCurves.sketchFittedSplines.add(combined_points2)
        combined_spline2.isClosed = True
        
        # Esboço 3
        sketch3 = sketches.add(xz_plane)

        # Adicionar círculos
        center_point3 = adsk.core.Point3D.create(Altura3[0], Altura3[1], Altura3[2])
        circle3 = sketch3.sketchCurves.sketchCircles.addByCenterRadius(center_point3, realValueInputDI2.realValue)
        circle3.isConstruction = True

        inwardcircle3 = sketch3.sketchCurves.sketchCircles.addByCenterRadius(center_point3, ((realValueInputDI2.realValue-realValueInputDispI2.realValue)/2))
        inwardcircle3.isConstruction = True
        sketch3.geometricConstraints.addConcentric(circle3,inwardcircle3)
        
        constructionline3 = sketch3.sketchCurves.sketchLines.addByTwoPoints(center_point1,center_point3)
        constructionline3.isConstruction=True
        sketch3.geometricConstraints.addPerpendicularToSurface(constructionline3, xz_plane)
        sketch3.geometricConstraints.addCoincident(constructionline3.startSketchPoint, sketch3.originPoint)
        sketch3.geometricConstraints.addCoincident(constructionline3.endSketchPoint, circle3.centerSketchPoint)

        # Adicionando as dimensões
        dim3 = sketch3.sketchDimensions.addDiameterDimension(circle3, adsk.core.Point3D.create(Altura3[0], Altura3[1], Altura3[2] + realValueInputDI2.realValue))
        dim3.parameter.expression = userParam3.name
        dimOffset3 = sketch3.sketchDimensions.addConcentricCircleDimension(circle3,inwardcircle3, adsk.core.Point3D.create(Altura3[0], Altura3[1], Altura3[2] + realValueInputDispI2.realValue))
        dimOffset3.parameter.expression = userParamDisp3.name
        
        # Adicionando dimensão de altura
        height_dim3 = sketch3.sketchDimensions.addDistanceDimension(sketch3.originPoint, circle3.centerSketchPoint, adsk.fusion.DimensionOrientations.AlignedDimensionOrientation, adsk.core.Point3D.create(Altura3[0], Altura3[1], Altura3[2]))
        height_dim3.parameter.expression = userParamA3.name

        # Ângulo entre cada ponto
        angle_increment3 = 2 * math.pi / num_points

        # Raio dos círculos
        radius_outward3 = circle3.radius
        radius_inward3 = inwardcircle3.radius

        # Centro dos círculos
        center_point_outward3 = circle3.centerSketchPoint
        center_point_inward3 = inwardcircle3.centerSketchPoint

        # Listas para armazenar os pontos
        points_outward3 = []
        points_inward3 = []

        # Loop para criar as linhas radiais e pontos intercalados
        for i in range(num_points):
            # Calcular os ângulos para os pontos
            angle_outward3 = i * angle_increment3
            angle_inward3 = (i + 0.5) * angle_increment3

            # Calcular as coordenadas dos pontos
            x_outward3 = center_point_outward3.geometry.x + radius_outward3 * math.cos(angle_outward3)
            y_outward3 = center_point_outward3.geometry.y + radius_outward3 * math.sin(angle_outward3)
            point_outward3 = adsk.core.Point3D.create(x_outward3, y_outward3, Altura3[2])

            x_inward3 = center_point_inward3.geometry.x + radius_inward3 * math.cos(angle_inward3)
            y_inward3 = center_point_inward3.geometry.y + radius_inward3 * math.sin(angle_inward3)
            point_inward3 = adsk.core.Point3D.create(x_inward3, y_inward3, Altura3[2])

            # Adicionar os pontos às listas
            points_outward3.append(point_outward3)
            points_inward3.append(point_inward3)

            # Criar as linhas radiais
            line_outward3 = sketch3.sketchCurves.sketchLines.addByTwoPoints(point_outward3, circle3.centerSketchPoint)
            line_inward3 = sketch3.sketchCurves.sketchLines.addByTwoPoints(point_inward3, inwardcircle3.centerSketchPoint)
            line_outward3.isConstruction = True
            line_inward3.isConstruction = True
            sketch3.geometricConstraints.addPerpendicular(constructionline3,line_outward3)
            sketch3.geometricConstraints.addPerpendicular(constructionline3,line_inward3)


            # Adicionar restrições de coincidência entre as linhas radiais e os círculos
            sketch3.geometricConstraints.addCoincident(line_outward3.startSketchPoint, circle3)
            sketch3.geometricConstraints.addCoincident(line_inward3.startSketchPoint, inwardcircle3)


        # Criar spline usando os pontos intercalados
        combined_points3 = adsk.core.ObjectCollection.create()
        for i in range(num_points):
            combined_points3.add(points_outward3[i])
            combined_points3.add(points_inward3[i])
        combined_points3.add(points_outward3[0])
        combined_spline3 = sketch3.sketchCurves.sketchFittedSplines.add(combined_points3)
        combined_spline3.isClosed = True



        # Esboço 4
        sketch4 = sketches.add(xz_plane)

        # Adicionar círculos
        center_point4 = adsk.core.Point3D.create(Altura4[0], Altura4[1], Altura4[2])
        circle4 = sketch4.sketchCurves.sketchCircles.addByCenterRadius(center_point4, realValueInputDI3.realValue)
        circle4.isConstruction = True

        inwardcircle4 = sketch4.sketchCurves.sketchCircles.addByCenterRadius(center_point4, ((realValueInputDI3.realValue-realValueInputDispI3.realValue)/2))
        inwardcircle4.isConstruction = True
        sketch4.geometricConstraints.addConcentric(circle4,inwardcircle4)
        
        constructionline4 = sketch4.sketchCurves.sketchLines.addByTwoPoints(center_point1,center_point4)
        constructionline4.isConstruction=True
        sketch4.geometricConstraints.addPerpendicularToSurface(constructionline4, xz_plane)
        sketch4.geometricConstraints.addCoincident(constructionline4.startSketchPoint, sketch4.originPoint)
        sketch4.geometricConstraints.addCoincident(constructionline4.endSketchPoint, circle4.centerSketchPoint)

        # Adicionando as dimensões
        dim4 = sketch4.sketchDimensions.addDiameterDimension(circle4, adsk.core.Point3D.create(Altura4[0], Altura4[1], Altura4[2] + realValueInputDI3.realValue))
        dim4.parameter.expression = userParam4.name
        dimOffset4 = sketch4.sketchDimensions.addConcentricCircleDimension(circle4,inwardcircle4, adsk.core.Point3D.create(Altura4[0], Altura4[1], Altura4[2] + realValueInputDispI3.realValue))
        dimOffset4.parameter.expression = userParamDisp4.name

        # Adicionando dimensão de altura
        height_dim4 = sketch4.sketchDimensions.addDistanceDimension(sketch4.originPoint, circle4.centerSketchPoint, adsk.fusion.DimensionOrientations.AlignedDimensionOrientation, adsk.core.Point3D.create(Altura4[0], Altura4[1], Altura4[2]))
        height_dim4.parameter.expression = userParamA4.name

        # Ângulo entre cada ponto
        angle_increment4 = 2 * math.pi / num_points

        # Raio dos círculos
        radius_outward4 = circle4.radius
        radius_inward4 = inwardcircle4.radius

        # Centro dos círculos
        center_point_outward4 = circle4.centerSketchPoint
        center_point_inward4 = inwardcircle4.centerSketchPoint

        # Listas para armazenar os pontos
        points_outward4 = []
        points_inward4 = []

        # Loop para criar as linhas radiais e pontos intercalados
        for i in range(num_points):
            # Calcular os ângulos para os pontos
            angle_outward4 = i * angle_increment4
            angle_inward4 = (i + 0.5) * angle_increment4

            # Calcular as coordenadas dos pontos
            x_outward4 = center_point_outward4.geometry.x + radius_outward4 * math.cos(angle_outward4)
            y_outward4 = center_point_outward4.geometry.y + radius_outward4 * math.sin(angle_outward4)
            point_outward4 = adsk.core.Point3D.create(x_outward4, y_outward4, Altura4[2])

            x_inward4 = center_point_inward4.geometry.x + radius_inward4 * math.cos(angle_inward4)
            y_inward4 = center_point_inward4.geometry.y + radius_inward4 * math.sin(angle_inward4)
            point_inward4 = adsk.core.Point3D.create(x_inward4, y_inward4, Altura4[2])

            # Adicionar os pontos às listas
            points_outward4.append(point_outward4)
            points_inward4.append(point_inward4)

            # Criar as linhas radiais
            line_outward4 = sketch4.sketchCurves.sketchLines.addByTwoPoints(point_outward4, circle4.centerSketchPoint)
            line_inward4 = sketch4.sketchCurves.sketchLines.addByTwoPoints(point_inward4, inwardcircle4.centerSketchPoint)
            line_outward4.isConstruction = True
            line_inward4.isConstruction = True
            sketch4.geometricConstraints.addPerpendicular(constructionline4,line_outward4)
            sketch4.geometricConstraints.addPerpendicular(constructionline4,line_inward4)


            # Adicionar restrições de coincidência entre as linhas radiais e os círculos
            sketch4.geometricConstraints.addCoincident(line_outward4.startSketchPoint, circle4)
            sketch4.geometricConstraints.addCoincident(line_inward4.startSketchPoint, inwardcircle4)


        # Criar spline usando os pontos intercalados
        combined_points4 = adsk.core.ObjectCollection.create()
        for i in range(num_points):
            combined_points4.add(points_outward4[i])
            combined_points4.add(points_inward4[i])
        combined_points4.add(points_outward4[0])
        combined_spline4 = sketch4.sketchCurves.sketchFittedSplines.add(combined_points4)
        combined_spline4.isClosed = True



        # Esboço 5
        sketch5 = sketches.add(xz_plane)

        # Adicionar círculos
        center_point5 = adsk.core.Point3D.create(Altura5[0], Altura5[1], Altura5[2])
        circle5 = sketch5.sketchCurves.sketchCircles.addByCenterRadius(center_point5, realValueInputDT.realValue)
        circle5.isConstruction = True

        inwardcircle5 = sketch5.sketchCurves.sketchCircles.addByCenterRadius(center_point5, ((realValueInputDT.realValue-realValueInputDispT.realValue)/2))
        inwardcircle5.isConstruction = True
        sketch5.geometricConstraints.addConcentric(circle5,inwardcircle5)

        constructionline5 = sketch5.sketchCurves.sketchLines.addByTwoPoints(center_point1,center_point5)
        constructionline5.isConstruction=True
        sketch5.geometricConstraints.addPerpendicularToSurface(constructionline5, xz_plane)
        sketch5.geometricConstraints.addCoincident(constructionline5.startSketchPoint, sketch5.originPoint)
        sketch5.geometricConstraints.addCoincident(constructionline5.endSketchPoint, circle5.centerSketchPoint)
        
        # Adicionando as dimensões
        dim5 = sketch5.sketchDimensions.addDiameterDimension(circle5, adsk.core.Point3D.create(Altura5[0], Altura5[1], Altura5[2] + realValueInputDT.realValue))
        dim5.parameter.expression = userParam5.name
        dimOffset5 = sketch5.sketchDimensions.addConcentricCircleDimension(circle5,inwardcircle5, adsk.core.Point3D.create(Altura5[0], Altura5[1], Altura5[2] + realValueInputDispT.realValue))
        dimOffset5.parameter.expression = userParamDisp5.name

        # Adicionando dimensão de altura
        height_dim5 = sketch5.sketchDimensions.addDistanceDimension(sketch5.originPoint, circle5.centerSketchPoint, adsk.fusion.DimensionOrientations.AlignedDimensionOrientation, adsk.core.Point3D.create(Altura5[0], Altura5[1], Altura5[2]))
        height_dim5.parameter.expression = userParamA5.name

        # Ângulo entre cada ponto
        angle_increment5 = 2 * math.pi / num_points

        # Raio dos círculos
        radius_outward5 = circle5.radius
        radius_inward5 = inwardcircle5.radius

        # Centro dos círculos
        center_point_outward5 = circle5.centerSketchPoint
        center_point_inward5 = inwardcircle5.centerSketchPoint

        # Listas para armazenar os pontos
        points_outward5 = []
        points_inward5 = []

        # Loop para criar as linhas radiais e pontos intercalados
        for i in range(num_points):
            # Calcular os ângulos para os pontos
            angle_outward5 = i * angle_increment5
            angle_inward5 = (i + 0.5) * angle_increment5

            # Calcular as coordenadas dos pontos
            x_outward5 = center_point_outward5.geometry.x + radius_outward5 * math.cos(angle_outward5)
            y_outward5 = center_point_outward5.geometry.y + radius_outward5 * math.sin(angle_outward5)
            point_outward5 = adsk.core.Point3D.create(x_outward5, y_outward5, Altura5[2])

            x_inward5 = center_point_inward5.geometry.x + radius_inward5 * math.cos(angle_inward5)
            y_inward5 = center_point_inward5.geometry.y + radius_inward5 * math.sin(angle_inward5)
            point_inward5 = adsk.core.Point3D.create(x_inward5, y_inward5, Altura5[2])

            # Adicionar os pontos às listas
            points_outward5.append(point_outward5)
            points_inward5.append(point_inward5)

            # Criar as linhas radiais
            line_outward5 = sketch5.sketchCurves.sketchLines.addByTwoPoints(point_outward5, circle5.centerSketchPoint)
            line_inward5 = sketch5.sketchCurves.sketchLines.addByTwoPoints(point_inward5, inwardcircle5.centerSketchPoint)
            line_outward5.isConstruction = True
            line_inward5.isConstruction = True
            sketch5.geometricConstraints.addPerpendicular(constructionline5,line_outward5)
            sketch5.geometricConstraints.addPerpendicular(constructionline5,line_inward5)


            # Adicionar restrições de coincidência entre as linhas radiais e os círculos
            sketch5.geometricConstraints.addCoincident(line_outward5.startSketchPoint, circle5)
            sketch5.geometricConstraints.addCoincident(line_inward5.startSketchPoint, inwardcircle5)


        # Criar spline usando os pontos intercalados
        combined_points5 = adsk.core.ObjectCollection.create()
        for i in range(num_points):
            combined_points5.add(points_outward5[i])
            combined_points5.add(points_inward5[i])
        combined_points5.add(points_outward5[0])
        combined_spline5 = sketch5.sketchCurves.sketchFittedSplines.add(combined_points5)
        combined_spline5.isClosed = True



    # Loft
        loft_features = root_comp.features.loftFeatures
        loft_feature_input = loft_features.createInput(adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        loft_feature_input.isSolid = False

        # Adicionar perfis à entrada do loft
        loft_feature_input.loftSections.add(sketch1.profiles.item(0))
        loft_feature_input.loftSections.add(sketch2.profiles.item(0))
        loft_feature_input.loftSections.add(sketch3.profiles.item(0))
        loft_feature_input.loftSections.add(sketch4.profiles.item(0))
        loft_feature_input.loftSections.add(sketch5.profiles.item(0))

        # Criar sólido com a operação de loft
        loft_feature = loft_features.add(loft_feature_input)
        

        # Criar a superfície plana a partir do esboço 1
        patch_features = root_comp.features.patchFeatures
        patch_input = patch_features.createInput(sketch1.profiles.item(0), adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        patch_input.isChainSelection = True


        # Adicionar a superfície plana
        patch_feature = patch_features.add(patch_input)

        # Obter as faces da superfície loft e da superfície plana
        surfCol = adsk.core.ObjectCollection.create()
        for body in loft_feature.bodies:
            surfCol.add(body)
        for body in patch_feature.bodies:
            surfCol.add(body)       
        
        faceCol = adsk.core.ObjectCollection.create()
        for face in loft_feature.faces:
            faceCol.add(face)
        for face in patch_feature.faces:
            faceCol.add(face)

        # Criar a entrada de costura com tolerância
        tolerance = adsk.core.ValueInput.createByReal(1.0)
        stitch_features = root_comp.features.stitchFeatures
        stitch_input = stitch_features.createInput(surfCol, tolerance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Adicionar a operação de costura
        stitch_feature = stitch_features.add(stitch_input)

        # Criar a entrada de espessura
        thicken_features = root_comp.features.thickenFeatures
        thicken_input = thicken_features.createInput(faceCol,adsk.core.ValueInput.createByReal(0.08),True,adsk.fusion.FeatureOperations.NewBodyFeatureOperation, True)
        thickness_value = adsk.core.ValueInput.createByReal(0.02)  # Defina a espessura desejada
        thicken_input.thickness = thickness_value
        thicken_input.isSolid = True 

        # Adicionar a espessura à superfície costurada
        thicken_feature = thicken_features.add(thicken_input)

         
        # Aplicar filet a todas as arestas do corpo resultante
        fillet_features = root_comp.features.filletFeatures
        edges = adsk.core.ObjectCollection.create()

        # Coletar todas as arestas do corpo resultante
        body = thicken_feature.bodies.item(0)
        for edge in body.edges:
            edges.add(edge)

        # Criar a entrada de filet
        fillet_input = fillet_features.createInput()
        radius = adsk.core.ValueInput.createByReal(0.05)  # Defina o raio desejado para o filet
        fillet_input.addConstantRadiusEdgeSet(edges, radius, True)

        # Adicionar a operação de filet
        fillet_feature = fillet_features.add(fillet_input)     
          
        # set material
        faces = thicken_feature.faces
        body = faces[0].body
        objCol = adsk.core.ObjectCollection.create()
        objCol.add(body)
        VaseMaterial = 'PrismMaterial-022'
        materialLibId = 'C1EEA57C-3F56-45FC-B8CB-A9EC46A9994C'
        materialLibs = app.materialLibraries
        materials = materialLibs.itemById(materialLibId).materials
        body.material = materials.itemById(VaseMaterial)

        

        # Atualizar a visualização
        app.activeViewport.refresh()
    


def run(context):
    try:
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        if not design:
            ui.messageBox('A Fusion design must be active when running this script.')
            return
        commandDefinitions = ui.commandDefinitions
        #check the command exists or not
        cmdDef = commandDefinitions.itemById('Prato')
        if not cmdDef:
            cmdDef = commandDefinitions.addButtonDefinition('Prato',
                    'Criar Prato',
                    'Criar Prato.',
                    '') 

        onCommandCreated = PratoCommandCreatedHandler()
        cmdDef.commandCreated.add(onCommandCreated)
        # keep the handler referenced beyond this function
        handlers.append(onCommandCreated)
        inputs = adsk.core.NamedValues.create()
        cmdDef.execute(inputs)

        # prevent this module from being terminate when the script returns, because we are waiting for event handlers to fire
        adsk.autoTerminate(False)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
