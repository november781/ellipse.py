# -*- coding: utf-8 -*-
from blessings import Terminal
import math
t=Terminal()
def elipse():
	#asks for a,and b
	print t.white("for a circle A and B need to be equal. \nin this elipse A is whatever value is in the denominator for x")
	A=float(raw_input("what is A?"))
	while A == 0:
		A=float(raw_input ("A cannot be 0, choose another number"))
	B=float(raw_input("what is B?"))
	while B == 0:
		B=float(raw_input ("B cannot be 0, choose another number"))
	#asks for the center
	print t.white("what is the center of the elipse? (H,K)")
	H=float(raw_input("what is H?"))
	K=float(raw_input("what is K?"))
	A2=math.pow(A, 2)
	B2=math.pow(B, 2)
	if A2>=B2:
		C2=A2-B2
	else:
		C2=B2-A2
	C=math.sqrt(C2)	
	#telling the user if the eilipse is horizontal, verticle, or a circle
	if A2>B2:
		print t.bright_yellow("you have a horizontal elipse\n")
	elif B2>A2:
		print t.bright_yellow("you have a verticle elipse\n")
	elif A2==B2:
		print t.bright_yellow("you have a circle\n")
	print t.bright_yellow("conic form")
	print t.green("((X-"+str(H)+")"u"\u00B2"")/"+str(A2)+" + ((Y-"+str(K)+")"u"\u00B2""/"+str(B2)+"=1\n")
	print t.bright_yellow("Y= equations:")
	print t.green("top half Y="+str(K)+"+"u'\u221A'"("+str(B)+""u"\u00B2""(1-(x-"+str(H)+")"u"\u00B2""/"+str(A)+""u"\u00B2""))")
	print t.green("bottom half Y="+str(K)+"-"u'\u221A'"("+str(B)+""u"\u00B2""(1-(x-"+str(H)+")"u"\u00B2""/"+str(A)+""u"\u00B2""))\n")
	#defining the foci 
	print t.bright_yellow("Foci:")
	if A2>B2:
		print t.green("(" + str(H + C) + "," + str(K) + ")\nand \n(" + str(H - C) + "," + str(K) + ")\n")
	elif B2>A2:
		print t.green("(" + str(H) + "," + str(K + C) + ")\nand \n(" + str(H) + "," + str(K - C) + ")\n")
	elif A2==B2:
		print t.green("none, this is a circle\n")
	#defining the Vertexes and endpoints
	if A2>=B2:
		print t.bright_yellow("Vertices")
		print t.green("(" + str(H + A) + "," + str(K) + ")\nand \n(" + str(H - A) + "," + str(K) + ") \n")
		print t.bright_yellow("Endpoints") 
		print t.green("(" + str(H) + "," + str(K+B) + ")\nand\n(" + str(H) + "," + str(K-B) + ")\n")
	else:
		print t.bright_yellow("Vertices")
		print t.green("(" + str(H) + "," + str(K+B) + ")\nand \n(" + str(H) + "," + str(K-B) +") \n")
		print t.bright_yellow("Endpoints")
		print t.green("(" + str(H+A) + "," + str(K) + ") \nand \n(" + str(H-A) + "," + str(K) + ")\n")
elipse()
