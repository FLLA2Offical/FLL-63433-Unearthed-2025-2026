from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait


hub = PrimeHub()
leftWheel   = Motor(Port.D, Direction.COUNTERCLOCKWISE)
rightWheel  = Motor(Port.C, Direction.CLOCKWISE)
wheelsize   = 62.4
axletrackwidth = 110
#robot and robot initial settings
robot = DriveBase(leftWheel,rightWheel,wheelsize,axletrackwidth)
robot.settings(straight_speed=600,straight_acceleration=300,turn_rate=300,turn_acceleration=200)

#left attachment motor
LAM = Motor(Port.B,Direction.COUNTERCLOCKWISE)
#right attachment motor
RAM = Motor(Port.F,Direction.COUNTERCLOCKWISE)

#Turn on Gyro Sensor if the hub is good, turn off if it is bad
robot.use_gyro(True)
hub.imu.reset_heading(0)

async def main():
   if hub.imu.ready():

        await robot.straight(540)
        await multitask(RAM.run_angle(100,-100),robot.straight(-100))
        await RAM.run_angle(1200,250)
        await robot.turn(-90)
        await robot.straight(50)
        await robot.turn(90)
        await robot.straight(400)
        await robot.straight(200)
        await robot.turn(30)
        await robot.turn(-30)
        await robot.straight(-150)
        await robot.turn(-90)
        await robot.straight(90)
        await robot.turn(90)
        robot.settings(straight_speed=500,straight_acceleration=600,turn_rate=400,turn_acceleration=200 )
        await robot.straight(360)
        await robot.turn(90)
        await robot.straight(128)
        await robot.straight(-20)
        await robot.turn(15)
        await robot.straight(52)
        await robot.turn(-30) 
        await robot.straight(-7)
        await LAM.run_angle(10000,1250)
        robot.settings(straight_speed=1000,straight_acceleration=2000,turn_rate=600,turn_acceleration=200 )
        await robot.straight(-100)
        await robot.turn(-90)
        await robot.straight(500)
        await robot.turn(60)
        await robot.straight(475)
# Runs the main program from start to finish.
run_task(main())