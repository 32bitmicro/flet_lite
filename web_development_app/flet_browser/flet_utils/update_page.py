import flet


def update_page(page:flet.Page, update_content:dict):
    for p in update_content['props']:
        if hasattr(page, p):
            setattr(page, p, update_content['props'][p])
    

    if update_content['appbar_class_props'] != {}:
        pass