import time
from mirte_robot import robot
mirte = robot.createRobot()

# Starting in a laying position
def start():
	mirte.setServoAngle('1', 12)
	mirte.setServoAngle('2', 155)
	mirte.setServoAngle('3', 97)
	mirte.setServoAngle('4', 100)
	mirte.setServoAngle('5', 17)
	mirte.setServoAngle('6', 81)
	mirte.setServoAngle('7', 15)
	mirte.setServoAngle('8', 160)
	mirte.setServoAngle('9', 83)
	mirte.setServoAngle('10', 162)
	mirte.setServoAngle('11', 15)
	mirte.setServoAngle('12', 97)

# Going to the laying position in a controlled manner 
def lay():
	mirte.setServoAngle('1', 50)
	mirte.setServoAngle('2', 140)
	mirte.setServoAngle('3', 97)
	mirte.setServoAngle('4', 62)
	mirte.setServoAngle('5', 36)
	mirte.setServoAngle('6', 81)
	mirte.setServoAngle('7', 55)
	mirte.setServoAngle('8', 143)
	mirte.setServoAngle('9', 83)
	mirte.setServoAngle('10', 121)
	mirte.setServoAngle('11', 31)
	mirte.setServoAngle('12', 97)
	time.sleep(1)
	mirte.setServoAngle('1', 12)
	mirte.setServoAngle('2', 155)
	mirte.setServoAngle('3', 97)
	mirte.setServoAngle('4', 100)
	mirte.setServoAngle('5', 17)
	mirte.setServoAngle('6', 81)
	mirte.setServoAngle('7', 15)
	mirte.setServoAngle('8', 160)
	mirte.setServoAngle('9', 83)
	mirte.setServoAngle('10', 162)
	mirte.setServoAngle('11', 15)
	mirte.setServoAngle('12', 97)


# Standing up with the rear legs first
def stretch():
	mirte.setServoAngle('7', 95)
	mirte.setServoAngle('8', 125)
	mirte.setServoAngle('9', 83)
	mirte.setServoAngle('10', 80)
	mirte.setServoAngle('11', 47)
	mirte.setServoAngle('12', 97)
	time.sleep(0.5)
	mirte.setServoAngle('1', 88)
	mirte.setServoAngle('2', 125)
	mirte.setServoAngle('3', 100)
	mirte.setServoAngle('4', 20)
	mirte.setServoAngle('5', 55)
	mirte.setServoAngle('6', 80)

# Giving a paw for 3 seconds
def paw():
    mirte.setServoAngle('1', 88)
    mirte.setServoAngle('2', 125)
    mirte.setServoAngle('3', 100)
    mirte.setServoAngle('4', 20)
    mirte.setServoAngle('5', 55)
    mirte.setServoAngle('6', 80)
    mirte.setServoAngle('7', 95)
    mirte.setServoAngle('8', 125)
    mirte.setServoAngle('9', 83)
    mirte.setServoAngle('10', 80 + 30)
    mirte.setServoAngle('11', 47 - 20)
    mirte.setServoAngle('12', 97)
    time.sleep(0.5)
    mirte.setServoAngle('2', 125-80)
    time.sleep(3)
    mirte.setServoAngle('2', 125)
    time.sleep(0.5)
    mirte.setServoAngle('10', 80)
    mirte.setServoAngle('11', 47)
    
# Making one step in the forward direction
def forward():
	a = 10
	b = 5
	c = 2
	d = 10
	sleep = 0.2

	mirte.setServoAngle('4', 20 - a)
	mirte.setServoAngle('5', 55 - b)
	mirte.setServoAngle('7', 95 + a)
	mirte.setServoAngle('8', 125 + b)
	time.sleep(sleep)
	mirte.setServoAngle('4', 20 + c)
	mirte.setServoAngle('5', 55 - d)
	mirte.setServoAngle('7', 95 - c)
	mirte.setServoAngle('8', 125 + d)
	time.sleep(sleep)
	mirte.setServoAngle('4', 20 + b)
	mirte.setServoAngle('5', 55)
	mirte.setServoAngle('7', 95 - b)
	mirte.setServoAngle('8', 125)
	time.sleep(sleep)
	mirte.setServoAngle('4', 20)
	mirte.setServoAngle('7', 95)
	mirte.setServoAngle('1', 88 + a)
	mirte.setServoAngle('2', 125 + b)
	mirte.setServoAngle('10', 80 - a)
	mirte.setServoAngle('11', 47 - b)
	time.sleep(sleep)
	mirte.setServoAngle('1', 88 - c)
	mirte.setServoAngle('2', 125 + d)
	mirte.setServoAngle('10', 80 + c)
	mirte.setServoAngle('11', 47 - d)
	time.sleep(sleep)
	mirte.setServoAngle('1', 88 - b)
	mirte.setServoAngle('2', 125)
	mirte.setServoAngle('10', 80 + b)
	mirte.setServoAngle('11', 47)
	time.sleep(sleep)
	mirte.setServoAngle('1', 88)
	mirte.setServoAngle('10', 80)

	# Making one step in the backward direction
def backward():
	a = 10
	b = 5
	c = 2
	d = 10
	sleep = 0.2

	mirte.setServoAngle('4', 20 - a)
	mirte.setServoAngle('5', 55 + b)
	mirte.setServoAngle('7', 95 + a)
	mirte.setServoAngle('8', 125 - b)
	time.sleep(sleep)
	mirte.setServoAngle('4', 20 - a)
	mirte.setServoAngle('5', 55 + d)
	mirte.setServoAngle('7', 95 + a)
	mirte.setServoAngle('8', 125 - d)
	time.sleep(sleep)
	mirte.setServoAngle('4', 20 + b)
	mirte.setServoAngle('5', 55)
	mirte.setServoAngle('7', 95 - b)
	mirte.setServoAngle('8', 125)
	time.sleep(sleep)
	mirte.setServoAngle('4', 20)
	mirte.setServoAngle('7', 95)
	mirte.setServoAngle('1', 88 + a)
	mirte.setServoAngle('2', 125 - b)
	mirte.setServoAngle('10', 80 - a)
	mirte.setServoAngle('11', 47 + b)
	time.sleep(sleep)
	mirte.setServoAngle('1', 88 + a)
	mirte.setServoAngle('2', 125 - d)
	mirte.setServoAngle('10', 80 - a)
	mirte.setServoAngle('11', 47 + d)
	time.sleep(sleep)
	mirte.setServoAngle('1', 88 - b)
	mirte.setServoAngle('2', 125)
	mirte.setServoAngle('10', 80 + b)
	mirte.setServoAngle('11', 47)
	time.sleep(sleep)
	mirte.setServoAngle('1', 88)
	mirte.setServoAngle('10', 80)


# Making one step in the forward direction
def slow():
	a = 15
	b = 10
	c = 5
	d = 10
	e = 20
	sleep = 0.2

	mirte.setServoAngle('7', 95 - a)
	time.sleep(0.5)
	mirte.setServoAngle('4', 20 + b)
	mirte.setServoAngle('5', 55 - c)
	time.sleep(0.5)
	mirte.setServoAngle('5', 55 + d)
	time.sleep(0.5)
	mirte.setServoAngle('7', 95)
	mirte.setServoAngle('4', 20 + e)
	time.sleep(0.5)
	mirte.setServoAngle('7', 95 - b)
	mirte.setServoAngle('8', 125 + c)
	time.sleep(0.5)
	mirte.setServoAngle('8', 125 - d)
