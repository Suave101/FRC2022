import wpilib
import ctre


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.frLeft = ctre.VictorSPX(2)
        self.frRight = ctre.VictorSPX(3)
        self.reLeft = ctre.VictorSPX(1)
        self.reRight = ctre.VictorSPX(4)
        self.stick = wpilib.XboxController(1)
        self.timer = wpilib.Timer()
        # Set Inverted
        self.frLeft.setInverted(False)
        self.reLeft.setInverted(False)
        self.frRight.setInverted(False)
        self.reRight.setInverted(True)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)
