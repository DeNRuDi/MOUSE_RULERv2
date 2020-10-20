import pyautogui
from pynput import mouse, keyboard
from time import sleep

class Values:
	"""Клас для определения параметров"""
	def __init__(self, resolution_x, resolution_y):
		self.i = 1
		self.count = 0
		self.resolution_x = resolution_x
		self.resolution_y = resolution_y
		pyautogui.FAILSAFE = False

		
x, y = pyautogui.size()		
value = Values(x, y)		

	
def measure_by_wheel(): # 1 пункт
	def on_press(key):
		if key == keyboard.Key.esc:
			return False	
	
	def on_scroll(x, y, dx, dy):
		print(value.i, end='\r')
		value.i+=1
		
	with mouse.Listener(on_scroll=on_scroll), keyboard.Listener(on_press=on_press) as listener:
		listener.join()
	result = float(value.i - 1) / 3.4
	print("Твой результат: " + str(round((result),1)) + " Cм\n")
	
	
def measure_by_laser(): # 2 пункт
	print("Выход - 'CTRL + C'")
	while True:
		x, y = pyautogui.position()
		if x <= int(value.resolution_x / 3.495) or x >=  int(value.resolution_x / 3.48):
			pyautogui.moveTo((value.resolution_x / 3.49), y)
		if y >= value.resolution_y - 50:
			pyautogui.moveTo(int(value.resolution_x / 3.49), 0)
			value.count += 2
		sleep(0.1)
		print("Твой результат ~ ", end='') 
		print(str(value.count) + " Cм", end='\r')

		
if __name__ == "__main__":
	try:
		print("\nMOUSE_RULER v2.1\nCopyright © 2020 DeNRuDi (Denis Rudnitskiy)\n")
		answer = input("[1]Измерить предмет колёсиком мыши\n[2]Измерить предмет лазером мыши\n[3]Выход\n\nВведите ответ>")
		if answer == str(1):
			i = 1
			print("После измерения, нажмите - 'ESC'")
			measure_by_wheel()
		elif answer == str(2):
			pyautogui.moveTo(250, 0)
			measure_by_laser()
		elif answer == str(3):
			exit(0)
		else:
			print("\nВведен неверный ответ!\n")
	except KeyboardInterrupt:
		print('\nВыход')		
