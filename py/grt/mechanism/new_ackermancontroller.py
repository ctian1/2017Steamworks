import math
from wpilib import CANTalon

class NewAckermanController:

    def __init__(self, joystick, xbox_controller, swerve_module):

        self.swerve_module = swerve_module

        self.joystick = joystick
        self.xbox_controller = xbox_controller

        self.joystick.add_listener(self._joylistener)
        self.xbox_controller.add_listener(self._xbox_controller_listener)

    def _joylistener(self, sensor, state_id, datum):

        pass


    def _xbox_controller_listener(self, sensor, state_id, datum):

        #TO ZERO: press B, move to correct positions, then press A

        if state_id == 'a_button':

            if datum:

                self.swerve_module.set_enc_position(0)

        elif state_id == 'b_button':

            if datum: 

                self.swerve_module.switch_to_percentvbus()

        #MANUAL SWITCH TO STRAFING

        elif state_id == 'x_button':

            if datum:

                self.swerve_module.set_strafing(True)
                print("SWITCHED TO STRAFING")

        #MANUAL SWITCH TO ACKERMAN

        elif state_id == 'y_button':

            if datum:

                self.swerve_module.set_strafing(False)
                print("SWITCHED TO ACKERMAN")


        #RIGHT JOYSTICK FOR STRAFING

        elif state_id in ('r_y_axis', 'r_x_axis'):

            
            x = self.xbox_controller.r_x_axis
            y = self.xbox_controller.r_y_axis

            
            if abs(x) > .2 or abs(y) > .2:

                self.swerve_module.set_strafing(True)
                #print("SWITCHED TO STRAFING")

                angle = math.atan2(x,-y)
                

                power = math.sqrt(x ** 2 + y ** 2)

                self.swerve_module.strafe(angle, power)

            else:

                self.swerve_module.strafe(0, 0)

                self.swerve_module.set_strafing(False)
                print("SWITCHED TO ACKERMAN")

        elif state_id in ('l_y_axis', 'l_x_axis'):

            x = self.xbox_controller.l_x_axis
            y = self.xbox_controller.l_y_axis

            if (abs(x) > .2 or abs(y) > .2) and not self.strafing:

                joy_angle = math.atan2(x, -y)
                print("JOY ANGLE")
                print(joy_angle)

                #DETERMINE POWER: size of vector based on joystick x and y

                power = math.sqrt(x**2 + y**2)
                
                self.swerve_module.ackerman_turn(joy_angle, power)


            else:

                self.swerve_module.ackerman_turn(0,0)
                

    def _limit_listener(self, source, state_id, datum):

        if state_id == 'pressed' and datum and self.strafing:


            print("listener zeroing")

            self.turn_r1.setEncPosition(0)
            self.turn_r2.setEncPosition(0)
            self.turn_l1.setEncPosition(0)
            self.turn_l2.setEncPosition(0)