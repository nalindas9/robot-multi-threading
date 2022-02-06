import threading
import time
import rospy
from sensor_msgs.msg import NavSatFix, BatteryState

class Thread(threading.Thread):
    """Multithreading"""
    def __init__(self, name, thread_id, rate, publisher, msg):
        threading.Thread.__init__(self)
        self.name = name
        self.thread_id = thread_id
        self.rate = rate
        self.publisher = publisher
        self.msg = msg

    def load_msg(self):
        """Loads the message to be published"""
        if self.name == 'location_info':
            msg = NavSatFix()
            msg.latitude = self.msg.get_latitude()
            msg.longitude = self.msg._longitude # TODO: Fix 'LocationInfo' object has no attribute '_current' in location_info.py 
            msg.status.status = self.msg.get_fix()

        elif self.name == 'battery_info':
            msg = BatteryState()
            msg.voltage = self.msg.get_voltage()
            msg.current = self.msg.get_current()
            msg.charge = self.msg.get_charge_percentage()
            msg.power_supply_status = self.msg.get_is_charging()

        else:
            raise Exception('Unknown thread name')

        return msg

    def run(self):
        """Runs the thread"""
        print("Starting " + self.name)
        r = rospy.Rate(self.rate)

        while not rospy.is_shutdown():
            msg = self.load_msg()
            self.publisher.publish(msg) # Publish the message at 'rate' hz
            print('Publishing {}'.format(msg))
            r.sleep()
        
        print("Exiting " + self.name)