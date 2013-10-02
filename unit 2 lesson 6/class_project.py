class Fish:
	breathes_in_water = True
	skin = "scales"
	color: "green"
	def move(self,speed): 
			print "Swimming upright %s" % speed
class Flounder(Fish): 
	color: "blue"
spencer = Fish()