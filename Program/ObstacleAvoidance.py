import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):	
	print('===============')
	print('Right: ', msg.ranges[270])
	print('Front: ', msg.ranges[0])
	print('Left: ', msg.ranges[90])

	rospy.on_shutdown(shutdown())

	if(msg.ranges[0] > 0.5):
		move.linear.x = 0.5
		move.angular.z = 0.0
	else:
		move.linear.x = 0.0
		move.angular.z = 0.0

	pub.publish(move)


def shutdown(self):
	rospy.loginfo("Stop TurtleBot")
	self.cmd_vel.publish(Twist())
	rospy.sleep(1)


rospy.init_node('ObstacleAvoidance')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()