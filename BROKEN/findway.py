from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock
from kivy.uix.spinner import Spinner
from kivy.graphics import (Color, Line, Rectangle, Ellipse, Point)
from kivy.properties import (NumericProperty, StringProperty, ReferenceListProperty, ListProperty, ObjectProperty)
from kivy.vector import Vector
from kivy.core.window import Window
from kivy.factory import Factory
from math import fabs as modul
from kivy.graphics.texture import Texture

import importlib

import recmaze

import easy
import easyend
import normal
import normalend
import difficult
import difficultend
import impossible
import impossibleend

Window.size = (360, 640)

class Game(ScreenManager):
	pass

class Menu(Screen):
	def check_diff(self):

		if self.ids.difficulty.text == "Chose difficulty":
			self.ids.difficulty.background_color = [1, 0, 0, 1]
			print("difficulty is unchosen")

		else:
			self.parent.current = 'maze'

	def chose_difficulty(self, value):
		print(value)
		global val
		val = value
		self.ids.difficulty.background_color = [1, 1, 1, 1]

class Maze(Screen):
	texture = Texture.create(size=(1, 1))

	def open_back(self):
		BackPopup().open()

	def on_enter(self):
		Clock.schedule_interval(self.update, 1 / 30)

	def update(self, dt):
		print(Vector(modul(modul(Vector(self.ids.walker.direction).angle((1, 0))) - 90)/90, 0))

		
		self.ids.walker.is_last()

		# if self.ids.walker.current_dict == "y_dict":
			
		# 	if self.ids.walker.check_presence() and self.ids.walker.center[1] < self.ids.walker.last[1] + 10 and self.ids.walker.center[1] > self.ids.walker.last[1] - 10:
		# 		self.ids.walker.move()
		
		# 	elif not self.ids.walker.check_presence() and self.ids.walker.center[1] < self.ids.walker.last[1] + 10 and self.ids.walker.center[1] > self.ids.walker.last[1] - 10:
		# 		if self.ids.walker.center[0] > self.ids.walker.last[0]:
		# 			if modul(self.ids.walker.vect_angle) < 90:
		# 				self.ids.walker.vertical_slide()
		# 			elif modul(self.ids.walker.center[0]) >= 90:
		# 				self.ids.walker.move()
		# 		elif self.ids.walker.center[0] < self.ids.walker.last[0]:
		# 			if modul(self.ids.walker.vect_angle) > 90:
		# 				self.ids.walker.vertical_slide()
		# 			elif modul(self.ids.walker.vect_angle) <= 90:
		# 				self.ids.walker.move()

		# 	elif self.ids.walker.check_presence() and self.ids.walker.center[1] > self.ids.walker.last[1] + 10:
		# 		if self.ids.walker.vect_angle > 0:
		# 			self.ids.walker.horizontal_slide()
		# 		elif self.ids.walker.vect_angle <= 0:
		# 			self.ids.walker.move()

		# 	elif self.ids.walker.check_presence() and self.ids.walker.center[1] < self.ids.walker.last[1] - 10:
		# 		if self.ids.walker.vect_angle < 0:
		# 			self.ids.walker.horizontal_slide()
		# 		elif self.ids.walker.vect_angle > 0:
		# 			self.ids.walker.move()

		# else:

		# 	if self.ids.walker.check_presence() and self.ids.walker.center[0] < self.ids.walker.last[0] + 10 and self.ids.walker.center[0] > self.ids.walker.last[0] - 10:
		# 		self.ids.walker.move()
		
		# 	elif not self.ids.walker.check_presence() and self.ids.walker.center[0] < self.ids.walker.last[0] + 10 and self.ids.walker.center[0] > self.ids.walker.last[0] - 10:
		# 		if self.ids.walker.center[1] > self.ids.walker.last[1]:
		# 			if self.ids.walker.vect_angle > 0:
		# 				self.ids.walker.horizontal_slide()
		# 			elif self.ids.walker.vect_angle <= 0:
		# 				pass

		# 			#if modul(self.ids.walker.vect_angle) < 90:
		# 			#	self.ids.walker.vertical_slide()
		# 			#elif modul(self.ids.walker.center[1]) >= 90:
		# 			#	pass
		# 		elif self.ids.walker.center[1] < self.ids.walker.last[1]:
		# 			if self.ids.walker.vect_angle < 0:
		# 				self.ids.walker.horizontal_slide()
		# 			elif self.ids.walker.vect_angle > 0:
		# 				pass


		# 			#if modul(self.ids.walker.vect_angle) > 90:
		# 				#self.ids.walker.vertical_slide()
		# 			#elif modul(self.ids.walker.vect_angle) <= 90:
		# 				#pass

		# 	elif self.ids.walker.check_presence() and self.ids.walker.center[0] > self.ids.walker.last[0] + 10:
		# 		if modul(self.ids.walker.vect_angle) < 90:
		# 			self.ids.walker.vertical_slide()
		# 		elif modul(self.ids.walker.center[1]) >= 90:
		# 			pass

		# 	elif self.ids.walker.check_presence() and self.ids.walker.center[0] < self.ids.walker.last[0] - 10:
		# 		if modul(self.ids.walker.vect_angle) > 90:
		# 			self.ids.walker.vertical_slide()
		# 		elif modul(self.ids.walker.vect_angle) <= 90:
		# 			pass
		
		if self.ids.walker.check_presence():
			self.ids.walker.move()
			self.ids.walker.is_last()
		else:
			if self.ids.walker.change_dirrection():
				self.ids.walker.change_dirrection()
			else:
				self.ids.walker.slide()

		if val == "Easy":
			if self.ids.walker.collide_point(easyend.b[0],easyend.b[1]):
				print("easyend")
				self.ids.mazezone.change_maze()
				self.ids.mazezone.change_end()
				self.stop_updating()
				self.ids.walker.direction = Vector(0, 0)
				EndPopup(self.ids.mazezone).open()

		if val == "Normal":
			if self.ids.walker.collide_point(normalend.b[0], normalend.b[1]):
				print("normalend")
				self.ids.mazezone.change_maze()
				self.ids.mazezone.change_end()
				self.stop_updating()
				self.ids.walker.direction = Vector(0, 0)
				EndPopup(self.ids.mazezone).open()

		if val == "Difficult":
			if self.ids.walker.collide_point(difficultend.b[0], difficultend.b[1]):
				print("difficultend")
				self.ids.mazezone.change_maze()
				self.ids.mazezone.change_end()
				self.stop_updating()
				self.ids.walker.direction = Vector(0, 0)
				EndPopup(self.ids.mazezone).open()

		if val == "Impossible":
			if self.ids.walker.collide_point(impossibleend.b[0], impossibleend.b[1]):
				print("impossibleend")
				self.ids.mazezone.change_maze()
				self.ids.mazezone.change_end()
				self.stop_updating()
				self.ids.walker.direction = Vector(0, 0)
				EndPopup(self.ids.mazezone).open()

	def stop_updating(self):
		Clock.unschedule(self.update)

