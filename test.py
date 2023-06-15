from flet import *
import flet


def main (page:flet.Page):
    print("here!")
    page.add(Text("gg"))

flet.app(target=main)