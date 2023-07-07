import flet



def manage_clean_request (control_number, main_class):
    if f"{control_number}".lower() == "page":
        main_class.page.clean()
        main_class.page.update()
    else:
        if f"{control_number}" in dict(main_class.all_controls):
            control : flet.Control = main_class.all_controls[f"{control_number}"]
            control.clean()
            if control.page != None:
                control.update()