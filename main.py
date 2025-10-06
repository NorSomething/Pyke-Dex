import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import customtkinter as ctk



class pokeGUI:

    def __init__(self):

        self.base_url = "https://pokeapi.co/api/v2/"

        self.root = ctk.CTk()

        self.root.geometry('1800x1200')

        self.root.title("Poke-GUI")

        self.label = ctk.CTkLabel(self.root, text="Poke-GUI", font=('Arial', 35))
        self.label.pack(padx=10, pady=10)

        self.textbox = ctk.CTkTextbox(self.root, height=1, font=('Arial', 25))
        self.textbox.pack(padx=200,pady=10)

        self.checkState = ctk.IntVar() #check if button is clicked

        self.button = ctk.CTkButton(self.root, text="Get Information", command=self.getInfo, font=('Arial', 20)) 
        self.button.pack(padx=10, pady=10)

        self.label_sprite = ctk.CTkLabel(self.root, text="") 
        self.label_sprite.pack(padx=10, pady=10)

        self.label_name = ctk.CTkLabel(self.root, text="") #just declaring label here
        self.label_name.pack(padx=10,pady=10, anchor='w')

        self.label_type = ctk.CTkLabel(self.root, text="")
        self.label_type.pack(padx=10, pady=10, anchor='w')

        self.label_ability1 = ctk.CTkLabel(self.root, text="", cursor='hand2')
        self.label_ability1.pack(padx=10, pady=10, anchor='w')

        self.label_ability2 = ctk.CTkLabel(self.root, text="", cursor='hand2')
        self.label_ability2.pack(padx=10, pady=10, anchor='w')

        

        self.root.mainloop()

    def getInfo(self):
        self.pokemon_name = self.textbox.get('1.0', 'end').strip().lower()
        self.pokemon_info = self.get_pokemon_info(self.pokemon_name)

        pName = self.pokemon_info['forms'][0]['name']
        pType = self.pokemon_info['types'][0]['type']['name']
        pAbility1 = self.pokemon_info['abilities'][0]['ability']['name']
        pAbility2 = self.pokemon_info['abilities'][1]['ability']['name']

        self.label_name.configure(text=f"Name : {pName.title()}", font=('Arial', 20)) #modifying the label per function call
        self.label_type.configure(text=f"Type : {pType.title()}", font=('Arial', 20)) #not including self.root here as im just modifying the label?

        self.label_ability1.configure(text=f"Ability 1 : {pAbility1.title()}", font=('Arial', 20))
        self.label_ability1.bind("<Button-1>", self.show_ability1_info) #binding mb1 to func call

        self.label_ability2.configure(text=f"Ability 2 : {pAbility2.title()}", font=('Arial', 20))
        self.label_ability2.bind("<Button-1>", self.show_ability2_info)

        sprite_url = self.pokemon_info['sprites']['front_default']
        self.show_sprites(sprite_url)

    def show_ability1_info(self, event):
        #to get info out of ability, need to request the url inside the abilities key dict    
        url = self.pokemon_info['abilities'][0]['ability']['url']
        response = requests.get(url)
        ability_data = response.json()

        ability_details = ability_data['effect_entries'][1]['effect']

        messagebox.showinfo("Popup", ability_details)  

    def show_ability2_info(self, event):
        #to get info out of ability, need to request the url inside the abilities key dict    
        url = self.pokemon_info['abilities'][1]['ability']['url']
        response = requests.get(url)
        ability_data = response.json()

        ability_details = ability_data['effect_entries'][1]['effect']

        messagebox.showinfo("Popup", ability_details)  

    def show_sprites(self, url):
        response = requests.get(url)
        self.sprite_image = tk.PhotoImage(data=response.content)
        #self.sprite_image = PhotoImage(data=response.content)
        self.sprite_image_resized = self.sprite_image.zoom(3,3) #Xx and Yx (multipliyers), only integer multiplyers
        self.label_sprite.configure(image=self.sprite_image_resized, text="")

    def get_pokemon_info(self, name):
        url = f"{self.base_url}/pokemon/{name}"
        response = requests.get(url) 

        if response.status_code == 200:
            pokemon_data = response.json() 
            return (pokemon_data) 
        else:
            print(f"Failed to retrieve data {response.status_code}")

pokeGUI()





