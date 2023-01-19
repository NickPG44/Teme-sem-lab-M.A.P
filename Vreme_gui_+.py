from tkinter import *
import tkinter
import customtkinter
import requests
import json
from datetime import datetime
 

 
root= customtkinter.CTk()
root.geometry(f"{400}x{400}")
root.title("Vremea")
 
city_value = StringVar()
 
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
 
city_value = StringVar()
 
def showWeather():
    api_key = "e4d0bdbbf86411baca209d357bf017b4"  
 
    city_name=city_value.get()

    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 

    response = requests.get(weather_url)
     
    weather_info = response.json()
 
    tfield.delete("1.0", "end") 
 
    if weather_info['cod'] == 200:
        kelvin = 273 
 
        temp = int(weather_info['main']['temp'] - kelvin)                                     
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
 
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
 

         
        weather = f"\nVremea din: {city_name}\nTemperatura (Celsius): {temp}°\nSe simte ca (Celsius): {feels_like_temp}°\nPresiunea: {pressure} hPa\nUmiditatea: {humidity}%\nRasaritul la {sunrise_time} and Apusul la {sunset_time}\nAcoperire nori: {cloudy}%\nInformatii: {description}"
    else:
        weather = f"\n\tVremea pentru '{city_name}' nu a fost gasita!\n\tIntrodu un nume valid!"
 
 
 
    tfield.insert(INSERT, weather) 
 
 
 

 
 

city_head = tkinter.StringVar(value="Numele orasului")

city_head= customtkinter.CTkLabel(master=root,
                               textvariable=city_head,
                               width=120,
                               height=25,
                               text_color=("white"),
                               font = ("Arial", 20),
                               corner_radius=8)
city_head.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)
 
entry = customtkinter.CTkEntry(master=root,
                               textvariable= city_value,
                               placeholder_text="Nume oras",
                               width=300,
                               height=35,
                               border_width=2,
                               corner_radius=10)
entry.place(relx=0.5, rely=0.13, anchor=tkinter.CENTER)



Button = customtkinter.CTkButton(master=root,
                                 width=170,
                                 height=45,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Verifica vremea",
                                 command=showWeather)
Button.place(relx=0.5, rely=0.27, anchor=tkinter.CENTER)

Wetherlabel = tkinter.StringVar(value="Datele despre vreme:")

Wetherlabel = customtkinter.CTkLabel(master=root,
                               textvariable=Wetherlabel,
                               width=165,
                               height=30,
                               text_color=("white"),
                               font = ("Arial", 20),
                               corner_radius=8)
Wetherlabel.place(relx=0.5, rely=0.40, anchor=tkinter.CENTER)

tfield = customtkinter.CTkTextbox(root,
                                width = 300,
                                height =200)    
tfield.grid(row=0, column=0)

tfield.place(relx = 0.5, rely = 0.7, anchor=tkinter.CENTER)



root.mainloop()