from battery_info import BatteryInfo
from location_info import LocationInfo


class Robot:
    def __init__(self):
        pass

    def get_battery_info(self):
        """Returns BatteryInfo representing current battery state of the Robot"""
        return BatteryInfo.generate_random()

    def get_location_info(self):
        """Returns LocationInfo representing current GPS state of the Robot"""
        return LocationInfo.generate_random()

    def move(self, speed: float, angle: float):
        """Moves robot forward at speed m/s with angle [-45,45] in degrees applied to the front wheels"""
        if angle > 45 or angle < -45:
            raise ValueError("Angle must be within [-45,45]")

