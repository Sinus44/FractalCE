from Engine import *
import time
import random
import math

class Fractal:
	def __init__(self, start_pos, window, symbol):
		self.points = start_pos
		self.no_drawed_points = []
		self.last_point = self.points[0]
		self.window = window
		self.symbol = symbol

	def draw_point(self, point):
		self.window.point(point[0], point[1], self.symbol)

	def select_vertexes(self):
		return random.choice(self.points)

	def update(self):
		random_vertex = self.select_vertexes()
		self.last_point = ((random_vertex[0] + self.last_point[0]) / 2, (random_vertex[1] + self.last_point[1]) / 2)
		self.no_drawed_points.append(self.last_point)

	def draw(self):
		for point in self.no_drawed_points:
			self.draw_point(point)
		
		self.no_drawed_points = []

class Main_Window(Scene):
	def select(self):
		self.window.fill()
		self.fractals = [
			#down
			Fractal([[74, 43], [130, 54], [147, 34]], self.window, Symbol(char="#", text_color=Color.rgb_text(127, 0, 0))),
			Fractal([[130, 54], [58, 61], [115, 71]], self.window, Symbol(char="#", text_color=Color.rgb_text(0, 127, 0))),
			Fractal([[2, 52], [58, 61], [74, 43]], self.window, Symbol(char="#", text_color=Color.rgb_text(0, 0, 127))),
			
			#up
			Fractal([[38, 26], [95, 37], [74, 1]], self.window, Symbol(char="#", text_color=Color.rgb_text(255, 0, 0))),
			Fractal([[95, 37], [58, 61], [115, 71]], self.window, Symbol(char="#", text_color=Color.rgb_text(0, 255, 0))),
			Fractal([[2, 52], [38, 26], [58, 61]], self.window, Symbol(char="#", text_color=Color.rgb_text(0, 0, 255))),
		]
		self.fractals2 = [
			Fractal([
				[0, self.window.h],
				[self.window.w, self.window.h],
				[self.window.w // 2, 0]
			], self.window, Symbol(char="#", text_color=Color.rgb_text(255, 0, 0)))
		]

	def update(self):
		for fractal in self.fractals:
			fractal.update()

	def draw(self):
		#self.window.fill()
		for event in self.window.input_tick():
			print(event)
			if event["type"] == "exit":
				self.app.close()

			if event["type"] == "window":
				if event["window_x"] != self.window.w or event["window_y"] != self.window.h:
					self.window.set_size(self.window.w, self.window.h)

		for fractal in self.fractals:
			fractal.draw()

		self.window.print()

class Fractal_App:
	def __init__(self, width=150, height=75):
		self.width = width
		self.height = height

		self.window = Window(self.width, self.height)
		self.window.set_title("Fractal")
		self.window.set_icon("icon.ico")

		self.scene_control = Scene_Control(update_time=0, frame_time=0.1)
		self.scene_control.add_from_dict({
			"main": Main_Window(window=self.window, scene_control=self.scene_control, app=self)
		})

		self.scene_control.set("main")

	def run(self):
		self.scene_control.play()

	def close(self):
		self.window.close()
		self.scene_control.stop()

if __name__ == "__main__":
	fractal_app = Fractal_App()
	fractal_app.run()
