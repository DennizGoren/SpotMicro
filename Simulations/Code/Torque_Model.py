import numpy as np
import matplotlib.pyplot as plt


#constants
g = 9.81
m_tot = 2.3
standup_time = 1.8
standup_deg = 70
dt = 180
#joints
#j_1
#j_2
#j_3

#masses of joints in kg
m_B1 = 0.06
m_B2 = 0.06
m_B3 = 0.06

#masses of links in kg
m_L1 = 0.0424
m_L2 = 0.0584
m_L3 = 0.00867

#arms in m
r_1 = 0.129
r_2 = 0.11
r_3 = 2.6

#angles
th_1 = np.linspace(180,110,dt)
th_2 = np.linspace(0,70,dt)
th_3 = np.linspace(90,90,dt)
th_33 = np.linspace(0,180,dt)

for i in range(len(th_1)):
    th_1[i] = np.deg2rad(th_1[i])
    th_2[i] = np.deg2rad(th_2[i])
    th_3[i] = np.deg2rad(th_3[i])
    th_33[i] = np.deg2rad(th_33[i])

    
#external forces
F = m_tot * g * (1/4)

#angular acceleration
omega_max = ( np.deg2rad(standup_deg) ) / ( (1/2) * standup_time)
rico = omega_max / (standup_time / 2)
omega_RPM = omega_max * 60 / (2*np.pi)

def omega(standup_time, rico):
    x = np.linspace(0, standup_time, dt)
    y = np.zeros(len(x))
    alpha = np.zeros(len(x))
    for i in range(0, round(dt*0.5)):
        y[i] = x[i] * rico
    for i in range(round(dt*0.5) ,dt):
        y[i] =  - x[i] * rico + 2* y[round(dt*0.5-1)]
    for i in range(0, round(dt*0.5)):
        alpha[i] = rico
    for i in range(round(dt*0.5) ,dt):
        alpha[i] = -rico
    return x, y, alpha

x, y, alpha = omega(standup_time, rico)

def hoeken(standup_time, dt, y):
    angles = np.zeros(len(x))
    angles[0] = 0
    for i in range(0, dt-1):
        angles[i+1] = angles[i] + y[i]*(standup_time/dt)
    return angles

angles = hoeken(standup_time, dt, y)

#torque_1
def torque_1(th_1):
    #due to gravity
    box_1 = np.cos(th_1) * r_1 * F
    link1_1 = np.cos(th_1) * r_1 * (1/2) * m_L1 * g

    #angular acceleration
    box_1a = alpha * m_tot * (np.cos(th_1) * r_1 ) ** 2
    link1_1a = alpha * (1/3) * m_L1 * (np.cos(th_1) * r_1) ** 2
    
    #total
    torque1 = box_1 + link1_1 + box_1a + link1_1a
    return torque1

torque1 = torque_1(th_1)

#torque_2
def torque_2(th_1, th_2):
    
    #due to gravity
    box_2 = (np.cos(th_1) * r_1 + np.cos(th_2) * r_2 ) * F
    joint1_2 = np.cos(th_2) * r_2 * m_B1 * g
    link1_2 = (np.cos(th_1) * r_1 * (1/2) + np.cos(th_2) * r_2 ) * m_L1 * g
    link2_2 = np.cos(th_2) * r_2 * (1/2) * m_L2 * g
    
    #angular acceleration
    box_2a = alpha * m_tot * ( np.cos(th_1) * r_1 + np.cos(th_2) * r_2 ) ** 2
    joint1_2a = alpha * m_B1 * ( np.cos(th_2) * r_2 ) ** 2
    link1_2a = alpha * (1/3) * m_L1 * (np.cos(th_1) * r_1 + np.cos(th_2) * r_2 ) ** 2   
    link2_2a = alpha * (1/3) * m_L2 * ( np.cos(th_2) * r_2 ) ** 2 

    #total
    torque2 = box_2 + joint1_2 + link1_2 + link2_2 + box_2a + joint1_2a + link1_2a + link2_2a
    
    return torque2

