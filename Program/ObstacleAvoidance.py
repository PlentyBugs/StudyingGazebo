import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class WrumWrumWasUberPodiehal():
	def __init__(self):	
		rospy.init_node('ObstacleAvoidance', anonymous=False)
		self.sub = rospy.Subscriber('/scan', LaserScan, self.callback)
		self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
		rospy.on_shutdown(self.shutdown)

		move_cmd = Twist()
		r = rospy.Rate(10);
		while not rospy.is_shutdown():
			print(2)

			print('===============')
			print('Right: ', msg.ranges[270])
			print('Front: ', msg.ranges[0])
			print('Left: ', msg.ranges[90])
			print('Back: ', msg.ranges[180])
			print('VelX: ', move_cmd.linear.x)

			if(msg.ranges[0] > 0.5):
				move_cmd.linear.x = 0.5
				move_cmd.angular.z = 0.0
			else:
				move_cmd.linear.x = 0.0
				move_cmd.angular.z = 0.0

			self.cmd_vel.publish(move_cmd)
			r.sleep()

	def callback(self, msg):
		print(1)

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