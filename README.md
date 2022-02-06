# Take home test

This test is meant to be relatively easy and quick. It should show basic understanding of ROS and good python practices. It should be easily finished in 2 hours so out of respect for your time/sanity don't go over! Don't worry about excessive documentation, just simple comments is fine. We're just trying to see a material example of your code and how you write python.

## Robot

You will find `robot.py`, `battery_info.py` and `location_info.py`. **Do not modify these**.

Please create a new file in which:

1. Create a ros node which has an instance of `Robot` and:
    1. Publishes a `sensor_msgs/NavSatFix` at 1hz according to the robot's `get_location_info`
    2. Publishes a `sensor_msgs/BatteryState` at 5hz according to the robot's `get_battery_info`
    3. Subscribes to `/cmd_vel` a `geometry_msgs/Twist` and calls `move_robot` accordingly

## Code with bug

You will find `code_with_bug.py`, modify this file:

-   Fix the bugs in the code
-   Fix the style of the code

#### Goal:

-   The behavior of the program should be to print messages received from the `/chatter` topic at a rate not exceeding 5 messages per second.
-   The time between messages that are printed should always exceed or equal 1/5th of a second.
-   If a message comes in and 1/5th of a second or more has passed since the last message, the message should always be printed.
-   Don't worry about making the time checking mechanism rigorous, Python's time.time method is fine.
