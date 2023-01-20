from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309
from pathlib import Path
import time
import random

from PIL import Image, ImageDraw, ImageShow

serial = spi(device=0, port=0)

device = ssd1309(serial)

# with canvas(device) as draw:
#     img_path = str(Path(__file__).resolve().parent.joinpath('images', 'eyes_questioning.png'))
#     plaatje = Image.open(img_path).convert(device.mode)
#     draw.bitmap((0,0), plaatje, fill="white")

def displayImage(message):
    with canvas(device) as draw:
        img_path = str(Path(__file__).resolve().parent.joinpath('images', message))
        plaatje = Image.open(img_path).convert(device.mode)
        draw.bitmap((0,0), plaatje, fill="white")
        time.sleep(1)

while True:
    action=random.randint(0,20)
    print(action)
    if action==1:
        displayImage('eyes_blink.png')
    if action==2:
        displayImage('eyes_cry.png')
    if action==3:
        displayImage('eyes_distressed.png')
    if action==4:
        displayImage('eyes_down.png')
    if action==5:
        displayImage('eyes_front.png')
    if action==6:
        displayImage('eyes_glare.png')
    if action==7:
        displayImage('eyes_happy.png')
    if action==8:
        displayImage('eyes_left.png')
    if action==9:
        displayImage('eyes_lowered_lids.png')
    if action==10:
        displayImage('eyes_middle.png')
    if action==11:
        displayImage('eyes_narrow.png')
    if action==12:
        displayImage('eyes_questioning.png')
    if action==13:
        displayImage('eyes_right.png')
    if action==14:
        displayImage('eyes_tired.png')
    if action==15:
        displayImage('eyes_up.png')
    if action==16:
        displayImage('eyes_wide.png')
    if action==17:
        displayImage('eyes_happy_blink.png')
    if action==18:
        displayImage('eyes_heart.png')