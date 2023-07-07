from flet_utils.flet_control_generator import generate_flet_control
from flet_utils.control_coder import dict_to_control
from flet_utils.append_to_content import append_view_into_content




def manage_add_request (controls:list, main_class):
    for con in controls:
        parent = con['parent']
        control = generate_flet_control(control_dict=con, main_class=main_class)
        if str(parent).lower() == "page":
            main_class.page.controls.append(control)
            main_class.parents_of_controls[control] = parent
        else:
            # if the givin parent is a flet_lite_control_number
            if str(parent) in main_class.all_controls:
                parent_control = main_class.all_controls[f"{parent}"]
                append_view_into_content(control=control, parent_control=parent_control)
    
        main_class.parents_of_controls[control] = parent
        main_class.all_controls[f'{control.flet_lite_number}'] = control
    main_class.page.update()