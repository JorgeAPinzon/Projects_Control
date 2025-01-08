"""
= This file is used for defining Ttk styles.

All style definitions should live in the function named:

   def setup_ttk_styles()

Use an instance of the ttk.Style class to define styles.

As this is a python module, now you can import any other
module that you need.


== In Pygubu Designer

Pygubu Designer will need to know which style definition file 
you wish to use in your project.

To specify a style definition file in Pygubu Designer:
Go to: Edit -> Preferences -> Ttk Styles -> Browse (button)

Assuming that you have specified a style definition file,
- Use the 'style' combobox drop-down menu in Pygubu Designer
  to select a style that you have defined.
- Changes made to the chosen style definition file will be
  automatically reflected in Pygubu Designer.


The code below shows the minimal example definition file.

"""

import tkinter as tk
import tkinter.ttk as ttk


def setup_ttk_styles(master=None):
    my_font = ("SF Pro Display", 11, "bold")
    
    style = ttk.Style(master)
    
    style.configure("primary.TButton",
                    font=my_font,
                    background="#4582EC",
                    foreground="white",
                    borderwidth=1)
    style.configure("secondary.TButton",
                    font=my_font,
                    background="#ADB5BD", 
                    foreground="white")
    style.configure("warning.TButton",
                    font=my_font,
                    background="#F0AD4E", 
                    foreground="white")    
    style.configure("danger.TButton",
                    font=my_font,
                    background="#D9534F", 
                    foreground="white")
    style.configure("boton_off.TButton",
                    font=my_font,
                    background="#ececec", 
                    foreground="darkred",
                    borderwidth=0)
    style.configure("boton_evento.TButton",
                    font=my_font,
                    background="#1b6889", 
                    foreground="white",
                    borderwidth=2)
    style.configure("boton_operando.TButton",
                    font=my_font,
                    background="#cbf603", 
                    foreground="#2bb903",
                    borderwidth=0)
    style.configure("MyStyle.TLabel",
                    font=my_font,
                    background="#e4e0d3", 
                    foreground="#444648")
    style.configure("Entrada.TLabel",
                    font=my_font, 
                    background="#aca6a3", 
                    foreground="black")
    style.configure("Radio_estilo_1.TRadiobutton", 
                    font=my_font,
                    background="#14a6ff", 
                    foreground="white",
                    borderwidth=2)
    style.configure("Radio_estilo_2.TRadiobutton", 
                    font=my_font,
                    background="#14a6ff", 
                    foreground="#cbf603",
                    borderwidth=2)
    style.configure("Userentry1.TEntry",
                    foreground="green")
