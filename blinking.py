import pigpio
import time
pi = pigpio.pi()

class Mode:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
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
            pi.set_PWM_dutycycle(self.red,colors[0])
            pi.set_PWM_dutycycle(self.green,colors[1])
            pi.set_PWM_dutycycle(self.blue,colors[2])
            time.sleep(0.0001)
if __name__ == "__main__":
    app = Mode(17, 22, 24)
    app.dissolve()

