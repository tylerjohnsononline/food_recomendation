import flet as ft
import random as r
import numpy as np
import pandas as pd
from tkinter import filedialog

import webbrowser
import img_google
class DataHolder ():
  def __init__(self):
    self.ingredients_list = ["","",""]
    self.food_path = "food_data\\food_list.csv"
    self.df = pd.read_csv(self.food_path)
  
FoodData = DataHolder()
df = FoodData.df
# food_path = "food_data\\food_list.csv"
# df = pd.read_csv(food_path)

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
    
    def recommend_based_on_ingredients():
# contains pepperoni 
        user_has_ingredient = "ep"#  available_ingredients.value
        # print(df.loc[df["ingredients"].str.contains( user_has_ingredient)])
        temp_df = df.loc[df["ingredients"].str.contains( user_has_ingredient)]
        temp_df.set_index(pd.Index([xx for xx in range(len(temp_df))]))  #df.loc[df["ingredients"].str.contains("pep")]
        number = r.randint(1,len(temp_df))
        # print(number, temp_df)
        input.value = str(temp_df["food"][number])
        image.src = str(temp_df["imgfilepath"][number])
        description.value = str(temp_df["description"][number])
        ingredients.value = str(temp_df["ingredients"][number])
        instructions.value = str(temp_df["instructions"][number])
        


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

    available_ingredients = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)
    available_ingredients.value =  str(df["description"][starter ])

    
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
    def get_options():
        options = ["pepperoni","sausage"]

        return [ft.DropdownOption(
            key=option,
            content = ft.Text(value=option)
        )
            for option in options]
    # def d1_update():
    #     FoodData.ingredients_list[0] = d1.value
    # def d2_update():
    #     FoodData.ingredients_list[1] = d2.value
    # def d3_update():
    #     FoodData.ingredients_list[2] = d3.value
        # self.update() 
    def recommend_based_on_available_ingredients():
    #    print([xx.value for xx in  dropdown_ingredients])
      for xx in  dropdown_ingredients:
         print(xx.value) 
    
    d1 = ft.Dropdown(value= "",editable=True,label="one ingredient you have",options = get_options())
    d2 = ft.Dropdown(value= "",editable=True,label="one ingredient you have",options = get_options())
    d3 = ft.Dropdown(value= "",editable=True,label="one ingredient you have",options = get_options())
    dropdown_ingredients = [d1,d2,d3]
    on_ingredients = ft.TextButton(content = "Based on ingredients",on_click = recommend_based_on_available_ingredients)
    page.add(
        ft.ResponsiveRow(
           controls = dropdown_ingredients
            
        )
    )
    page.add(
        ft.ResponsiveRow(
           controls = [on_ingredients]
            
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