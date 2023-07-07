import flet




def get_all_subControls_on_the_page (parent:flet.Control):
    """
    Get all the sub controls of all parents (such as Rows, Columns, Containers, etc..)
    
    This function also will make the parent adopt its childs by set `control.parent = <parent class>`
    """
    all_sub_controls = []
    if hasattr(parent, "controls"):
        for I in parent.controls:
            all_sub_controls.append(I)
            
            if not hasattr(I, "parent"):
                setattr(I, "parent", parent)
            
            if not hasattr(I, "page"):
                setattr(I, "page", parent.page)

            for i in get_all_subControls_on_the_page(I):
                all_sub_controls.append(i)
    elif hasattr(parent, "content"):
        if parent.content != None:
            all_sub_controls.append(parent.content)
            if not hasattr(parent.content, "parent"):
                    setattr(parent.content, "parent", parent)
            if not hasattr(parent.content, "page"):
                setattr(parent.content, "page", parent.page)
            for I in get_all_subControls_on_the_page(parent.content):
                all_sub_controls.append(I)


    while None in all_sub_controls:
        all_sub_controls.remove(None)

    return all_sub_controls

if __name__ == "__main__":
    c = flet.Container(content=flet.Row([
        flet.Text("Hi"),
        flet.Column([
            flet.TextButton("dd")
        ])
    ]))

    print(get_all_subControls_on_the_page(c))