import flet





def generate_a_control (page:flet.Page, update_content:dict):
    """Generate a flet control based on back-end host request"""
    control_data = update_content["control_data"]
    control_name = control_data['name']
    flet_class_dict = control_data['flet_class_dict']
    control = flet.__dict__[f'{control_name}']()
            
    for i in flet_class_dict:
        if hasattr(control, i):
            setattr(control, i, flet_class_dict[i])
    
    return control