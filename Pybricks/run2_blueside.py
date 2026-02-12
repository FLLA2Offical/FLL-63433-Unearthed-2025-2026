from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task


hub = PrimeHub()
leftWheel   = Motor(Port.D, Direction.COUNTERCLOCKWISE)
rightWheel  = Motor(Port.C, Direction.CLOCKWISE)
wheelsize   = 62.4
axletrackwidth = 110
#robot and robot initial settings
robot = DriveBase(leftWheel,rightWheel,wheelsize,axletrackwidth)
robot.settings(straight_speed=400,straight_acceleration=200,turn_rate=400,turn_acceleration=200 )

#left attachment motor
LAM = Motor(Port.B, Direction.COUNTERCLOCKWISE)
#right attachment motor
RAM = Motor(Port.F,Direction.COUNTERCLOCKWISE)

#Turn on Gyro Sensor if the hub is good, turn off if it is bad
robot.use_gyro(True)
hub.imu.reset_heading(0)

async def main():
        print("running")
        if hub.imu.ready():
                hub.display.number(0)
                await robot.straight(165)
                hub.display.number(1)
                await robot.turn(-65)
                hub.display.number(2)
                await robot.straight(410)
                hub.display.number(3)
                await RAM.run_angle(-500,200)
                await robot.straight(4)
                await RAM.run_angle(500,200)
                await robot.straight(-50)
                hub.display.number(5)
                await robot.turn(10)
                await RAM.run_angle(-500,200)
                hub.display.number(6)
                await robot.straight(-200)
                hub.display.number(7)
                await robot.turn(5)
                await robot.straight(-155)
                hub.display.number(8)
                await robot.straight(5)
                await RAM.run_angle(830,200)
                hub.display.number(9)
                await robot.straight(-195)
                hub.display.number(10)
                await robot.turn(5)
                hub.display.number(11)
                await robot.straight(390)
                hub.display.number(12)
                await robot.turn(-75)
                hub.display.number(13)
                await robot.straight(-200)
                await robot.turn(75)
                hub.display.number(14)
                await robot.straight(-400)
                hub.display.number(15)
                await robot.turn(-50)
                hub.display.number(16)
                await robot.straight(635)
                hub.display.number(17)
                await robot.turn(85)
                hub.display.number(18)
                await robot.straight(200)
                hub.display.number(19)
                await robot.turn(20)
                hub.display.number(20)
                await robot.straight(-100)
                
# Runs the main program from start to finish.
run_task(main())
