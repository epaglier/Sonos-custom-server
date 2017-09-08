import soco
import sys

print "started"

listOfZones = list(soco.discover())

#Main determines what mode to run in
def main(argv=sys.argv):
    try:
        if argv[1] == "1": #play next file
            play_next()
            print "Skipping current song"
        elif argv[1] == "2":
            print ""
    except:
        print "Run with commands 1, 2, or 3"

def play_next():
    if len(listOfZones) == 0:
        print "No zones found"
    else:
        for (i = 0; i < len(listOfZones); i++):
            listOfZones[i].next()
    print "Zones Playing Next"
        

if __name__=="__main__":
    main()
