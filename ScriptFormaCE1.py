#Author- Carlos Costa
#Description- Cria um vaso com sketches de circulos que se pode editar a altura e diametro 

import adsk.core, adsk.fusion, adsk.cam, traceback, math

# Função para calcular o raio a partir da circunferência
def raio_da_circunferencia(circunferencia):
    return circunferencia / (2 * math.pi)

def Tese_Forma():
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
    defaultInputDB = '20 cm'
    parameterName1 = 'Diametro_Base'
    newInputDB = ui.inputBox('Inserir valor do Diâmetro Base:', 'Novo Valor', defaultInputDB)
    realInputDB = unitsMgr.evaluateExpression(newInputDB[0], unitsMgr.defaultLengthUnits)
    realValueInputDB = adsk.core.ValueInput.createByReal(realInputDB)
    # Altura
    defaultInputAB = '0 cm'
    parameterNameA1 = 'Altura_Base'
    newInputAB = ui.inputBox('Inserir valor da Altura da Base (convem ser 0):', 'Novo Valor', defaultInputAB)
    realInputAB = unitsMgr.evaluateExpression(newInputAB[0], unitsMgr.defaultLengthUnits)
    realValueInputAB = adsk.core.ValueInput.createByReal(realInputAB)
    Altura1 = (0, 0, realValueInputAB.realValue)
    # Dispersão
    defaultInputDispB = str(realValueInputDB.realValue - 1) + ' cm'
    parameterNameDisp1 = 'Dispersao_Base'
    newInputDispB = ui.inputBox('Inserir valor da Dispersão da Base:', 'Novo Valor', defaultInputDispB)
    realInputDispB = unitsMgr.evaluateExpression(newInputDispB[0], unitsMgr.defaultLengthUnits)
    realValueInputDispB = adsk.core.ValueInput.createByReal(realInputDispB)

    # 2º Sketch
    # Diâmetro
    defaultInputDI1 = '25 cm'
    parameterName2 = 'Diametro_Intermedio1'
    newInputDI1 = ui.inputBox('Inserir valor do Primeiro Diâmetro da Base-Centro:', 'Novo Valor', defaultInputDI1)
    realInputDI1 = unitsMgr.evaluateExpression(newInputDI1[0], unitsMgr.defaultLengthUnits)
    realValueInputDI1 = adsk.core.ValueInput.createByReal(realInputDI1)
    # Altura
    defaultInputAI1 = '15 cm'
    parameterNameA2 = 'Altura_Intermedia1'
    newInputAI1 = ui.inputBox('Inserir valor da Altura da Base-Centro:', 'Novo Valor', defaultInputAI1)
    realInputAI1 = unitsMgr.evaluateExpression(newInputAI1[0], unitsMgr.defaultLengthUnits)
    realValueInputAI1 = adsk.core.ValueInput.createByReal(realInputAI1)
    Altura2 = (0, 0, realValueInputAI1.realValue)
    # Dispersão
    defaultInputDispI1 = str(realValueInputDI1.realValue - 1) + ' cm'
    parameterNameDisp2 = 'Dispersao_Intermedia1'
    newInputDispI1 = ui.inputBox('Inserir valor da Dispersão da Base-Centro:', 'Novo Valor', defaultInputDispI1)
    realInputDispI1 = unitsMgr.evaluateExpression(newInputDispI1[0], unitsMgr.defaultLengthUnits)
    realValueInputDispI1 = adsk.core.ValueInput.createByReal(realInputDispI1)

    # 3º Sketch
    # Diâmetro
    defaultInputDI2 = '20 cm'
    parameterName3 = 'Diametro_Intermedio2'
    newInputDI2 = ui.inputBox('Inserir valor do Diâmetro do Centro:', 'Novo Valor', defaultInputDI2)
    realInputDI2 = unitsMgr.evaluateExpression(newInputDI2[0], unitsMgr.defaultLengthUnits)
    realValueInputDI2 = adsk.core.ValueInput.createByReal(realInputDI2)
    # Altura
    defaultInputAI2 = '20 cm'
    parameterNameA3 = 'Altura_Intermedia2'
    newInputAI2 = ui.inputBox('Inserir valor da Altura do Centro:', 'Novo Valor', defaultInputAI2)
    realInputAI2 = unitsMgr.evaluateExpression(newInputAI2[0], unitsMgr.defaultLengthUnits)
    realValueInputAI2 = adsk.core.ValueInput.createByReal(realInputAI2)
    Altura3 = (0, 0, realValueInputAI2.realValue)
    # Dispersão
    defaultInputDispI2 = str(realValueInputDI2.realValue - 1) + ' cm'
    parameterNameDisp3 = 'Dispersao_Intermedia2'
    newInputDispI2 = ui.inputBox('Inserir valor da Dispersão do Centro:', 'Novo Valor', defaultInputDispI2)
    realInputDispI2 = unitsMgr.evaluateExpression(newInputDispI2[0], unitsMgr.defaultLengthUnits)
    realValueInputDispI2 = adsk.core.ValueInput.createByReal(realInputDispI2)

    # 4º Sketch
    # Diâmetro
    defaultInputDI3 = '20 cm'
    parameterName4 = 'Diametro_Intermedio3'
    newInputDI3 = ui.inputBox('Inserir valor do Diâmetro do Centro-Topo:', 'Novo Valor', defaultInputDI3)
    realInputDI3 = unitsMgr.evaluateExpression(newInputDI3[0], unitsMgr.defaultLengthUnits)
    realValueInputDI3 = adsk.core.ValueInput.createByReal(realInputDI3)
    # Altura
    defaultInputAI3 = '30 cm'
    parameterNameA4 = 'Altura_Intermedia3'
    newInputAI3 = ui.inputBox('Inserir valor da ALtura do Centro-Topo:', 'Novo Valor', defaultInputAI3)
    realInputAI3 = unitsMgr.evaluateExpression(newInputAI3[0], unitsMgr.defaultLengthUnits)
    realValueInputAI3 = adsk.core.ValueInput.createByReal(realInputAI3)
    Altura4 = (0, 0, realValueInputAI3.realValue)
    # Dispersão
    defaultInputDispI3 = str(realValueInputDI3.realValue - 1) + ' cm'
    parameterNameDisp4 = 'Dispersao_Intermedia3'
    newInputDispI3 = ui.inputBox('Inserir valor da Dispersão do Centro-Topo:', 'Novo Valor', defaultInputDispI3)
    realInputDispI3 = unitsMgr.evaluateExpression(newInputDispI3[0], unitsMgr.defaultLengthUnits)
    realValueInputDispI3 = adsk.core.ValueInput.createByReal(realInputDispI3)

    # 5º Sketch
    # Diâmetro
    defaultInputDT = '30 cm'
    parameterName5 = 'Diametro_Topo'
    newInputDT = ui.inputBox('Inserir valor do Diâmetro Topo:', 'Novo Valor', defaultInputDT)
    realInputDT = unitsMgr.evaluateExpression(newInputDT[0], unitsMgr.defaultLengthUnits)
    realValueInputDT = adsk.core.ValueInput.createByReal(realInputDT)
    # Altura
    defaultInputAT = '40 cm'
    parameterNameA5 = 'Altura_Topo'
    newInputAT = ui.inputBox('Inserir valor da Altura do Topo:', 'Novo Valor', defaultInputAT)
    realInputAT = unitsMgr.evaluateExpression(newInputAT[0], unitsMgr.defaultLengthUnits)
    realValueInputAT = adsk.core.ValueInput.createByReal(realInputAT)
    Altura5 = (0, 0, realValueInputAT.realValue)
    # Dispersão
    defaultInputDispT = str(realValueInputDT.realValue - 1) + ' cm'
    parameterNameDisp5 = 'Dispersao_Topo'
    newInputDispT = ui.inputBox('Inserir valor da Dispersão do Topo:', 'Novo Valor', defaultInputDispT)
    realInputDispT = unitsMgr.evaluateExpression(newInputDispT[0], unitsMgr.defaultLengthUnits)
    realValueInputDispT = adsk.core.ValueInput.createByReal(realInputDispT)

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
    num_points = 20
    
    # Esboço 1
    sketch1 = sketches.add(xz_plane)

    # Adicionar círculos
    center_point1 = adsk.core.Point3D.create(Altura1[0], Altura1[1], Altura1[2])
    circle1 = sketch1.sketchCurves.sketchCircles.addByCenterRadius(center_point1, realValueInputDB.realValue)
    circle1.isConstruction = True


    inwardcircle1 = sketch1.sketchCurves.sketchCircles.addByCenterRadius(center_point1, ((realValueInputDispB.realValue)/2))
    inwardcircle1.isConstruction = True
    
    # Adicionando as dimensões
    dim1 = sketch1.sketchDimensions.addDiameterDimension(circle1, adsk.core.Point3D.create(Altura1[0], Altura1[1], Altura1[2] + realValueInputDB.realValue))
    dim1.parameter.expression = userParam1.name
    dimOffset1 = sketch1.sketchDimensions.addDiameterDimension(inwardcircle1, adsk.core.Point3D.create(Altura1[0], Altura1[1], Altura1[2] + realValueInputDispB.realValue))
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

    inwardcircle2 = sketch2.sketchCurves.sketchCircles.addByCenterRadius(center_point2, ((realValueInputDispI1.realValue)/2))
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
    dimOffset2 = sketch2.sketchDimensions.addDiameterDimension(inwardcircle2, adsk.core.Point3D.create(Altura2[0], Altura2[1], Altura2[2] + realValueInputDispI1.realValue))
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

    inwardcircle3 = sketch3.sketchCurves.sketchCircles.addByCenterRadius(center_point3, ((realValueInputDispI2.realValue)/2))
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
    dimOffset3 = sketch3.sketchDimensions.addDiameterDimension(inwardcircle3, adsk.core.Point3D.create(Altura3[0], Altura3[1], Altura3[2] + realValueInputDispI2.realValue))
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

    inwardcircle4 = sketch4.sketchCurves.sketchCircles.addByCenterRadius(center_point4, ((realValueInputDispI3.realValue)/2))
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
    dimOffset4 = sketch4.sketchDimensions.addDiameterDimension(inwardcircle4, adsk.core.Point3D.create(Altura4[0], Altura4[1], Altura4[2] + realValueInputDispI3.realValue))
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

    inwardcircle5 = sketch5.sketchCurves.sketchCircles.addByCenterRadius(center_point5, ((realValueInputDispT.realValue)/2))
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
    dimOffset5 = sketch5.sketchDimensions.addDiameterDimension(inwardcircle5, adsk.core.Point3D.create(Altura5[0], Altura5[1], Altura5[2] + realValueInputDispT.realValue))
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
    thicken_input = thicken_features.createInput(faceCol,adsk.core.ValueInput.createByReal(0.08),False,adsk.fusion.FeatureOperations.NewBodyFeatureOperation, True)
    thickness_value = adsk.core.ValueInput.createByReal(0.1)  # Defina a espessura desejada
    thicken_input.thickness = thickness_value
    thicken_input.isSolid = True 

    # Adicionar a espessura à superfície costurada
    thicken_feature = thicken_features.add(thicken_input)

    # Atualizar a visualização
    app.activeViewport.refresh()

def run(context):
    try:
        Tese_Forma()
    except Exception as e:
        ui = None
        app = adsk.core.Application.get()
        if app:
            ui = app.userInterface
            ui.messageBox('Falha:\n{}'.format(traceback.format_exc()))

def stop(context):
    app = adsk.core.Application.get()
    if app.userInterface:
        app.userInterface.messageBox('Parado')

if __name__ == '__main__':
    run(adsk.fusion.Design().activeProduct)
