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
robot.settings(straight_speed=600,straight_acceleration=300,turn_rate=200,turn_acceleration=100)

#left attachment motor
LAM = Motor(Port.B, Direction.COUNTERCLOCKWISE)
#right attachment motor
RAM = Motor(Port.F,Direction.COUNTERCLOCKWISE)

#Turn on Gyro Sensor if the hub is good, turn off if it is bad
robot.use_gyro(True)
hub.imu.reset_heading(0)

async def main():
   if hub.imu.ready():
        await RAM.run_time(-500,500)
        await robot.straight(650)
        await robot.turn(-30)
        await robot.straight(180)
        await robot.straight(-75)
        await RAM.run_time(600,450)
        await robot.turn(-14)
        await robot.straight(30)
        await RAM.run_time(600,350)
        await robot.straight(100)
        await RAM.run_time(-800,1200)
        await multitask(RAM.run_time(-800,1200),robot.straight(-120))
        # await robot.straight(-120)
        await robot.turn(45)
        await robot.straight(-900)

run_task(main())