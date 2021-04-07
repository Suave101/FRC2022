## Welcome to Team 5616 RobotPy Code

You can use the code here for your robot. This code uses the wpilib RobotPy library and the ctre RobotPy library.

You can report issues and have conversations on this repository about the code. You can also make pull requests.

### The Code

To install the ctre and wpilib RobotPy librarys  on your computer you must run the code below:

```markdown
py -3 -m pip install robotpy
py -3 -m pip install -U robotpy[ctre]
```

To make your Roborio understand the code you must first download the packages to your computer by running these commands:

```markdown
py -3 -m robotpy_installer download-python
py -3 -m robotpy_installer download robotpy
py -3 -m robotpy_installer download -U robotpy[ctre]
```

Once you download these packages you must CONNECT TO YOUR ROBOTS WIFI then run these commands to send the librarys to the Roborio.

```markdown
py -3 -m robotpy_installer install-python
py -3 -m robotpy_installer install robotpy
py -3 -m robotpy_installer install robotpy[ctre]
```

### Support

Having trouble with the code? Create an issue [here](https://github.com/FRC-Team-5616/Robot-Python-Code/issues/new).
