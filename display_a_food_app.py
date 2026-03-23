import flet as ft
import random as r
import numpy as np
import pandas as pd

food_path = "food_data\\food_list.csv"
df = pd.read_csv(food_path)

# import flet as ft

def myapp(page: ft.Page):
    # Set theme mode (DARK or LIGHT)

    def new_food(e):
        number = r.randint(0,len(df)-1)
        input.value = str(df["food"][number])
        image.src = str(df["imgfilepath"][number])
    page.theme_mode = ft.ThemeMode.DARK  
    input = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    input.value = str(df["food"][0])
    image = ft.Image(src=df["food"][0],width=100,height=100,
                          placeholder_fade_out_animation=ft.Animation(duration=ft.Duration(milliseconds=900),curve=ft.AnimationCurve.EASE_IN,),)
    image.src = str(df["imgfilepath"][0])

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(ft.Icons.ADD, on_click=new_food),
                input,
                # ft.IconButton(ft.Icons.REMOVE, on_click=plus_click),
            ],
        )
    )
    page.add(
        ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(ft.Icons.ADD, on_click=new_food),
                # ft.IconButton(ft.Icons.REMOVE, on_click=plus_click),
            ],
        )
    )
    
    page.add(
        ft.ResponsiveRow(

        image 
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
