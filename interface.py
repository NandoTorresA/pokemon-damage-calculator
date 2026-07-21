import tkinter as tk
from tkinter import ttk
from calculadora import damage_calculate, hp_calculate
from models.pokemons import Pokemon
from models.moves import Move
from list import pokemons_list, moves_list
import pandas as pd
from PIL import Image, ImageTk
import io
import base64

df = pd.read_csv('pokemons.csv', sep=';', index_col='nome')

window = tk.Tk()
window.title('Pokemon Damage Calculator')

weathers = ['none', 'sun', 'rain', 'hail', 'sandstorm']
terrains = ['none', 'eletric', 'psychic', 'grassy', 'misty']
screens = ['none', 'reflect', 'light screen', 'aurora veil']

label_attacker_pokemon = tk.Label(text='Attacker Pokemon')
label_attacker_pokemon.grid(row=0, column=0, padx=20, pady=20, sticky='nswe')


label_img_attacker = tk.Label(window, image='')
label_img_attacker.grid(row=1, column=0, padx=20, pady=10, sticky='nswe', columnspan=2, rowspan=3)

label_attacker_name = tk.Label(text='Attacker Pokemon')
label_attacker_name.grid(row=5, column=0, padx=20, pady=10, sticky='nswe')

entry_attacker_name = tk.Entry()
entry_attacker_name.grid(row=6, column=0, padx=20, pady=10, sticky='nswe')

label_defender_name = tk.Label(text='defender Pokemon')
label_defender_name.grid(row=7, column=0, padx=20, pady=10, sticky='nswe')

entry_defender_name = tk.Entry()
entry_defender_name.grid(row=8, column=0, padx=20, pady=10, sticky='nswe')

label_move = tk.Label(text='Move', anchor='w')
label_move.grid(row=9, column=0, padx=20, pady=10, sticky='nswe')

entry_move = tk.Entry()
entry_move.grid(row=10, column=0, padx=20, pady=10, sticky='nswe')

label_target = tk.Label(text='n° Targets', anchor='w')
label_target.grid(row=11, column=0, padx=20, pady=10, sticky='nswe')

entry_target = tk.Entry()
entry_target.grid(row=12, column=0, padx=20, pady=10, sticky='nswe')

label_weather = tk.Label(text='Weather', anchor='w')
label_weather.grid(row=13, column=0, padx=10, pady=10, sticky='nswe')

combobox_weather = ttk.Combobox(values=weathers)
combobox_weather.grid(row=14, column=0, padx=10, pady=10, sticky='nswe')
combobox_weather.set('none')

label_burn = tk.Label(text='Burn', anchor='w')
label_burn.grid(row=15, column=0, padx=10, pady=10, sticky='nswe')

var_burn = tk.BooleanVar(value=False)
frame_burn = tk.Frame()
frame_burn.grid(row=16, column=0, columnspan=2, sticky='w', padx=10)

true_burn = tk.Radiobutton(frame_burn, text='yes', variable=var_burn, value=True)
true_burn.pack(side='left')
false_burn = tk.Radiobutton(frame_burn, text='no', variable=var_burn, value=False)
false_burn.pack(side='left')

label_terrain = tk.Label(text='Terrain', anchor='w')
label_terrain.grid(row=17, column=0, padx=10, pady=10, sticky='nswe')

combobox_terrain = ttk.Combobox(values=terrains)
combobox_terrain.grid(row=18, column=0, padx=10, pady=10, sticky='we')
combobox_terrain.set('none')

label_screen = tk.Label(text='Screen', anchor='w')
label_screen.grid(row=19, column=0, padx=10, pady=10, sticky='nswe')
label_screen.grid(row=19, column=0, padx=10, pady=10, sticky='nswe')

combobox_screen = ttk.Combobox(values=screens)
combobox_screen.grid(row=20, column=0, padx=10, pady=10, sticky='nswe')
combobox_screen.set('none')

label_attacker_attributes = tk.Label(text='Attacker atributes')
label_attacker_attributes.grid(row=4, column=3, padx=10, pady=10, sticky='nswe')

label_attacker_hp = tk.Label(text='hp', anchor='w')
label_attacker_hp.grid(row=5, column=3, padx=20, pady=5, sticky='nswe')

entry_attacker_hp = tk.Entry()
entry_attacker_hp.grid(row=6, column=3, padx=20, pady=10, sticky='nswe')

label_attacker_attack = tk.Label(text='attack', anchor='w')
label_attacker_attack.grid(row=7, column=3, padx=20, pady=5, sticky='nswe')

entry_attacker_attack = tk.Entry()
entry_attacker_attack.grid(row=8, column=3, padx=20, pady=10, sticky='nswe')

label_attacker_defense = tk.Label(text='defense', anchor='w')
label_attacker_defense.grid(row=9, column=3, padx=20, pady=5, sticky='nswe')

entry_attacker_defense = tk.Entry()
entry_attacker_defense.grid(row=10, column=3, padx=20, pady=10, sticky='nswe')

label_attacker_special_attack = tk.Label(text='special_attack', anchor='w')
label_attacker_special_attack.grid(row=11, column=3, padx=10, pady=5, sticky='nswe')

entry_attacker_special_attack = tk.Entry()
entry_attacker_special_attack.grid(row=12, column=3, padx=20, pady=10, sticky='nswe')

