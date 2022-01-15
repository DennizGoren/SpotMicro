import matplotlib.pyplot as plt
import pandas as pd
import imageio,glob,numpy as np 

#Part 1: alculating the actual position, velocity and acceleration

def png_to_gif(foldername,gifname):
  images = [] 
  filenames = glob.glob(foldername+'/*.png') # Get all the pngs in the directory
  # Sort the images by #, th  s may need to be tweaked for your use case
  list.sort(filenames, key=lambda x: int(x.split('_')[1].split('.png')[0])) 
  for filename in filenames:
    images.append(imageio.imread(filename))
  imageio.mimsave(gifname, images)

def robot_plot(max):
  for i in range(0, max):  
    fig, axes = plt.subplots(figsize=(6, 6))
    axes.set_xlim(0, 0.5)
    axes.set_ylim(0, 0.5)

    t = run.loc['sch-l']['t'][i]
    time=f'{t:.2f}'
    axes.text(0.1, 0.4, 't='+time, size=12, color='purple')

    #x en y voor i-de groen punt - schouders?  
    x_values = [run.loc['sch-l']['x'][i], run.loc['sch-r']['x'][i]]
    y_values = [run.loc['sch-l']['y'][i], run.loc['sch-r']['y'][i]]
    _ = axes.plot(x_values,y_values,'go')

    #x en y voor i-de blauwe punt - heupen?  
    x_values = [run.loc['el-l']['x'][i], run.loc['el-r']['x'][i]]
    y_values = [run.loc['el-l']['y'][i], run.loc['el-r']['y'][i]]
    _ = axes.plot(x_values,y_values,'bo')

    #x en y voor i-de rode punt - voeten?  
    x_values = [run.loc['p-l']['x'][i], run.loc['p-r']['x'][i]]
    y_values = [run.loc['p-l']['y'][i], run.loc['p-r']['y'][i]]
    _ = axes.plot(x_values,y_values,'ro')

    #x en y voor lijnen linker-kant
    x_values = [run.loc['p-l']['x'][i], run.loc['el-l']['x'][i], run.loc['sch-l']['x'][i]]
    y_values = [run.loc['p-l']['y'][i], run.loc['el-l']['y'][i], run.loc['sch-l']['y'][i]]
    _ = axes.plot(x_values,y_values,'.k',linestyle="--")
    #x en y voor lijnen rechter-kant
    x_values = [run.loc['p-r']['x'][i], run.loc['el-r']['x'][i], run.loc['sch-r']['x'][i]]
    y_values = [run.loc['p-r']['y'][i], run.loc['el-r']['y'][i], run.loc['sch-r']['y'][i]]
    _ = axes.plot(x_values,y_values,'.k',linestyle="--")
    #x en y voor lijnen rechter-linker-kant
    x_values = [run.loc['sch-l']['x'][i], run.loc['sch-r']['x'][i]]
    y_values = [run.loc['sch-l']['y'][i], run.loc['sch-r']['y'][i]]
    _ = axes.plot(x_values,y_values,'.k',linestyle="--")

    filename='export/foo_'+f'{i:02d}'+'.png'
    plt.savefig(filename)
    # plt.show()
    plt.close(fig)
    
def lengte(x1, x2, y1, y2):
  return np.sqrt((x1-x2)**2 +  (y1-y2)**2)

def arc(x1, x2, x3, y1, y2, y3):
  a = lengte(x2, x3, y2, y3)
  b = lengte(x1, x3, y1, y3)
  c = lengte(x1, x2, y1, y2)
  return np.arccos((a**2 - b**2 + c**2) / 2*a*c)

run_4 = pd.read_csv('run_4.csv',skiprows=[1]).round(3)
run_5 = pd.read_csv('run_5.csv',skiprows=[1]).round(3)
run_10 = pd.read_csv('run_10.csv',skiprows=[1]).round(3)
run_11 = pd.read_csv('run_11.csv',skiprows=[1]).round(3)
run_pa = pd.read_csv('run_pa.csv',skiprows=[1]).round(3)
run_pv = pd.read_csv('run_pv.csv',skiprows=[1]).round(3)


run_4['time'] = run_4['time'] - run_4['time'][0]
run_5['time'] = run_5['time'] - run_5['time'][0]
run_10['time'] = run_10['time'] - run_10['time'][0]
run_11['time'] = run_11['time'] - run_11['time'][0]
run_pa['time'] = run_pa['time'] - run_pa['time'][0]
run_pv['time'] = run_pv['time'] - run_pv['time'][0]

