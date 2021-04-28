#!/usr/bin/python

# Hello! Please follow the instructions in each step to get n estimated diameter!
# Steps
import tkinter
from tkinter.font import Font
from tkinter import *
from PIL import Image, ImageTk

root = tkinter.Tk()

# TKINTER PICKERS
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)
# Risk factor
riskFactor = tkinter.IntVar()
riskFactor.set(0)
# MaterialPicker
material = tkinter.IntVar()
material.set(0)
# Conditions
condition = tkinter.IntVar()
condition.set(0)
# Temperature
temperatureFactor = tkinter.IntVar()
temperatureFactor.set(0)
# Weather
weather = tkinter.IntVar()
weather.set(0)
# Conditions
# Polishing

# TKINTER GLOBAL PLACEHOLDERS
global condRespLab
condRespLab = Label(text = '', justify = LEFT)
# Temperature Factor
global tfRespLab
tfRespLab = Label(text = '', justify = LEFT)
# Weather condition
global wRespLabel
wRespLabel = Label(text = '', justify = LEFT)

# EQUATION VARIABLES
# Sut = tensile strength of selected material (May vary)
# Sy =
Sut = 0.0
Sy = 0.0
# Polish realted success rate
ka = 0.0
# We have an unknown diammeter so we will assume the size factor for our first guess
# Choose a size factor ranging from 0.7 to 1.0:
kb = 1 # Size factor
kc = 1 # Loading factor
# Weather
ke = 0.0

# FONTS
headingsFont = Font(
	family  = 'Helvetivca',
	size = 12,
	weight = 'bold')
bodyFont = Font(
	family  = 'Helvetivca',
	size = 11,
	weight = 'normal')

materialOptions = {
	'Steel': 1,
	'Wood': 2,
	'Glass': 3,
	'Aluminum': 4,
	'Plastic': 5
}
materialImages = {
	1: 'steel_material.jpg',
	2: 'wood_material.jpg',
	3: 'glass_material.jpg',
	4: 'aluminum_material.jpg',
	5: 'plastic_material.jpg'
}
mCharacteristics = {
	'Steel': {
		'Sut': 73,
		'Sy': 36
	},
	'Wood': {
		'Sut': .305,
		'Sy': .508
	},
	'Glass': {
		'Sut': 5.61,
		'Sy': 15
	},
	'Aluminum': {
		'Sut': 45,
		'Sy': 40
	},
	'Plastic': {
		'Sut': 70,
		'Sy': 40
	}
}
shaftConditions = {
	1: 'Not Polished',
	2: 'Some Polished',
	3: 'Very Polished'
}
condtionWarnings = [
	'You selected no polish, this dropped the success rate of your shaft by 20 percent',
	'You selected somewhat polished, this dropped the success rate of your shaft by 10 percent',
	'You selected very polished, this dropped the success rate of your shaft by 0'
]
tfOptions = {
	1: 'The engine temperature is normal!',
	2: 'The engine temperature might be too high for the shaft'
}
tfWarnings = [
	'You selected the engine temperature to be normal, this dropped the success rate of your shaft by 0 percent',
	'You selected that the engine cooling system still needs some work, this dropped the success rate of your shaft by 5 percent'
]
wOptions = {
	1: 'Rainy Day',
	2: 'Clear Sunny Day'
}
wWarnings = [
	'You considered rainy weather, this dropped the success rate of your shaft by 5 percent',
	'You selected a sunny warm day!, this dropped the success rate of your shaft by 0 percent'
]

def updateImage():
	bg = Image.open(materialImages[material.get()])
	bg = bg.resize((100,100), Image.ANTIALIAS)
	render = ImageTk.PhotoImage(bg)
	img = Label(root, image = render)
	img.image = render
	img.place(x = 180, y = 260)
	# Set Sut and Sy
	if (material.get() == 1):
		Sut = 73
		Sy = 36
	elif (material.get() == 2):
		Sut = .305
		Sy = .508
	elif (material.get() == 2):
		Sut = .305
		Sy = .508

def setCondition():
	if(condition.get() == 1):
		condRespLab.config(
			text = condtionWarnings[0],
			font = bodyFont,
			justify = LEFT,
			fg='#FAC800')
		ka = 0.8
	elif(condition.get() == 2):
		condRespLab.config(
			text = condtionWarnings[1],
			font = bodyFont,
			justify = LEFT,
			fg='#FAC800')
		ka = 0.9
	elif(condition.get() == 3):
		condRespLab.config(
			text = condtionWarnings[2],
			font = bodyFont,
			justify = LEFT,
			fg='green')
		ka = 1.0
	condRespLab.pack(anchor = tkinter.W)

def setTemperatureFactor():
	if (temperatureFactor.get() == 1):
		kd = 1
		tfRespLab.config(
			text = tfWarnings[0],
			font = bodyFont,
			justify = LEFT,
			fg='green')
	elif (temperatureFactor.get() == 2):
		kd = 0.95
		tfRespLab.config(
			text = tfWarnings[1],
			font = bodyFont,
			justify = LEFT,
			fg = '#FAC800')