label_attacker_special_defense = tk.Label(text='special_defense', anchor='w')
label_attacker_special_defense.grid(row=13, column=3, padx=10, pady=15, sticky='nswe')

entry_attacker_special_defense = tk.Entry()
entry_attacker_special_defense.grid(row=14, column=3, padx=20, pady=10, sticky='nswe')

label_defender_pokemon = tk.Label(text='Defender Pokemon')
label_defender_pokemon.grid(row=0, column=4, padx=10, pady=20, sticky='nswe')

label_img_defender = tk.Label(window, image='')
label_img_defender.grid(row=1, column=4, padx=10, pady=10, sticky='nswe', columnspan=2, rowspan=3)

label_defender_attributes = tk.Label(text='Defender attributes')
label_defender_attributes.grid(row=4, column=4, padx=10, pady=10, sticky='nswe')

label_defender_hp = tk.Label(text='hp', anchor='w')
label_defender_hp.grid(row=5, column=4, padx=20, pady=10, sticky='nswe')

entry_defender_hp = tk.Entry()
entry_defender_hp.grid(row=6, column=4, padx=20, pady=10, sticky='nswe')

label_defender_attack = tk.Label(text='attack', anchor='w')
label_defender_attack.grid(row=7, column=4, padx=20, pady=10, sticky='nswe')

entry_defender_attack = tk.Entry()
entry_defender_attack.grid(row=8, column=4, padx=20, pady=10, sticky='nswe')

label_defender_defense = tk.Label(text='defense', anchor='w')
label_defender_defense.grid(row=9, column=4, padx=20, pady=10, sticky='nswe')

entry_defender_defense = tk.Entry()
entry_defender_defense.grid(row=10, column=4, padx=20, pady=10, sticky='nswe')

label_defender_special_attack = tk.Label(text='special_attack', anchor='w')
label_defender_special_attack.grid(row=11, column=4, padx=20, pady=10, sticky='nswe')

entry_defender_special_attack = tk.Entry()
entry_defender_special_attack.grid(row=12, column=4, padx=20, pady=10, sticky='nswe')

label_defender_special_defense = tk.Label(text='special_defense', anchor='w')
label_defender_special_defense.grid(row=13, column=4, padx=20, pady=10, sticky='nswe')

entry_defender_special_defense = tk.Entry()
entry_defender_special_defense.grid(row=14, column=4, padx=20, pady=10, sticky='nswe')


def calculate():
    weather = combobox_weather.get()
    terrain = combobox_terrain.get()
    screen = combobox_screen.get()
    attacker_effect = True if var_burn.get() else False

    attacker = Pokemon(entry_attacker_name.get())
    defender = Pokemon(entry_defender_name.get())
    move = Move(entry_move.get())
    defender_hp = entry_defender_hp.get() or 0

    damage = damage_calculate(
        move=move,
        attacker=attacker,
        defender=defender,
        weather=weather,
        terrain=terrain,
        screen=screen,
        attacker_effect=attacker_effect,
        att_attack=entry_attacker_attack.get() or 0,
        att_sp_atk=entry_attacker_special_attack.get() or 0,
        def_hp=entry_defender_hp.get() or 0,
        def_def=entry_defender_defense.get() or 0,
        def_sp_def=entry_defender_special_defense.get() or 0,
        )

    hp_calculate(
        pokemon=defender,
        hp_stat=defender_hp,
    )

    label_result['text'] = f'O ataque causará entre {damage[0]}% - {damage[1]}% de dano'



def autocomplete(entry, options):
    listbox = tk.Listbox(window, height=6)

    def update(event):
        if event.keysym in ('Up', 'Down', 'Return'):
            return

        digited = entry.get().lower()
        listbox.delete(0, tk.END)
        if digited == '':
            listbox.place_forget()
            return

        combinations = [name for name in options if digited in name.lower()]
        if not combinations:
            listbox.place_forget()
            return

        for name in combinations[:8]:
            listbox.insert(tk.END, name)
        listbox.place(in_=entry, x=0, rely=1, relwidth=1)


    def select(event):
        if not listbox.curselection():
            return
        nome = listbox.get(listbox.curselection())
        entry.delete(0, tk.END)
        entry.insert(0, nome)

        if entry is not entry_move:
            pokemon_db_img = df.loc[entry.get(), 'sprite']
            pokemon_db_img = base64.b64decode(pokemon_db_img)
            pokemon_img = Image.open(io.BytesIO(pokemon_db_img))
            pokemon_img = pokemon_img.resize((100, 100))
            img_tk = ImageTk.PhotoImage(pokemon_img)
            
            if entry is entry_attacker_name:
                label_img_attacker['image'] = img_tk
                label_img_attacker.image = img_tk
            elif entry is entry_defender_name:
                label_img_defender['image'] = img_tk
                label_img_defender.image = img_tk
                   
        listbox.place_forget()

    entry.bind('<KeyRelease>', update)
    listbox.bind('<<ListboxSelect>>', select)



button_calculate = tk.Button(text='Calculate', command=calculate)
button_calculate.grid(row=17, column=4, padx=10, pady=20, sticky='nswe')

label_result = tk.Label(text='')
label_result.grid(row=18, column=4, padx=10, pady=20, sticky='nswe')

autocomplete(entry_attacker_name, pokemons_list)
autocomplete(entry_defender_name, pokemons_list)
autocomplete(entry_move, moves_list)

window.mainloop()