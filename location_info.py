import random


class LocationInfo:
    @classmethod
    def generate_random(cls):
        fix = random.random() > 0.9
        return cls(
            0 if not fix else random.random() * 100000,
            0 if not fix else random.random() * 100000,
            fix,
        )

    def __init__(self, latitude, longitude, fix):
        self._latitude = latitude
        self._longitude = longitude
        self._fix = fix

    def get_latitude(self):
        """Returns latitude"""
        return self._latitude

    def get_longitude(self):
        """Returns longitude"""
        return self._current

    def get_fix(self):
        """Returns Boolean represenitng if the signal has fix"""
        return self._fix
