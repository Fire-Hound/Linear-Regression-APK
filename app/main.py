from kivy.app import App 
from kivy.uix.textinput import TextInput 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
# class Scroll(ScrollView):
# 	def __init__(self, **kwargs):
# 		super(Scroll, self).__init__(**kwargs)
# 		self.size_hint=(1, None)
# 		self.size=(Window.width, Window.height)

class Scrol(ScrollView,GridLayout):
	def __init__(self, **kwargs):
		super(Scrol, self).__init__(**kwargs)
		self.cols = 2
		
		self.size_hint=(1, None)
		self.size=(Window.width, Window.height)
	def update_padding(self, text_input, *args):
		text_width = text_input._get_text_width(text_input.text, text_input.tab_width, text_input._label_cached)
		print(text_width, " ",text_input.width)
		text_input.padding_x = (text_input.width - text_width)/2

	# def test(self, instance):
	# 	x = [self.children[i].text for i in range(-3,-13,-2)]
	# 	y = [self.children[i].text for i in range(-4,-14,-2)]
	# 	n = 5
	# 	print(self.ids["lol2"].text)

	def calculation(self):
		x = [float(self.children[0].children[i].text) for i in range(-3,-13,-2)]
		y = [float(self.children[0].children[i].text) for i in range(-4,-14,-2)]
		n = 5
		
		
		sum_of_x = sum(x)
		sum_of_y = sum(y)

		squared_x = [z*z for z in x]
		squared_y = [z*z for z in y]

		sum_of_squared_x = sum(squared_x)
		sum_of_squared_y = sum(squared_y)
		

		x_mul_y = [x[a]*y[a] for a in range(5)]
		

		sum_of_x_mul_y = sum(x_mul_y)


		x_bar = sum_of_x / n
		y_bar = sum_of_y / n

		byx = ((n * sum_of_x_mul_y) - (sum_of_x * sum_of_y)) / ((n*sum_of_squared_x)-(sum_of_x * sum_of_x))
		bxy = ((n * sum_of_x_mul_y) - (sum_of_x * sum_of_y)) / ((n*sum_of_squared_y)-(sum_of_y * sum_of_y))

		if(self.ids["lol10"].choosen):
			X = float(self.ids["lol10"].text)
			Y = (byx*X) + (byx*x_bar) - y_bar
			self.ids["lol13"].text = "byx = " + str(byx) + "\n" + "Y = " + str(Y)

		if(self.ids["lol11"].choosen):
			Y = float(self.ids["lol11"].text)
			X = (bxy*Y) + (bxy*y_bar) - x_bar
			self.ids["lol13"].text = "bxy = " + str(bxy) + "\n" + "X = " + str(X)
	
		

class LinearApp(App):
	def build(self):

		return Scrol()

if __name__=="__main__":
	LinearApp().run()