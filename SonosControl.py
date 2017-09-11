import soco
import sys

print "started"

listOfZones = list(soco.discover())

for i in range(len(listOfZones)):
    print listOfZones[i].player_name

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

def pauseAll():
    try:
        for i in range(len(listOfZones)):
            listOfZones[i].pause()
        return 1
    except:
        print "failed"
        return 0
    print "Skipped current song on all zones"

def playAll():
    try:
        for i in range(len(listOfZones)):
            listOfZones[i].play()
        return 1
    except:
        print "failed"
        return 0
    print "Skipped current song on all zones"

def play_nextAll():
    try:
        for i in range(len(listOfZones)):
            listOfZones[i].next()
        return 1
    except:
        print "failed"
        return 0
    print "Skipped current song on all zones"

def play_previousAll():
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
        #for i in range(len(listOfZones)):
            #print listOfZones[i].get_current_transport_info()['current_transport_state']
        return listOfZones[0].get_current_transport_info()['current_transport_state']
    except:
        print "failed"
        return 0
    print "Skipped current song on all zones"

def setZoneVolumeEqual():
    try:
        for i in range(1,len(listOfZones)):
            listOfZones[i].volume = listOfZones[i-1].volume
    except:
        print "failed"
        return 0
    print "All zones volume equal"
    return 1


def volumeUpAll():
    setZoneVolumeEqual()
    try:
        for i in range(len(listOfZones)):
            listOfZones[i].volume = listOfZones[i].volume + 5
        print "Volume++"
        return 1
    except:
        print "failed"
        return 0

def volumeDownAll():
    setZoneVolumeEqual()
    try:
        for i in range(len(listOfZones)):
            listOfZones[i].volume = listOfZones[i].volume - 5
        print "Volume--"
        return 1
    except:
        print "failed"
        return 0

def isPlayingAll():
    if getStatus() == 'PLAYING':
        return 1
    else:
        return 0


#Individual players
def pause(name):
    try:
        for i in range(len(listOfZones)):
            if (listOfZones[i].player_name == name):
                listOfZones[i].pause()
                return 1
    except:
        print "failed"
        return 0
    
    print "failed"
    return 0

def play(name):
    try:
        for i in range(len(listOfZones)):
            if (listOfZones[i].player_name == name):
                listOfZones[i].play()
                return 1
    except:
        print "failed"
        return 0
    print "failed"
    return 0

def play_next(name):
    try:
        for i in range(len(listOfZones)):
            if (listOfZones[i].player_name == name):
                listOfZones[i].next()
                return 1
    except:
        print "failed"
        return 0
    return 0

def play_previous(name):
    try:
        for i in range(len(listOfZones)):
            if (listOfZones[i].player_name == name):
                listOfZones[i].previous()
                return 1
    except:
        print "failed"
        return 0
    return 0

def getStatus(name):
    try:
        for i in range(len(listOfZones)):
            if (listOfZones[i].player_name == name):
                return listOfZones[i].get_current_transport_info()['current_transport_state']
    except:
        print "failed"
        return 0
    return 0

def volumeUp(name):
    try:
        for i in range(len(listOfZones)):
            if (listOfZones[i].player_name == name):
                listOfZones[i].volume = listOfZones[i].volume + 5
                print "Volume++"
                return 1
    except:
        print "failed"
        return 0
    return 0

def volumeDown(name):
    try:
        for i in range(len(listOfZones)):
            if (listOfZones[i].player_name == name):
                listOfZones[i].volume = listOfZones[i].volume - 5
                print "Volume--"
                return 1
    except:
        print "failed"
        return 0
    return 0

def isPlaying(name):
    for i in range(len(listOfZones)):
        if (listOfZones[i].player_name == name):
            if listOfZones[i].get_current_transport_info()['current_transport_state'] == 'PLAYING':
                return 1
        else:
            return 0

if __name__=="__main__":
    main()
