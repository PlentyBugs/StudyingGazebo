import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class WrumWrumWasUberPodiehal():
	def __init__(self):	
		rospy.init_node('ObstacleAvoidance', anonymous=True)
		self.sub = rospy.Subscriber('/scan', LaserScan, self.callback)
		self.cmd_vel = rospy.Publisher('/cmd_vel', Twist)
		move_cmd = Twist()
		rospy.on_shutdown(self.shutdown)
		r = rospy.Rate(10);

	def callback():
		while not rospy.is_shutdown():

			print('===============')
			print('Right: ', msg.ranges[270])
			print('Front: ', msg.ranges[0])
			print('Left: ', msg.ranges[90])
			print('Back: ', msg.ranges[180])

			if(msg.ranges[0] > 0.5):
				move.linear.x = 0.5
				move.angular.z = 0.0
			else:
				move.linear.x = 0.0
				move.angular.z = 0.0

			pub.publish(move)
			self.cmd_vel.publish(move_cmd)
			r.sleep()

	def shutdown(self):
		rospy.loginfo("Stop TurtleBot")
		self.cmd_vel.publish(Twist())
		rospy.sleep(1)

if __name__ == '__main__':
    try:
        WrumWrumWasUberPodiehal()
    except Exception, e:
        rospy.loginfo("WrumWrumWasUberPodiehal node terminated.")
        rospy.loginfo(str(e))