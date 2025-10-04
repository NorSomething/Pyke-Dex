import requests
import tkinter as tk
from tkinter import messagebox

class pokeGUI:

    def __init__(self):

        self.base_url = "https://pokeapi.co/api/v2/"

        self.root = tk.Tk()

        self.root.geometry('800x600')

        self.root.title("Poke-GUI")

        self.label = tk.Label(self.root, text="Poke-GUI", font=('Arial', 35))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=1, font=('Arial', 25))
        self.textbox.pack(padx=200,pady=10)

        self.checkState = tk.IntVar()

        self.button = tk.Button(self.root, text="Get Information", command=self.getInfo, font=('Arial', 20)) 
        self.button.pack(padx=10, pady=10)

        self.label_name = tk.Label(self.root, text="") #just declaring label here
        self.label_name.pack(padx=10,pady=10, anchor='w')

        self.label_type = tk.Label(self.root, text="")
        self.label_type.pack(padx=10, pady=10, anchor='w')

        self.label_ability = tk.Label(self.root, text="", cursor='hand2')
        self.label_ability.pack(padx=10, pady=10, anchor='w')

        self.root.mainloop()

    def getInfo(self):
        self.pokemon_name = self.textbox.get('1.0', tk.END).strip().lower()
        self.pokemon_info = self.get_pokemon_info(self.pokemon_name)

        pName = self.pokemon_info['forms'][0]['name']
        pType = self.pokemon_info['types'][0]['type']['name']
        pAbility = self.pokemon_info['abilities'][0]['ability']['name']

        self.label_name.config(text=f"Name : {pName.title()}", font=('Arial', 20)) #modifying the label per function call
        self.label_type.config(text=f"Type : {pType.title()}", font=('Arial', 20)) #not including self.root here as im just modifying the label?

        self.label_ability.config(text=f"Ability : {pAbility.title()}", font=('Arial', 20))
        self.label_ability.bind("<Button-1>", self.show_ability_info) #binding mb1 to func call

        #print(f"Name of the Pokemon is : {pName.title()}")
        #print(f"Type of the Pokemon is : {pType.title()}")

    def show_ability_info(self, event):
        #to get info out of ability, need to request the url inside the abilities key dict    
        url = self.pokemon_info['abilities'][0]['ability']['url']
        response = requests.get(url)
        ability_data = response.json()

        ability_details = ability_data['effect_entries'][1]['effect']

        messagebox.showinfo("Popup", ability_details)   


    def get_pokemon_info(self, name):
        url = f"{self.base_url}/pokemon/{name}"
        response = requests.get(url) 

        if response.status_code == 200:
            pokemon_data = response.json() 
            return (pokemon_data) 
        else:
            print(f"Failed to retrieve data {response.status_code}")

pokeGUI()





