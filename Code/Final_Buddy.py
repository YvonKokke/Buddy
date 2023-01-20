from flask import Flask, request
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309
from pathlib import Path

from PIL import Image, ImageDraw, ImageShow
import time

serial = spi(device=0, port=0)

device = ssd1309(serial)

app = Flask(__name__)

wachten = 7

def displayImage(message):
    with canvas(device) as draw:
        img_path = str(Path(__file__).resolve().parent.joinpath('images', message))
        plaatje = Image.open(img_path).convert(device.mode)
        draw.bitmap((0,0), plaatje, fill="white")

def naamImage():
    displayImage('eyes_happy.png')
    time.sleep(1.5)
    displayImage('eyes_front.png')
    
def halloImage():
    displayImage('eyes_happy.png')
    time.sleep(2)
    displayImage('eyes_happy_blink.png')

def vraagImage():
    displayImage('eyes_happy.png')
    time.sleep(1)
    displayImage('eyes_left.png')
    time.sleep(0.5)
    displayImage('eyes_right.png')
    time.sleep(0.5)
    displayImage('eyes_middle.png')
    time.sleep(0.5)
    displayImage('eyes_questioning.png')

def kleurImage():
    displayImage('eyes_heart.png')
    time.sleep(1)
    displayImage('eyes_happy.png')
    time.sleep(0.5)
    displayImage('eyes_happy_blink.png')
    time.sleep(1.2)
    displayImage('eyes_front.png')
    
def dierImage():
    displayImage('eyes_heart.png')
    time.sleep(1)
    displayImage('eyes_happy.png')
    time.sleep(0.5)
    displayImage('eyes_questioning.png')

def weetNietImage():
    displayImage('eyes_happy_blink.png')
    time.sleep(1)
    displayImage('eyes_happy.png')

def verdrietigImage():
    displayImage('eyes_front.png')
    time.sleep(0.5)
    displayImage('eyes_cry.png')
    time.sleep(2)
    displayImage('eyes_distressed.png')

def vakantieLeukImageComplete():
    displayImage('eyes_front.png')
    time.sleep(0.3)
    displayImage('eyes_heart.png')
    time.sleep(1)
    displayImage('eyes_happy.png')

def vakantieLeukImageIncomplete():
    displayImage('eyes_front.png')
    time.sleep(0.3)
    displayImage('eyes_heart.png')
    time.sleep(1)
    displayImage('eyes_front.png')
    time.sleep(0.2)
    displayImage('eyes_happy.png')

def vakantieNietImage():
    displayImage('eyes_front.png')
    time.sleep(0.5)
    displayImage('eyes_happy.png')
    time.sleep(2)
    displayImage('eyes_happy_blink.png')
    time.sleep(0.8)
    displayImage('eyes_happy.png')

def vakantieJaImage():
    displayImage('eyes_front.png')
    time.sleep(0.5)
    displayImage('eyes_happy_blink.png')
    time.sleep(0.8)
    displayImage('eyes_happy.png')

def vakantieNeeImage():
    displayImage('eyes_front.png')
    time.sleep(1)
    displayImage('eyes_happy.png')
    time.sleep(2)
    displayImage('eyes_happy_blink.png')
    time.sleep(0.8)
    displayImage('eyes_happy.png')
    

