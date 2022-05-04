import wpilib
import wpilib.drive
import ctre


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        can1 = wpilib.CAN(1)
        can2 = wpilib.CAN(2)
        can3 = wpilib.CAN(3)
        can4 = wpilib.CAN(4)
        camera_enabled = False
        self.front_left_motor = ctre.TalonSRX(0)
        self.front_right_motor = ctre.TalonSRX(1)
        self.back_left_motor = ctre.TalonSRX(0)
        self.back_right_motor = ctre.TalonSRX(1)
        self.drive = wpilib.drive.MecanumDrive(self.front_left_motor, self.back_left_motor, self.front_right_motor, self.back_right_motor)
        self.stick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()
        if camera_enabled:
            wpilib.CameraServer.launch('vision.py:main')

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        a4 = self.stick.getRawAxis(4)
        y = (self.stick.getY() / 2) * a4
        x = (self.stick.getX() / 2) * a4
        z = (self.stick.getZ() / 2) * a4
        self.drive.driveCartesian(y, x, z)


if __name__ == "__main__":
    wpilib.run(MyRobot)
