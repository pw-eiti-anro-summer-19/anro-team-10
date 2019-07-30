#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
import math 
from sensor_msgs.msg import JointState

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    hz=10
    rate = rospy.Rate(hz) # 10hz
    d=0.0
    theta1 = 1.5
    theta2 = 1.3
    theta3 = 1.0
    time = 3
    movement_cal = time * hz
    theta1_new = 0
    theta2_new = 0
    theta3_new = 0
    theta_tem1 = theta1 / movement_cal 
    theta_tem2 = theta2 / movement_cal 
    theta_tem3 = theta3 / movement_cal
 
    while movement_cal > 0:
        msg=JointState()
        theta1_new += theta_tem1
        theta2_new += theta_tem2
        theta3_new += theta_tem3
        msg.header.stamp = rospy.get_rostime()
        msg.name=['base_to_link_1','base_to_link_2','base_to_link_3']
        msg.position=[theta1_new,theta2_new,theta3_new]
        pub.publish(msg)
        rate.sleep()
        movement_cal += (-1)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
