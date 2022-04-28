from pickle import FRAME
from tkinter import *
from tkinter import ttk
from Library import download_image_from_url, set_desktop_background_image
from Pokeapi import get_pokemon_list, get_pokemon_image_url
import os
import sys
import ctypes

def main():

    script_dir = sys.path[0]
    image_dir = os.path.join(script_dir, 'images')
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    #Create the window and set icon
    root = Tk()
    root.title('Pokemon Image Viewer')
    app_id = 'pokemon.image.viewer'

    #Allowing python to call a function from a Windows library
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

    root.iconbitmap(os.path.join(script_dir, 'Poke-Ball.ico'))
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.minsize(500, 600)

    #Create the frame
    frm = ttk.Frame(root)
    frm.grid(sticky=(N,S,E,W))
    frm.rowconfigure(0, weight=1)
    frm.columnconfigure(0, weight=1)

    #Gets Pokemon image
    img_poke = PhotoImage(file=os.path.join(script_dir, 'Poke-Ball.png'))
    lbl_img = ttk.Label(frm, image=img_poke)
    lbl_img.grid(row=0, column=0, padx=10, pady=10)

    #Gets combobox
    pokemon_list = get_pokemon_list()
    pokemon_list.sort()
    pokemon_list = [p.capitalize() for p in pokemon_list]
    cbo_pokemon = ttk.Combobox(frm, values=pokemon_list, state='readonly')
    cbo_pokemon.set('Select a Pokemon')
    cbo_pokemon.grid(row=1, column=0, padx=10, pady=10)

    #Event that gets generated when the user selects a Pokemon
    def handle_poke_select(event):
        """
        Gets a directory of all pokemon from the PokeAPI.

        :param event: Offers more information about this event.
        :returns: Downloads url of specified pokemon's image, 
        downloads and saves that image, then sets that in the "PhotoImage" object.
        """

        #Gets the name of the Pokemon currently selected from the combobox, use the 
        #to download the url of that Pokemon's image, then download and save that image,
        #then set the image in teh "PhotoImage" object
        pokemon_name = cbo_pokemon.get()
        image_url = get_pokemon_image_url(pokemon_name)
        image_path = os.path.join(image_dir, pokemon_name + '.png')
        download_image_from_url(image_url, image_path)

        #Changes picture beoing displayed in the PhotoImage object
        img_poke['file'] = image_path
        
        btn_set_desktop.state(['!disabled'])

    cbo_pokemon.bind('<<ComboboxSelected>>', handle_poke_select)

    def handle_btn_set_desktop():
        """
        Makes a button to set the desktop image to a specified Pokemon.

        :param handle_btn_desktop: Button for setting the desktop background.
        :returns: A button to click on if a pokemon has been chosen.
        """
        pokemon_name = cbo_pokemon.get()
        image_path = os.path.join(image_dir, pokemon_name + '.png')
        set_desktop_background_image(image_path)

    btn_set_desktop = ttk.Button(frm, text='Set as Desktop Image', command=handle_btn_set_desktop)
    btn_set_desktop.state(['disabled'])
    btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)

    root.mainloop()

main()