import wpilib
import wpilib.drive
import math

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.front_left_motor = wpilib.PWMTalonFX(12)
        self.front_right_motor = wpilib.PWMTalonFX(13)
        self.rear_left_motor = wpilib.PWMTalonFX(14)
        self.rear_right_motor = wpilib.PWMTalonFX(15)

        self.left_motors = wpilib.SpeedControllerGroup(self.front_left_motor, self.rear_left_motor)
        self.right_motors = wpilib.SpeedControllerGroup(self.front_right_motor, self.rear_right_motor)

        self.drive = wpilib.drive.DifferentialDrive(self.left_motors, self.right_motors)
        self.movement_controls = wpilib.XboxController(1)
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control.
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())"""
        fourFive = math.sqrt(2) / 2
        xLeft = self.movement_controls.kLeftX
        yLeft = self.movement_controls.kLeftY
        xRight = self.movement_controls.kRightX
        yRight = self.movement_controls.kRightY
        if 0 < yLeft <= 1 and fourFive > xLeft > (-1 * fourFive):
            self.drive.arcadeDrive(yLeft, 1)
        elif -1 <= yLeft < 0 and fourFive > xLeft > (-1 * fourFive):
            self.left_motors.set(xRight)
            self.left_motors.set(-1*xRight)
        elif fourFive > yRight > (-1 * fourFive) and 0 < xRight <= 1:
            self.left_motors.set(-1 * xRight)
            self.left_motors.set(xRight)
        elif yRight == 0 and xRight == 0 and yLeft == 0 and xLeft == 0:
            self.drive.arcadeDrive(0, 0)


if __name__ == "__main__":
    wpilib.run(MyRobot)
