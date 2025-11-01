import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import customtkinter as ctk
from PIL import Image, ImageTk  
import io 


class pokeGUI:

    def __init__(self):

        self.base_url = "https://pokeapi.co/api/v2/"

        self.root = ctk.CTk()

        self.root.geometry('1920x1080')

        self.root.title("Poke-GUI")

        #Top Frame -> Title, Textbox and Get Info button
        #Info Frame -> Name, Type, Abilities    
        #Sprite Frame -> Sprite

        self.top_frame = ctk.CTkFrame(self.root)
        self.top_frame.pack(padx=20, pady=20, fill='x')

        self.info_frame = ctk.CTkFrame(self.root)
        self.info_frame.pack(padx=20, pady=20, fill="both", expand=True)

        #self.sprite_frame = ctk.CTkFrame(self.info_frame)
        #self.sprite_frame.pack(padx=20, pady=10, fill="x")

        self.label = ctk.CTkLabel(self.top_frame, text="Poke-GUI", font=('Arnoldboecklin', 55))
        self.label.pack(padx=10, pady=10)

        self.textbox = ctk.CTkTextbox(self.top_frame, width=500, height=10, font=('Arnoldboecklin', 45))
        self.textbox.pack(padx=10,pady=10)

        self.checkState = ctk.IntVar() #check if button is clicked

        self.button = ctk.CTkButton(self.top_frame, text="Get Information", command=self.getInfo, font=('ArnoldboecklinKalinga', 30)) 
        self.button.pack(padx=20, pady=10)

        self.sprite_name_frame = ctk.CTkFrame(self.info_frame)
        self.sprite_name_frame.pack(padx=10, pady=10, fill='x')

        self.label_sprite = ctk.CTkLabel(self.sprite_name_frame, text="") 
        self.label_sprite.pack(padx=10, pady=10)

        self.label_name = ctk.CTkLabel(self.sprite_name_frame, text="") #just declaring label here
        self.label_name.pack(padx=10,pady=10)

        #self.label_type = ctk.CTkLabel(self.info_frame, text="")
        #self.label_type.pack(padx=10, pady=10, anchor='w')

        #Lower Frame (has types and abilities)
        self.lower_frame = ctk.CTkFrame(self.info_frame)
        self.lower_frame.pack(padx=10, pady=10, fill='x')

        #Type Frame
        self.type_frame = ctk.CTkFrame(self.lower_frame)
        self.type_frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)

        self.label_type = ctk.CTkLabel(self.type_frame, text="", font=('Arial', 35))
        self.label_type.pack(padx=10, pady=10, anchor='w')

        # Abilities Frame
        self.ability_frame = ctk.CTkFrame(self.lower_frame)
        self.ability_frame.pack(side='right', padx=10, pady=10, fill='both', expand=True)

        self.label_ability1_heading = ctk.CTkLabel(self.ability_frame, text="", cursor='hand2')
        self.label_ability1_heading.grid(row=0, column = 0, padx=10, pady=10)
        self.label_ability1 = ctk.CTkLabel(self.ability_frame, text="", cursor='hand2')
        self.label_ability1.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        #self.label_ability1_info = ctk.CTkLabel(self.ability_frame, text="", font=('Arial', 25))
        #self.label_ability1_info.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        self.label_ability2_heading = ctk.CTkLabel(self.ability_frame, text="")
        self.label_ability2_heading.grid(row = 1, column = 0, padx=10, pady=10)
        self.label_ability2 = ctk.CTkLabel(self.ability_frame, text="", cursor='hand2')
        self.label_ability2.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        #self.label_ability2_info = ctk.CTkLabel(self.ability_frame, text="", font=('Arial', 25))
        #self.label_ability2_info.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        

        self.root.mainloop()

    def getInfo(self):
        self.pokemon_name = self.textbox.get('1.0', 'end').strip().lower()
        self.pokemon_info = self.get_pokemon_info(self.pokemon_name)

        pName = self.pokemon_info['forms'][0]['name']
        pType = self.pokemon_info['types'][0]['type']['name']
        abilities = self.pokemon_info['abilities']

        self.label_name.configure(text=f"{pName.title()}", font=('Arial', 25)) #modifying the label per function call
        self.label_type.configure(text=f"Type : {pType.title()}", font=('Arial', 25)) #not including self.root here as im just modifying the label?

        if len(abilities) > 0: #why == 0 and == 1 not work?
            pAbility1 = self.pokemon_info['abilities'][0]['ability']['name']
            self.label_ability1_heading.configure(text="Ability 1 : ", font=('Kalinga', 40))
            self.label_ability1.configure(text=f"{pAbility1.title()}", font=('Arial', 25))
            self.label_ability1.bind("<Button-1>", self.show_ability1_info) #binding mb1 to func call
        
        if len(abilities) > 1:
            pAbility2 = self.pokemon_info['abilities'][1]['ability']['name']    
            self.label_ability2_heading.configure(text="Ability 2 : ", font=('Kalinga', 40))
            self.label_ability2.configure(text=f"{pAbility2.title()}", font=('Arial', 25))
            self.label_ability2.bind("<Button-1>", self.show_ability2_info)    

        sprite_url = self.pokemon_info['sprites']['front_default']
        self.show_sprites(sprite_url)

    def show_ability1_info(self, event):
        #to get info out of ability, need to request the url inside the abilities key dict    
        url = self.pokemon_info['abilities'][0]['ability']['url']
        response = requests.get(url)
        ability_data = response.json()

        ability_details = ability_data['effect_entries'][1]['effect']

        #self.label_ability1.configure(text=f"Ability 1 : {self..title()} - {effect}")

        #messagebox.showinfo("Popup", ability_details)  

    def show_ability2_info(self, event):
        #to get info out of ability, need to request the url inside the abilities key dict    
        url = self.pokemon_info['abilities'][1]['ability']['url']
        response = requests.get(url)
        ability_data = response.json()

        ability_details = ability_data['effect_entries'][1]['effect']

        #messagebox.showinfo("Popup", ability_details)  

    def show_sprites(self, url):
        response = requests.get(url)
        #self.sprite_image = tk.PhotoImage(data=response.content)
        #self.sprite_image = PhotoImage(data=response.content)
        ##self.sprite_image_resized = self.sprite_image.zoom(3,3) #Xx and Yx (multipliyers), only integer multiplyers
        #self.label_sprite.configure(image=self.sprite_image_resized, width=500, text="")

        if response.status_code == 200:
            
            image_data = response.content #gives raw bytes
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((320, 240))

            self.sprite_image = ImageTk.PhotoImage(image)
            self.label_sprite.configure(image=self.sprite_image, text="", width=500)

    def get_pokemon_info(self, name):
        url = f"{self.base_url}/pokemon/{name}"
        response = requests.get(url) 

        if response.status_code == 200:
            pokemon_data = response.json() 
            return (pokemon_data) 
        else:
            messagebox.showerror("Error", f"Couldn't retreive Pokemon {name}.")
            return None

pokeGUI()





