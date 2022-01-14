import time
from mirte_robot import robot
import curses
from functions import start, lay, stretch, paw, forward, backward

mirte = robot.createRobot()
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

#Start-up in laying position
start()

while True:
	#Get user input
	char = screen.getch()
	if char == ord('q'):
		break
	elif char == ord('l'):
		lay()
	elif char == ord('s'):
		stretch()
	elif char == ord('p'):
		paw()
	elif char == curses.KEY_UP:
		forward()
	elif char == curses.KEY_DOWN:
		backward()
	elif char == curses.KEY_RIGHT:
		print('Right')           
	elif char == curses.KEY_LEFT:
		print('LEFT')
