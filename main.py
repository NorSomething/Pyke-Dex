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

        self.button = tk.Button(self.root, text="Display Information", command=self.showInfo, font=('Arial', 20))
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def getInfo(self):
        pokemon_name = self.textbox.get('1.0', tk.END).strip().lower()
        pokemon_info = self.get_pokemon_info(pokemon_name)

        pName = pokemon_info['forms'][0]['name']
        pType = pokemon_info['types'][0]['type']['name']

        print(f"Name of the Pokemon is : {pName.title()}")
        print(f"Type of the Pokemon is : {pType.title()}")

    def showInfo(self):
        label = tk.Label(self.root, text="This is a test.")
        label.pack(padx=10,pady=10)

    def get_pokemon_info(self, name):
        url = f"{self.base_url}/pokemon/{name}"
        response = requests.get(url) 

        if response.status_code == 200:
            pokemon_data = response.json() 
            return (pokemon_data) 
        else:
            print(f"Failed to retrieve data {response.status_code}")

pokeGUI()





