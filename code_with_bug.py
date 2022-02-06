import time
import rospy
from std_msgs.msg import String

def throttled_print(message):
    """Throttle (drop) messages that come in too fast."""
    global last_print_time # bug fix
    current_time = time.time() # style fix
    
    if (current_time - last_print_time) > 1/rate_limit_hz: # bug fix
        print(message)
        last_print_time = current_time

if __name__ == "__main__":
    last_print_time = 0.0
    rate_limit_hz = 5

    rospy.init_node("printer")
    sub = rospy.Subscriber("/chatter", String, throttled_print)
    rospy.spin()
