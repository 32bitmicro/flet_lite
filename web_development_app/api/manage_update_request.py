





def manage_update_request (control_number, main_class, updated_control_content):
    if str(control_number) not in main_class.all_controls: return

    control = main_class.all_controls[f"{control_number}"]

    for I in updated_control_content:
        if str(I).startswith("__"): pass
        else:
            if hasattr(control, I):
                setattr(control, I, updated_control_content[I])
    
    if control.page != None:
        control.update()