class EasyMaze(Widget):

	def draweasy(self):
		with self.canvas:
			Color(1, 0, 0, 1)
			#print(recmaze.trans(0, 0, 5, 8, 70, 30, 10, 17))
			for lists in easy.a:
				Line(points = tuple(lists), 
					close = False, 
					width = 30, 
					cap = 'square', 
					joint = 'miter')

	def draweasyfinal(self):
		with self.canvas:
			Color(0, 1, 0, 1)
			Point(points = tuple(easyend.b),
				pointsize = 10)

#чисто для мене
	def dot_the_way_easy(self):
		with self.canvas:
			Color(1, 0, 1, 1)
			for point in recmaze.dotway(easy.a):
				Point(points = point,
					pointsize = 1)

class NormalMaze(Widget):

	def drawnormal(self):
		with self.canvas:
			Color(1, 0, 0, 1)
			#print(recmaze.trans(0, 0, 7, 11, 49, 22, 11, 25))

			for lists in normal.a:
				Line(points = tuple(lists), 
					close = False, 
					width = 22, 
					cap = 'square', 
					joint = 'miter')

	def drawnormalfinal(self):
		with self.canvas:
			Color(0, 1, 0, 1)
			Point(points = normalend.b,
				pointsize = 7)
#чисто для мене 
	def dot_the_way_normal(self):
		with self.canvas:
			Color(1, 0, 1, 1)
			for point in recmaze.dotway(normal.a):
				Point(points = point,
					pointsize = 1)

class DifficultMaze(Widget):

	def drawdifficult(self):
		with self.canvas:
			Color(1, 0, 0, 1)
			#print(recmaze.trans(0, 0, 10, 16, 34, 15, 12, 22))

			for lists in difficult.a:
				Line(points = tuple(lists), 
					close = False, 
					width = 15, 
					cap = 'square', 
					joint = 'miter')

	def drawdifficultfinal(self):
		with self.canvas:
			Color(0, 1, 0, 1)
			Point(points = difficultend.b,
				pointsize = 5)
