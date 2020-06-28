import rospy
from std_msgs.msg import String

pub = rospy.Publisher("pubnode", String, queue_size=20)
rospy.init_node('talker', anonymous = True)
rate = rospy.Rate(10) # Hz

while not rospy.is_shutdown():
    msg = "hello world! %s" % rospy.get_time()
    rospy.loginfo(msg)
    pub.publish(msg)
    rate.sleep()
