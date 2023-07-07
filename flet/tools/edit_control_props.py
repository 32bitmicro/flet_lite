import flet



def edit_control_props (control):
    """Edit control props, so for example change: change `flet.MainAxxesAlignment.CENTER` into `center`"""
    
    for i in control.__dict__:
        if control.__dict__[i] == flet.MainAxisAlignment.CENTER or control.__dict__[i] == flet.TextAlign.CENTER:
            control.__dict__[i] = "center"