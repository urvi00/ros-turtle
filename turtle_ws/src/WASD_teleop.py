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


import rospy
from geometry_msgs.msg import Twist
import sys

global msg1 #for W
msg1=Twist()
msg1.linear.x = 1
msg1.linear.y = 0
msg1.linear.z = 0
msg1.angular.x = 0
msg1.angular.y = 0
msg1.angular.z = 0

global msg2 #for S
msg2=Twist()
msg2.linear.x = -1
msg2.linear.y = 0
msg2.linear.z = 0
msg2.angular.x = 0
msg2.angular.y = 0
msg2.angular.z = 0

global msg3 #for D
msg3=Twist()
msg3.linear.x = 0
msg3.linear.y = 0
msg3.linear.z = 0
msg3.angular.x = 0
msg3.angular.y = 0
msg3.angular.z = -1

global msg4 #for A
msg4=Twist()
msg4.linear.x = 0
msg4.linear.y = 0
msg4.linear.z = 0
msg4.angular.x = 0
msg4.angular.y = 0
msg4.angular.z = 1

def WASD_teleop():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('WASD_teleop')
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        inp=raw_input("Reading from keyboard - use WASD keys to move the turtle.")
        inps=str(inp)
        if inps=="w":
            pub.publish(msg1)
        elif inps=="s":
            pub.publish(msg2)
        elif inps=="d":
            pub.publish(msg3)
        elif inps=="a":
            pub.publish(msg4)
        rate.sleep()

if __name__ == '__main__':
    try:
        WASD_teleop()
    except rospy.ROSInterruptException:
        pass
