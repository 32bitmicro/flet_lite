from flet import *
import time

def main(page:Page):
    page.add(Text("Opps"))

app(target=main, debug=False)