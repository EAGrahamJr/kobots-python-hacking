"""
Stuff for servos, including a "smooth move" just to keep things from going off the rails.

Used as a physical test thingie, with the stepping used to prevent any hardware attached
from "zooming" to an agle with.
"""

from time import sleep
import board
from adafruit_motor.servo import Servo

def move_servo(servo:Servo, angle: float, rate: float = 0.025):
        """Move a servo to a certain angle.

        Args:
            servo (Servo): the servo
            angle (float): where to move to
            rate (float): pause between steps in seconds or fractions thereof
        """
        current = round(servo.angle)
        if angle == current:
            return
        if angle > current:
            delta = 1
        else:
            delta = -1

        for i in range(current, angle, delta):
            servo.angle = i
            sleep(rate)

        servo.angle = angle

def gpio(pin = board.D18) -> Servo:
    """Create a servo for a GPIO pin

    Args:
        pin (Pin, optional): which pin to use. Defaults to board.D18.

    Returns:
        Servo: an Adafruit "Servo" for the pin
    """
    import pwmio
    pwm = pwmio.PWMOut(pin, duty_cycle=2 ** 15, frequency=50)
    return Servo(pwm, actuation_range=180)

def hat(channel:int = 0) -> Servo:
    """Create a servo for a specific channel on a servo driver board.

    Args:
        channel (int, optional): channel to use. Defaults to 0.

    Returns:
        Servo: an Adafruit "Servo" for the channel
    """
    from adafruit_pca9685 import PCA9685
    pca = PCA9685(board.I2C())
    pca.frequency = 50
    pwm = pca.channels[channel]
    return Servo(pwm, actuation_range=180)

def crickit(index:int = 1) -> Servo:
    """Create a servo for the specific CRICKIT Hat output.

    Args:
        index (int, optional): one of the 4 servo channels (1-4). Defaults to 1.

    Returns:
        Servo: an Adafruit "Servo" for the channel
    """
    from adafruit_crickit import crickit
    if index == 1:
        return crickit.servo_1
    if index == 2:
        return crickit.servo_2
    if index == 3:
        return crickit.servo_3
    return crickit.servo_4

class RotoServo:
    """
    Just wraps the move_servo in a class for easier dorking
    """
    def __init__(self, servo:Servo) -> None:
        self._servo = servo
        self._speed = 0.025
        servo.angle = 0

    @property
    def speed(self)->float:
        """The amount of "time" to sleep between steps (defaults to .025)

        Returns:
            float: pause time
        """
        return self._speed

    @speed.setter
    def speed(self, howFast:float=0.025):
        """Sets the "speed"

        Args:
            howFast (float, optional): the speed to use. Defaults to 0.025.
        """
        self._speed = howFast

    @property
    def angle(self)->float:
        """Get the current angle of the servo

        Returns:
            float: current angle of the servo
        """
        return self._servo.angle

    @angle.setter
    def angle(self, degrees:int):
        """Move the servo to this angle. Note this will "step"
        the servo using the speed property.

        Args:
            degrees (int): the desired angle
        """
        move_servo(self._servo,degrees,self._speed)

def sg90(servo:Servo) -> RotoServo:
    """Wraps a servo in a "speed-controlled" class.

    Also sets the servo trim to appropriate values for an SG90.

    Args:
        servo (Servo): the servo to wrap

    Returns:
        RotoServo: speed-controlled, "stepping" servo
    """
    servo.set_pulse_width_range(500,2400)
    return RotoServo(servo)

def mg90s(servo:Servo) -> RotoServo:
    """Wraps a servo in a "speed-controlled" class.

    Also sets the servo trim to appropriate values for an MG90S.
    Note that this may result in maximum angles > 180.

    Args:
        servo (Servo): the servo to wrap

    Returns:
        RotoServo: speed-controlled, "stepping" servo
    """
    servo.set_pulse_width_range(400,2600)
    return RotoServo(servo)

