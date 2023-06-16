from flet import *
import flet
import time

def main (page:flet.Page):
    tf = flet.TextField(label="Hmmmm..")
    page.add(tf)

flet.app(target=main, debug=False)