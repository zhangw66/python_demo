import numpy as np 
import os
from matplotlib import pyplot as plt
basetime=10962195
set_ltime_list = []
set_lspeed_list = []
set_rtime_list = []
set_rspeed_list = []

get_ltime_list = []
get_lspeed_list = []
get_rtime_list = []
get_rspeed_list = []
file = open("speed_value")
file_ss = open("setspeed")
file_gs = open("getspeed")
def ownstrsplit(filename, time_list, speed_list, is_right=0):
    line=0
    filename.seek(0)
    while 1:
        linestr = filename.readline()
        line = line + 1
        '''
        print linestr
        '''
        if not linestr or (line == 50000):
            break
        
        sss = linestr.split()
        '''
        print sss[0]+sss[1]
        '''
        time_list.append(str(long(sss[0])-basetime))
        if (is_right == 1) :
            speed_list.append(sss[2])
        else :
            speed_list.append(sss[1])


    print "File has "+str(line)+" lines\n"
    """
    print time_list
    print speed_list
    """
    return

ownstrsplit(file_ss, set_ltime_list, set_lspeed_list)
ownstrsplit(file_ss, set_rtime_list, set_rspeed_list, 1)
ownstrsplit(file_gs, get_ltime_list, get_lspeed_list)
ownstrsplit(file_gs, get_rtime_list, get_rspeed_list, 1)


"""
x = np.arange(1,11) 
y =  2  * x +  5
x1 = np.arange(11,21) 
y1 =  3  * x1 +  5  
"""
plt.title("left speed curve") 
plt.xlabel("x axis time") 
plt.ylabel("y axis speed")
plt.plot(set_ltime_list, set_lspeed_list, "y-")
plt.plot(get_ltime_list, get_lspeed_list, "b--")
"""
plt.figure()
plt.title("right speed curve") 
plt.xlabel("x axis time") 
plt.ylabel("y axis speed")
"""
plt.plot(set_rtime_list, set_rspeed_list, "r-")
plt.plot(get_rtime_list, get_rspeed_list, "g--")

plt.show()
