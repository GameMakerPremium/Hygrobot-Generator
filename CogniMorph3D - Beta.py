# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:35:34 2024

@author: gabri
"""
from tkinter import ttk
import tkinter as tk
import webbrowser
import pyautogui
import pygetwindow as gw
import os
import sys
import time
import shutil
import tkinter as tk
import os
from tkinter import ttk
import winsound
import webbrowser
import subprocess
from PIL import Image, ImageTk, ImageOps  # Ensure ImageOps is imported
from tkinter import PhotoImage, Label
import math
import tkinter as tk
from tkinter import messagebox, Toplevel, Scale, HORIZONTAL, Radiobutton, IntVar
import sympy as sp
import sys
from operator import itemgetter
import fullcontrol as fc
from math import tau
from copy import deepcopy
import os
import glob
import math
import time
import pyautogui
import pygetwindow as gw
from datetime import datetime
import ast
import numpy as np
import cv2
import sympy as sp
import tkinter as tk
from tkinter import *
from tkinter import messagebox
root = tk.Tk()

def _from_rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("400x300")
    tk.Label(new_window, text="This is the new window!").pack(pady=20)


def welcome():
    global root
    subtitle = "Welcome to CogniMorph 3D developed by Gabriele Dutli!"
    subtitle2 = "Experience and design the future of intelligent materials."
    
    def fade_in_label(label, text, delay=40, steps=40, callback=None):
        """
        Function to animate the label text with a fade-in effect.
    
        Args:
        - label (tk.Label): The label widget to animate.
        - text (str): The text to display in the label.
        - delay (int): Delay in milliseconds between color changes.
        - steps (int): Number of steps in the fade-in process.
        - callback (function): Function to call after the fade-in completes.
        """
        def fade(step=0):
            gray_value = int(240 * (1 - step / steps))  # Calculate gray value
            color = f"#{gray_value:02x}{gray_value:02x}{gray_value:02x}"  # Convert to hex
            label.config(text=text, fg=color)
            if step < steps:
                label.after(delay, fade, step + 1)
            else:
                if callback:
                    callback()  # Call the callback function after fade-in is complete
    
        fade()
    
    def fade_in_button(button, delay=40, steps=40):
        """
        Function to animate a button with a fade-in effect by gradually making it visible.
        
        Args:
        - button (tk.Button): The button widget to animate.
        - delay (int): Delay in milliseconds between visibility changes.
        - steps (int): Number of steps in the fade-in process.
        """
        button.place(x=450, y=400)  # Initially place the button, but it's not yet visible
        
        def fade(step=0):
            alpha_value = int(255 * (step / steps))  # Calculate opacity
            color = f"#{alpha_value:02x}{alpha_value:02x}{alpha_value:02x}"  # Create a color with transparency effect
            button.config(bg=color)  # Change button background color
            if step < steps:
                button.after(delay, fade, step + 1)
            else:
                button.config(state="normal")  # Enable the button after fade-in completes
    
        fade()
    

    root.destroy()
    root = tk.Tk()
    
    root.title("CogniMorph 3D")
    window_width = 1000
    window_height = 700
    root.geometry(f"{window_width}x{window_height}")

    # Create a title label with initially invisible text (white on white)
    title_label = tk.Label(root, text="CogniMorph 3D [beta]", font=("Helvetica", 24, "bold"), fg="#F0F0F0")
    title_label.pack(pady=40)

    # Create a subtitle label with initially invisible text (white on white)
    subtitle_label = tk.Label(root, text=subtitle, font=("Helvetica", 16), fg="#F0F0F0")
    subtitle_label.pack(pady=5)
    
    # Create a subtitle label with initially invisible text (white on white)
    subtitle_label2 = tk.Label(root, text=subtitle2, font=("Helvetica", 16), fg="#F0F0F0")
    subtitle_label2.pack(pady=5)

    # Create a button that opens a new window (initially hidden)
    button = tk.Button(root, text="START", state="disabled", command=return2main, cursor="hand2", font=("Helvetica", 15, "bold"))
    button.place_forget()  # Hide the button initially

    def fade_in_button_after_subtitles():
        # Fade in the button after both subtitles have faded in
        fade_in_button(button)

    def fade_in_subtitles():
        # Fade in the second subtitle and then start fading in the button
        fade_in_label(subtitle_label, subtitle, callback=lambda: fade_in_label(subtitle_label2, subtitle2, callback=fade_in_button_after_subtitles))

    # Start the fade-in animation for the title, then the subtitles
    fade_in_label(title_label, "CogniMorph 3D [beta]", callback=fade_in_subtitles)

    # Run the Tkinter event loop
    root.mainloop()    


def return2main():
    #Create "FILES" folder, if not present
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folder_name = "FILES"
    new_folder_path = os.path.join(current_directory, folder_name)
    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)
    
    
    def Pass():
        global root
        root.destroy()
        
        root = tk.Tk()
        
        root.title("TROUBLESHOOTING")
        window_width = 1000
        window_height = 700
        root.geometry(f"{window_width}x{window_height}")
        
        
    
    def _from_rgb(r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'
    
    #Return to main window:
    def mainWindow():
        global root
        global dropdown_var, dropdown_var2
        try:
            root.destroy() 
        except:
            pass
        
        root = tk.Tk()
        root.title("CogniMorph 3D")
        
        window_width = 1000
        window_height = 750
        root.geometry(f"{window_width}x{window_height}")
        
        title_label = tk.Label(root, text="CogniMorph 3D", font=("Helvetica", 24, "bold"))
        title_label.pack(pady=20)
        
        box_frame = tk.Frame(root)
        box_frame.pack(pady=20)
        
        box1 = tk.Button(box_frame, text="CREATE CUSTOM HYGROMORPHIC STRUCTURES", font=("Helvetica", 18, "bold"), padx=75, pady=50, fg="white", bg=_from_rgb(252, 103, 54), relief=tk.RAISED, cursor="hand2", wraplength=260)
        box1.pack(side=tk.LEFT, padx=10)
        box1.bind("<Button-1>", lambda event: create_hb())
        
        # Frame for the 2-column layout
        main_frame = tk.Frame(root)
        main_frame.pack(pady=10)
        
        # First row
        label2 = tk.Label(main_frame, text="My 3D printer:")
        label2.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        
        printer_options = ["Ender 3", "Prusa i3", "Ultimaker 2+", "Cr 10", "Bambulab x1", "Generic"]
        dropdown_var = tk.StringVar(root)
        dropdown_var.set(printer_options[0])
        
        dropdown = tk.OptionMenu(main_frame, dropdown_var, *printer_options)
        dropdown.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Second row
        label4 = tk.Label(main_frame, text="Nozzle Diameter (mm):")
        label4.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        
        diameter_options = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"]
        dropdown_var2 = tk.StringVar(root)
        dropdown_var2.set(diameter_options[0])
        
        dropdown2 = tk.OptionMenu(main_frame, dropdown_var2, *diameter_options)
        dropdown2.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        # Third row
        label3 = tk.Label(main_frame, text="Open material settings:")
        label3.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        
        open_button = tk.Button(main_frame, text="OPEN", relief=tk.RAISED, cursor="hand2", font=("Helvetica", 10, "bold"), bg=_from_rgb(0, 0, 0), fg="white", command=open_folder)
        open_button.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        # Forth row
        label = tk.Label(main_frame, text="Enter PATH to RepetierHost.exe:")
        label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        #my path: C:\Program Files\Repetier-Host\RepetierHost.exe
        
        text_area = tk.Text(main_frame, width=50, height=2)
        text_area.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        button = tk.Button(main_frame, text="SAVE", relief=tk.RAISED, cursor="hand2", font=("Helvetica", 10, "bold"), bg=_from_rgb(60, 100, 30), fg="white", command=lambda: print_text(text_area, button))
        button.grid(row=3, column=2, padx=5, pady=5, sticky="w")
        
        
        help_button = tk.Button(root, text="HELP", font=("Helvetica", 14, "bold"), relief=tk.RAISED, cursor="hand2", command=Help, fg="white", bg=_from_rgb(0, 0, 0))
        help_button.place(relx=0.5, rely=1.0, anchor=tk.S, y=-20, x=0)
        
        copyright_label = tk.Label(root, text="© GABRIELE DUTLI V-BETA", font=("Helvetica", 10))
        copyright_label.place(relx=1.0, rely=1.0, anchor=tk.SE)
        
        root.mainloop()
    
    #open folder with active/passive materials and their settings
    def open_folder():
        script_directory = os.path.dirname(os.path.abspath(__file__))
        folder_name = "FILES\materials"
        # Construct the path to the new folder
        new_folder_path = os.path.join(script_directory, folder_name)
        
        subprocess.Popen(['explorer', new_folder_path])
    
    #Validate PATH to visualization software (RepetierHost.exe)
    def print_text(text_area, button):
        text = text_area.get("1.0", "end-1c")
        print("Entered path:", text)
        valid = False
        file_path = text
        filename = os.path.basename(file_path)
        
        if filename == "RepetierHost.exe":
            valid = True
        else:
            valid = False
        
        if text == "" or not valid:
            button.config(text="): ERROR")
            non_valid_path()
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
        else:
            button.config(text="✔ SAVED")
            file_path = os.path.join(new_folder_path, "PATH.txt")
            with open(file_path, "w") as file:
                file.write(text)
    
    #Show error message
    def non_valid_path():
        messagebox = tk.Toplevel()
        messagebox.title("ALERT!")
        messagebox.configure(bg="red")
        
        message_label = tk.Label(messagebox, text="PATH NOT VALID", fg="white", bg="red", font=("Arial", 12, "bold"))
        message_label.pack(padx=20, pady=10)
        
        message_label = tk.Label(messagebox, text="PLEASE ENTER A VALID PATH", fg="white", bg="red", font=("Arial", 12, "bold"))
        message_label.pack(padx=20, pady=10, anchor='w')
        
        ok_button = tk.Button(messagebox, text="OK", command=messagebox.destroy, font=("Helvetica", 10, "bold"), fg="white", bg=_from_rgb(0, 0, 0))
        ok_button.pack(pady=10)

    mainWindow()

def Help():
        # This function will open the link in the default web browser
        webbrowser.open("https://drive.google.com/file/d/1AdfexEbIZNh2C5sB5yE8_ilXLU_sBCO1/view?usp=sharing")

updated_coords = []
all_coords = []
def create_hb():
        global root
        root.destroy()
        printer = dropdown_var.get()
        nozzle_diameter = dropdown_var2.get()

        def _from_rgb(r,g,b):
            
            return f'#{r:02x}{g:02x}{b:02x}'

        def element_replacer(ID, new_tuple):
            global updated_coords
            index = -1 #not found
            for i, t in enumerate(updated_coords):
                if t[0] == ID:
                    index = i
                    updated_coords.pop(i)
                    updated_coords.insert(i, new_tuple)
                    break
            if index != -1:
                return True
            else:
                return False
            
            # index = old_list.index(element_old)
            # old_list.pop(index)
            # new_list = old_list.insert(1, element_new)
            # return new_list


        class PolygonDrawer:
            def __init__(self, root):
                self.root = root
                self.root.title("CogniMorph 3D")
                
                self.create_widgets()
                self.create_grid()
                self.create_reference_scale()

                self.vertices = []
                self.polygons = []
                self.polygon_settings = {}
                self.selected_polygon = None
                self.drawing_enabled = False
                self.temp_items = []  # Store temporary lines and dots
                self.current_transform_window = None 
                
                self.canvas.bind("<Button-1>", self.add_vertex)

            def create_widgets(self):
                self.title_label = tk.Label(self.root, text="Create your geometries", font=("Helvetica", 16, "bold"))
                self.title_label.pack(pady=10)

                self.canvas = tk.Canvas(self.root, width=600, height=600, bg='white')
                self.canvas.pack()

                self.button_frame = tk.Frame(self.root)
                self.button_frame.pack()
                
                self.start_button = tk.Button(self.button_frame, text="START POLYGON", font=("Helvetica", 10, "bold"), relief=tk.RAISED, cursor="hand2",  fg="white", bg=_from_rgb(0,0,0), command=self.enable_drawing)
                self.start_button.pack(side=tk.LEFT)

                self.finish_button = tk.Button(self.button_frame, text="FINISH POLYGON", font=("Helvetica", 10, "bold"), relief=tk.RAISED, cursor="hand2",  fg="white", bg=_from_rgb(0,0,0), command=self.finish_polygon, state=tk.DISABLED)
                self.finish_button.pack(side=tk.LEFT)

                self.clear_button = tk.Button(self.button_frame, text="CLEAR ALL", font=("Helvetica", 10, "bold"), relief=tk.RAISED, cursor="hand2",  fg="white", bg=_from_rgb(0,0,0), command=self.clear_canvas)
                self.clear_button.pack(side=tk.LEFT)

                self.print_button = tk.Button(self.button_frame, text="FINISH", font=("Helvetica", 10, "bold"), relief=tk.RAISED, cursor="hand2",  fg="white", bg=_from_rgb(0,0,0), command=self.print_polygon_settings)
                self.print_button.pack(side=tk.LEFT)
                
                self.print_button = tk.Button(self.button_frame, text="HELP", font=("Helvetica", 10, "bold"), relief=tk.RAISED, cursor="hand2",  fg="white", bg=_from_rgb(0,0,0), command=self.help_button)
                self.print_button.pack(side=tk.LEFT)

            def create_grid(self):
                for i in range(0, 600, 15):  # vertical lines every 20 pixels
                    self.canvas.create_line(i, 0, i, 600, fill='lightgray')
                for i in range(0, 600, 15):  # horizontal lines every 20 pixels
                    self.canvas.create_line(0, i, 600, i, fill='lightgray')

            def create_reference_scale(self):
                # Create a reference scale at the bottom right corner
                self.canvas.create_line(495, 585, 495, 600, fill='black', width=3)  # vertical line
                self.canvas.create_line(495, 585, 510, 585, fill='black', width=3)  # horizontal line
                self.canvas.create_text(490, 590, anchor=tk.E, text="5 mm", fill='black')

            def enable_drawing(self):
                self.drawing_enabled = True
                self.start_button.config(state=tk.DISABLED)
                self.finish_button.config(state=tk.NORMAL)

            def add_vertex(self, event):
                if not self.drawing_enabled:
                    return
                
                x, y = event.x, event.y
                self.vertices.append((x, y))
                dot = self.canvas.create_oval(x-2, y-2, x+2, y+2, fill='black')
                self.temp_items.append(dot)
                if len(self.vertices) > 1:
                    line = self.canvas.create_line(self.vertices[-2][0], self.vertices[-2][1], x, y, fill='black')
                    self.temp_items.append(line)

            def finish_polygon(self):
                global all_coords
                if len(self.vertices) < 3:
                    messagebox.showerror("Error", "A polygon must have at least 3 vertices.")
                    return
                
                polygon = self.canvas.create_polygon(self.vertices, outline='black', fill='black', width=2, tags="polygon")
                self.polygons.append(polygon)
                #print(polygon) => polygon-ID
                self.polygon_settings[polygon] = {
                    "original_vertices": self.vertices[:],
                    "translation": (0, 0),
                    "scale": 1.0,
                    "rotation": 0,
                    #"bending_direction": 0,
                    "reverse_bilayer": 1, #changed to 1
                    "angle": 0,
                    "stability": 1
                }
                self.vertices = []
                self.drawing_enabled = False
                self.start_button.config(state=tk.NORMAL)
                self.finish_button.config(state=tk.DISABLED)
                self.canvas.tag_bind(polygon, "<Button-1>", self.on_polygon_click)
                
                # Delete temporary items
                for item in self.temp_items:
                    self.canvas.delete(item)
                self.temp_items = []
                
                #update list with all coords of all existing polygons
                all_coords = []
                for ID in range(len(self.polygons)):
                    try:
                        all_coords.append((self.polygons[ID], self.polygon_settings[self.polygons[ID]]["original_vertices"])) #save as tuple: (ID, coords)
                    except:
                        pass

            def on_polygon_click(self, event):
                item = self.canvas.find_closest(event.x, event.y)
                if item and "polygon" in self.canvas.gettags(item):
                    self.selected_polygon = item[0]
                    self.open_transform_window()

            def clear_canvas(self):
                self.canvas.delete("all")
                self.vertices = []
                self.polygons = []
                self.polygon_settings = {}
                self.drawing_enabled = False
                self.start_button.config(state=tk.NORMAL)
                self.finish_button.config(state=tk.DISABLED)
                self.create_grid()
                self.create_reference_scale()

            def open_transform_window(self):
                if self.selected_polygon is None:
                    return

                # Close the current transform window if it's open
                if self.current_transform_window is not None:
                    self.current_transform_window.destroy()

                settings = self.polygon_settings[self.selected_polygon]
                transform_window = Toplevel(self.root)
                self.current_transform_window = transform_window  # Set the current transform window
                
                transform_window.title("Transform Polygon")

                # Left column frame
                left_frame = tk.Frame(transform_window)
                left_frame.pack(side=tk.LEFT, padx=10, pady=10)

                # Right column frame
                right_frame = tk.Frame(transform_window)
                right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

                # Translation scales
                tk.Label(left_frame, text="Translate X:").pack()
                self.translate_x_scale = Scale(left_frame, from_=-1000, to=1000, orient=HORIZONTAL, command=self.update_transformations)
                self.translate_x_scale.set(settings["translation"][0])
                self.translate_x_scale.pack()

                tk.Label(left_frame, text="Translate Y:").pack()
                self.translate_y_scale = Scale(left_frame, from_=-600, to=600, orient=HORIZONTAL, command=self.update_transformations)
                self.translate_y_scale.set(settings["translation"][1])
                self.translate_y_scale.pack()

                # Scale
                tk.Label(left_frame, text="Scale:").pack()
                self.scale_scale = Scale(left_frame, from_=0.1, to=10.0, orient=HORIZONTAL, resolution=0.1, command=self.update_transformations)
                self.scale_scale.set(settings["scale"])
                self.scale_scale.pack()

                # Rotation
                tk.Label(left_frame, text="Rotate:").pack()
                self.rotate_scale = Scale(left_frame, from_=-360, to=360, orient=HORIZONTAL, command=self.update_transformations)
                self.rotate_scale.set(settings["rotation"])
                self.rotate_scale.pack()

                # Reverse bilayer switch
                tk.Label(right_frame, text="Reverse bilayer?").pack()
                self.reverse_bilayer_var = IntVar(value=settings["reverse_bilayer"])
                self.reverse_bilayer_top = Radiobutton(right_frame, text="Top", variable=self.reverse_bilayer_var, value=1, command=self.update_transformations)
                self.reverse_bilayer_top.pack()
                self.reverse_bilayer_bottom = Radiobutton(right_frame, text="Bottom", variable=self.reverse_bilayer_var, value=0, command=self.update_transformations)
                self.reverse_bilayer_bottom.pack()

                # Angle
                tk.Label(right_frame, text="Angle:").pack()
                self.angle_scale = Scale(right_frame, from_=-90, to=90, orient=HORIZONTAL, command=self.update_transformations)
                self.angle_scale.set(settings["angle"])
                self.angle_scale.pack()

                # Stability
                tk.Label(right_frame, text="Stability:").pack()
                self.stability_scale = Scale(right_frame, from_=1, to=5, orient=HORIZONTAL, command=self.update_transformations)
                self.stability_scale.set(settings["stability"])
                self.stability_scale.pack()

                # Delete button
                delete_button = tk.Button(right_frame, text="Delete", font=("Helvetica", 10, "bold"), relief=tk.RAISED, cursor="hand2",  fg="white", bg=_from_rgb(0,0,0), command=lambda: self.delete_polygon(transform_window))
                delete_button.pack(pady=10)

            def update_transformations(self, *args):
                global coords
                
                if self.selected_polygon is None:
                    return

                settings = self.polygon_settings[self.selected_polygon]
                original_vertices = settings["original_vertices"]
                
                # Retrieve the current transformation values
                x_offset = self.translate_x_scale.get()
                y_offset = self.translate_y_scale.get()
                scale_factor = self.scale_scale.get()
                angle = self.rotate_scale.get()
                #bending_direction = self.bending_direction_scale.get()
                reverse_bilayer = self.reverse_bilayer_var.get()
                angle_value = self.angle_scale.get()
                stability = self.stability_scale.get()

                # Apply transformations
                coords = [coord for vertex in original_vertices for coord in vertex]
                coords = self.apply_translation(coords, x_offset, y_offset)
                coords = self.apply_scaling(coords, scale_factor)
                coords = self.apply_rotation(coords, angle)

                self.canvas.coords(self.selected_polygon, *coords)
                
                
                # Update stored settings
                settings["translation"] = (x_offset, y_offset)
                settings["scale"] = scale_factor
                settings["rotation"] = angle
                settings["reverse_bilayer"] = reverse_bilayer
                settings["angle"] = angle_value
                settings["stability"] = stability
                
                
                coordinates = []
                for i in range(int(len(coords)/2)):
                    coordinates.append((coords[i*2], coords[i*2+1]))
                #try to replace existing updates in updated_coords
                new_tuple = (self.selected_polygon, coordinates)
                status = element_replacer(self.selected_polygon, new_tuple)
                if status == True:
                    pass
                else: #add new tuple, if not replaced
                    updated_coords.append(new_tuple)
                
            def apply_translation(self, coords, x_offset, y_offset):
                return [
                    coords[i] + x_offset if i % 2 == 0 else coords[i] + y_offset
                    for i in range(len(coords))
                ]

            def apply_scaling(self, coords, scale_factor):
                cx = sum(coords[i] for i in range(0, len(coords), 2)) / (len(coords) // 2)
                cy = sum(coords[i] for i in range(1, len(coords), 2)) / (len(coords) // 2)
                return [
                    cx + (coords[i] - cx) * scale_factor if i % 2 == 0 else cy + (coords[i] - cy) * scale_factor
                    for i in range(len(coords))
                ]

            def apply_rotation(self, coords, angle):
                angle_rad = math.radians(angle)
                cx = sum(coords[i] for i in range(0, len(coords), 2)) / (len(coords) // 2)
                cy = sum(coords[i] for i in range(1, len(coords), 2)) / (len(coords) // 2)
                return [
                    cx + (coords[i] - cx) * math.cos(angle_rad) - (coords[i + 1] - cy) * math.sin(angle_rad) if i % 2 == 0
                    else cy + (coords[i - 1] - cx) * math.sin(angle_rad) + (coords[i] - cy) * math.cos(angle_rad)
                    for i in range(len(coords))
                ]

            def delete_polygon(self, window):
                global all_coords
                
                if self.selected_polygon:
                    self.canvas.delete(self.selected_polygon)
                    del self.polygon_settings[self.selected_polygon]
                    self.selected_polygon = None
                    window.destroy()
                    self.current_transform_window = None
                
                #update list with all coords of all existing polygons
                all_coords = []
                for ID in range(len(self.polygons)):
                    try:
                        all_coords.append((self.polygons[ID], self.polygon_settings[self.polygons[ID]]["original_vertices"])) #save as tuple: (ID, coords)
                    except:
                        pass       
            
            def help_button(self):
                # Create a new Toplevel window
                Help()
                    
            def print_polygon_settings(self):
                if len(self.polygon_settings.items()) == 0: #No polygon was drawn!
                    messagebox.showerror("Error", "Draw a polygon first!")
                    print("NONE")
                else:
                        setting_collection = []
                        setting_collection_2 = []
                        for polygon, settings in self.polygon_settings.items():
                            setting_collection.append((polygon,settings))
                        #     print("settings:", settings)
                        # print("ID?", self.polygon_settings.items())
                        for polygon in range(len(setting_collection)):
                            interesting_settings = []
                            interesting_settings.append(setting_collection[polygon][1]["reverse_bilayer"])
                            interesting_settings.append(setting_collection[polygon][1]["angle"])
                            interesting_settings.append(setting_collection[polygon][1]["stability"])
                            
                            setting_collection_2.append((setting_collection[polygon][0], interesting_settings))
                        
                        # print(setting_collection_2) #printing-related settings of all polygons
                        # print("updated:", updated_coords) #for updated polygons
                        # print("existing:", all_coords) #for not updated polygons
                        
                        final_data = [] #finished-formatted data
                        #assembly/combination of all informations
                        for polygon in range(len(all_coords)):
                            for polygon2 in range(len(setting_collection_2)):
                                if setting_collection_2[polygon2][0] == all_coords[polygon][0]: #combine with printing-related settings
                                    
                                    found = False #updated coords have been found?
                                    for polygon3 in range(len(updated_coords)):
                                        if updated_coords[polygon3][0] == all_coords[polygon][0]:
                                            final_data.append((all_coords[polygon][0], updated_coords[polygon3][1], setting_collection_2[polygon2][1]))
                                            found = True
                                    if found == False:
                                        final_data.append((all_coords[polygon][0], all_coords[polygon][1], setting_collection_2[polygon2][1]))
                                else:
                                    pass
                                    
                        #check if a polygon is out
                        polygon_out = False
                        for polygon in range(len(final_data)):
                            for coord_tuple in range(len(final_data[polygon][1])):
                                if final_data[polygon][1][coord_tuple][0] < 0 or final_data[polygon][1][coord_tuple][0] > 600: #x-coordinates
                                    messagebox.showerror("Error", "Draw your polygons inside the playground!")
                                    polygon_out = True
                                elif final_data[polygon][1][coord_tuple][1] < 0 or final_data[polygon][1][coord_tuple][1] > 600: #y-coordinates
                                    messagebox.showerror("Error", "Draw your polygons inside the playground!")
                                    polygon_out = True
                                else:
                                    pass
                      
                        if polygon_out == True:
                            pass
                        else: #Ready for GCode generation!
                            #print("final data:", final_data)
                            # print("")
                            # for polygon in range(len(final_data)):
                            #     print(final_data[polygon])
                            createGCode(printer, nozzle_diameter, final_data)

        if __name__ == "__main__":
            root = tk.Tk()
            app = PolygonDrawer(root)
            root.mainloop()



auto_visualize = False
passive_bottom = []
active = []
passive_top = []


successful = True
stability_list = [(2,1), (3,1), (4,1), (4,2), (5,2)] 

passive_bottom_used = True
passive_position = ""

current_directory = os.path.dirname(os.path.abspath(__file__))

multiple_parts = False
steps=[]
points=[] #all points that make up trajectory of nozzle
active_layers_list = [] #points inside lists (= layers) to print layer-wise

#translate information to this format: list elements: ((m, q), (x-limits), (y-limits))
function_list = []

def rounddecimals(number, places):
    new_float = round(number, places)
    return new_float


def createGCode(printer, nozzle_diameter, polygons):
    global steps, points, auto_visualize, passive_bottom, active, passive_top, successful
    global passive_bottom_used, passive_position, multiple_parts, active_layers_list, function_list
    
    messagebox.showinfo("INFO", "Your GCode files are going to be generated... Click 'ok' and don't touch your machine!")
    
    auto_visualize = False
    passive_bottom = []
    active = []
    passive_top = []

    successful = True 

    passive_bottom_used = True
    passive_position = ""

    multiple_parts = False
    steps=[]
    points=[] #all points that make up trajectory of nozzle
    active_layers_list = [] #points inside lists (= layers) to print layer-wise

    #translate information to this format: list elements: ((m, q), (x-limits), (y-limits))
    function_list = []
    
    nozzle_width = float(nozzle_diameter)
    if nozzle_width <= 0.2:
        path_width = nozzle_width
    else:
        path_width = nozzle_width-0.2 #overlap path's crosssections
    if nozzle_width <= 0.2:
        passive_density = 8 * rounddecimals((0.4/nozzle_width),1)
    elif nozzle_width <= 0.4:
        passive_density = 8 * rounddecimals((1.0/nozzle_width),1)
    elif nozzle_width <= 0.6:
        passive_density = 8 * rounddecimals((0.6/nozzle_width),1)
    elif nozzle_width <= 0.8:
        passive_density = 8 * rounddecimals((2.0/nozzle_width),1)
    else:
        passive_density = 8 * rounddecimals((1.5/nozzle_width),1)
    thickness_passive_lines = 2 #math.ceil(0.8/path_width) #round up, because min 1 path
    if nozzle_width > 0.6:
        thickness_passive_lines = 1
    
    
    
    #translate information to this format: list elements: ((m, q), (x-limits), (y-limits))
    function_list = []
    for polygon in range(len(polygons)):
        function_list.append([]) #create new list for each new polygon and its points & functions
        for coord in range(len(polygons[polygon][1])): 
            scale = 1/3 #scale dimensions of polygon to printing bed + move origin to left/bottom corner
            polygons[polygon][1][coord] = (polygons[polygon][1][coord][0]*scale, 200-polygons[polygon][1][coord][1]*scale)
            #print(polygons[polygon][1][coord])
        #turn -90 to 90
        if polygons[polygon][2][1] == -90:
            polygons[polygon][2][1] = 90
        for coord in range(len(polygons[polygon][1])): 
            if coord == len(polygons[polygon][1])-1:
                coord2 = 0 # create function between last and first coords too
            else:
                coord2 = coord+1
            
            if polygons[polygon][1][coord][0] == polygons[polygon][1][coord2][0]:
                polygons[polygon][1][coord2] = (polygons[polygon][1][coord2][0] + 0.1, polygons[polygon][1][coord2][1] - 0.1)
            if polygons[polygon][1][coord][1] == polygons[polygon][1][coord2][1]:
                polygons[polygon][1][coord2] = (polygons[polygon][1][coord2][0] - 0.1, polygons[polygon][1][coord2][1] + 0.1)
            
            dy = polygons[polygon][1][coord2][1] - polygons[polygon][1][coord][1]
            dx = polygons[polygon][1][coord2][0] - polygons[polygon][1][coord][0]
            #avoid division by 0, by introducing a slight imperfection
            if dx == 0:
                dx = 0.01
            m = dy/dx
            #print((polygons[polygon][1][coord][0],polygons[polygon][1][coord][1]), (polygons[polygon][1][coord2][0],polygons[polygon][1][coord2][1]), m)

            #q = y1 - mx1
            q = polygons[polygon][1][coord][1] - m*polygons[polygon][1][coord][0]
            
            #limits
            x_limits = (polygons[polygon][1][coord][0], polygons[polygon][1][coord2][0])
            y_limits = (polygons[polygon][1][coord][1], polygons[polygon][1][coord2][1])
            
            #avoid completely vertical or horizontal lines
            # if x_limits[0] == x_limits[1]:
            #     x_limits = (x_limits[0], x_limits[1]+0.01)
            # if y_limits[0] == y_limits[1]:
            #     y_limits = (y_limits[0], y_limits[1]+0.01)
            
            output = [(m,q), x_limits, y_limits]
            function_list[polygon].append(output)
    
    def nozzle_state(state):
        steps.append(fc.Extruder(on=state))
        
    def point_func(x,y,z):
        global steps, points, auto_visualize, passive_bottom, active, passive_top, successful
        global passive_bottom_used, passive_position, multiple_parts, active_layers_list, function_list
        points.append((x,y,z))
        steps.append(fc.Point(x=x,y=y,z=z))
    
    def custom_bilayer(function_list):
        global steps, points, auto_visualize, passive_bottom, active, passive_top, successful
        global passive_bottom_used, multiple_parts, active_layers_list
        # position_start = (50,50, 0.2) #start position of nozzle
        # steps.append(fc.Extruder(on=False))
        # steps.append(fc.Point(x=position_start[0],y=position_start[1],z=position_start[2]))
        # points.append((position_start[0],position_start[1],position_start[2]))
        nozzle_state(False)
        point_func(35, 15, 0.2)
        point_func(35, 15, 15)
        #add this start to active, passive_bottom, passive_top
        active.extend(steps)
        active_layers_list.append(([(35, 15, 0.2), (35, 15, 15)], 0.0))
        passive_bottom.extend(steps)
        passive_top.extend(steps)
        steps = []
        
        for polygon in range(len(polygons)):
            
            stability = polygons[polygon][2][2]
            active_layers = stability_list[stability-1][0]
            passive_layers = stability_list[stability-1][1]
            if polygons[polygon][2][0] == 0:
                passive_position = "bottom" #the passive material is printed on the bottom
            else:
                passive_position = "top"
            
            height = 0.2
            
            for layer in range(active_layers+passive_layers): #loop through all layers
                switch = False #has the material switched?
                if passive_position == "top":
                    if layer == active_layers: #all active layers finished
                        status = "passive_material"
                        switch = True
                    elif layer >= active_layers: #all active layers finished
                        status = "passive_material"
                        switch = True
                    else:
                        status = "active_material"
                        switch = False
                else:
                    if layer == passive_layers: #all passive layers finished
                        status = "active_material"
                        switch = False
                    if layer < passive_layers: #all passive layers finished
                        status = "passive_material"
                        switch = True
                    if layer > passive_layers:
                        status = "active_material"
                        switch = False
                    
            
                #Layer
                error = False
                #get the stored wpla angle: at which (global) angle should the bilayer bend?
                #wpla angle is offset by 90° of actual given value
                if polygons[polygon][2][1] > 0:
                    angle_wpla = -90+polygons[polygon][2][1]
                    if switch == True:
                        angle_wpla = polygons[polygon][2][1]
                elif polygons[polygon][2][1] < 0:
                    angle_wpla = polygons[polygon][2][1]+90
                    if switch == True:
                        angle_wpla = polygons[polygon][2][1]
                else: #if polygons[polygon][2][1] == 0:
                    angle_wpla = 90
                    if switch == True:
                        angle_wpla = 0
                m_wpla = math.tan(math.radians(angle_wpla))
                
                if angle_wpla > 90 or angle_wpla < 90:
                    non90degpath(angle_wpla, m_wpla, height, status, polygon, passive_position)
                            
                    #find intersections + append in list in right order
                    #gradually lower q until no intersections found anymore
                    #create paths between points
                    
                if angle_wpla == 90 or angle_wpla == -90:
                    deg90path(angle_wpla, m_wpla, height, status, polygon, passive_position)
                    
                # go up one layer
                height = height + 0.2
                
                #high non-printing path for transition to next layer, use last point and move up z-axis
                nozzle_state(False)
                point_func(points[-1][0], points[-1][1], points[-1][2]+5)
                
                #add to corresponding layer collection
                if passive_position == "bottom" and status == "passive_material":
                    #EMPTY POINTS TOO?
                    passive_bottom.extend(steps)
                    steps = []
                elif passive_position == "top" and status == "passive_material":
                    passive_top.extend(steps)
                    steps = []
                elif status == "active_material":
                    active.extend(steps)
                    steps = []
                else:
                    pass

            #high non-printing path for transition to next bilayer, use last point and move up z-axis
            nozzle_state(False)
            point_func(points[-1][0], points[-1][1], points[-1][2]+10)
    
    def deg90path(angle_wpla, m_wpla, height, status, polygon, passive_position):
        global steps, points, auto_visualize, passive_bottom, active, passive_top, successful
        global passive_bottom_used, multiple_parts, active_layers_list, function_list
        global error, successful
        current_active_layer = [] #collects all points of a wpla layer
        
        #scanner, determine points from intersections with scanner from left to right
        corners = polygons[polygon][1]
        x_level = min(corners, key=lambda x: x[0])[0]
        
        step = path_width
        
        num_intersections = 0
        intersecting = True
        intersections = []
        
        #as long as intersections are found, keep the loop going
        while intersecting == True:
            #move the scanner forward for next iteration
            x_level = x_level + path_width
            
            func_found = []  #list with all func found 
            
            for func in range(len(function_list[polygon])):
                #print(function_list[polygon][func])
                #for each function check, if the x-level is in the x-limits
                #sort max and min
                max_x_limit = max(function_list[polygon][func][1][0], function_list[polygon][func][1][1]) + 0.001 #add imperfections too avoid rare errors
                min_x_limit = min(function_list[polygon][func][1][0], function_list[polygon][func][1][1]) + 0.001

                if min_x_limit <= x_level and max_x_limit >= x_level:
                    intersecting = True
                    func_found.append(func)
                
                    
            if len(func_found) == 0:
                # print("Error or FINISHED")
                intersecting = False
            
            else: #scanner still hovers above shape
                num_intersections = num_intersections + len(func_found)
                unsorted_intersections = []
                #determine all points of intersection, add to list and visualize
                for intersect_point in range(len(func_found)):
                    m_func = function_list[polygon][func_found[intersect_point]][0][0]
                    q_func = function_list[polygon][func_found[intersect_point]][0][1]
                    
                    #find y value 
                    y = m_func * x_level + q_func
                    #add the intersection point
                    unsorted_intersections.append((x_level, y))

                #sort intersections by distance and add intersection points
                if len(intersections) == 0:
                    #for first intersections
                    intersections.append(unsorted_intersections)
                    # print("first intersections", intersections)
                else: 
                    #if not first intersection point in collection, calculate distance
                    dist_ordered_points_list = []
                    for i in range(len(unsorted_intersections)):

                        x1 = intersections[-1][-1][0]
                        y1 = intersections[-1][-1][1]
                        x2 = unsorted_intersections[i][0]
                        y2 = unsorted_intersections[i][1]

                        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                        dist_ordered_points_list.append((unsorted_intersections[i], distance))
                    #sort for distance
                    dist_ordered_points_list = sorted(dist_ordered_points_list, key=lambda x: x[1])
                    #omit distances
                    dist_ordered_points_list2 = []
                    for point in range(len(dist_ordered_points_list)):
                        dist_ordered_points_list2.append(dist_ordered_points_list[point][0])
                    #add all the new point for one x-level to the whole list
                    intersections.append(dist_ordered_points_list2)
                    
        #visualization, convert to gcode
        if num_intersections == 0 or round(num_intersections/2) != num_intersections/2:
             # print("ERROR, number of intersections", num_intersections)   
             successful = False
        
        if status == "passive_material":
            new_path_nr = int(math.ceil(len(intersections)/(passive_density*thickness_passive_lines))) # 2 points = 1 passive line
        else:
            new_path_nr = len(intersections) 
        
        for path in range(new_path_nr):
            counter = 0
            if status == "passive_material":
                path = int(path * passive_density * thickness_passive_lines) 
                for i in range(thickness_passive_lines):
                    path = path + 1
                    if counter == 0 and path == 0: #ensures travel paths while traveling to new polygon
                        pass
                    else:
                        if i == 0:
                            pass
                        else:
                            nozzle_state(True)
                        
                    try: #avoid out of range error
                        for intersect_points in range(len(intersections[path])):
                            counter += 1
                            #print("points:", (rounddecimals(intersection_points[path][intersect_points][0],1),rounddecimals(intersection_points[path][intersect_points][1],1)))
                            x, y = rounddecimals(intersections[path][intersect_points][0],2), rounddecimals(intersections[path][intersect_points][1],2)
                            if passive_position == "top":
                                height_new = height - 0.1 #increase material adhesion to avoid delamination
                                point_func(x, y, height_new)
                            else:
                                point_func(x, y, height)
                            if counter/2 == round(counter/2) and counter != 0:
                                nozzle_state(False)
                            else:
                                nozzle_state(True)
                    except:
                        pass
            else:
                if counter == 0 and path == 0: #ensures travel paths while traveling to new polygon
                    pass
                else:
                    nozzle_state(True)
                    
                for intersect_points in range(len(intersections[path])):
                    counter += 1
                    #print("points:", (rounddecimals(intersection_points[path][intersect_points][0],1),rounddecimals(intersection_points[path][intersect_points][1],1)))
                    x, y = rounddecimals(intersections[path][intersect_points][0],2), rounddecimals(intersections[path][intersect_points][1],2)
                    if height*10/4 == round(height*10/4) and status == "active_material": #x offset for better inter-layer cohesion
                        x = x + path_width/2
                    if passive_position == "bottom":
                        height_new = height - 0.2
                        point_func(x, y, height_new)
                    else:
                        point_func(x, y, height)
                    
                    if passive_position == "bottom":
                        height_new = height - 0.2
                        current_active_layer.append((x,y,height_new)) #add points 
                    else:
                        current_active_layer.append((x,y,height)) #add points 
                    
                    if counter/2 == round(counter/2) and counter != 0:
                        nozzle_state(False)
                    else:
                        nozzle_state(True)
        active_layers_list.append((current_active_layer, height))              

    def non90degpath(angle_wpla, m_wpla, height, status, polygon, passive_position):
        global error, successful
        global steps, points, auto_visualize, passive_bottom, active, passive_top, successful
        global passive_bottom_used, multiple_parts, active_layers_list, function_list
        
        current_active_layer = []
        error = False
        q_list = []
        #print("function_list[polygon]:", len(function_list[polygon]))
        for func in range(len(function_list[polygon])):
            #ensure that despite the angle, the q is always chosen so that initial wpla function
            #is above the build plate
            if angle_wpla > 0 or angle_wpla == 0: 
                q_wpla = 210 #max of build plate
            if angle_wpla < 0:
                q_wpla = 200-200*m_wpla +10
            
            m_func = function_list[polygon][func][0][0]
            q_func = function_list[polygon][func][0][1]
            x_limits = function_list[polygon][func][1]
            y_limits = function_list[polygon][func][2]
            
            #if x_limits are the same (perfectly vertical lines)
            # tolerance = 0.001
            # if x_limits[0] <= x_limits[1]+tolerance and x_limits[0] >= x_limits[1]-tolerance:
            #     x_limits = (x_limits[0], x_limits[1] + 0.01) #trick for avoiding errors
            #     function_list[polygon][func][1] = x_limits # move the x_coord of one point
                # print("x coord moved")
            
            #sort the x_limits
            limits_list = list(x_limits)
            limits_list.sort()
            x_limits = tuple(limits_list)
            
            intersections_found = False
            
            #find highest intersection between wpla-func and polygon + define wpla-func (find highest q possible)
            while intersections_found == False:
                    
                f1x1 = x_limits[0]*m_func + q_func
                f2x1 = x_limits[0]*m_wpla + q_wpla
                f1x2 = x_limits[1]*m_func + q_func
                f2x2 = x_limits[1]*m_wpla + q_wpla
                
                # if f1x1 == f1x2: #avoiding completely horizontal lines
                #     f1x1 = f1x1 + 0.1
                    # print("executed")
                    
                # if q_wpla < -999:
                #     print(f1x1, f1x2)
                
                #determines if intersection happened
                if f2x1 > f1x1 and f2x2 < f1x2:
                    q_list.append((q_wpla, func))
                    intersections_found = True
                if f2x1 < f1x1 and f2x2 > f1x2:
                    q_list.append((q_wpla, func))
                    intersections_found = True
                if f1x1 == f2x1 or f1x2 == f2x2:
                    q_list.append((q_wpla, func))
                    intersections_found = True
                if q_wpla < -1000:
                    # print("PROBLEM WHILE LOOP, Q NOT FOUND")
                    successful = False
                    error = True
                    
                    #STOP THE PROGRAM, GENÜGT DIESES LIMIT FÜR 1°? 
                    # print(func, angle_wpla, m_wpla, q_wpla, q_list)
                    
                    intersections_found = True #LIE, but better stop the while-loop
                
                #0.1 resolution since, for nearly parallel wpla func compared to polygon funcs
                #no intersection can be found with the method used!
                q_wpla = q_wpla - 0.1 #0.1 
                #intersections_found = False
        
        #find out intersection with func of polygon-points, where the wpla-func has biggest q
        #max_q => tupel with max q and corresponding func (func is index inside the polygon list in function_list)
        max_q = max(q_list, key=lambda x: x[0])
        #create initial wpla function
        q_wpla = max_q[0]
        
        #print("wpla func:", m_wpla, "*x + ", q_wpla)
        
        #test output intersection between initial wpla func and func of polygon points
        intersecting_polynom = True
        intersection_points = []
        while intersecting_polynom == True:
            num_intersections = 0
            new_points = [] #newly found intersections, which have to be ordered and than added to intersection_points list
            for func in range(len(function_list[polygon])):
                x = sp.symbols('x')
                m_func = function_list[polygon][func][0][0]
                q_func = function_list[polygon][func][0][1]
                
                f1 = m_wpla*x + q_wpla
                f2 = m_func*x + q_func

                x_min = min(function_list[polygon][func][1][0], function_list[polygon][func][1][1])
                x_max = max(function_list[polygon][func][1][0], function_list[polygon][func][1][1])

                intersection_x = sp.solveset(f1 - f2, x)
                valid_intersections = [sol for sol in intersection_x if x_min <= sol <= x_max]

                if valid_intersections:
                    for x_value in valid_intersections:
                        y_value = f1.subs(x, x_value)
                        num_intersections += 1
                        #adds new intersection points to a list
                        #for testing: print(func,":",m_func, (x_value, y_value))
                        new_points.append((x_value, y_value))
                else:
                    pass
            
            if len(new_points) != 0:
                #add the points from new_points to intersection_points
                #add in order: shortest distance from last point in list
                dist_ordered_points_list = []
                if len(intersection_points) == 0: #the order is not important
                        intersection_points.append(new_points)
                else:
                    for intersection in range(len(new_points)):
                        #order by measuring the distance between new points and the last point
                        #distance = math.sqrt(dx**2 + dy**2)
                        x1 = intersection_points[-1][-1][0]
                        y1 = intersection_points[-1][-1][1]
                        x2 = new_points[intersection][0]
                        y2 = new_points[intersection][1]
                        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                        #add new point with distance to list 
                        dist_ordered_points_list.append((new_points[intersection], distance))
                
                
                    #sort by distance and add to existing intersection list
                    dist_ordered_points_list = sorted(dist_ordered_points_list, key=lambda x: x[1])
                    dist_ordered_points_list_2 = [] #collect only coords (omit distance)
                    for point in range(len(dist_ordered_points_list)):
                        dist_ordered_points_list_2.append(dist_ordered_points_list[point][0])  
                    #new intersection points are added as lists to the big list
                    intersection_points.append(dist_ordered_points_list_2)
               

            #there has to be at least 2 intersections or a higher even number
            if round(num_intersections/2) != num_intersections/2:
                intersecting_polynom = False
                #possible if points moved to avoid completeley vertical/horizontal lines
                # print("ERROR, intersections: ", num_intersections)
                successful = False
            if num_intersections == 0:
                 intersecting_polynom = False
                 # print("FINISHED (or error), intersections: 0")
                 
            #lower the wpla function: dy = m * dx
            #q_wpla = q_wpla - m_wpla * path_width
            q_wpla = q_wpla - path_width / math.cos(math.radians(angle_wpla))
        
        if error == False: #don't add info of faulty polygons to final list for visualization
            #after ALL intersections collected: create wpla paths for gcode generation
            if status == "passive_material":
                new_path_nr = int(math.ceil(len(intersection_points)/(passive_density*thickness_passive_lines))) # 2 points = 1 passive line
            else:
                new_path_nr = len(intersection_points)
                
            for path in range(new_path_nr):
                counter = 0
                if status == "passive_material":
                        path = int(path * passive_density * thickness_passive_lines)
                        for i in range(thickness_passive_lines):
                            path = path + 1
                            
            
                            if counter == 0 and path == 0:
                                pass
                            else:
                                if i == 0:
                                    pass
                                else:
                                    nozzle_state(True)
                            try: #prevent index outside of range
                                for intersect_points in range(len(intersection_points[path])):
                                    counter += 1
                                    #print("points:", (rounddecimals(intersection_points[path][intersect_points][0],1),rounddecimals(intersection_points[path][intersect_points][1],1)))
                                    x, y = rounddecimals(intersection_points[path][intersect_points][0],2), rounddecimals(intersection_points[path][intersect_points][1],2)
                                    if passive_position == "top":
                                        height_new = height - 0.1 #increase material adhesion to avoid delamination
                                        point_func(x, y, height_new)
                                    else:
                                        point_func(x, y, height)
                                    if counter/2 == round(counter/2) and counter != 0:
                                        nozzle_state(False)
                                    else:
                                        nozzle_state(True)
                            except:
                                # print("EXCEPTION RAISED!")
                                successful = False
                else:
                        if counter == 0 and path == 0:
                            pass
                        else:
                            nozzle_state(True)
                        for intersect_points in range(len(intersection_points[path])):
                            counter += 1
                            #print("points:", (rounddecimals(intersection_points[path][intersect_points][0],1),rounddecimals(intersection_points[path][intersect_points][1],1)))
                            x, y = rounddecimals(intersection_points[path][intersect_points][0],2), rounddecimals(intersection_points[path][intersect_points][1],2)
                            if height*10/4 == round(height*10/4) and status == "active_material": #x offset for better inter-layer cohesion
                                sin_value = math.sin(math.radians(angle_wpla))
                                if sin_value == 0: #avoid division by zero
                                    #x = x + path_width/2
                                    y = y + path_width/2
                                elif angle_wpla <= 20 or angle_wpla >= -20: #big angles create too big x_offsets!
                                    x = x + path_width/2
                                else:
                                    x = x + path_width/(2*sin_value)
                            if passive_position == "bottom":
                                height_new = height - 0.2
                                point_func(x, y, height_new)
                            else:
                                point_func(x, y, height)
                            
                            if passive_position == "bottom":
                                height_new = height - 0.2
                                current_active_layer.append((x,y,height_new)) #add points 
                            else:
                                current_active_layer.append((x,y,height)) #add points 
                            
                            if counter/2 == round(counter/2) and counter != 0:
                                nozzle_state(False)
                            else:
                                nozzle_state(True)
            
        active_layers_list.append((current_active_layer, height))    
    
    def error_msg():
        messagebox.showerror('POTENTIAL ERROR IN GCODE', 'Check GCode or try again')
    
    def extract_txt(path, why):
        if why == "settings":
            with open(path, 'r') as file:
                list1 = file.readlines()
            list2 = []
                # Print the lines or use them as needed
            for line in list1:
                    input_string = line.strip()  # Remove leading/trailing whitespace if needed
                    # Splitting the string based on ":"
                    result_list = input_string.split("=")
                    # Displaying the result
                    list2.append(result_list)
            return list2
    
    def visualize(material, stage):
        global steps, points, auto_visualize, passive_bottom, active, passive_top, successful
        global passive_bottom_used, passive_position, multiple_parts, active_layers_list, function_list
        if stage == 0: #when starting
            #delete existing .gcode files
            for file in os.listdir(current_directory):
                if file.endswith('.gcode'):
                    file_path = os.path.join(current_directory, file)
                    os.remove(file_path)
        
        #create gcode, save and create file
        design_name = 'custom bilayer design'
        printer_name='ender_3'
        #controls the flowrate
        EW = path_width * 1.2 #add 20%
        EH = 0.2 #always, to prevent overflow
        
        if material == "passive_top" or material == "passive_bottom":
            printer_settings_passive = extract_txt("materials/passive.txt", "settings")
            printer_settings = [int(inner_list[1]) for inner_list in printer_settings_passive]
        elif material == "active":
            printer_settings_active = extract_txt("materials/active.txt", "settings")
            printer_settings = [int(inner_list[1]) for inner_list in printer_settings_active]
        # elif material == "tpu":
        #     printer_settings_tpu = extract_txt("materials/tpu.txt", "settings")
        #     printer_settings = [int(inner_list[1]) for inner_list in printer_settings_tpu]
        else: #if no material is specified just take the settings from pla
            printer_settings_passive = extract_txt("materials/passive.txt", "settings")
            printer_settings = [int(inner_list[1]) for inner_list in printer_settings_passive]
        
        parameters = printer_settings

        gcode_controls = fc.GcodeControls(
            printer_name=printer_name,
            save_as=design_name,
            initialization_data={
                'primer': 'front_lines_then_y',
                'print_speed': parameters[2],
                'nozzle_temp': parameters[0],
                'bed_temp': parameters[1],
                'fan_percent': parameters[3],
                'extrusion_width': EW,
                'extrusion_height': EH})
        
        gcode = fc.transform(steps, 'gcode', gcode_controls)  
        
        #visualize through RepetierHost
        
        #rename file
        current_datetime = datetime.now() # Get the current date and time
        formatted_datetime = current_datetime.strftime("%d-%m-%Y"+"__"+"%H-%M-%S") # Format the date and time as a string
        old_name = "custom bilayer design__" +formatted_datetime+ ".gcode"
        if material == "active":
            new_name = "active.gcode"
        elif material == "passive_bottom":
            new_name = "passive_bottom.gcode"
        elif material == "passive_top":
            new_name = "passive_top.gcode"
        else:
            new_name = "visualization" # merge all files for a complete visualization
        old_path = os.path.join(current_directory, old_name)
        new_path = os.path.join(current_directory, new_name)
        os.rename(old_path, new_path)
        folder_name = "FILES"
        output_file = os.path.join(current_directory, new_name) 
        
        if material == "active":
            output_window()
    
    nozzle_state(False)
    custom_bilayer(function_list)
    
    if successful == False:
        error_msg()

    steps = passive_bottom
    if len(steps) <= 4:
        passive_bottom_used = False
    else:
        #add a final print path to avoid premature cooling of nozzle (easy fix for unsolved bug)
        nozzle_state(False)
        point_func(170, 30, 20)
        point_func(188, 5, 0.2)
        nozzle_state(True)
        point_func(178, 5, 0.2)
        point_func(178, 5.4, 0.2)
        point_func(188, 5.4, 0.2)
        visualize("passive_bottom", 0)

    steps = passive_top
    if len(steps) <= 4:
        pass
    else:
        #add a final print path to avoid premature cooling of nozzle (easy fix for unsolved bug)
        nozzle_state(False)
        point_func(170, 30, 20)
        point_func(198, 5, 0.2)
        nozzle_state(True)
        point_func(188, 5, 0.2)
        point_func(188, 5.4, 0.2)
        point_func(198, 5.4, 0.2)
        if passive_bottom_used == False:
            visualize("passive_top", 0)
        else:
            visualize("passive_top", 2)


    steps = active
    # steps = []
    # active_layers_list_sorted = sorted(active_layers_list, key=lambda x: x[1]) #sort for layers
    # for layer in range(len(active_layers_list_sorted)):
    #     for point in range(len(active_layers_list_sorted[layer][0])):
    #         nozzle_state(True)
    #         x = active_layers_list_sorted[layer][0][point][0]
    #         y = active_layers_list_sorted[layer][0][point][1]
    #         z = active_layers_list_sorted[layer][0][point][2]
    #         if active_layers_list_sorted[layer][1] == 0.0: #move towards first polygon: not printing
    #             nozzle_state(False)
    #         elif layer == 1 and point == 0:
    #             nozzle_state(False)
    #         elif point == 0: #transition path
    #             nozzle_state(False)
    #         point_func(x, y, z)
            
    #         if point + 1 == len(active_layers_list_sorted[layer][0]): #transition path
    #             nozzle_state(False)
    #             point_func(x, y, z+5)

    #for changing layer add this point: active_layers_list.append(([(points[-1][0], points[-1][1], points[-1][2]+10)], 0.0))

    visualize("active", 1)
   
    

def merge_gcode_files():
    file1 = 'active.gcode'
    file2 = 'passive_top.gcode'
    base_file = 'passive_bottom.gcode'
    output_file = 'visualization.gcode'
    
    # Initialize merged content with the base gcode content
    try: #depending on design, not necessary
        with open(base_file, 'r') as base:
            merged_content = base.read()
    except:
        pass
        
    # Append content from file1
    with open(file1, 'r') as f1:
        try:
            merged_content += '\n' + f1.read()
        except: #in case passive bottom is not needed
            merged_content = f1.read()

    try:
        with open(file2, 'r') as f2:
            merged_content += '\n' + f2.read()
    except:
        pass

    # Write the merged content to the output file
    with open(output_file, 'w') as output:
        output.write(merged_content)

def visualize_open():
    merge_gcode_files()

    # Check if Repetier-Host is already running
    repetier_host_windows = gw.getWindowsWithTitle('Repetier-Host')

    #read the path entered and saved at path.txt
    # Construct the path to the folder and the text file inside it
    folder_name = "FILES"
    folder_path = os.path.join(current_directory, folder_name)
    file_path = os.path.join(folder_path, "PATH.txt")
    # Check if the folder exists
    if os.path.exists(folder_path):
        # Check if the file exists
        if os.path.exists(file_path):
            # Open the file and read its content
            with open(file_path, "r") as file:
                file_content = file.read()
        else:
            content_not_found("Error", "GCode file for visualization not found!")
    else:
        content_not_found("Error", "Provided path to RepetierHost not valid!")
    
    
    # If Repetier-Host is not running, open it
    if not repetier_host_windows:
        pyautogui.hotkey('winleft', 'r')
        pyautogui.write(file_content)  #C:\Program Files\Repetier-Host\RepetierHost.exe
        pyautogui.press('enter')
        
        # Wait for Repetier-Host to open (timeout of 30 seconds)
        for _ in range(30):
            repetier_host_windows = gw.getWindowsWithTitle('Repetier-Host')
            if repetier_host_windows:
                break
            time.sleep(1)
        else:
            content_not_found("Failed to open Repetier-Host!")
            
            
    else:
        repetier_host_window = repetier_host_windows[0]  # Assuming there's only one Repetier-Host window
        repetier_host_window.activate()  # Bring the window to the foreground

    pyautogui.hotkey('ctrl', 'o')
    pyautogui.write('visualization.gcode') #output_file
    pyautogui.press('enter')

def content_not_found(type_msg, msg):
    messagebox.showerror(type_msg, msg)

def instructions():
    webbrowser.open("https://drive.google.com/file/d/1KD-AhEBomPZxbTnpIP89aMYnhb8U5_Vg/view?usp=sharing")

def openfolder():
    subprocess.Popen(['explorer', os.path.dirname(os.path.abspath(__file__))])

def output_window():
    global root  # Access the global root window
    
    root.destroy()  # Destroy the root window and all its child windows
    
    root = tk.Tk()
    
    root.title("CogniMorph 3D")
    # Set window dimensions
    window_width = 1000
    window_height = 700
    root.geometry(f"{window_width}x{window_height}")
    
    # Title label
    title_label = tk.Label(root, text="Hygromorphic composites are ready, let's start printing!", font=("Arial", 18, "bold"))
    title_label.pack(pady=20)
    

    # Create a frame to hold the widgets for the first line
    frame1 = tk.Frame(root)
    frame1.pack(anchor=tk.W, padx=20, pady=10)

    # Create a label widget for the first line
    label1 = tk.Label(frame1, text="Show me the visualization:")
    label1.pack(side=tk.LEFT)

    # Create a button widget for the first line
    button1 = tk.Button(frame1, text="VISUALIZE", font=("Helvetica", 10, "bold"), relief=tk.RAISED, cursor="hand2",  fg="white", bg=_from_rgb(0,0,0), command=visualize_open)
    button1.pack(side=tk.LEFT, padx=5)

    # Create a frame to hold the widgets for the second line
    frame2 = tk.Frame(root)
    frame2.pack(anchor=tk.W, padx=20, pady=10)

    # Create a label widget for the second line
    label2 = tk.Label(frame2, text="How should I print the composites?")
    label2.pack(side=tk.LEFT)

    # Create a button widget for the second line
    button2 = tk.Button(frame2, text="INSTRUCTIONS", font=("Helvetica", 10, "bold"), relief=tk.RAISED, cursor="hand2",  fg="white", bg=_from_rgb(0,0,0), command=instructions)
    button2.pack(side=tk.LEFT, padx=5)
    
    # Create a frame to hold the widgets for the second line
    frame3 = tk.Frame(root)
    frame3.pack(anchor=tk.W, padx=20, pady=10)

    # Create a label widget for the second line
    label3 = tk.Label(frame3, text="Where are the generated files saved?")
    label3.pack(side=tk.LEFT)

    # Create a button widget for the second line
    button3 = tk.Button(frame3, text="OPEN FOLDER", font=("Helvetica", 10, "bold"), relief=tk.RAISED, cursor="hand2",  fg="white", bg=_from_rgb(0,0,0), command=openfolder)
    button3.pack(side=tk.LEFT, padx=5)
    
    # Create a frame to hold the widgets for the second line
    frame4 = tk.Frame(root)
    frame4.pack(anchor=tk.W, padx=20, pady=10)

    bottom_left_button = tk.Button(root, text="BACK", font=("Helvetica", 14, "bold"), relief=tk.RAISED, cursor="hand2", command=return2main, fg="white", bg=_from_rgb(0,0,0))
    bottom_left_button.place(relx=0.0, rely=1.0, anchor=tk.SW, x=10, y=-10)
    
    root.mainloop() 
    
welcome()
# return2main()


