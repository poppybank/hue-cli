#!/usr/bin/python

# Install phue and touchphat with pip3
# pip3 install phue
from phue import Bridge
import time

# The IP address of the Hue bridge and a list of lights you want to use
bridgeip = '192.168.1.139'  # <<<<<<<<<<<


# Find the room number from the room name
def getroomnumber(name):
    allrooms = b.get_group()
    roomnumber = 0
    for room in allrooms.keys():
        if allrooms[room]['name'] == name:
            roomnumber = int(room)
            break
    if roomnumber == 0:
        print('The room name you have supplied is not recognised. Please try again.')
    return roomnumber


def getroomnumbers(names):
    allrooms = b.get_group()
    result = []
    for room in allrooms.keys():
        if allrooms[room]['name'] in names:
            result += [int(room)]
    return result            



def printroomnames():
    allrooms = b.get_group()
    for room in allrooms.keys():
        print allrooms[room]['name'] + " (" + str(room) + ")"


# Identifies if any of the lamps in the room are on
# Return Value: True if any lamps are on, otherwise False
def isroomon(roomnumber):
    result = False

    roomon = b.get_group(roomnumber)
    result = roomon['state']['any_on']

    return result



## set up the command line argument parsing
import argparse

parser = argparse.ArgumentParser(description='Do the hue')


parser.add_argument('-room')
parser.add_argument('-brightness', '--brightness', type=int, default=-1, help='set the room brightness')
parser.add_argument('-rooms', nargs='+', required=False, help='multiple rooms to apply commands to')

group = parser.add_mutually_exclusive_group()
group.add_argument('--on', action='store_true', help='turn on the lights')
group.add_argument('--off', action='store_true', help='turn off the lights')
group.add_argument('--state', action='store_true', help='return room lighting state')
parser.add_argument('--connect', action='store_true', help='connect to the bridge')
parser.add_argument('--showrooms', action='store_true', help='list the available rooms')
args = parser.parse_args()


# Connect to the bridge
b = Bridge(bridgeip)

# If the --connect argument is passed, make a connection to the hue bridge
# Make sure to press the hue bridge button before running to authorize access

if args.connect:
	b.connect()

# assume no configured room
roomnum = 0
roomnums = None

if args.room:
	roomnum = getroomnumber(args.room)

if args.rooms:
    print args.rooms
    roomnums = getroomnumbers(args.rooms)
    print roomnums


if args.on:
    if roomnum > 0:
        b.set_group(roomnum, 'on', True)
        if args.brightness > 0:
            b.set_group(roomnum, 'bri', args.brightness)
    elif roomnums:
        for num in roomnums:
            b.set_group(num, 'on', True)
            if args.brightness > 0:
                b.set_group(num, 'bri', args.brightness)
else:
    if args.brightness >= 0:
        b.set_group(roomnum, 'bri', args.brightness)


if args.off:
    if roomnum > 0:
        b.set_group(roomnum, 'on', False)
    elif roomnums:
        for num in roomnums:
            b.set_group(num, 'on', False)

if args.state: 
    if roomnum > 0:
        print isroomon(roomnum) 

if args.showrooms:
        printroomnames()

