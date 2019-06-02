import tkinter as tk
from tkinter import font
import requests
HEIGHT = 500
WIDTH = 600




def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = round(weather['main']['temp']-273)
		
		final_str  = 'City: %s \nConditions: %s \nTemperature: %s (°C)' % (name,desc,str(temp))
		label['font'] = ('Courier',18)
		label['fg']='black'
	except:
		final_str = 'There was a problem recieving that information \n (May be the name of your city)'
		label['font']=('Courier',10)
		label['fg']='red'

	return final_str

def get_weather(city):
	weather_key = 'faca287f9cab90913d10d91eb8f23ef7'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID':weather_key, 'q':city, 'units':'Celsius'}
	respose = requests.get(url, params=params)
	weather = respose.json()
	
	label['text'] = format_response(weather)
	

#starting the window

root = tk.Tk()



canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='#42d1f4', bd=5)#bd is for the border around the widgets
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


entry = tk.Entry(frame, font=('Courier',18))
entry.place(relwidth=0.65, relheight=1 )

button = tk.Button(frame, text="Get Weather", font=('Courier',12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#42d1f4', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n' )

label = tk.Label(lower_frame, text='Result here', font=('Courier',18),anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

note = tk.Label(root, text='Example : Algiers , DZ', anchor='s', bd=4)
note.place(relx=0.5, rely=0.9,relwidth=0.2, relheight=0.05)




root.mainloop()
