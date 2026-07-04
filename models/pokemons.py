import pandas as pd
pokemons_df = pd.read_csv('pokemons.csv', sep=';', index_col='nome')

class Pokemon:

    def __init__(self, nome):
        dados = pokemons_df.loc[nome]
        self.nome = nome
        self.hp = dados['hp']
        self.attack = dados['attack']
        self.defense = dados['defense']
        self.special_attack = dados['special-attack']
        self.special_defense = dados['special-defense']
        self.speed = dados['speed']

        self.type = [dados['type_1']]
        if not pd.isna(dados['type_2']):
            self.type.append(dados['type_2'])

