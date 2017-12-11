"""
Display a count down until the new years.

Author: Michael B. Kulik

image release under creative commons at
https://commons.wikimedia.org/wiki/File%3AFireworks_-_Adelaide_Skyshow_2010.jpg
"""

from datetime import datetime
from guizero import App, Text, Picture

NEW_YEARS = datetime(datetime.today().year + 1, 1, 1)

def tick():
    """
    calculate new duration until new years and update text label
    """
    diff = NEW_YEARS - NEW_YEARS.now()

    if diff.total_seconds() > 0:
        text.set(diff)
        text.after(10, tick)
    else:
        text.set("HAPPY NEW YEAR!")
        picture.set('fireworks.gif')

if __name__ == '__main__':
    app = App(title="New Year Countdown Clock", height=800, width=1024)
    text = Text(app, text='', size=30)
    picture = Picture(app, image='')
    text.after(10, tick)
    app.display()
