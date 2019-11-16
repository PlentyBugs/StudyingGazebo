import rospy
from geometry_msgs.msg import Twist


def stop():
	print(1)
	rospy.init_node('stop')
	print(2)
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
	print(3)
	move = Twist()
	print(4)
	move.linear.x = 0
	move.linear.y = 0
	move.linear.z = 0
	move.angular.x = 0
	move.angular.y = 0
	move.angular.z = 0
	print(5)
	pub.publish(move)
	print(6)


if __name__ == '__main__':
	try:
		stop()
		print(7)
		rospy.spin()
		print(8)
	except rospy.ROSInterruptException:
		pass