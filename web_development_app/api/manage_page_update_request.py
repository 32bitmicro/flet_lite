from flet_utils.appbar_coder import dict_to_appbar
from flet_utils.view_coder import dict_to_view



def manage_page_update_request (update_dict, main_class):
    for i in update_dict['props']:
            if hasattr(main_class.page, i):
                if update_dict['props'][i] != None:
                    setattr(main_class.page, i, update_dict['props'][i])
    
    if 'appbar' in update_dict:
        if update_dict['appbar'] == None:
            main_class.page.appbar = None
        else:
            main_class.page.appbar = dict_to_appbar(update_dict['appbar'])
    
    if 'views' in update_dict:
        clear_all = False
        for i in update_dict['views']:
            if i['route'] == "/":
                clear_all = True
                break
        if clear_all:
            main_class.page.views.clear()
        for v in update_dict['views']:
            main_class.page.views.append (dict_to_view(view_dict=v, main_class=main_class))