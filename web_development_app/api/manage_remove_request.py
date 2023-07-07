import flet



def manage_remove_request (control_number, main_class):
    if f"{control_number}" in main_class.all_controls:
        control = main_class.all_controls[f"{control_number}"]
        parent = main_class.parents_of_controls[control]
        parent = main_class.all_controls[f"{parent}"]

        if parent == "page":
            main_class.page.remove (control)
            main_class.page.update()
        else:
            if hasattr(parent, "controls"):
                parent.controls.remove(control)
            elif hasattr(parent, "content"):
                parent.content = None
            
            if parent.page == None:
                main_class.page.update()
            else:
                parent.update()