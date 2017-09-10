import soco
import sys

print "started"

listOfZones = list(soco.discover())

def printZones():
    try:
        for i in range(len(listOfZones)):
            print listOfZones[i].player_name
        return 1
    except:
        print "failed"
        return 0
    print "Skipped current song on all zones"

#Main determines what mode to run in
def main(argv=sys.argv):
    print argv[1] #debug
    if len(listOfZones) == 0:
        print "No zones found"
        return
    try:
        if argv[1] == "next": #play next file
            play_next()
        elif argv[1] == "prev":
            play_previous()
        elif argv[1] == "list":
            printZones()
        elif argv[1] == "status":
            getStatus()
        elif argv[1] == "pause":
            pause()
        elif argv[1] == "play":
            play()
        else:
            print "Run with commands next, prev, list, status, play or pause"
    except:
        print "Failed"

def pause():
    try:
        for i in range(len(listOfZones)):
            listOfZones[i].pause()
        return 1
    except:
        print "failed"
        return 0
    print "Skipped current song on all zones"

def play():
    try:
        for i in range(len(listOfZones)):
            listOfZones[i].play()
        return 1
    except:
        print "failed"
        return 0
    print "Skipped current song on all zones"

def play_next():
    try:
        for i in range(len(listOfZones)):
            listOfZones[i].next()
        return 1
    except:
        print "failed"
        return 0
    print "Skipped current song on all zones"

def play_previous():
    try:
        for i in range(len(listOfZones)):
            listOfZones[i].previous()
        return 1
    except:
        print "failed"
        return 0
    print "Skipped current song on all zones"

def getStatus():
    try:
        for i in range(len(listOfZones)):
            print listOfZones[i].get_current_transport_info()['current_transport_state']
        return listOfZones[0].get_current_transport_info()['current_transport_state']
    except:
        print "failed"
        return 0
    print "Skipped current song on all zones"


if __name__=="__main__":
    main()
