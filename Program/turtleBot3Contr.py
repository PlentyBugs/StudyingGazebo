import rospy
from geomentry_msgs.msgs import Twist
from sensor_msgs.msg import LaserScan


def talker():
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
	move = Twist()
	rate = rospy.Rate(1)
	while not rospy.is_shutdown:
		move.linear.x = 1
		move.angular.z = 1
		pub.publish(move)
		rate.sleep()


def callback(msg):
	print("=========================") #From 0 to 359
	print('Front: ', msg.ranges[0])
	print('Left: ', msg.ranges[90])
	print('Back: ', msg.ranges[180])
	print('Right: ', msg.ranges[270])


if __name__ == '__main__':
	try:
		rospy.init_node('turtleBot3Contr')
		sub = rospy.Subscriber('scan', LaserScan, callback)
		#rospy.spin()
		talker()
	except rospy.ROSInterruptException:
		pass