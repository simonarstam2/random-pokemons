import requests
import random

pokemons_johto = requests.get(url='https://randompokemon.com/dex/johto.json').json()
pokemons_kanto = requests.get(url='https://randompokemon.com/dex/kanto.json').json()
pokemons_hoenn = requests.get(url='https://randompokemon.com/dex/hoenn.json').json()
pokemons_sinnoh = requests.get(url='https://randompokemon.com/dex/sinnoh_pt.json').json() 
pokemons_unova = requests.get(url='https://randompokemon.com/dex/unova.json').json() 

pokemons = pokemons_johto + pokemons_kanto + pokemons_hoenn + pokemons_sinnoh + pokemons_unova
secure_random = random.SystemRandom()

for x in range(6): 
    rand = secure_random.choice(pokemons)
    print(rand['name'])
    print('  ' + ', '.join(rand['types']))