def setWeather():
	if (weather.get() == 1):
		ke = 0.95
		wRespLabel.config(
			text = wWarnings[0],
			font = bodyFont,
			justify = LEFT,
			fg = '#FAC800')
	elif (weather.get() == 2):
		ke = 1
		wRespLabel.config(
			text = wWarnings[1],
			font = bodyFont,
			justify = LEFT,
			fg = 'green')

def main():
	instructionList = ('Hello! Please follow the instructions in each step to get an estimated diameter!',
		'     1) Input Factor of Safety',
		'     2) Select a material for your driveshaft',
		'     3) Select the conditions for your shaft',
		'     4) Plug in the amount of loading that your shaft will experience',
		'     5) Find Geometry Parameters',
		'     6) Your diameter size is. . . .')
	inputsRequired = [{
		'Step':'Step 1: Please, enter a "Factory of Safety" value between 1 and 10',
		'Reference':'(Refer to Source #1)',
		'InputStatement':'Enter a factor of safety: '
	}, {
		'Step':'Step 2: Select a material for your driveshaft',
		'Reference':'(Refer to Source #2)',
		'InputStatement':
			['Steel', 'Wood', 'Glass', 'Aluminum', 'Plastic']
	}, {
		'Step': 'Step 3: Select the conditions for your shaft',
		'InputStatement': 'Now that you picked your material, your shaft is manafactured! But will it be Not polished, Somewhat polished, or Very polished?'
	}, {
		'Step': 'Perhaps during the competition, your car engine might be too hot and will start melting your shaft',
		'InputStatement': 'Step 4: Select the temperature you predict for your engine'
	}, {
		'Step': 'Perhaps it will rain during the DISTANCE Competition, that might cause corrosion like rusting on your shaft. . .',
		'InputStatement': 'Step 5: Select the weather you predict on the day of the competition'
	}]

	s = '\n'
	instructionsString = s.join(instructionList)

	title = tkinter.Label(
		text = 'Instructions',
		font = headingsFont,
		justify = LEFT)
	title.pack(anchor = tkinter.W)

	instructions = tkinter.Label(
		text = instructionsString,
		font = bodyFont,
		justify = LEFT)
	instructions.pack(anchor = tkinter.W)

	# 1) Input a factor of safety
	stepOneLabel = Label(
		text = '\n\n' + inputsRequired[0]['Step'],
		font = bodyFont,
		justify = LEFT)
	stepOneLabel.pack(anchor = tkinter.W)
	w = Scale(root, digits = 2, from_ = 0, to = 10, font = bodyFont, orient = HORIZONTAL)
	w.pack(anchor = tkinter.W)

	# 2) Select the materials and its parameters
	avMaterialsLabel = Label(
		text = '\n\n' + inputsRequired[1]['Step'],
		font = bodyFont,
		justify = LEFT)
	avMaterialsLabel.pack(anchor = 'w')
	avMaterials = Label(
		text = 'Available Materials:',
		font = bodyFont,
		justify = LEFT)
	avMaterials.pack(anchor = 'w')

	for (key, value) in materialOptions.items():
		rb = tkinter.Radiobutton(root, text = key, variable = material, value = value, font = bodyFont, command = updateImage)
		rb.pack(anchor = tkinter.W)

	# 3) Select the conditions of your shaft
	conditionsLabel01 = Label(
		text = 	f'\n{inputsRequired[2]["Step"]}\n{inputsRequired[2]["InputStatement"]}',
		font = bodyFont,
		justify = LEFT
	).pack(anchor = tkinter.W)

	for (key,value) in shaftConditions.items():
		rb = tkinter.Radiobutton(root, text = value, variable = condition, value = key, font = bodyFont, command = setCondition)
		rb.pack(anchor = tkinter.W)

	condRespLab.pack(anchor = tkinter.W)

	# 4) Temperature Factor
	tempFactorLabel = Label(
		text = f'\n{inputsRequired[3]["Step"]}\n{inputsRequired[3]["InputStatement"]}',
		font = bodyFont,
		justify = LEFT).pack(anchor = tkinter.W)

	for (key, value) in tfOptions.items():
		rb = tkinter.Radiobutton(root, text = value, variable = temperatureFactor, value = key, font = bodyFont, command = setTemperatureFactor)
		rb.pack(anchor = tkinter.W)

	tfRespLab.pack(anchor = tkinter.W)

	# 5) Weather Label
	weatherLabel = Label(
		text = f'\n{inputsRequired[4]["Step"]}\n{inputsRequired[4]["InputStatement"]}',
		font = bodyFont,
		justify = LEFT)
	weatherLabel.pack(anchor = tkinter.W)

	for (key, value) in wOptions.items():
		rb = tkinter.Radiobutton(root, text = value, variable = weather, value = key, font = bodyFont, command = setWeather)
		rb.pack(anchor = tkinter.W)

	wRespLabel.pack(anchor = tkinter.W)

	root.mainloop()

if __name__ == "__main__":
	main()
