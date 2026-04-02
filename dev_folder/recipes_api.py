# 

# using input api key
import requests
# https://api-ninjas.com/profile

api_url = "https://api-ninjas.com/"

api_key = input(f"what is your api key for {api_url}: ")
print(api_key)
if api_key != "" :
  response = requests.get(url=f"{api_url}")
# title as name

# ingredients is extra
# name, image path, ingredients, instructions,description
# with open 
# ingredients, instructions, 



# ingredients
# servings
# instructions
# nutrition
for x in dictsa:
    print (x)

options
for xx in response.json()[0]: print(xx)

import json
with open('data.json', 'w') as f:
    json.dump(data, f)
