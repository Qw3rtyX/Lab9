import requests

def get_pokemon_info(name):
    """
    Gets a directory of information from the PokeAPI for a specified Pokemon.

    :param name: Pokemon's name (or Poke index)
    :returns: Dictionary of Pokemon information if sucessful; None if otherwise
    """
    print("Getting Pokemon information...", end='')

    if name is None:
        print('error: Missing name parameter')
        return

    name = name.strip().lower()
    if name == '':
        print('error: Empty name parameter')
        return

    URL = 'https://pokeapi.co/api/v2/pokemon/' + str(name)
    response = requests.get(URL)

    if response.status_code == 200:
        print('sucess')
        return response.json()
    else:
        print('failed. Response code:', response.status_code)
        return

def get_pokemon_list(limit=2000, offset=0):
    """
    Gets a list of the Pokemon's names from the PokeAPI.

    :param URL: PokeAPI's URL
    :returns: either sucess or failed response depending on the response status code
    """
    print("Getting list of Pokemon...", end='')
    URL = 'https://pokeapi.co/api/v2/pokemon/'

    #Creates dictionary with {}
    params = {
        'offset': offset,
        'limit': limit
    }

    #Assign the dictionary variable
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        print('sucess')
        poke_dict = response.json()

        #Pulls all names out of PokeAPI and puts them into a list
        return [p['name'] for p in poke_dict['results']]
    
    else:
        print('failed. Response code:', response.status_code)

def get_pokemon_image_url(name):
    """
    Accepts name of a specified Pokemon and gets photo of it from the PokeAPI

    :param poke_dict: gets pokemon name from the PokeAPI
    :returns: Pokemon photo if sucessful; None if otherwise
    """
    poke_dict = get_pokemon_info(name)
    if poke_dict:

        #Gets the url for the image of specified pokemon
        poke_url = poke_dict['sprites']['other']['official-artwork']['front_default']
        return poke_url