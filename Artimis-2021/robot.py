import wpilib
import wpilib.drive
import ctre
from ctre._ctre import ControlMode
import math


class MyRobot(wpilib.TimedRobot):

    def __init__(self, period=0.02):
        super().__init__(period)
        self.timer = wpilib.Timer()

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.flm = ctre.VictorSPX(2)
        self.frm = ctre.VictorSPX(3)
        self.frm.setInverted(True)
        self.blm = ctre.VictorSPX(1)
        self.brm = ctre.VictorSPX(4)
        self.brm.setInverted(True)
        self.flm.set(ControlMode.PercentOutput, 0)
        self.frm.set(ControlMode.PercentOutput, 0)
        self.blm.set(ControlMode.PercentOutput, 0)
        self.brm.set(ControlMode.PercentOutput, 0)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        if self.timer.get() < 2.0:
            self.flm.set(ControlMode.PercentOutput, 0.5)
            self.frm.set(ControlMode.PercentOutput, 0.5)
            self.blm.set(ControlMode.PercentOutput, 0.5)
            self.brm.set(ControlMode.PercentOutput, 0.5)
        else:
            self.flm.set(ControlMode.PercentOutput, 0)
            self.frm.set(ControlMode.PercentOutput, 0)
            self.blm.set(ControlMode.PercentOutput, 0)
            self.brm.set(ControlMode.PercentOutput, 0)

    def teleopInit(self):
        self.controller = wpilib.XboxController(0)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        fourFive = math.sqrt(2)/2
        xL = self.controller.getX(self.controller.Hand.kLeftHand)
        yL = self.controller.getY(self.controller.Hand.kLeftHand)
        yR = self.controller.getY(self.controller.Hand.kRightHand)
        xR = self.controller.getX(self.controller.Hand.kRightHand)
        if 0 < yL <= 1 and fourFive > xL > (-1 * fourFive):
            self.flm.set(ControlMode.PercentOutput, yL)
            self.frm.set(ControlMode.PercentOutput, yL)
            self.blm.set(ControlMode.PercentOutput, yL)
            self.brm.set(ControlMode.PercentOutput, yL)
        elif -1 <= yL < 0 and fourFive > xL > (-1 * fourFive):
            self.flm.set(ControlMode.PercentOutput, yL)
            self.frm.set(ControlMode.PercentOutput, yL)
            self.blm.set(ControlMode.PercentOutput, yL)
            self.brm.set(ControlMode.PercentOutput, yL)
        elif fourFive > yR > (-1 * fourFive) and 0 < xR <= 1:
            self.flm.set(ControlMode.PercentOutput, -1*xR/2)
            self.frm.set(ControlMode.PercentOutput, xR/2)
            self.blm.set(ControlMode.PercentOutput, -1*xR/2)
            self.brm.set(ControlMode.PercentOutput, xR/2)
        elif fourFive > yR > (-1 * fourFive) and -1 <= xR < 0:
            self.flm.set(ControlMode.PercentOutput, -1 * xR / 2)
            self.frm.set(ControlMode.PercentOutput, xR / 2)
            self.blm.set(ControlMode.PercentOutput, -1 * xR / 2)
            self.brm.set(ControlMode.PercentOutput, xR / 2)
        else:
            self.flm.set(ControlMode.PercentOutput, 0)
            self.frm.set(ControlMode.PercentOutput, 0)
            self.blm.set(ControlMode.PercentOutput, 0)
            self.brm.set(ControlMode.PercentOutput, 0)


if __name__ == "__main__":
    wpilib.run(MyRobot)

"""
import wpilib

# https://github.com/robotpy/examples
# pginter@lizajackson.org
class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.LFM = wpilib.Jaguar(4)  # LFM = Left Front Motor
        self.LRM = wpilib.Jaguar(3)  # LRM = Left Rear Motor
        self.RFM = wpilib.Jaguar(5)  # RFM = Right Front Motor
        self.RRM = wpilib.Jaguar(6)  # RRM = Right Rear Motor
        self.LFM_R = 0
        self.LRM_R = 0
        self.RFM_R = 0
        self.RRM_R = 0

    def go_forward(self):
        self.LFM.set(-1 + self.LFM_R)
        self.LRM.set(-1 + self.LRM_R)
        self.RFM.set(0.5 + self.RFM_R)
        self.RRM.set(0.5 + self.RRM_R)

    def go_right(self):
        self.LFM.set(-1 + self.LFM_R)
        self.LRM.set(-1 + self.LRM_R)
        self.RFM.set(-0.5 + self.RFM_R)
        self.RRM.set(-0.5 + self.RRM_R)

    def go_left(self, speed):
        self.LFM.set((-0.2 * speed) + self.LFM_R)
        self.LRM.set((-0.2 * speed) + self.LRM_R)
        self.RFM.set((0.1 * speed) + self.RFM_R)
        self.RRM.set((0.1 * speed) + self.RRM_R)
"""
