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
robot.settings(straight_speed=400,straight_acceleration=700,turn_rate=400,turn_acceleration=700 )

#left attachment motor
LAM = Motor(Port.B, Direction.COUNTERCLOCKWISE)
#right attachment motor
RAM = Motor(Port.F,Direction.COUNTERCLOCKWISE)

#Turn on Gyro Sensor if the hub is good, turn off if it is bad
robot.use_gyro(True)
hub.imu.reset_heading(0)

async def main():
   if hub.imu.ready():
        await robot.straight(755)
        await robot.turn(-57)
        await robot.straight(75)
        wait(2000)
        await robot.straight(15)
        await robot.straight(-150)
        await robot.turn(-32)
        await robot.straight(-330)
        await robot.turn(86)
        await robot.straight(100)
        await robot.turn(-20)
        await LAM.run_time(190,1100)
        await robot.straight(-40)
        robot.settings(straight_speed=400,straight_acceleration=300,turn_rate=800,turn_acceleration=800)
        await robot.turn(95)
        await LAM.run_time(-190,1000)
        await robot.turn(-95)
        await robot.straight(-755)
        

        #await multitask(RAM.run_time(200,2000),LAM.run_time(200,2000))
        #await robot.straight(100)
        #await robot.turn(90)
  


# Runs the main program from start to finish.
run_task(main())