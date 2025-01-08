#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 08:50:51 2024

@author: antiXLinux
"""

import tkinter as tk
import tkinter.ttk as ttk
import Estilos_interfaz_Cl_  # Styles definition module
from pygubu.widgets.calendarframe import CalendarFrame
from tkdial import Meter
import tkinter.messagebox as messagebox
from tkdial import ScrollKnob
import time
import datetime
import pygubu.widgets.simpletooltip as tooltip
from simple_model import predict
from sklearn.linear_model import LinearRegression
import threading
from fuzzy_logic import fuzzy
from fuzzy_logic import evaluar_temperatura
import control
from pid_controller import controlPID

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation


class Guiv1App:
    
    def __init__(self, master=None):
        
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=200, width=200)
        
        # First object created
        Estilos_interfaz_Cl_.setup_ttk_styles(toplevel1)

        frame1 = ttk.Frame(toplevel1)
        frame1.configure(height=200, width=200)
        self.notificaciones = 0
        self.contadoraux = 0
        self.valoraux = 0
        self.advertencia = 0
        self.temperaturamanual = 0 # meter
        self.temperaturaerror = 0 # error PI 
        self.temperaturaactual =0 # error PI + manual meter
        self.temperaturaconfort = 0 # knob
        self.temperaturaautomatica = 0 # modo automatico + real regresion 
        
        
        label1 = ttk.Label(frame1)
        self.img_fondo_modos_op = tk.PhotoImage(file="fondo_modos_op.png")
        label1.configure(
            background="#ffffff",
            borderwidth=0,
            image=self.img_fondo_modos_op,
            text='label1')
        label1.grid(column=0, row=0)
        
        label2 = ttk.Label(frame1)
        label2.configure(
            background="#149bd8",
            font="{SF Pro Display} 10 {bold}",
            foreground="#f0f3f8",
            text='Hora:')
        label2.grid(column=0, padx=43, pady=130, row=0, sticky="nw")
        self.label2 = label2 # instancia de la clase ttklabel para label2.config
        
        label3 = ttk.Label(frame1)
        label3.configure(
            background="#149bd8",
            font="{SF Pro Display} 10 {bold}",
            foreground="#f0f3f8",
            text='Fecha:')
        label3.grid(column=0, padx=43, pady=155, row=0, sticky="nw")
        self.label3 = label3
        
        label4 = ttk.Label(frame1)
        label4.configure(
            background="#001321",
            font="{SF Pro Display} 20 {}",
            foreground="#e6e6eb",
            text='__')
        label4.grid(column=0, pady=210, row=0, sticky="n")
        self.label4 = label4
        
        label5 = ttk.Label(frame1)
        label5.configure(
            background="#14a6ff",
            font="{SF Pro Display} 12 {bold}",
            foreground="#f0f3f8",
            text='Regresión lineal:')
        #label5.grid(column=0, padx=86, pady=270, row=0, sticky="nw")
        self.label5 = label5
        
        label6 = ttk.Label(frame1)
        label6.configure(
            background="#6bc0e4",
            font="{SF Pro Display} 9 {}",
            foreground="#ffffff",
            text='0')
        label6.grid(column=0, padx=92, pady=88, row=0, sticky="ne")
        self.label6 = label6
        
        
        radiobutton1 = ttk.Radiobutton(frame1)
        self.var = tk.StringVar(value='')
        radiobutton1.configure(
            style="Radio_estilo_1.TRadiobutton",
            text='Modo manual',
            value="manual",
            variable=self.var)
        radiobutton1.grid(column=0, padx=86, pady=60, row=0, sticky="sw")
        radiobutton1.configure(command=self.ajuste_temperatura) # necesario para el try
        self.radiobutton1 = radiobutton1
        tooltip.create(self.radiobutton1,"Click cada vez que ajuste el indicador emergente a la temperatura deseada.")
        
        radiobutton3 = ttk.Radiobutton(frame1)
        radiobutton3.configure(
            style="Radio_estilo_1.TRadiobutton",
            text='Modo semiautomático',
            value="semiautomatico",
            variable=self.var)
        radiobutton3.grid(column=0, padx=260, pady=60, row=0, sticky="sw")
        radiobutton3.configure(command=self.ajuste_temperatura)
        self.radiobutton3 = radiobutton3
        tooltip.create(self.radiobutton3,"Click cada vez que ajuste el indicador emergente al confort deseado (scroll).")
        
        radiobutton4 = ttk.Radiobutton(frame1)
        radiobutton4.configure(
            style="Radio_estilo_1.TRadiobutton",
            text='Modo automático',
            value="automatico",
            variable=self.var)
        radiobutton4.grid(column=0, padx=475, pady=60, row=0, sticky="sw")
        radiobutton4.configure(command=self.ajuste_temperatura)
        self.radiobutton4 = radiobutton4
        
        
        meter2 = Meter(frame1, radius=55, start=6, end=40, border_width=2,border_color="white",
                       fg="gray", text_color="#1c2130", start_angle=180, end_angle=-90,
                       text_font="Crystal 11", scale_color="gray", axis_color="#1c2130",
                       bg="#14a6ff",needle_color="#1c2130",text="°C")
        meter2.set_mark(1, 12, "#beff00")  # verde
        meter2.set_mark(14, 20, "yellow")  # amarillo
        meter2.set_mark(22, 40, "#e32c00") #rojo
        meter2.set(0) 
        #meter2.grid(column=0, padx=115, pady=180, row=0, sticky="sw")
        self.meter2 = meter2
        self.meter2_visible = False
        self.meter2.set(11)
        
        
        knob1 = ScrollKnob(frame1, radius=60, progress_color="#3ca0c1", steps=25,
                         bg="#14a6ff",border_width=5, start_angle=90, inner_width=0, outer_width=0,
                         fg="#66c1e8",text_font="Ubuntu 8", text_color="#f1f0f1", bar_color="#66c1e8")
        #knob1.grid(column=0, padx=315, pady=180, row=0, sticky="sw")
        self.knob1 = knob1
        self.knob1_visible = False
        tooltip.create(self.knob1,
        "0% Frío 3-9°C \n25% Fresco 10-13°C \n50% Confortable 14-17°C \n75% Templado 18-21°C \n100% Cálido 22-27°C")
        
        
        button2 = ttk.Button(frame1)
        self.img_iconooff_rojo = tk.PhotoImage(file="iconooff_rojo.png")
        button2.configure(
            image=self.img_iconooff_rojo,
            style="boton_off.TButton",
            text='button2')
        button2.grid(column=0, padx=52, pady=62, row=0, sticky="nw")
        button2.configure(command=self.presion_boton_off)
        self.button2 = button2
        
        button3 = ttk.Button(frame1)
        button3.configure(style="boton_evento.TButton", text='Gráfico')
        button3.grid(column=0, padx=140, pady=51, row=0, sticky="ne")
        button3.configure(command=self.boton_grafico)
        self.button3 = button3
        tooltip.create(self.button3,"Presione cada vez que desee actualizar el grafico (modos de operación)")
        
        button4 = ttk.Button(frame1)
        button4.configure(style="boton_evento.TButton", text='Notificaciones')
        button4.grid(column=0, padx=140, pady=90, row=0, sticky="ne")
        button4.configure(command=self.boton_notificaciones)
        self.button4 = button4
        
        
        self.fig, self.ax = plt.subplots()
        objeto = FigureCanvasTkAgg(self.fig, master=None)
        objeto.get_tk_widget().config(width=325, height=210)
        #objeto.get_tk_widget().grid(column=0, padx=20, pady=170, row=0, sticky="ne")
        objeto.draw()
        self.objeto = objeto
        self.objeto_visible = False
        
        text1 = tk.Text(frame1)
        text1.configure(
            background="#14a6d3",
            borderwidth=0,
            font="{SF Pro Display} 11 {}",
            foreground="#ffffff",
            height=10,
            highlightbackground="#14a6d3",
            highlightcolor="#e6e6e6",
            highlightthickness=2,
            insertbackground="#e6e6e6",
            width=40)
        _text_ = 'Area de notificaciones'
        text1.insert("0.0", _text_)
        #text1.grid(column=0, padx=20, pady=2, row=0, sticky="se")
        self.text1 = text1
        self.text1_visible = False
        
        calendarframe1 = CalendarFrame(frame1)
        calendarframe1.configure(
            borderwidth=0,
            calendarbg="#f9f6f8",
            calendarfg="#000623",
            firstweekday=6,
            headerbg="#14a6e0",
            headerfg="#f1f1f1",
            linewidth=1,
            selectbg="#14a6e0",)
        #calendarframe1.grid(column=0, padx=220, pady=15, row=0, sticky="nw")
        self.calendarframe1 = calendarframe1
        self.calendar_visible = False
        tooltip.create(self.calendarframe1,"Seleccione una fecha con el cursor.")
        
        entry1 = ttk.Entry(frame1)
        _text_ = 'Hora(Militar H:Min)→'
        entry1.delete("0", "end")
        entry1.insert("0", _text_)
        #entry1.grid(column=0, ipadx=0, padx=265, pady=180, row=0, sticky="nw") por defecto oculto
        self.entry1= entry1
        entry1.bind("<FocusIn>", self.focus_entry)
        self.entry_focused = False
        #self.entry1_visible = False linea hasta el momento innecesaria OJO
        tooltip.create(self.entry1,"Ingrese la hora en formato 00:00 y presione programar.→→→→→→ ↑↑")
        
        button1 = ttk.Button(frame1)
        self.img_iconoprogramar = tk.PhotoImage(file="iconoprogramar.png")
        button1.configure(
            image=self.img_iconoprogramar,
            style="boton_off.TButton",
            text='button1')
        #button1.grid(column=0, padx=384, pady=178, row=0, sticky="nw")
        button1.configure(command=self.programar)
        self.button1 = button1
        self.button1_visible = False
        tooltip.create(self.button1,"Programar.")
        # para el apagado automatico
        self.hora =0
        self.minutos=0
        
        
        frame1.grid(column=0, row=0)
        self.frame1 = frame1
        
        # Main widget
        self.mainwindow = toplevel1
        self.reloj_programado_off()
        
        
    def reloj_programado_off(self):
        
        """
        -
        Función que establece la hora/fecha y las visualiza en la GUI + cierre programado.
        """
        
        if self.contadoraux <=0:
            
            self.modelo,self.temperatura,self.calor = predict()
            vectorcalorpredicho = self.modelo.predict(self.temperatura.reshape((-1, 1)))
            
            error = self.calor - vectorcalorpredicho  
            indice_error_minimo = np.argmin(np.abs(error))
            valor_predicho_minimo = vectorcalorpredicho[indice_error_minimo]
            self.temperaturaautomatica = valor_predicho_minimo*10000
            
            self.label4.config(text=str(round(self.temperaturaautomatica,2)) + '°')
            print(f"Temperatura real a {self.temperaturaautomatica}")
            
        self.tiempo_actual = time.strftime('%I:%M:%S %p')  # Formato de 12 horas con AM/PM
        self.tiempo_actual2 = time.strftime('%H:%M:%S')  # Formato de 24 horas
        fecha_actual = time.strftime('%d-%m-%Y')
        self.label2.config(text='Hora:  ' + self.tiempo_actual)
        self.label3.config(text='Fecha:  ' + fecha_actual)
        
        horareal = self.tiempo_actual2.split(":")[0]
        minutoreal = self.tiempo_actual2.split(":")[1]
        
        vectorcalorpredicho = self.modelo.predict(self.temperatura.reshape((-1, 1)))
        
        
        #error = calor - vectorcalorpredicho
        #error_MSE = np.mean((calor - vectorcalorpredicho) ** 2)
        
        #print('Prediccion (°C):',vectorcalorpredicho * 100)
        # Imprimir cada elemento del vector
        # Crear un evento para controlar el bucle
        
        detener_prediccion = threading.Event()

        def prediccion_loop():
            
            prev_value = None
            
            while not detener_prediccion.is_set():
                
                for valor in vectorcalorpredicho:
                    
                    self.valoraux = round(valor*100,3) # valor adquirido solamente aca en la gui
                    
                    if prev_value != self.valoraux:
                        
                        #print('Predicción (°C):', self.valoraux)
                        self.label5.config(text='Regresión lineal: ' + str(self.valoraux*100)) # multiplicado por 100
                                                            # exclusivamente por efectos del main
                        prev_value = self.valoraux
                        
                    time.sleep(0.5)  # espera 0.1 segundos antes de actualizar el label
                    
        hilo =  threading.Thread(target=prediccion_loop)
        hilo.start()
        #print(self.contadoraux)
        self.contadoraux+=1
        #print('Error:', error * 100)
        #print('Error cuadratico medio:',error_MSE * 100)
        #r2 = modelo.score(temperatura, calor)
        #print('Coeficiente de determinación (R^2):', r2)
        
        # Temporizador de apagado
        
        selected_date = self.calendarframe1.selection
        fecha_actual2 = datetime.date.today()
        
        if selected_date is not None:
            
            selected_date_obj = datetime.date(selected_date.year, selected_date.month, selected_date.day)
        
            if self.hora == int(horareal) and self.minutos == int(minutoreal) and selected_date_obj == fecha_actual2:
                
                self.mainwindow.destroy()
        
        self.mainwindow.after(1000, self.reloj_programado_off)
        
        detener_prediccion.set() # detiene el hilo pero no se detiene hasta llegar a la ultima 
                                # posicion y su respectiva iteracion 
        
              
        
    def run(self):
        
        """
        -
        Bucle main

        Returns
        -------
        None.

        """
        
        self.mainwindow.mainloop()
        
        
    def presion_boton_off(self):
        
        """
        -
        Función que muestra/oculta los elementos de interfaz y "limpia" el area de notificaciones
        """
        
        self.text1.insert("1.0", "Programar apagado...\n") # ojo aca va una NOTIFICACION 
        self.notificaciones +=1
        self.label6.config(text=str(self.notificaciones))
        
        if self.calendar_visible:
            
            self.calendarframe1.grid_remove()
            self.entry1.grid_remove()
            self.button1.grid_remove()
            
        else:
            
            self.calendarframe1.grid(column=0, padx=220, pady=15, row=0, sticky="nw")
            self.entry1.grid(column=0, ipadx=0, padx=265, pady=180, row=0, sticky="nw")
            self.button1.grid(column=0, padx=384, pady=178, row=0, sticky="nw")
            
        self.calendar_visible = not self.calendar_visible
    
    
    def programar(self):
        
        """
        -
        Función que establece la hora y fecha en la que se cierra la aplicación
        """
        
        if not self.entry_focused:
            
            self.text1.insert("1.0", "No ha seleccionado la hora en formato 00:00\n")
            self.notificaciones +=1
            self.label6.config(text=str(self.notificaciones))
        # Obtener la fecha seleccionada 
        
        selected_date = self.calendarframe1.selection
        fecha_actual = datetime.date.today() # usado para preguntar fechas a partir de hoy
        
        if selected_date is not None and self.entry_focused:
            
            # Convertir la fecha seleccionada a un objeto datetime.date
            # pasado a esta ubicacion y no en linea antes del if por excepcion de primera ejecucion
            
            selected_date_obj = datetime.date(selected_date.year, selected_date.month, selected_date.day)
            
            if selected_date_obj >= fecha_actual:
                
                #hora_minutos = self.entry1.get().split(":")
                try:
                    
                    hora_minutos = [int(x) for x in self.entry1.get().split(":")]
                    
                except ValueError:
                    
                        self.text1.insert("1.0", "Error: Valor no numérico encontrado\n")
                        self.notificaciones +=1
                        self.label6.config(text=str(self.notificaciones))
                        
                        return
                    
                if len(hora_minutos) == 2:
                    
                    self.hora = int(hora_minutos[0])
                    self.minutos = int(hora_minutos[1])
                    horareal = self.tiempo_actual2.split(":")[0]
                    minutoreal = self.tiempo_actual2.split(":")[1]
                    
                    if self.hora <=23 and self.minutos <=60:
                                                                                 # es decir los minutos ingresados son mayores
                        if selected_date_obj == fecha_actual and self.hora <= int(horareal) and self.minutos<int(minutoreal):
                            
                            self.text1.insert("1.0", "Verifique la hora ingresada\n")
                            self.notificaciones +=1
                            self.label6.config(text=str(self.notificaciones))
                            self.style = ttk.Style()
                            self.button1.config(style='warning.TButton',text = '')   
                            
                        else:
                            
                            self.notificaciones +=1
                            self.label6.config(text=str(self.notificaciones))
                            
                            if self.hora >= int(horareal) or selected_date_obj > fecha_actual:
                                
                                # pseudo - animacion del boton programar
                                
                                self.style = ttk.Style()
                                
                                self.button1.config(style='boton_operando.TButton',text = '')
                                print(f"Hora Programada: {self.hora}:{self.minutos}")
                                self.text1.insert("1.0", f"Hora Programada: {self.hora}:{self.minutos}\n")
                                print (f"Fecha Programada: {selected_date_obj}")
                                self.text1.insert("1.0", f"Fecha Programada: {selected_date_obj}\n")
                                print (f"Ejecutado a las: {horareal}:{minutoreal}")
                                self.text1.insert("1.0", f"Ejecutado a las: {horareal}:{minutoreal}\n")
                            #print (f"Minuto real 24H: {minutoreal}")
                            
                    else:
                        
                        self.notificaciones +=1
                        self.label6.config(text=str(self.notificaciones))
                        self.text1.insert("1.0", "Solo formato militar H : min\n")
                        self.style = ttk.Style()
                        self.button1.config(style='warning.TButton',text = '')
                else:
                    
                    self.notificaciones +=1
                    self.label6.config(text=str(self.notificaciones))
                    self.text1.insert("1.0", "Por favor, ingrese la hora en formato HH:MM\n")
                    self.style = ttk.Style()
                    self.button1.config(style='danger.TButton',text = '')  
            
            else:
                
                self.notificaciones +=1
                self.label6.config(text=str(self.notificaciones))
                self.text1.insert("1.0", "La fecha seleccionada debe ser igual o posterior a la fecha actual.\n")
                self.style = ttk.Style()
                self.button1.config(style='danger.TButton',text = '')  
        else:
            
            self.notificaciones +=1
            self.label6.config(text=str(self.notificaciones))
            self.text1.insert("1.0", "Seleccione una fecha\n")
            self.style = ttk.Style()
            self.button1.config(style='danger.TButton',text = '')  
    
    
    def focus_entry(self, event): # necesita el event por que no es un widget atribuido
                                   # y se usa la palabra clave arriba .bind focusin
        """
        -
        Funcion tipo self/event que usa el focusin para limpiar el dataentry 
        """  
                         
        self.entry1.delete("0", "end")
        self.entry1.focus_set()
        self.entry_focused = True
        
        
    def ajuste_temperatura(self):
        
        """
        -
        Función que se encarga de restringir y desplegar los elementos de ajuste ui
        """
        
        try:
            
            seleccion = self.var.get()
            
            
            if seleccion == 'manual':
                
                self.label5.grid_remove()
                self.knob1.grid_remove()
                self.notificaciones +=1
                self.label6.config(text=str(self.notificaciones))
                self.text1.insert("1.0", "Ajuste manual activado\n")
                self.radiobutton3.configure(style="Radio_estilo_1.TRadiobutton")
                self.radiobutton4.configure(style="Radio_estilo_1.TRadiobutton")
                self.temperaturamanual = self.meter2.get() # toma el valor manual como un dato de entrada 
                self.advertencia +=1
                
                
                # restricciones
                
                if (self.temperaturamanual > self.temperaturaautomatica + 2 or self.temperaturamanual < self.temperaturaautomatica - 2) and self.advertencia ==2: 
                    
                    messagebox.showwarning("Advertencia","Tenga en cuenta las implicaciones de cambiar la temperatura ±2°C cada vez. ")
                    # self.meter2.set(int(self.temperaturaautomatica))
                    # self.temperaturamanual = self.temperaturaautomatica
                
                if self.advertencia == 5 or self.advertencia == 6:
                    
                    messagebox.showwarning("Advertencia","Tenga en cuenta las implicaciones de cambiar la temperatura frecuentemente")
                
                if self.temperaturamanual > 27:
                    
                    messagebox.showerror("Error","Confort térmico comprometido.")
                    self.meter2.set(27)
                    self.temperaturamanual = 27
                    
                if self.temperaturaautomatica >= 25 and self.advertencia <= 1:
                  
                    messagebox.showinfo("Confort","La temperatura actual es muy grande.")
                    self.meter2.set(22)
                    self.temperaturamanual = 22
                    
                if self.temperaturaautomatica > 11 and self.advertencia<=1:
                    
                    self.meter2.set(int(self.temperaturaautomatica))
                    self.temperaturamanual = self.temperaturaautomatica
                
                # -- Modo manual PI 
                
                (error_estacionario , risetime, settlingtime, settlingmin, settlingmax,
                 overshoot, undershoot, t, y, sistema, sistema_controlado) = controlPID()
                
                tiempo = np.linspace(0, 10, 227)
                entrada_paso = self.temperaturamanual*np.ones_like(tiempo) 
                entrada_rampa = tiempo
                entradas = [entrada_paso, entrada_rampa]
                nombres = ['Paso']
                
                for entrada, nombre in zip(entradas, nombres ):
                    
                    respuesta= control.forced_response(sistema_controlado, tiempo, entrada)
                    tiempo_respuesta, y_respuesta = respuesta
                      
                    e = abs(y_respuesta[-1] - entrada[-1])
                    #print(f'El error de estado estacionario para una entrada {nombre} es {e}')

                # grafico por consola estatico
                
                # plt.figure()
                # plt.plot(tiempo_respuesta, y_respuesta)
                # plt.title(f'Respuesta al escalon para una entrada {nombre}')
                # plt.xlabel('Tiempo (s)')
                # plt.ylabel('Amplitud')
                # plt.grid(True)
                # plt.show()

                if self.meter2_visible:
                    
                    self.meter2.grid_remove()
                    
                else:
                    
                    self.meter2.grid(column=0, padx=115, pady=180, row=0, sticky="sw")
                    self.style = ttk.Style()
                    self.radiobutton1.configure(style="Radio_estilo_2.TRadiobutton")
                    self.label4.config(text=str(round(self.temperaturamanual + e,2)) + '°')
                    self.temperaturaerror = e
                    self.temperaturaactual = e + self.temperaturamanual
                    print(f'Temperatura manual configurada a {self.temperaturamanual}°C')
                    #print(f'El error registrado en este punto es {self.temperaturaerror}°C') # solo e
                    self.text1.insert("1.0", f'Temperatura manual configurada a {self.temperaturamanual}°C \n')
                    #print(self.temperaturamanual)
                    #print(self.temperatura*100) # temperatura de entrada de simple_model.py
                                         
            self.calendar_visible = not self.calendar_visible
            
            
            if seleccion == 'semiautomatico':
                
                self.label5.grid_remove()
                self.meter2.grid_remove()
                self.notificaciones +=1
                self.label6.config(text=str(self.notificaciones))
                self.text1.insert("1.0", "Ajuste semiautomático activado\n")
                self.radiobutton1.configure(style="Radio_estilo_1.TRadiobutton")
                self.radiobutton4.configure(style="Radio_estilo_1.TRadiobutton")
                self.temperaturaconfort = self.knob1.get()
                self.advertencia +=1
                sistemaf = fuzzy()
                valor_calor_fuzzy = evaluar_temperatura(sistemaf, self.temperaturaactual)
                
                if self.knob1_visible:
                    
                    self.knob1.grid_remove()
                    
                else:
                    
                    self.knob1.grid(column=0, padx=315, pady=180, row=0, sticky="sw")
                    self.style = ttk.Style()
                    self.radiobutton3.configure(style="Radio_estilo_2.TRadiobutton")
                    
                    # restricciones
                    
                    if self.temperaturamanual == 0 and self.temperaturaactual ==0:
                        
                        messagebox.showinfo("Info","A la espera de cambios en la entrada ó modo manual)")
                        
                        if 27 > self.temperaturaautomatica > 21:
                            
                            valor_calor_fuzzy = 48
                            
                        if 21 > self.temperaturaautomatica > 18:
                            
                            valor_calor_fuzzy = 48
                            
                        if 17 > self.temperaturaautomatica > 14:
                            
                            valor_calor_fuzzy = 52
                            
                        if 13 > self.temperaturaautomatica > 10:
                            
                            valor_calor_fuzzy = 60
                            
                        if 9 > self.temperaturaautomatica > 3:
                            
                            valor_calor_fuzzy = 82
                        
                    if self.temperaturaactual > 27.5:
                        
                        messagebox.showerror("Error","Confort térmico comprometido.")
                    
                    if self.temperaturaactual > 37: # modo recovery
                        
                        messagebox.showerror("Error","Confort térmico comprometido.")
                        
                        self.text1.insert("1.0", "Ajuste no permitido,\n en caso de fallas consulte con soporte técnico\n")
                        self.notificaciones +=1
                        self.meter2.set(27)
                        self.temperaturamanual = 27    
                    
                    # Confort predeterminado 
                    
                    if self.temperaturaconfort == 0 and 83.5 > valor_calor_fuzzy > 80.8:
                        
                        sistemaf = fuzzy()
                        valor_calor_fuzzy = evaluar_temperatura(sistemaf, self.temperaturaactual)
                        
                        self.meter2.set(9)
                        self.temperaturaactual = 9 + self.temperaturaerror # actualiza la variable
                        self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                        self.text1.insert("1.0", f'Temperatura semiautomática configurada a {round(self.temperaturaactual,3)}°C\n')
                        
                        print(f'Temperatura semiautomática configurada a {self.temperaturaactual}°C')
                        
                    if self.temperaturaconfort == 25 and 80.6 > valor_calor_fuzzy > 55:
                        
                        sistemaf = fuzzy()
                        valor_calor_fuzzy = evaluar_temperatura(sistemaf, self.temperaturaactual)
                        
                        self.meter2.set(13)
                        self.temperaturaactual = 13 + self.temperaturaerror
                        self.text1.insert("1.0", f'Temperatura semiautomática configurada a {round(self.temperaturaactual,3)}°C\n')
                        self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                        
                        print(f'Temperatura semiautomática configurada a {self.temperaturaactual}°C')
                    
                    if self.temperaturaconfort == 50 and 53 > valor_calor_fuzzy > 50.5:
                        
                        sistemaf = fuzzy()
                        valor_calor_fuzzy = evaluar_temperatura(sistemaf, self.temperaturaactual)
                        
                        self.meter2.set(16)
                        self.temperaturaactual = 16 + self.temperaturaerror
                        self.text1.insert("1.0", f'Temperatura semiautomática configurada a {round(self.temperaturaactual,3)}°C\n')
                        self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                        
                        print(f'Temperatura semiautomática configurada a {self.temperaturaactual}°C')
                    
                    if self.temperaturaconfort == 75 and 50.25 > valor_calor_fuzzy > 40.86:
                        
                        sistemaf = fuzzy()
                        valor_calor_fuzzy = evaluar_temperatura(sistemaf, self.temperaturaactual)
                        
                        self.meter2.set(18)
                        self.temperaturaactual = 18 + self.temperaturaerror
                        self.text1.insert("1.0", f'Temperatura semiautomática configurada a {round(self.temperaturaactual,3)}°C\n')
                        self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                        self.temperaturaautomatica = self.temperaturaactual
                        
                        print(f'Temperatura semiautomática configurada a {self.temperaturaactual}°C')
                        
                    if self.temperaturaconfort == 100 and 49.88 > valor_calor_fuzzy > 47.55:
                        
                        sistemaf = fuzzy()
                        valor_calor_fuzzy = evaluar_temperatura(sistemaf, self.temperaturaactual)
                        
                        self.meter2.set(22)
                        self.temperaturaactual = 22 + self.temperaturaerror
                        self.text1.insert("1.0", f'Temperatura semiautomática configurada a {round(self.temperaturaactual,3)}°C\n')
                        self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                        
                        print(f'Temperatura semiautomática configurada a {self.temperaturaactual}°C')
               
                
            if seleccion == 'automatico':
                
                self.meter2.grid_remove()
                self.knob1.grid_remove()
                self.notificaciones +=1
                self.label6.config(text=str(self.notificaciones))
                self.text1.insert("1.0", "Ajuste automático activado\n")
                self.radiobutton1.configure(style="Radio_estilo_1.TRadiobutton")
                self.radiobutton3.configure(style="Radio_estilo_1.TRadiobutton")
                self.style = ttk.Style()
                self.radiobutton4.configure(style="Radio_estilo_2.TRadiobutton")
                self.label5.grid(column=0, padx=86, pady=270, row=0, sticky="nw")
            
                # print(self.temperaturaerror)
                # print(self.temperaturaactual)
                # print(self.temperaturamanual)
                # print(self.temperaturaautomatica)
                
                if self.temperaturaerror ==0 and self.temperaturaactual ==0:
                    
                    if self.temperaturaautomatica > 24:
                        
                        self.temperaturaautomatica = self.temperaturaautomatica - 2
                        self.meter2.set(int(self.temperaturaautomatica))
                        self.temperaturaactual = self.temperaturaautomatica  # por coherencia solamente 
                    
                    else:
                        
                        self.temperaturaactual = self.temperaturaautomatica
                        self.meter2.set(int(self.temperaturaautomatica))
                    
                    self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                    self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                    print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                
                if self.temperaturaactual >= 0 and self.temperaturaconfort == 0 and self.var.get() == 'semiautomatico':  # esto es practicamente una excepcion
                    
                    self.meter2.set(11)
                    self.temperaturamanual = 11  # por inicio de operacion y quitar la primera advertencia
                    self.temperaturaactual = 11  # prioriza el modo automatico del semiautomatico
                    self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                    self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                    print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                    
                    # restriccion 
                    
                    if self.temperaturaactual >=11 and self.temperaturaconfort == 25:
                        
                        self.meter2.set(13)
                        self.temperaturamanual = 13  # por inicio de operacion y quitar la primera advertencia
                        self.temperaturaactual = 13  # prioriza el modo automatico del semiautomatico
                        self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                        self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                        print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                        
                if self.temperaturaerror != self.temperaturamanual: # modo manual a automatico activado
                        
                    print("modo manual a automatico activado")
                    
                    vectorcalorpredicho = self.modelo.predict(self.temperatura.reshape((-1, 1)))
                    r2 = self.modelo.score(self.temperatura, self.calor)
                    #r2 = 0.7
                    #print (r2)
                    
                    if r2 <= 0.6: 

                        error = self.calor - vectorcalorpredicho  
                        indice_error_minimo = np.argmin(np.abs(error))
                        valor_predicho_minimo = vectorcalorpredicho[indice_error_minimo]

                    # print('Valor predicho asociado al menor error:', valor_predicho_minimo * 100)  # Multiplicado por 100 si es necesario
                    # print('Error mínimo:', error[indice_error_minimo])
                    
                        sistemaf = fuzzy()
                        self.temperaturaautomatica = valor_predicho_minimo*10000 # por parametros de prediccion solamente
                        valor_automatico_difuso = evaluar_temperatura(sistemaf, self.temperaturaautomatica)
                        #valor_automatico_difuso = 82 # para realizar testing solamente
                        #print (self.temperaturaautomatica)
                        
                        if self.temperaturamanual > 26.5:
                            
                            print("Confort térmico comprometido")
                            messagebox.showerror("Error","Confort térmico comprometido.")
                    
                        if 49.88 > valor_automatico_difuso > 47.55 and 27 > self.temperaturamanual > 18:
                            
                            self.meter2.set(22)
                            self.temperaturamanual = 22 + self.temperaturaerror # por inicio de operacion y quitar la primera advertencia
                            self.temperaturaactual = 22 + self.temperaturaerror # prioriza el modo automatico del semiautomatico
                            self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                            self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                            print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                            
                            diferencia = self.temperaturaautomatica - self.temperaturamanual
                            
                            if diferencia > 3 and self.temperaturaconfort > 0:
                                
                                messagebox.showwarning("Atención", "Cambio de temperatura comprometido")             
                            
                        if 50.25 > valor_automatico_difuso > 40.86 and 20 > self.temperaturamanual > 16: 
                            
                            self.meter2.set(18)
                            self.temperaturamanual = 18 + self.temperaturaerror # por inicio de operacion y quitar la primera advertencia
                            self.temperaturaactual = 18 + self.temperaturaerror # prioriza el modo automatico del semiautomatico
                            self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                            self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                            print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                            
                        if 53 > valor_automatico_difuso > 50.5 and 18 > self.temperaturamanual > 14:
                            
                            self.meter2.set(16)
                            self.temperaturamanual = 16 + self.temperaturaerror # por inicio de operacion y quitar la primera advertencia
                            self.temperaturaactual = 16 + self.temperaturaerror # prioriza el modo automatico del semiautomatico
                            self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                            self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                            print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                            
                        if 80.6 > valor_automatico_difuso > 55 and 15 > self.temperaturamanual > 11:
                            
                            self.meter2.set(13)
                            self.temperaturamanual = 13 + self.temperaturaerror # por inicio de operacion y quitar la primera advertencia
                            self.temperaturaactual = 13 + self.temperaturaerror # prioriza el modo automatico del semiautomatico
                            self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                            self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                            print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                            
                        if 83.5 > valor_automatico_difuso > 80.8 and 11 > self.temperaturamanual > 7:
                            
                            self.meter2.set(9)
                            self.temperaturamanual = 9 + self.temperaturaerror # por inicio de operacion y quitar la primera advertencia
                            self.temperaturaactual = 9 + self.temperaturaerror # prioriza el modo automatico del semiautomatico
                            self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                            self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                            print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                            
                    if 1 >= r2 > 0.6:
                        
                        error = self.calor - vectorcalorpredicho  
                        indice_error_minimo = np.argmin(np.abs(error))
                        valor_predicho_minimo = vectorcalorpredicho[indice_error_minimo]
                        self.temperaturaautomatica = valor_predicho_minimo*10000 
                        print (self.temperaturaautomatica)
                        print (self.meter2.get())
                                              
                        if self.meter2.get() > self.temperaturaautomatica:
                            
                            print("El usuario ha decidido aumentar la temperatura...")
                            
                            #-----------------------------------------------------# Codigo clonado
                            sistemaf = fuzzy()
                            self.temperaturaautomatica = valor_predicho_minimo*10000 
                            valor_automatico_difuso = evaluar_temperatura(sistemaf, self.temperaturaautomatica)
                            # valor_automatico_difuso =49 
                            # self.temperaturamanual =29  
                            
                            if self.temperaturamanual > 26.5:
                                
                                print("Confort térmico comprometido")
                                messagebox.showerror("Error","Confort térmico comprometido.")
                            
                            if 49.88 > valor_automatico_difuso > 47.55 and 27 > self.temperaturamanual > 18:
                                
                                self.meter2.set(22)
                                self.temperaturamanual = 22 + self.temperaturaerror 
                                self.temperaturaactual = 22 + self.temperaturaerror 
                                self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                                self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                                print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                                
                                diferencia = self.temperaturaautomatica - self.temperaturamanual
                                
                                if diferencia > 3 and self.temperaturaconfort > 0:
                                    
                                    messagebox.showwarning("Atención", "Cambio de temperatura comprometido")  
                                  
                            if 50.25 > valor_automatico_difuso > 40.86 and 20 > self.temperaturamanual > 16: 
                                
                                self.meter2.set(18)
                                self.temperaturamanual = 18 + self.temperaturaerror 
                                self.temperaturaactual = 18 + self.temperaturaerror 
                                self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                                self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                                print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                                
                            if 53 > valor_automatico_difuso > 50.5 and 18 > self.temperaturamanual > 14:
                                
                                self.meter2.set(16)
                                self.temperaturamanual = 16 + self.temperaturaerror 
                                self.temperaturaactual = 16 + self.temperaturaerror 
                                self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                                self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                                print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                                
                            if 80.6 > valor_automatico_difuso > 55 and 15 > self.temperaturamanual > 11:
                                
                                self.meter2.set(13)
                                self.temperaturamanual = 13 + self.temperaturaerror 
                                self.temperaturaactual = 13 + self.temperaturaerror 
                                self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                                self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                                print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                                
                            if 83.5 > valor_automatico_difuso > 80.8 and 11 > self.temperaturamanual > 7:
                                
                                self.meter2.set(9)
                                self.temperaturamanual = 9 + self.temperaturaerror 
                                self.temperaturaactual = 9 + self.temperaturaerror 
                                self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                                self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                                print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                            #-----------------------------------------------------#
                            
                            
                        elif self.meter2.get() < self.temperaturaautomatica:
                            
                            diferencia = self.temperaturaautomatica - self.meter2.get()
                            
                            if diferencia <=2:
                                
                                self.temperaturaautomatica = self.meter2.get()
                                self.meter2.set(self.temperaturaautomatica)
                                self.temperaturamanual = self.temperaturaautomatica + self.temperaturaerror 
                                self.temperaturaactual = self.temperaturaautomatica + self.temperaturaerror 
                                self.label4.config(text=str(round(self.temperaturaactual,2)) + '°')
                                self.text1.insert("1.0", f'Temperatura automática configurada a {round(self.temperaturaactual,3)}°C\n')
                                print(f'Temperatura automática configurada a {self.temperaturaactual}°C')
                                
                            else: 
                                
                                print(f"Diferencia de temperatura {diferencia}°C")
                                       
        except ValueError:
            
            print("Error en la ejecución contacte con el desarrollador.")
            
    
    def boton_grafico(self):
        
        """
        -
        Funcion que se encarga del "objeto" grafico tipo matplotlib
        """
        
        #print('boton grafico oprimido ') # elemento auxiliar solamente
        
        if self.objeto_visible:
            
            self.objeto.get_tk_widget().grid_remove()
                   
        else:
            
            self.objeto.get_tk_widget().grid(column=0, padx=20, pady=170, row=0, sticky="ne")
            
            (error_estacionario , risetime, settlingtime, settlingmin, settlingmax,
             overshoot, undershoot, t, y, sistema, sistema_controlado) = controlPID()
            
            tiempo = np.linspace(0, 10, 227)
            
            if self.var.get() == 'manual': 
                
                entrada_paso = self.temperaturamanual*np.ones_like(tiempo)
                
            if self.var.get() == 'semiautomatico': 
                
                entrada_paso = self.temperaturaactual*np.ones_like(tiempo)
                
            if self.var.get() == 'automatico': 
                
                entrada_paso = self.temperaturaactual*np.ones_like(tiempo)
                
            if self.var.get() == '': 
                
                entrada_paso = self.temperaturaautomatica*np.ones_like(tiempo)
                self.text1.insert("1.0", f'Temperatura del sistema aproximada {round(self.temperaturaautomatica,3)}°C\n')
                
                        
            entrada_rampa = tiempo
            entradas = [entrada_paso, entrada_rampa]
            nombres = ['Paso']
            
            for entrada, nombre in zip(entradas, nombres ):

                respuesta= control.forced_response(sistema_controlado, tiempo, entrada)
                tiempo_respuesta, y_respuesta = respuesta
                
                e = abs(y_respuesta[-1] - entrada[-1])
                
                self.ax.clear()  # Limpiar el gráfico actual
                self.ax.plot(tiempo_respuesta, y_respuesta)
                self.ax.set_title(f'Respuesta al escalón para una entrada {nombre}')
                self.ax.set_xlabel('Tiempo (s)')
                self.ax.set_ylabel('Amplitud')
                self.ax.grid(True)
                
                # Redibujar el gráfico actualizado
                self.fig.canvas.draw()
            
        self.objeto_visible = not self.objeto_visible
       
    
    def boton_notificaciones(self):
        
        """
        -
        Función que despliega/oculta la caja de texto "notificaciones"
        """
        
        if self.text1_visible:
            
            self.text1.grid_remove()
            
        else:
            
            self.text1.grid(column=0, padx=20, pady=2, row=0, sticky="se")
            
        self.text1_visible = not self.text1_visible
         
            
if __name__ == "__main__":
    
    app = Guiv1App()
    app.run()