#!/usr/bin/python

import pigpio
import time
import sys, getopt

pi = pigpio.pi()
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hm:",["mode="])
    except getopt.GetoptError:
        print 'blinking.py -m <mode>'
        sys.exit(2)
    app = Mode(17, 22, 24)
    for opt, arg in opts:
        if opt == '-h':
           print 'nking.py -m <mode>'
           sys.exit()
        elif opt in ("-m", "--mode"):
           if arg == 'dissolve':
               app.dissolve()
           elif arg == 'strobe':
               app.strobe()
           else:
               print 'invalid mode'
               sys.exit(2)              
    
class Mode:
    def __init__(self, red, green, blue):
        self.pins = [red, green, blue]

    def lightColors(self,values):
        for i in range(len(self.pins)):
            pi.set_PWM_dutycycle(self.pins[i],values[i])

    def dissolve(self):
        colors=[0,128,255]
        phases=[1,1,1]
        while True:
            for i in range(len(colors)):
                if colors[i] == 255:
                  phases[i] = -1
                if colors[i] == 0:
                  phases[i] = 1
                colors[i] += phases[i]
            self.lightColors(colors)
            time.sleep(0.0001)

    def strobe(self):
        while True:
            colors = [255,255,255]
            self.lightColors(colors)
            time.sleep(0.01)        
            colors = [0,0,0]
            self.lightColors(colors)
            time.sleep(0.1)        

if __name__ == "__main__":
    main(sys.argv[1:])
