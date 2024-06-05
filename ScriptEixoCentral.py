#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        # Get the application and user interface
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)        
        
        # Get the root component
        root_comp = design.rootComponent
        
        # Initialize variables
        surface = None
        
        # Iterate through all bodies in the root component
        for body in root_comp.bRepBodies:
            for face in body.faces:
                surface = face.geometry
                if surface:
                    break
            if surface:
                break
        
        # Check if surface is found
        if surface is None:
            ui.messageBox("No suitable surface found.")
            return
        
        # Initialize variables to store the most distant points and their distances
        max_distance_x = 0
        max_distance_z = 0
        
        # Create SurfaceEvaluator for surface
        surface_evaluator = surface.evaluator
        
        # Iterate over points on the surface
        num_u_samples = 10  # Number of samples to take in the u-direction
        num_v_samples = 10  # Number of samples to take in the v-direction
        for i in range(num_u_samples):
            for j in range(num_v_samples):
                u = i / (num_u_samples - 1)  # Parameter value between 0 and 1
                v = j / (num_v_samples - 1)  # Parameter value between 0 and 1
                uv_point = adsk.core.Point2D.create(u, v)
                retVal, surface_point = surface_evaluator.getPointAtParameter(uv_point)
                if retVal:
                    # Calculate distances in x and z from the origin
                    distance_x = abs(surface_point.x)
                    distance_z = abs(surface_point.z)
                    
                    # Update maximum distances
                    if distance_x > max_distance_x:
                        max_distance_x = distance_x
                    if distance_z > max_distance_z:
                        max_distance_z = distance_z
        
        # Prepare the results string
        results = (
            f"Maximum distance in X from central axis: {max_distance_x:.2f} cm\n"
            f"Maximum distance in Z from central axis: {max_distance_z:.2f} cm"
        )
        
        # Print results in a single message box
        ui.messageBox(results)
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