torque2 = torque_2(th_1, th_2)

#torque_3
def torque_3(th_3):    

    #due to gravity
    box_3 = np.cos(th_3) * r_3 * F
    joint1_3 = np.cos(th_3) * r_3 * m_B1 * g
    joint2_3 = np.cos(th_3) * r_3 * m_B2 * g
    link1_3 = np.cos(th_3) * r_3 * m_L1 * g
    link2_3 = np.cos(th_3) * r_3 * m_L2 * g
    link3_3 = np.cos(th_3) * r_3 * m_L3 * g
    
    #angular acceleration
    box_3a = alpha * m_tot * (np.cos(th_3) * r_3 )**2
    joint1_3a = alpha * m_B1 * (np.cos(th_3) * r_3 )**2 
    joint2_3a =  alpha * m_B2 * (np.cos(th_3) * r_3 )**2
    link1_3a = alpha * (1/3) *m_L1 *(np.cos(th_3) * r_3 )**2 
    link2_3a = alpha * (1/3) * m_L2 *(np.cos(th_3) * r_3 )**2 
    link3_3a = alpha * (1/3) * m_L3 * (np.cos(th_3) * r_3 )**2
    
    #total 
    torque3 = box_3 + joint1_3 + joint2_3 + link1_3 + link2_3 + link3_3 + box_3a + joint1_3a + joint2_3a + link1_3a + link2_3a + link3_3a 
    
    return torque3

#plots
torque3 = torque_3(th_3)
fig = plt.figure()
plt.grid()
plt.title('Torque j_1')
plt.ylabel('Torque (Nm)')
plt.xlabel('Angle (rad)')
plt.plot(th_1 , torque_1(th_1), 'r', label = 'j_1')
plt.legend()
plt.savefig('plots/tj1')


fig = plt.figure()
plt.grid()
plt.title('Torque j_2')
plt.ylabel('Torque (Nm)')
plt.xlabel('Angle (rad)')
plt.plot(th_2 , torque_2(th_1, th_2), 'b', label = 'j_2')
plt.legend()
plt.savefig('plots/tj2')


fig = plt.figure()
plt.grid()
plt.title('Torque j_3')
plt.ylabel('Torque (Nm)')
plt.xlabel('Angle (rad)')
plt.plot(th_33 , torque_3(th_3), 'g', label = 'j_3')
plt.legend()
plt.savefig('plots/tj3')


fig = plt.figure()
plt.grid()
plt.title('Reference in absolute values')
plt.ylabel('Torque (Nm)')
plt.xlabel('Angle (rad)')
plt.plot(th_1 , np.absolute(torque_1(th_1)), 'r', label = 'j_1')
plt.plot(th_2 , np.absolute(torque_2(th_1, th_2)), 'b', label = 'j_2')
plt.plot(th_33 , np.absolute(torque_3(th_3)), 'g', label = 'j_3')
plt.legend()
plt.savefig('plots/ref_abs')


fig = plt.figure()
plt.grid()
plt.title('Velocity')
plt.ylabel('Angular velocity (rad/s)')
plt.xlabel('Time t (s)')
plt.plot(x , y, 'b')
plt.savefig('plots/angular_vel')


fig = plt.figure()
plt.grid()
plt.title('Position')
plt.ylabel('Angular position (rad)')
plt.xlabel('Time t (s)')
plt.plot(x , angles, 'b')
plt.savefig('plots/angular_pos')


fig = plt.figure()
plt.grid()
plt.title('Acceleration')
plt.ylabel('Angular acceleration (rad/s^2)')
plt.xlabel('Time t (s)')
plt.plot(x , alpha, 'b')
plt.savefig('plots/angular_acc')


plt.show()


#determine maxima
maxt1 = np.where( torque1 == np.amax(torque1))
maxt2 = np.where( torque2 == np.amax(torque2))
maxt3 = np.where( torque3 == np.amax(torque3))


