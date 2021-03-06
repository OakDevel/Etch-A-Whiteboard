# +---------------------------------------------------------------------------+
# |                         Etch-A-Whiteboard driver                          |
# |                               Nate Foss                                   |
# |                                5/24/16                                    |
# |                          TJHSST Robotics Lab                              |
# +---------------------------------------------------------------------------+
import sys
#import RPi.GPIO as GPIO
import time
import Movement

###################################START OF PROGRAM#############################
#===============================< MAIN >========================================
def main():
    Movement.initSteppers()

    filename = sys.argv[1]
    print('Reading from file', filename)
    f = open ( filename )

    line = f.readLine()
    while(line):
        print(line)
        Movement.parseLine(line.strip().split())
        line = f.readLine()
#------------------------------------------------------------Etch-A-Whiteboard--
if __name__ == '__main__': main()
#############################< END OF PROGRAM >#################################