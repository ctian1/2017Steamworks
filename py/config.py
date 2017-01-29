"""
Config File for Robot
"""

from wpilib import Solenoid, Compressor, DriverStation, CANTalon, DigitalInput

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
#from grt.sensors.gyro import Gyro
from grt.core import SensorPoller
from grt.mechanism.swervemodule import SwerveModule 
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset
from grt.sensors.ticker import Ticker
from grt.sensors.encoder import Encoder
#from grt.sensors.talon import Talon
from grt.mechanism.mechcontroller import MechController
from grt.mechanism.swervecontroller import TestSwerveDriveController
from grt.mechanism.ackermancontroller import AckermanController
from grt.mechanism.beta_mechs import Shooter, Intake, Gear, Climber, Hopper
from grt.mechanism import ZeroTest, TalonTester
from grt.sensors.switch import Switch


#DT Talons and Objects


# TALON ASSIGNMENT:


# 1:
# 2: front right dt power
# 3: back left dt power 
# 4: back left dt turn
# 5: back right dt turn
# 6: 
# 7: back left dt power NOT WORKING ATM!
# 8: bottom front shooter motor
# 9: front left dt turn
# 10: front right dt turn
# 11: back right dt power boop
# 12: integration
# 13: intake
# 14: front left dt power
# 15: top front shooter motor
# 16:

#SOLENOID ASSIGNMENT:

# o:
# 1:
# 2: 
# 3: gear 
# 4: gear indexer


test_solenoid = Solenoid(2)

talon_test = TalonTester(test_solenoid)


#UNCOMMENT THE FOLLOWING LATER
turn_l2 = CANTalon(4)
turn_l2.changeControlMode(CANTalon.ControlMode.Position)
turn_l2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_l2.setPID(1.0, 0.0, 0.0)

turn_r2 = CANTalon(5)
turn_r2.changeControlMode(CANTalon.ControlMode.Position)
turn_r2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_r2.setPID(1.0, 0.0, 0.0)

turn_left = CANTalon(9)
turn_left.changeControlMode(CANTalon.ControlMode.Position)
turn_left.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_left.setPID(1.0, 0.0, 0.0)

turn_right = CANTalon(10)#5
turn_right.changeControlMode(CANTalon.ControlMode.Position)
turn_right.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_right.setPID(1.0, 0.0, 0.0)


#TAKEN FOR TURNING: 8 9 2 5
#AVAILABLE: 

#front right 6 turning: 5
#front left 1 turning: 2
#back right 7 turning: 9
#back left 4 turning: 8

dt_right = CANTalon(2)
dt_left = CANTalon(14)

dt_l2 = CANTalon(3)
dt_r2 = CANTalon(11)


shooter1_m1 = CANTalon(15)
shooter1_m2 = CANTalon(8)
shooter2_m1 = CANTalon(20)
shooter2_m2 = CANTalon(20)

# shooter1_m1.changeControlMode(CANTalon.ControlMode.Speed)
# shooter1_m1.setPID(.33, 0, 0, f=.17)

# shooter1_m2.changeControlMode(CANTalon.ControlMode.Speed)
# shooter1_m2.setPID(.33, 0, 0, f=.17)

# shooter2_m1.changeControlMode(CANTalon.ControlMode.Speed)
# shooter2_m1.setPID(.33, 0, 0, f=.17)

# shooter2_m2.changeControlMode(CANTalon.ControlMode.Speed)
# shooter2_m2.setPID(.33, 0, 0, f=.17)

load_m = CANTalon(12)

angle_change = Solenoid(0)

shooter = Shooter(shooter1_m1, shooter1_m2, shooter2_m1, shooter2_m2, load_m, angle_change)

intake_motor = CANTalon(13)

intake = Intake(intake_motor)


climber_motor = CANTalon(20)

c2 = CANTalon(20)

c2.changeControlMode(CANTalon.ControlMode.Follower)
c2.set(climber_motor.getDeviceID())

climber = Climber(climber_motor)


gear_pneumatic_1 = Solenoid(3)
gear_pneumatic_2 = Solenoid(4)

gear_mech = Gear(gear_pneumatic_1, gear_pneumatic_2)


hopper_pneumatic = Solenoid(1)


hopper = Hopper(hopper_pneumatic)

limit_r1 = Switch(1, reverse=True)
limit_r2 = Switch(0, reverse=True)
limit_l1 = Switch(3, reverse=True)
limit_l2 = Switch(2, reverse=True)

#zero_test = ZeroTest(turn_right, limit_switch)

#dt = SwerveModule(power_motor, turn_motor)

#needs to be changed for left and right
tank_dt = DriveTrain(dt_left, dt_right, left_shifter=None, left_encoder=None, right_encoder=None)
#Skeleton sensor poller
#gyro = Gyro(1)
# define sensor poller
# sp = SensorPoller()


# Drive Controllers
l_joystick = Attack3Joystick(0)

#r_joystick = Attack3Joystick(3)
xbox_controller = XboxJoystick(1)
xbox_controller_2 = XboxJoystick(2)
#ac = ArcadeDriveController(tank_dt, l_joystick)
hid_sp = SensorPoller((l_joystick, xbox_controller, xbox_controller_2))  # human interface devices
sp = SensorPoller((limit_r1, limit_r2, limit_l1, limit_l2))


# Mech Talons, objects, and controller

#sc = TestSwerveDriveController(l_joystick, r_joystick, xbox_controller, dt=dt, turn_motor=turn_motor, power_motor=power_motor, turn_2 = turn_2, turn_3 = turn_3)

ac = AckermanController(l_joystick, xbox_controller, turn_right, turn_r2, turn_left, turn_l2, dt_right, dt_r2, dt_left, dt_l2, limit_r1, limit_r2, limit_l1, limit_l2)

# define MechController
mc = MechController(l_joystick, xbox_controller_2, shooter, intake, climber, gear_mech, hopper, talon_test=talon_test)

# define DriverStation
ds = DriverStation.getInstance()





