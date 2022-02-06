import random


class BatteryInfo:
    @classmethod
    def generate_random(cls):
        return cls(
            random.random() * 30,
            random.random() * 5,
            random.random() * 100,
            random.random() > 0.5,
        )

    def __init__(self, voltage, current, charge_percentage, is_charging):
        self._voltage = voltage
        self._current = current
        self._charge_percentage = charge_percentage
        self._is_charging = is_charging

    def get_voltage(self):
        """Returns voltage in volts of battery"""
        return self._voltage

    def get_current(self):
        """Returns current in ampres of battery"""
        return self._current

    def get_charge_percentage(self):
        """Returns charge percentage [0, 100] """
        return self._charge_percentage

    def get_is_charging(self):
        """Returns Boolean representing if the battery is charging"""
        return self._is_charging
