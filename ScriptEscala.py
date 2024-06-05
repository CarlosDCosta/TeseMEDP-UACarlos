# Author-
# Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def copyPasteBody(comp, body):
    """Pass in component paste in to and body to paste"""
    copyPasteBody = comp.features.copyPasteBodies.add(body)
    return copyPasteBody

def createNewComponent(name='', activ=False):
    """This function will create a new component. To name it something specific, pass it
    as name of your choice. To activate it make activ = True. It defaults to False and
    is an optional argument."""
    app = adsk.core.Application.get()
    design = app.activeProduct
    rootComp = design.rootComponent
    # Create new component
    newComp = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    # Activate the new component
    if activ:
        newComp.activate()
    # Get the new component
    revComp = newComp.component
    # Rename the new component
    if name:
        revComp.name = name
    return revComp

def pointDistance(x1, y1, z1, x2, y2, z2):
    import math
    distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2))
    return distance

def scaleBody(body, xScale, yScale, zScale):
    app = adsk.core.Application.get()
    # Get the parent component for the scaling feature
    comp = body.parentComponent
    # Create body collection
    bodies = adsk.core.ObjectCollection.create()
    bodies.add(body)
    
    vPoint = body.vertices
    dist = float('inf')
    minPoint = body.boundingBox.minPoint
    x1 = minPoint.x
    y1 = minPoint.y
    z1 = minPoint.z
    # Find the closest vertex to boundingBox.minPoint
    for i in vPoint:
        d = pointDistance(x1, y1, z1, i.geometry.x, i.geometry.y, i.geometry.z)
        if d < dist:
            dist = d
            dPoint = i
    # Set the scale point equal to the closest vertex
    scalePoint = dPoint
    # Get the scale features from the parent component
    scaleFeatures = comp.features.scaleFeatures
    # Create the inputs for the scale
    input = scaleFeatures.createInput(bodies, scalePoint, adsk.core.ValueInput.createByReal(1.0))
    # Set the scale to be non-uniform
    x = adsk.core.ValueInput.createByReal(xScale)
    y = adsk.core.ValueInput.createByReal(yScale)
    z = adsk.core.ValueInput.createByReal(zScale)
    input.setToNonUniform(x, y, z)
    # Add the scaling feature
    scaleFeature = scaleFeatures.add(input)
    return body

try:
    app = adsk.core.Application.get()
    ui = app.userInterface

    # Select body
    body = ui.selectEntity('Select a body', 'Bodies').entity

    # Create new component for tray layout
    newComp = createNewComponent('Tray Layout', True)

    # Paste in first occurrence
    seedBody = body
    newBody = copyPasteBody(newComp, seedBody)
    newBody = newComp.bRepBodies.item(0)

    drying_shrinkage = 9.0  # Example value, replace with actual input
    sintering_shrinkage = 8.0  # Example value, replace with actual input
      
    # Calculate total shrinkage
    total_shrinkage = drying_shrinkage + sintering_shrinkage

    # Calculate scaling factor
    scaling_factor = 1.0 - (total_shrinkage / 100.0)
    
    # Scale the body
    scaled_body = scaleBody(newBody, scaling_factor, scaling_factor, scaling_factor)
    print(scaled_body)

except Exception as e:
    if ui:
        ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
