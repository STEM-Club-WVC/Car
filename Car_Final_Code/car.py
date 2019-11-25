from adafruit_servokit import ServoKit
#import Servo
#import SunFounder_PCA9685.Servo
#from SunFounder_PCA9685 import Servo

class Car():

    def __init__(self):
        self.defaultMotorAngle = 46
        self.defaultSteeringAngle = 50
        self.steeringPin = 0
        self.motorPin = 1
        self.kit = self.setupServos(self.steeringPin, self.motorPin)
        self.currentSpeed = 46;
        self.currentAngle = 50

    def setupServos(self, steeringPin, motorPin):
        kit = ServoKit(channels=16)
        #steering = Servo.Servo(steeringPin)
        #motor = Servo.Servo(motorPin)

        #Servo.Servo(steeringPin).setup()
        #Servo.Servo(motorPin).setup()

        #steering.write(self.defaultSteeringAngle)
        #motor.write(self.defaultMotorAngle)
        kit.servo[self.steeringPin].angle = self.defaultSteeringAngle
        kit.servo[self.motorPin].angle = self.defaultMotorAngle
        return kit

    def updateMovement(self, motorAngle, servoAngle):
        #self.steering.write(servoAngle)
        self.kit.servo[self.steeringPin].angle = servoAngle
        #self.motor.write(motorAngle)
        self.kit.servo[self.motorPin].angle = motorAngle
        self.currentAngle = servoAngle
        self.currentSpeed = motorAngle

    def emergencyStop(self):
        #self.motor.write(self.defaultMotorAngle)
        self.kit.servo[self.motorPin].angle = self.defaultMotorAngle
        #self.steering.write(self.defaultSteeringAngle)
        self.kit.servo[self.steeringPin].angle = self.defaultSteeringAngle
        self.currentAngle = self.defaultSteeringAngle
        self.currentSpeed = self.defaultMotorAngle