print("For j_1, maximum torque:", np.amax(torque1), "Nm, at angle", th_1[maxt1], "rad")
print("For j_2, maximum torque:", np.amax(torque2), "Nm, at angle", th_1[maxt2], "rad")
print("For j_3, maximum torque:", np.amax(torque3), "Nm, at every angle")


#determine motor charachteristics available motors
x = np.linspace(0,100,100)

#DS3218 5V
speed_t5 = 0.15
torque_t5 = 18

RPM_t5 = np.round(60/speed_t5)*(1/6)
stall_torque_t5 = (g*torque_t5)/100

#DS3218 6.8V
speed_t68 = 0.13
torque_t68 = 21.5

RPM_t68 = np.round(60/speed_t68)*(1/6)
stall_torque_t68 = (g*torque_t68)/100

#MG996R 4.8V
speed_s48 = 0.19
torque_s48 = 9.4

RPM_s48 = np.round(60/speed_s48)*(1/6)
stall_torque_s48 = (g*torque_s48)/100

#MG996R 6V
speed_s6 = 0.15
torque_s6 = 11

RPM_s6 = np.round(60/speed_s6)*(1/6)
stall_torque_s6 = (g*torque_s6)/100

#very cheap motors charachteristics

#SG90 6V
#speed_sg90 = 0.12
#torque_sg90 = 1.5
#
#RPM_sg90 = np.round(60/speed_sg90)*(1/6)
#stall_torque_sg90 = (g*torque_sg90)/100

#MG90S 6V
#speed_sg90 = 0.1
#torque_sg90 = 2.2
#
#RPM_sg90 = np.round(60/speed_sg90)*(1/6)
#stall_torque_sg90 = (g*torque_sg90)/100

#‎29SV40 6V
#speed_sg90 = 0.16
#torque_sg90 = 3.2
#
#RPM_sg90 = np.round(60/speed_sg90)*(1/6)
#stall_torque_sg90 = (g*torque_sg90)/100

#‎S3003 6V
#speed_sg90 = 0.19
#torque_sg90 = 4.1
#
#RPM_sg90 = np.round(60/speed_sg90)*(1/6)
#stall_torque_sg90 = (g*torque_sg90)/100

#PS-1171MG 6V
#speed_sg90 = 0.11
#torque_sg90 = 3.5
#
#RPM_sg90 = np.round(60/speed_sg90)*(1/6)
#stall_torque_sg90 = (g*torque_sg90)/100

#CS-239MG 6V
speed_sg90 = 0.14
torque_sg90 = 4.6

RPM_sg90 = np.round(60/speed_sg90)*(1/6)
stall_torque_sg90 = (g*torque_sg90)/100

def DS3218(RPM, torque):
    y = -(torque/RPM)*x + torque
    return y

y_t5 = DS3218(RPM_t5, stall_torque_t5)
y_t68 = DS3218(RPM_t68, stall_torque_t68)
y_s48 = DS3218(RPM_s48, stall_torque_s48)
y_s6 = DS3218(RPM_s6, stall_torque_s6)
y_sg90 = DS3218(RPM_sg90, stall_torque_sg90)

maxima = [np.absolute(np.amax(torque1)),np.absolute(np.amax(torque2)),np.absolute(np.amax(torque3))]
max = np.max(maxima)

#plot motor charachteristics
fig = plt.figure()
plt.axes( xlim=(0,80),ylim=(0, 2.2))
plt.grid()
plt.title('Motor criteria')
plt.ylabel('Torque (Nm)')
plt.xlabel('RPM')
plt.plot(x , y_t5,  label = "DS3218 5V")
plt.plot(x , y_t68,  label = "DS3218 6.8V")
plt.plot(x , y_s48, label = "MG996R 4.8V")
plt.plot(x , y_s6, label = "MG996R 6V")
plt.plot(x , y_sg90, label = "CS-239MG   6V")
plt.axhline(y = max ,color='blue',linestyle='dashed', label= "torque requirements")
plt.axvline(x = omega_RPM ,color='red',linestyle='dashed', label= "max RPM")
plt.legend()
plt.savefig('plots/motor_charachteristics')

plt.show()


















