from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

class parent3(object):
	def __init__(self, **kwargs):
		print "class pareft3"
		super(parent3, self).__init__()
class parent2(object):
	def __init__(self, **kwargs):
		print "ClASS parent2"
class parent1(parent3):
	def __init__(self, **kwargs):
		print "Class PArent1"
		super(parent1, self).__init__()

class child(parent1, parent2):
	def __init__(self, **kwargs):
		print kwargs
		super(child, self).__init__()
		
parent = child(k="yo")