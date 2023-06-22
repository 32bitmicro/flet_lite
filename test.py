from flet import *
import time

def main(page:Page):
    tf = TextField(label="username")
    page.add(tf)
    page.add(TextField(label="password", password=True))
    page.add(TextField(label="suggestion"))

    time.sleep(2)

    tf.label = "no username"
    tf.disabled = True
    page.update()

app(target=main, debug=False)