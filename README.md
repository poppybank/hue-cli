# hue-cli
A command line utility for controlling Philips Hue lighting

usage: hue.py [-h] [-room ROOM] [-brightness BRIGHTNESS]
              [-rooms ROOMS [ROOMS ...]] [--on | --off | --state] [--connect]
              [--showrooms]

Do the hue that you do so well

optional arguments:
  -h, --help            show this help message and exit
  -room ROOM
  -brightness BRIGHTNESS, --brightness BRIGHTNESS
                        set the room brightness
  -rooms ROOMS [ROOMS ...]
                        multiple rooms to apply commands to
  --on                  turn on the lights
  --off                 turn off the lights
  --state               return room lighting state
  --connect             connect to the bridge
  --showrooms           list the available rooms