#чисто для мене
	def dot_the_way_difficult(self):
		with self.canvas:
			Color(1, 0, 1, 1)
			for point in recmaze.dotway(difficult.a):
				Point(points = point,
					pointsize = 1)

class ImpossibleMaze(Widget):

	def drawimpossible(self):
		with self.canvas:
			Color(1, 0, 0, 1)
			#print(recmaze.trans(0, 0, 17, 27, 20, 9, 11, 23))

			for lists in impossible.a:
				Line(points = tuple(lists), 
					close = False, 
					width = 9, 
					cap = 'square', 
					joint = 'miter')

	def drawimpossiblefinal(self):
		with self.canvas:
			Color(0, 1, 0, 1)
			Point(points = impossibleend.b,
				pointsize = 3)
#чисто для мене
	def dot_the_way_impossible(self):
		with self.canvas:
			Color(1, 0, 1, 1)
			for point in recmaze.dotway(impossible.a):
				Point(points = point,
					pointsize = 1)

class SituativeMaze(EasyMaze, NormalMaze, DifficultMaze, ImpossibleMaze):
	walker = ObjectProperty(None)
	mazezone = ObjectProperty(None)
	touch_pos = (0,0)
	move_pos = (0,0)

	def on_touch_down(self, touch):
		self.touch_pos = (touch.x, touch.y)

	def on_touch_move(self, touch):
		self.move_pos = (touch.x, touch.y)
		self.walker.direction = Vector(touch.x - self.touch_pos[0], touch.y - self.touch_pos[1]).normalize()

	def on_touch_up(self, touch):
		self.walker.direction = Vector(0, 0)

	def reset_clock(self):
		self.parent.on_enter()

	def change_maze(self):
		#викликає "maze", потім "trans" з початком в "easyend.py",
		#потім заміняє "easy.py" новим "trans"
		if val == "Easy":
			recmaze.maze((easyend.b[0] - 30 - 10)/70, (easyend.b[1] - 30 - 17)/70, 5, 8)
			with open("easy.py", "w") as easymaze:
				easymaze.write("a = {}\nx_dict = {}\ny_dict = {}".format(
					recmaze.trans(
					(easyend.b[0] - 30 - 10)/70, 
					(easyend.b[1] - 30 - 17)/70, 
					5, 
					8,
					70,
					30, 
					10, 
					17
					), 
				recmaze.x_dict_gen(recmaze.trans(
					(easyend.b[0] - 30 - 10)/70, 
					(easyend.b[1] - 30 - 17)/70, 
					5, 
					8,
					70,
					30, 
					10, 
					17
					)),
				recmaze.y_dict_gen(recmaze.trans(
					(easyend.b[0] - 30 - 10)/70, 
					(easyend.b[1] - 30 - 17)/70, 
					5, 
					8,
					70,
					30, 
					10, 
					17
					))
				))
			recmaze.x_dict.clear()
			recmaze.y_dict.clear()
			importlib.reload(easy)

		if val == "Normal":
			recmaze.maze((normalend.b[0] - 22 - 11)/49, (normalend.b[1] - 22 - 25)/49, 7, 11)
			with open("normal.py", "w") as normalmaze:
				normalmaze.write("a = {}\nx_dict = {}\ny_dict = {}".format(recmaze.trans(
					(normalend.b[0] - 22 - 11)/49, 
					(normalend.b[1] - 22 - 25)/49, 
					7, 
					11,
					49,
					22, 
					11, 
					25
					),
				recmaze.x_dict_gen(recmaze.trans(
					(normalend.b[0] - 22 - 11)/49, 
					(normalend.b[1] - 22 - 25)/49, 
					7, 
					11,
					49,
					22, 
					11, 
					25)),
				recmaze.y_dict_gen(recmaze.trans(
					(normalend.b[0] - 22 - 11)/49, 
					(normalend.b[1] - 22 - 25)/49, 
					7, 
					11,
					49,
					22, 
					11, 
					25))
				))
			recmaze.x_dict.clear()
			recmaze.y_dict.clear()
			importlib.reload(normal)

		if val == "Difficult":
			recmaze.maze((difficultend.b[0] - 15 - 12)/34, (difficultend.b[1] - 15 - 22)/34, 10, 16)
			with open("difficult.py", "w") as difficultmaze:
				difficultmaze.write("a = {}\nx_dict = {}\ny_dict = {}".format(recmaze.trans(
					(difficultend.b[0] - 15 - 12)/34, 
					(difficultend.b[1] - 15 - 22)/34, 
					10, 
					16,
					34,
					15, 
					12, 
					22
					),
				recmaze.x_dict_gen(recmaze.trans(
					(difficultend.b[0] - 15 - 12)/34, 
					(difficultend.b[1] - 15 - 22)/34, 
					10, 
					16,
					34,
					15, 
					12, 
					22
					)),
				recmaze.y_dict_gen(recmaze.trans(
					(difficultend.b[0] - 15 - 12)/34, 
					(difficultend.b[1] - 15 - 22)/34, 
					10, 
					16,
					34,
					15, 
					12, 
					22
					))
				))
			recmaze.x_dict.clear()
			recmaze.y_dict.clear()
			importlib.reload(difficult)

		if val == "Impossible":
			recmaze.maze((impossibleend.b[0] - 9 - 11)/20, (impossibleend.b[1] - 9 - 23)/20, 17, 27)
			with open("impossible.py", "w") as impossiblemaze:
				impossiblemaze.write("a = {}\nx_dict = {}\ny_dict = {}".format(recmaze.trans(
					(impossibleend.b[0] - 9 - 11)/20, 
					(impossibleend.b[1] - 9 - 23)/70, 
					17, 
					27,
					20,
					9, 
					11, 
					23
					),
				recmaze.x_dict_gen(recmaze.trans(
					(impossibleend.b[0] - 9 - 11)/20, 
					(impossibleend.b[1] - 9 - 23)/70, 
					17, 
					27,
					20,
					9, 
					11, 
					23
					)),
				recmaze.y_dict_gen(recmaze.trans(
					(impossibleend.b[0] - 9 - 11)/20, 
					(impossibleend.b[1] - 9 - 23)/70, 
					17, 
					27,
					20,
					9, 
					11, 
					23
					))
				))
			recmaze.x_dict.clear()
			recmaze.y_dict.clear()
			importlib.reload(impossible)

	def change_end(self):
		# змінює файл з кінцем на новий з "chose_final"
		# і почистити словник "way" (way.clear())
		if val == "Easy":
			with open("easyend.py", "w") as easyending:
				easyending.write("b = {}".format(recmaze.chose_final(
					70,
					30, 
					10, 
					17
					)))
			importlib.reload(easyend)

		if val == "Normal":
			with open("normalend.py", "w") as normalending:
				normalending.write("b = {}".format(recmaze.chose_final(
					49,
					22, 
					11, 
					25
					)))
			importlib.reload(normalend)

		if val == "Difficult":
			with open("difficultend.py", "w") as difficultending:
				difficultending.write("b = {}".format(recmaze.chose_final(
					34,
					15, 
					12, 
					22
					)))
			importlib.reload(difficultend)

		if val == "Impossible":
			with open("impossibleend.py", "w") as impossibleending:
				impossibleending.write("b = {}".format(recmaze.chose_final(
					20,
					9, 
					11, 
					23
					)))
			importlib.reload(impossibleend)

		recmaze.way.clear()

	def clear_widget(self):
		self.canvas.clear()

	def chosen_diff(self):
		self.walker.set_start()
		if val == "Easy":
			self.draweasy()
			self.draweasyfinal()
			self.dot_the_way_easy()

		if val == "Normal":
			self.drawnormal()
			self.drawnormalfinal()
			self.dot_the_way_normal()

		if val == "Difficult":
			self.drawdifficult()
			self.drawdifficultfinal()
			self.dot_the_way_difficult()

		if val == "Impossible":
			self.drawimpossible()
			self.drawimpossiblefinal()
			self.dot_the_way_impossible()

