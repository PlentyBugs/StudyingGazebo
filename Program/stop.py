import rospy
from geometry_msgs.msg import Twist


def stop():
	rospy.init_node('vel_publisher')
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
	move = Twist()
	rate = rospy.Rate(1)
	move.linear.x = 0
	move.angular.z = 0
	pub.publish(move)


if __name__ == '__main__':
	try:
		rospy.init_node('stop')
		stop()
	except rospy.ROSInterruptException:
		pass