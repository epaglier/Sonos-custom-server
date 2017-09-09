import soco
import sys

print "started"

listOfZones = list(soco.discover())

for i in range(len(listOfZones)):
    print listOfZones[i].name

#Main determines what mode to run in
def main(argv=sys.argv):
    try:
        if argv[1] == "1": #play next file
            play_next()
            
        elif argv[1] == "2":
            print ""
    except:
        print "Run with commands 1, 2, or 3"

def play_next():
    if len(listOfZones) == 0:
        print "No zones found"
        return
    else:
        try:
            for i in range(len(listOfZones)):
                listOfZones[i].next()
        except:
            print "failed"
    print "Skipped current song on all zones"
        

if __name__=="__main__":
    main()
