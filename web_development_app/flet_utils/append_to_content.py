




def append_view_into_content (control, parent_control):
    """This will add the control into the parent controls or content"""
    if hasattr(parent_control, "controls"):
        setattr(control, "parent_class", parent_control)
        parent_control.controls.append(control)
    elif hasattr(parent_control, "content"):
        setattr(control, "parent_class", parent_control)
        parent_control.content = control
    
    control.parent_class = parent_control