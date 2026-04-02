import flet as ft
import random as r
import numpy as np
import pandas as pd
from tkinter import filedialog

import webbrowser
import img_google

food_path = "food_data\\food_list.csv"
df = pd.read_csv(food_path)

def myapp(page: ft.Page):
    
    # Set theme mode (DARK or LIGHT)


    def new_food(e):
        number = r.randint(0,len(df)-1)
        input.value = str(df["food"][number])
        image.src = str(df["imgfilepath"][number])
        description.value = str(df["description"][number])
        ingredients.value = str(df["ingredients"][number])
        instructions.value = str(df["instructions"][number])
    def image_search_button():
        query = input.value
        img_google.image_search(search_query=query)
    
    page.theme_mode = ft.ThemeMode.DARK  
    input = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)
    starter =0
    input.value = str(df["food"][starter])
    description = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)
    description.value =  str(df["description"][starter ])
    ingredients = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)
    ingredients.value = str(df["ingredients"][starter ])
    instructions = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)
    instructions.value = str(df["instructions"][starter ])
    
    image = ft.Image(src=df["food"][0],width=300,height=300,
                          placeholder_fade_out_animation=ft.Animation(duration=ft.Duration(milliseconds=900),curve=ft.AnimationCurve.EASE_IN,),)
    image.src = str(df["imgfilepath"][0])

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextButton(content="newfood", on_click=new_food),
                input,
                # ft.IconButton(ft.Icons.REMOVE, on_click=plus_click),
            ],
        )
    )
    
    page.add(
        ft.ResponsiveRow(
        image 
        )
    )
    page.add(
        ft.ResponsiveRow(
        # input.description = str(df["description"][number])
        input, ingredients, instructions, description, 
        # input.instructions,
        # input.description
        )
    )
                    
    page.add(
        ft.ResponsiveRow(
            ft.TextButton(content="firefox google image search", on_click=image_search_button),

        )
    )
                        
    # window size
    # page.window_height = 400
    # page.window_width = 500
    
    # Set app title
    page.title = ""
    # page.
    page.update()

ft.run(main=myapp)
