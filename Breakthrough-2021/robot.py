import wpilib
import ctre


class Modes:
    def __init__(self):
        self.Victor = "Victor"
        self.Talon = "Talon"


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        modes = Modes()
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        ds = wpilib.DriverStation()
        mode = modes.Talon
        if mode == modes.Talon:
            self.frLeft = ctre.TalonSRX(2)
            self.frRight = ctre.TalonSRX(3)
            self.reLeft = ctre.TalonSRX(1)
            self.reRight = ctre.TalonSRX(4)
        elif mode == modes.Victor:
            self.frLeft = ctre.VictorSPX(2)
            self.frRight = ctre.VictorSPX(3)
            self.reLeft = ctre.VictorSPX(1)
            self.reRight = ctre.VictorSPX(4)
        else:
            self.frLeft = ctre.TalonSRX(2)
            self.frRight = ctre.TalonSRX(3)
            self.reLeft = ctre.TalonSRX(1)
            self.reRight = ctre.TalonSRX(4)
        self.controller = wpilib.XboxController(1)
        self.timer = wpilib.Timer()
        self.stick = wpilib.XboxController(1)
        self.timer = wpilib.Timer()
        # Set Inverted
        self.frLeft.setInverted(False)
        self.reLeft.setInverted(False)
        self.frRight.setInverted(False)
        self.reRight.setInverted(True)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.frLeft.set(ctre.ControlMode.PercentOutput, 0)
        self.reLeft.set(ctre.ControlMode.PercentOutput, 0)
        self.frRight.set(ctre.ControlMode.PercentOutput, 0)
        self.reRight.set(ctre.ControlMode.PercentOutput, 0)
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def disabledInit(self):
        self.timer.stop()
        self.frLeft.set(ctre.ControlMode.PercentOutput, 0)
        self.reLeft.set(ctre.ControlMode.PercentOutput, 0)
        self.frRight.set(ctre.ControlMode.PercentOutput, 0)
        self.reRight.set(ctre.ControlMode.PercentOutput, 0)

    def disabledPeriodic(self):
        self.frLeft.set(ctre.ControlMode.PercentOutput, 0)
        self.reLeft.set(ctre.ControlMode.PercentOutput, 0)
        self.frRight.set(ctre.ControlMode.PercentOutput, 0)
        self.reRight.set(ctre.ControlMode.PercentOutput, 0)

    def teleopInit(self):
        self.timer.reset()
        self.timer.start()
        self.frLeft.set(ctre.ControlMode.PercentOutput, 0)
        self.reLeft.set(ctre.ControlMode.PercentOutput, 0)
        self.frRight.set(ctre.ControlMode.PercentOutput, 0)
        self.reRight.set(ctre.ControlMode.PercentOutput, 0)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        turnRatio_1 = 0.25
        turnRatio_2 = 0.75
        xLeft = self.controller.getX(wpilib.XboxController.Hand.kLeftHand)
        yLeft = self.controller.getY(wpilib.XboxController.Hand.kLeftHand)
        xRight = self.controller.getX(wpilib.XboxController.Hand.kRightHand)
        yRight = self.controller.getY(wpilib.XboxController.Hand.kRightHand)
        if self.ds.getBatteryVoltage() < 9:
            self.ds.reportError("Brownout Warning - Charge Your Battery - IE", printTrace=False)
            self.frLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.reLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.frRight.set(ctre.ControlMode.PercentOutput, 0)
            self.reRight.set(ctre.ControlMode.PercentOutput, 0)
        elif yLeft < 0 and xRight < 0:
            self.frLeft.set(ctre.ControlMode.PercentOutput, xRight*-1*turnRatio_1)
            self.reLeft.set(ctre.ControlMode.PercentOutput, xRight*-1*turnRatio_1)
            self.frRight.set(ctre.ControlMode.PercentOutput, yLeft*-1)
            self.reRight.set(ctre.ControlMode.PercentOutput, yLeft*-1)
        elif yLeft < 0 and xRight > 0:
            self.frLeft.set(ctre.ControlMode.PercentOutput, yLeft*-1)
            self.reLeft.set(ctre.ControlMode.PercentOutput, yLeft*-1)
            self.frRight.set(ctre.ControlMode.PercentOutput, xRight * turnRatio_1)
            self.reRight.set(ctre.ControlMode.PercentOutput, xRight * turnRatio_1)
        elif yLeft > 0 and xRight < 0:
            self.frLeft.set(ctre.ControlMode.PercentOutput, xRight * turnRatio_1)
            self.reLeft.set(ctre.ControlMode.PercentOutput, xRight * turnRatio_1)
            self.frRight.set(ctre.ControlMode.PercentOutput, yLeft*-1)
            self.reRight.set(ctre.ControlMode.PercentOutput, yLeft*-1)
        elif yLeft > 0 and xRight > 0:
            self.frLeft.set(ctre.ControlMode.PercentOutput, yLeft*-1)
            self.reLeft.set(ctre.ControlMode.PercentOutput, yLeft*-1)
            self.frRight.set(ctre.ControlMode.PercentOutput, xRight*-1*turnRatio_1)
            self.reRight.set(ctre.ControlMode.PercentOutput, xRight*-1*turnRatio_1)
        elif yLeft > 0 and (xRight > 0 or xRight < 0):
            self.frLeft.set(ctre.ControlMode.PercentOutput, -1*yLeft)
            self.reLeft.set(ctre.ControlMode.PercentOutput, -1*yLeft)
            self.frRight.set(ctre.ControlMode.PercentOutput, -1*yLeft)
            self.reRight.set(ctre.ControlMode.PercentOutput, -1*yLeft)
        elif yLeft < 0 and (xRight > 0 or xRight < 0):
            self.frLeft.set(ctre.ControlMode.PercentOutput, -1*yLeft)
            self.reLeft.set(ctre.ControlMode.PercentOutput, -1*yLeft)
            self.frRight.set(ctre.ControlMode.PercentOutput, -1*yLeft)
            self.reRight.set(ctre.ControlMode.PercentOutput, -1*yLeft)
        elif xRight > 0 and (yLeft > 0 or yLeft < 0):
            self.frLeft.set(ctre.ControlMode.PercentOutput, xRight*turnRatio_2)
            self.reLeft.set(ctre.ControlMode.PercentOutput, xRight*turnRatio_2)
            self.frRight.set(ctre.ControlMode.PercentOutput, xRight * -1 * turnRatio_2)
            self.reRight.set(ctre.ControlMode.PercentOutput, xRight * -1 * turnRatio_2)
        elif xRight < 0 and (yLeft > 0 or yLeft < 0):
            self.frLeft.set(ctre.ControlMode.PercentOutput, xRight*turnRatio_2)
            self.reLeft.set(ctre.ControlMode.PercentOutput, xRight*turnRatio_2)
            self.frRight.set(ctre.ControlMode.PercentOutput, xRight * -1 * turnRatio_2)
            self.reRight.set(ctre.ControlMode.PercentOutput, xRight * -1 * turnRatio_2)
        else:
            self.frLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.reLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.frRight.set(ctre.ControlMode.PercentOutput, 0)
            self.reRight.set(ctre.ControlMode.PercentOutput, 0)


if __name__ == "__main__":
    wpilib.run(MyRobot)