class Walker(Widget):

	dir_x = NumericProperty(0)
	dir_y = NumericProperty(0)
	direction = ReferenceListProperty(dir_x, dir_y)
	koef = NumericProperty(0)
	base = ListProperty([])
	last = None
	current_dict = StringProperty('')


	def move(self):
		self.pos = Vector(*self.direction) * self.koef + self.pos

	def slide(self):
		if self.current_dict == "y_dict":
			angle = modul(Vector(self.direction).angle((1, 0)))
			if angle > 0 and angle < 90:
				self.pos = Vector(-angle/90 + 1, 0) * self.koef + self.pos
			elif angle >= 90 and angle <= 180:
				self.pos = Vector(-(angle - 90)/90, 0) * self.koef + self.pos
		elif self.current_dict == "x_dict":
			angle = modul(Vector(self.direction).angle((0, 1)))
			if angle > 0 and angle < 90:
				self.pos = Vector(0, -angle/90 + 1) * self.koef + self.pos
			elif angle >= 90 and angle <= 180:
				self.pos = Vector(0, -(angle - 90)/90) * self.koef + self.pos


	def horizontal_slide(self):
		vect_angle = Vector(self.direction).angle((1, 0))
		self.pos = Vector(modul(modul(self.vect_angle) - 90)/90, 0) * self.koef + self.pos

	def vertical_slide(self):
		vect_angle = Vector(self.direction).angle((1, 0))
		self.pos = Vector(0, - (modul(vect_angle) - 90)/90 +1)
		pass

	def chose_first_base(self):
		self.last = self.center
		if val == "Easy":
			if (self.center[0] - 14, self.center[1]) in easy.y_dict[self.center[1]] or (self.center[0] + 14, self.center[1]) in easy.y_dict[self.center[1]]:
				self.base = easy.y_dict[self.center[1]]
				self.current_dict = "y_dict"
				print("y_dict")
				
			else:
				self.base = easy.x_dict[self.center[0]]
				self.current_dict = "x_dict"
				print("x_dict")

		elif val == "Normal":
			if (self.center[0] - 9.8, self.center[1]) in normal.y_dict[self.center[1]] or (self.center[0] + 9.8, self.center[1]) in normal.y_dict[self.center[1]]:
				self.base = normal.y_dict[self.center[1]]
				self.current_dict = "y_dict"
				print("y_dict")
			else:
				self.base = normal.x_dict[self.center[0]]
				self.current_dict = "x_dict"
				print("x_dict")

		elif val == "Difficult":
			if (self.center[0] - 6.8, self.center[1]) in difficult.y_dict[self.center[1]] or (self.center[0] + 6.8, self.center[1]) in difficult.y_dict[self.center[1]]:
				self.base = difficult.y_dict[self.center[1]]
				self.current_dict = "y_dict"
				print("y_dict")
			else:
				self.base = difficult.x_dict[self.center[0]]
				self.current_dict = "x_dict"
				print("x_dict")	

		elif val == "Impossible":
			if (self.center[0] - 4, self.center[1]) in impossible.y_dict[self.center[1]] or (self.center[0] + 4, self.center[1]) in impossible.y_dict[self.center[1]]:
				self.base = impossible.y_dict[self.center[1]]
				self.current_dict = "y_dict"
				print("y_dict")
			else:
				self.base = impossible.x_dict[self.center[0]]
				self.current_dict = "x_dict"
				print("x_dict")		

	def is_last(self):
		if val == "Easy":
			for point in self.base:
				if self.collide_point(point[0], point[1]):
					if self.current_dict == "x_dict" and point[1] in easy.y_dict.keys():
						self.last = point
					elif self.current_dict == "y_dict" and point[0] in easy.x_dict.keys():
						self.last = point
		if val == "Normal":
			for point in self.base:
				if self.collide_point(point[0], point[1]):
					if self.current_dict == "x_dict" and point[1] in normal.y_dict.keys():
						self.last = point
					elif self.current_dict == "y_dict" and point[0] in normal.x_dict.keys():
						self.last = point
		if val == "Difficult":
			for point in self.base:
				if self.collide_point(point[0], point[1]):
					if self.current_dict == "x_dict" and point[1] in difficult.y_dict.keys():
						self.last = point
					elif self.current_dict == "y_dict" and point[0] in difficult.x_dict.keys():
						self.last = point
		if val == "Impossible":
			for point in self.base:
				if self.collide_point(point[0], point[1]):
					if self.current_dict == "x_dict" and point[1] in impossible.y_dict.keys():
						self.last = point
					elif self.current_dict == "y_dict" and point[0] in impossible.x_dict.keys():
						self.last = point

	def check_presence(self):
		for point in self.base:
			if self.collide_point(point[0], point[1]):
				return True
		return False

	def change_dirrection(self):

		if val == "Easy":
			if self.current_dict == "x_dict":
				for point in easy.y_dict[self.last[1]]:
					if self.collide_point(point[0], point[1]):
						self.current_dict = "y_dict"
						self.base = easy.y_dict[self.last[1]]
						return True

			elif self.current_dict == "y_dict":
				for point in easy.x_dict[self.last[0]]:
					if self.collide_point(point[0], point[1]):
						self.current_dict = "x_dict"
						self.base = easy.x_dict[self.last[0]]
						return True
			return False

		if val == "Normal":
			if self.current_dict == "x_dict":
				for point in normal.y_dict[self.last[1]]:
					if self.collide_point(point[0], point[1]):
						self.current_dict = "y_dict"
						self.base = normal.y_dict[self.last[1]]
						return True

			elif self.current_dict == "y_dict":
				for point in normal.x_dict[self.last[0]]:
					if self.collide_point(point[0], point[1]):
						self.current_dict = "x_dict"
						self.base = normal.x_dict[self.last[0]]
						return True
			return False

		if val == "Difficult":
			if self.current_dict == "x_dict":
				for point in difficult.y_dict[self.last[1]]:
					if self.collide_point(point[0], point[1]):
						self.current_dict = "y_dict"
						self.base = difficult.y_dict[self.last[1]]
						return True

			elif self.current_dict == "y_dict":
				for point in difficult.x_dict[self.last[0]]:
					if self.collide_point(point[0], point[1]):
						self.current_dict = "x_dict"
						self.base = difficult.x_dict[self.last[0]]
						return True
			return False

		if val == "Impossible":
			if self.current_dict == "x_dict":
				for point in impossible.y_dict[self.last[1]]:
					if self.collide_point(point[0], point[1]):
						self.current_dict = "y_dict"
						self.base = impossible.y_dict[self.last[1]]
						return True

			elif self.current_dict == "y_dict":
				for point in impossible.x_dict[self.last[0]]:
					if self.collide_point(point[0], point[1]):
						self.current_dict = "x_dict"
						self.base = impossible.x_dict[self.last[0]]
						return True
			return False				


	def set_start(self):
		if val == "Easy":
			self.koef = 4
			self.pos = (easy.a[0][0] - 15, easy.a[0][1] - 15)
			self.size_hint = (None, None)
			self.size = (30, 30)

		if val == "Normal":
			self.koef = 2.94
			self.pos = (normal.a[0][0] - 11, normal.a[0][1] - 11)
			self.size_hint = (None, None)
			self.size = (22, 22)

		if val == "Difficult":
			self.koef = 2
			self.pos = (difficult.a[0][0] - 7.5, difficult.a[0][1] - 7.5)
			self.size_hint = (None, None)
			self.size = (15, 15)

		if val == "Impossible":
			self.koef = 1.2
			self.pos = (impossible.a[0][0] - 4.5, impossible.a[0][1] - 4.5)
			self.size_hint = (None, None)
			self.size = (9, 9)