run = pd.concat([run_4, run_5,run_10,run_11,run_pa,run_pv],keys=['el-r','sch-r','el-l','sch-l','p-l','p-r'])
run.rename(columns={'P1X': 'x', 'P1Y': 'y', 'time': 't'}, inplace=True)

robot_plot(len(run.loc['sch-l']))
png_to_gif(folder+'export',folder+'export/animation.gif')

rc_df = pd.DataFrame() 
rc_df['t']= run.loc['sch-r']['t'].values

rc_df['angle elbow left'] = np.arccos(( (lengte(run.loc['sch-l']['x'],run.loc['sch-r']['x'],run.loc['sch-l']['y'],run.loc['sch-r']['y']))**2 - (lengte(run.loc['el-l']['x'],run.loc['sch-r']['x'],run.loc['el-l']['y'],run.loc['sch-r']['y']))**2 + (lengte(run.loc['el-l']['x'],run.loc['sch-l']['x'],run.loc['el-l']['y'],run.loc['sch-l']['y']))**2 ) / ( 2 * ((lengte(run.loc['sch-l']['x'],run.loc['sch-r']['x'],run.loc['sch-l']['y'],run.loc['sch-r']['y']))) * ((lengte(run.loc['el-l']['x'],run.loc['sch-l']['x'],run.loc['el-l']['y'],run.loc['sch-l']['y']))) ) )
rc_df['angle wrist left'] = np.arccos(( (lengte(run.loc['el-l']['x'],run.loc['sch-l']['x'],run.loc['el-l']['y'],run.loc['sch-l']['y']))**2 - (lengte(run.loc['p-l']['x'],run.loc['sch-l']['x'],run.loc['p-l']['y'],run.loc['sch-l']['y']))**2 + (lengte(run.loc['p-l']['x'],run.loc['el-l']['x'],run.loc['p-l']['y'],run.loc['el-l']['y']))**2 ) / ( 2 * ((lengte(run.loc['el-l']['x'],run.loc['sch-l']['x'],run.loc['el-l']['y'],run.loc['sch-l']['y']))) * (lengte(run.loc['p-l']['x'],run.loc['el-l']['x'],run.loc['p-l']['y'],run.loc['el-l']['y'])) ) )
rc_df['angle elbow right'] = np.arccos(( (lengte(run.loc['sch-r']['x'],run.loc['el-r']['x'],run.loc['sch-r']['y'],run.loc['el-r']['y']))**2 - (lengte(run.loc['sch-l']['x'],run.loc['el-r']['x'],run.loc['sch-l']['y'],run.loc['el-r']['y']))**2 + (lengte(run.loc['sch-l']['x'],run.loc['sch-r']['x'],run.loc['sch-l']['y'],run.loc['sch-r']['y']))**2 ) / ( 2 * ((lengte(run.loc['sch-r']['x'],run.loc['el-r']['x'],run.loc['sch-r']['y'],run.loc['el-r']['y']))) * ((lengte(run.loc['sch-l']['x'],run.loc['sch-r']['x'],run.loc['sch-l']['y'],run.loc['sch-r']['y']))) ) )
rc_df['angle wrist right'] = np.arccos(( (lengte(run.loc['el-r']['x'],run.loc['sch-r']['x'],run.loc['el-r']['y'],run.loc['sch-r']['y']))**2 - (lengte(run.loc['p-r']['x'],run.loc['sch-r']['x'],run.loc['p-r']['y'],run.loc['sch-r']['y']))**2 + (lengte(run.loc['p-r']['x'],run.loc['el-r']['x'],run.loc['p-r']['y'],run.loc['el-r']['y']))**2 ) / ( 2 * ((lengte(run.loc['el-r']['x'],run.loc['sch-r']['x'],run.loc['el-r']['y'],run.loc['sch-r']['y']))) * (lengte(run.loc['p-r']['x'],run.loc['el-r']['x'],run.loc['p-r']['y'],run.loc['el-r']['y'])) ) )

rc_df['velocity wrist right'] = rc_df['angle wrist right'].diff() / rc_df['t'].diff()
rc_df['velocity wrist left'] = rc_df['angle wrist left'].diff() / rc_df['t'].diff()
rc_df['velocity elbow right'] = rc_df['angle elbow right'].diff() / rc_df['t'].diff()
rc_df['velocity elbow left'] = rc_df['angle elbow left'].diff() / rc_df['t'].diff()

rc_df['acceleration wrist right'] = rc_df['velocity wrist right'].diff() / rc_df['t'].diff()
rc_df['acceleration wrist left'] = rc_df['velocity wrist left'].diff() / rc_df['t'].diff()
rc_df['acceleration elbow right'] = rc_df['velocity elbow right'].diff() / rc_df['t'].diff()
rc_df['acceleration elbow left'] = rc_df['velocity elbow left'].diff() / rc_df['t'].diff()

