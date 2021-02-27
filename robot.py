import wpilib
import wpilib.drive
import ctre

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.flm = ctre.VictorSPX(2)
        self.frm = ctre.VictorSPX(3)
        self.blm = ctre.VictorSPX(1)
        self.brm = ctre.VictorSPX(4)
        self.left = wpilib.SpeedControllerGroup(self.flm, self.frm)
        self.right = wpilib.SpeedControllerGroup(self.blm, self.brm)
        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)
        self.stick = wpilib.XboxController(0)
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.arcadeDrive(self.stick.getY(self), self.stick.getX(self))


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