class EndPopup(Popup):
	def __init__(self, obj, **kwargs):
		super(EndPopup, self).__init__(**kwargs)
		self.obj = obj

class BackPopup(Popup):
	pass

class SettingsPopup(Popup):
	soundbutt = ObjectProperty(None)
	musicbutt = ObjectProperty(None)

	def first_sound(self):
		with open("sound.txt") as sound:
			self.onoffsound = sound.read()
			print(self.onoffsound)
			return self.onoffsound

	def first_music(self):
		with open("music.txt") as music:
			self.onoffmusic = music.read()
			print(self.onoffmusic)
			return self.onoffmusic

	def soundonoff(self):
		if self.onoffsound == "Sound: on":
			with open("sound.txt", "w") as sound:
				sound.write("Sound: off")
			with open("sound.txt") as sound:
				self.onoffsound = sound.read()
			
			self.ids.soundbutt.text = self.onoffsound

			print("sound is off")
			print("checking sound......{}".format(self.onoffsound))

		else:
			with open("sound.txt", "w") as sound:
				sound.write("Sound: on")
			with open("sound.txt") as sound:
				self.onoffsound = sound.read()
			
			self.ids.soundbutt.text = self.onoffsound

			print("sound is on")
			print("checking sound......{}".format(self.onoffsound))

	def musiconoff(self):

		if self.onoffmusic == "Music: on":
			with open("music.txt", "w") as music:
				music.write("Music: off")
			with open("music.txt") as music:
				self.onoffmusic = music.read()
			self.ids.musicbutt.text = self.onoffmusic

			print("music is off")

		else:
			with open("music.txt", "w") as music:
				music.write("Music: on")
			with open("music.txt") as music:
				self.onoffmusic = music.read()
			self.ids.musicbutt.text = self.onoffmusic

			print("music is on")

class FindWayApp(App):

	def open_settings(self):
		settingspop = SettingsPopup()
		settingspop.open()

	def build(self):
		return

if __name__ == "__main__":
    FindWayApp().run()