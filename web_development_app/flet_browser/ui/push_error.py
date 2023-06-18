import flet




def show_error_content (page:flet.Page, error:str):
    page.controls.clear()
    page.update()
    page.add(flet.Column([
        flet.Row([flet.Icon(color=flet.colors.RED, name=flet.icons.INFO_OUTLINE_ROUNDED)],alignment="center"),
        flet.Row([flet.Text(error, expand=True, color="red", text_align=flet.TextAlign.CENTER)], alignment="center")
    ]))
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.update()