@app.route('/', methods=["POST", "GET"])
def webhook():
    if request.method == "GET":
        return "Hello YouTube! - Not connected ot DiF."
    elif request.method == "POST":
        payload = request.json
        user_response = (payload['queryResult']['queryText'])
        bot_response = (payload['queryResult']['fulfillmentText'])
        intent_response = (payload['queryResult']['intent']['displayName'])
        if user_response or bot_response != "":
            #print(user_response)
            #print(bot_response)
            if intent_response != "":
                print("Intent: " + intent_response)
                # Hallo
                if intent_response == "Hallo":
                    time.sleep(wachten)
                    halloImage()
                # Naam
                if intent_response == "WieBenJij" or intent_response == "HalloNaam" or intent_response == "Hallo - Naam":
                    time.sleep(wachten)
                    naamImage()
                # Gaat goed
                if intent_response == "Hallo - Naam - GaatGoed" or intent_response == "GaatGoed":
                    time.sleep(wachten)
                    vraagImage()
                # Gaat niet goed
                if intent_response == "Hallo - Naam - GaatNietGoed":
                    time.sleep(wachten)
                    verdrietigImage()
                # Kleur
                if intent_response == "Hallo - Naam - GaatGoed - Kleur" or intent_response == "GaatGoed - Kleur":
                    time.sleep(wachten)
                    kleurImage()    
                if intent_response == "Hallo - Naam - GaatGoed - WeetNiet" or intent_response == "GaatGoed - WeetNiet":
                    time.sleep(wachten)
                    weetNietImage()
                # Dier
                if intent_response == "Hallo - Naam - GaatGoed - Kleur - WeetNiet" or intent_response == "GaatGoed - Kleur - WeetNiet":
                    time.sleep(wachten)
                    weetNietImage()
                if intent_response == "Hallo - Naam - GaatGoed - WeetNiet - WeetNiet" or intent_response == "GaatGoed - WeetNiet - WeetNiet":
                    time.sleep(wachten)
                    weetNietImage()
                if intent_response == "Hallo - Naam - GaatGoed - Kleur - Dier" or intent_response == "GaatGoed - Kleur - Dier":
                    time.sleep(wachten)
                    dierImage()
                if intent_response == "Hallo - Naam - GaatGoed - WeetNiet - Dier" or intent_response == "GaatGoed - WeetNiet - Dier":
                    time.sleep(wachten)
                    dierImage()
                # Leuke vakantie compleet
                if intent_response == "Hallo - Naam - GaatGoed - Kleur - Dier - VakantieLeuk" or intent_response == "GaatGoed - Kleur - Dier - VakantieLeuk":
                    time.sleep(wachten)
                    vakantieLeukImageComplete()
                # Leuke vakantie incompleet
                if intent_response == "Hallo - Naam - GaatGoed - WeetNiet - WeetNiet - VakantieLeuk" or intent_response == "GaatGoed - WeetNiet - WeetNiet - VakantieLeuk":
                    time.sleep(wachten)
                    vakantieLeukImageIncomplete()
                if intent_response == "Hallo - Naam - GaatGoed - Kleur - WeetNiet - VakantieLeuk" or intent_response == "GaatGoed - Kleur - WeetNiet - VakantieLeuk":
                    time.sleep(wachten)
                    vakantieLeukImageIncomplete()
                if intent_response == "Hallo - Naam - GaatGoed - WeetNiet - Dier - VakantieLeuk" or intent_response == "GaatGoed - WeetNiet - Dier - VakantieLeuk":
                    time.sleep(wachten)
                    vakantieLeukImageIncomplete()
                # Vakantie niks te doen
                if intent_response == "Hallo - Naam - GaatGoed - Kleur - Dier - VakantieNiet" or intent_response == "GaatGoed - Kleur - Dier - VakantieNiet":
                    time.sleep(wachten)
                    vakantieNietImage()
                if intent_response == "Hallo - Naam - GaatGoed - Kleur - WeetNiet - VakantieNiet" or intent_response == "GaatGoed - Kleur - WeetNiet - VakantieNiet":
                    time.sleep(wachten)
                    vakantieNietImage()
                if intent_response == "Hallo - Naam - GaatGoed - WeetNiet - Dier - VakantieNiet" or intent_response == "GaatGoed - WeetNiet - Dier - VakantieNiet":
                    time.sleep(wachten)
                    vakantieNietImage()
                if intent_response == "Hallo - Naam - GaatGoed - WeetNiet - WeetNiet - VakantieNiet" or intent_response == "GaatGoed - WeetNiet - WeetNiet - VakantieNiet":
                    time.sleep(wachten)
                    vakantieNietImage()
                # Vakantie uitrusten
                if intent_response == "Hallo - Naam - GaatGoed - Kleur - Dier - Vakantie - Ja" or intent_response == "GaatGoed - Kleur - Dier - Vakantie - Ja":
                    time.sleep(wachten)
                    vakantieJaImage()
                # Vakantie niet uitrusten
                if intent_response == "Hallo - Naam - GaatGoed - Kleur - Dier - Vakantie - Nee" or intent_response == "GaatGoed - Kleur - Dier - Vakantie - Nee":
                    time.sleep(wachten)
                    vakantieNeeImage()
        return "Message received."
    else:
        print(request.data)
        return "200"

#if __name__ == '__main__':
    #app.run(debug=True)