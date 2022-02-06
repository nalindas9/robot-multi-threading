import rospy
from sensor_msgs.msg import NavSatFix, BatteryState
from robot import Robot
from thread import Thread
from geometry_msgs.msg import Twist

def callback(msg):
    """Callback function for the subscriber"""
    print(msg)
    robot.move(msg.linear.x, msg.angular.z)

if __name__ == '__main__':
    rospy.init_node('main')
    print('main')

    robot = Robot() # Robot object
    location_info = robot.get_location_info()
    battery_info = robot.get_battery_info()
    
    location_pub = rospy.Publisher('location_info', NavSatFix, queue_size=10)
    battery_pub = rospy.Publisher('battery_info', BatteryState, queue_size=10)
    velocity_sub = rospy.Subscriber('cmd_vel', Twist, callback)

    location_thread = Thread(name='location_info',
                             thread_id=1,
                             rate=1,
                             publisher=location_pub,
                             msg=location_info)

    battery_thread = Thread(name='battery_info',
                            thread_id=2,
                            rate=5,
                            publisher=battery_pub,
                            msg=battery_info)
                            
    location_thread.start() # Start the thread
    battery_thread.start() # Start the thread
    rospy.spin()