#plotting these values

angles = rc_df.plot(x="t",y=['angle wrist right','angle elbow right','angle wrist left','angle elbow left'],figsize=(9, 8))
angles.grid()
angles.set_title('Position')
angles.set_ylabel('Angle (rad)')
angles.set_xlabel('Time (s)')

velocity = rc_df.plot(x="t",y=['velocity wrist right', 'velocity wrist left'],figsize=(9, 8))
velocity.grid()
velocity.set_title('Velocity wrists')
velocity.set_ylabel('Angular velocity (rad/s)')
velocity.set_xlabel('Time (s)')

velocity2 = rc_df.plot(x="t",y=['velocity elbow right','velocity elbow left'],figsize=(9, 8))
velocity2.grid()
velocity2.set_title('Velocity elbows')
velocity2.set_ylabel('Angular velocity (rad/s)')
velocity2.set_xlabel('Time (s)')

acceleration = rc_df.plot(x="t",y=['acceleration wrist right', 'acceleration wrist left'],figsize=(9, 8))
acceleration.grid()
acceleration.set_title('Acceleration wrists')
acceleration.set_ylabel('Angular acceleration (rad/s^2)')
acceleration.set_xlabel('Time (s)')

acceleration2 = rc_df.plot(x="t",y=['acceleration elbow right','acceleration elbow left'],figsize=(9, 8))
acceleration2.grid()
acceleration2.set_title('Acceleration elbows')
acceleration2.set_ylabel('Angular acceleration (rad/s^2)')
acceleration2.set_xlabel('Time (s)')

# Part 2: Using these values as inputs for the dynamical kinematics model

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

#torque_1
def torque_1(th_1,alpha):
    #due to gravity
    box_1 = np.cos(th_1) * r_1 * F
    link1_1 = np.cos(th_1) * r_1 * (1/2) * m_L1 * g

    #angular acceleration
    box_1a = alpha * m_tot * (np.cos(th_1) * r_1 ) ** 2
    link1_1a = alpha * (1/3) * m_L1 * (np.cos(th_1) * r_1) ** 2
    
    #total
    torque1 = box_1 + link1_1 + box_1a + link1_1a
    return torque1

#torque_2
def torque_2(th_1, th_2,alpha):
    
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

#torque_3
def torque_3(th_3,alpha):    

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

#Filling in the functions

rc_df["torque wrist left"] = torque_1(rc_df['angle wrist left'], rc_df['acceleration wrist left'])
rc_df["torque wrist right"] = torque_1(rc_df['angle wrist right'], rc_df['acceleration wrist right'])
rc_df["torque elbow left"] = torque_1(rc_df['angle elbow left'], rc_df['acceleration elbow left'])
rc_df["torque elbow right"] = torque_1(rc_df['angle elbow right'], rc_df['acceleration elbow right'])

#plotting the values

torque1 = rc_df.plot(x="angle wrist left",y=["torque wrist left"],figsize=(9, 8))
torque1.grid()
torque1.set_title('Torque requirement wrist left')
torque1.set_ylabel('Torque (Nm)')
torque1.set_xlabel('Angle (rad)')

torque2 = rc_df.plot(x="angle wrist right",y=["torque wrist right"],figsize=(9, 8))
torque2.grid()
torque2.set_title('Torque requirement wrist right')
torque2.set_ylabel('Torque (Nm)')
torque2.set_xlabel('Angle (rad)')

torque3 = rc_df.plot(x="angle elbow left",y=["torque elbow left"],figsize=(9, 8))
torque3.grid()
torque3.set_title('Torque requirement elbow left')
torque3.set_ylabel('Torque (Nm)')
torque3.set_xlabel('Angle (rad)')

torque4 = rc_df.plot(x="angle elbow right",y=["torque elbow right"],figsize=(9, 8))
torque4.grid()
torque4.set_title('Torque requirement elbow right')
torque4.set_ylabel('Torque (Nm)')
torque4.set_xlabel('Angle (rad)')

#Max realistic torque
T_1 = rc_df["torque wrist left"]
T_2 = rc_df["torque wrist right"]
T_3 = rc_df["torque elbow left"]
T_4 = rc_df["torque elbow right"]

maxt1 = T_1.max()
maxt2 = T_2.max()
maxt3 = T_3.max()
maxt4 = T_4.max()

print(max(maxt1,maxt2,maxt3,maxt4))