"""
A collection of activities and locations (in Sydney) to inspire creative writing, crowdsourced from friends and peers.
"""

# Import pandas

import pandas as pd

# Read .csv files

activities = pd.read_csv(r'/home/pi/Documents/Activities.csv', encoding = "ISO-8859-1")
locations = pd.read_csv(r'/home/pi/Documents/Locations.csv', encoding = "ISO-8859-1")
strategies = pd.read_csv(r'/home/pi/Documents/Oblique_strategies.csv', encoding = "ISO-8859-1")

# Include 'Anytime' activities and locations in options for each time of day

morning_options = ['Morning','Anytime']
afternoon_options = ['Afternoon','Anytime']
evening_options = ['Evening','Anytime']

# Create activity categories by time

morning_activity = activities.loc[activities['Time'].isin(morning_options)]
afternoon_activity = activities.loc[activities['Time'].isin(afternoon_options)]
evening_activity = activities.loc[activities['Time'].isin(evening_options)]

# Create location categories by time

morning_location = locations.loc[locations['Time'].isin(morning_options)]
afternoon_location = locations.loc[locations['Time'].isin(afternoon_options)]
evening_location = locations.loc[locations['Time'].isin(evening_options)]

# Create functions to call an activity or location based on time of day

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def activity():

    if current_time >= '06:00:00' and current_time <= '12:00:00':
        return morning_activity['Activity'].sample().iloc[0]

    elif current_time > '12:00:00' and current_time <= '18:00:00':
        return afternoon_activity['Activity'].sample().iloc[0]

    elif current_time > '18:00:00' and current_time <='22:00:00':
        return evening_activity['Activity'].sample().iloc[0]

    else:
          return 'Go to bed'

def location():

    if current_time >= '06:00:00' and current_time <= '12:00:00':
        return 'Go to Beare Park'

    elif current_time > '12:00:00' and current_time <= '18:00:00':
        return afternoon_location['Location'].sample().iloc[0]

    elif current_time > '18:00:00' and current_time <='22:00:00':
        return evening_location['Location'].sample().iloc[0]

    else:
        return 'Go to bed'

def strategy():

    return strategies['Oblique_strategies'].sample().iloc[0]

# Define functions to call in app

def give_activity():
    activity_message.value = activity()

def give_location():
    location_message.value = location()

def give_strategy():
    window.show()
    strategy_message.value = strategy()
    Picture(window, image = "/home/pi/Documents/Eno_resize.png")

def exit():
    app.destroy()

# Design app

from guizero import App, Window, Text, PushButton, Picture

## Design app windows

app = App(title="Crowdsourcing creativity", layout = 'grid', bg='white')
app.set_full_screen()

window = Window(app, title="Oblique strategies", width=300, height=300, bg='white')
window.hide()

## Add button to give activity

activity_button = PushButton(app, command=give_activity, image = "/home/pi/Documents/Do_icon.png", grid=[0,0])
activity_message = Text(app, text="Do something?", size=12, font="Helvetica", grid=[1,0])

space = Text(app,text="", grid=[0,1])

## Add button to give location

location_button = PushButton(app, command=give_location, image = "/home/pi/Documents/Go_icon.png", grid=[0,2])
location_message = Text(app, text="Go somewhere?", size=12, font="Helvetica", grid=[1,2])

space = Text(app,text="", grid=[0,3])

## Add button to give oblique strategy

strategy_button = PushButton(app, command=give_strategy, text = 'Got an idea?', width = 10, grid=[0,4])
strategy_message = Text(window, text="", size=12, font="Helvetica")

space = Text(app,text="", grid=[0,5])

## Add exit button

exit_button = PushButton(app, command=exit, text='Exit', grid=[0,6])

#Boot GUI when device is shaken

import serial

ser = serial.Serial('/dev/ttyACM0',baudrate=115200,timeout=0.01)

while(True):

    x = ser.readlines()

    if len(x) > 0 and __name__ == '__main__':

        app.display()
