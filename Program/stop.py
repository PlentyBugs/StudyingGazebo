import rospy
from geometry_msgs.msg import Twist


def stop():
	rospy.init_node('stop')
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
	move = Twist()
	rate = rospy.Rate(1)
	move.linear.x = 0
	move.linear.y = 0
	move.linear.z = 0
	move.angular.x = 0
	move.angular.y = 0
	move.angular.z = 0
	pub.publish(move)


if __name__ == '__main__':
	try:
		stop()
		rospy.spin()
	except rospy.ROSInterruptException:
		pass