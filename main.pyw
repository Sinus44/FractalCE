from Engine import *
import time
import random
import math
from datetime import datetime

class Main_Window(Scene):
	def select(self):
		self.window.fill(" ")
		self.points = [[0, self.window.h], [self.window.w, self.window.h], [self.window.w // 2, 1]]

		for point in self.points:
			self.draw_point(point)

		self.last_point = self.points[0]
		
		self.window.point(0, 0, Color.rgb_text(255, 255, 255) + " ")
		self.frames = 0

	def generate_point(self):
		return [random.randint(0, self.window.w), random.randint(0, self.window.h)]

	def select_vertexes(self):
		return random.choice(self.points)

	def draw_point(self, point):
		self.window.point(point[0], point[1], "#")

	def play(self):
		if self.frames % 10000 == 0:
			for event in self.window.input_tick():
				if event["type"] == "exit":
					self.app.enable = False
					
			time.sleep(0.01)
			self.window.print()

		self.frames += 1

		random_vertex = self.select_vertexes()
		calculated_point = ((random_vertex[0] + self.last_point[0]) / 2, (random_vertex[1] + self.last_point[1]) / 2)
		self.last_point = calculated_point
		self.draw_point(self.last_point)

class Fractal_App:
	def __init__(self, width=120, height=60):
		self.width = width
		self.height = height
		self.enable = False

		self.window = Window(self.width, self.height)
		time.sleep(0.1)
		self.window.set_title("Fractal")

		self.scene_control = Scene_Control()
		self.scene_control.add_from_dict({
			"main": Main_Window(window=self.window, scene_control=self.scene_control, app=self)
		})
		self.scene_control.set("main")

	def run(self):
		self.enable = True
		while self.enable:
			self.scene_control.play()

if __name__ == "__main__":
	fractal_app = Fractal_App()
	fractal_app.run()