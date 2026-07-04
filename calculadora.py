from models.moves import Move
from models.pokemons import Pokemon
import requests

def damage_calculate(
        move: Move,
        attacker: Pokemon,
        defender: Pokemon,
        weather: str,
        terrain: str,
        screen: str,
        attacker_effect: bool,

        att_attack,
        att_sp_atk,

        def_hp,
        def_def,
        def_sp_def,
        ):


    power = move.power
    move_category = move.damage_class
    move_type = move.type
    crit = False
    weather = None
    terrain = None
    attacker_effect = None

    screen = None

    if move_category == 'physical':
        attack_points = int(attacker.attack) + int(att_attack) + 20
        defense_points = int(defender.defense) + int(def_def) + 20

    else:
        attack_points = int(attacker.special_attack) + int(att_sp_atk) + 20
        defense_points = int(defender.special_defense) + int(def_sp_def) + 20

    ### Cálculo base
    damage = int((22 * power * attack_points/defense_points)/50) + 2

    r = requests.get(f'https://pokeapi.co/api/v2/type/{move_type}')
    data = r.json()

    ### Cálculo de STAB
    if move.type in attacker.type:
        damage *= 1.5

    for tipo in defender.type:
    ### Cálculo de super efetividade
        for i in range(len(data['damage_relations']['double_damage_to'])):
            if tipo in data['damage_relations']['double_damage_to'][i]['name']:
                damage *= 2

    ### Cálculo de resistência
        for j in range(len(data['damage_relations']['half_damage_to'])):
            if tipo in data['damage_relations']['half_damage_to'][j]['name']:
                damage /= 2

    ### Cálculo de imunidade
        if tipo in data['damage_relations']['no_damage_to']:
            damage *= 0

    ### Crítico
    if crit:
        damage *= 1.5

    ### Alterações pelo clima
    match weather:
        case 'sun':
            if move_type == 'fire':
                damage *= 1.5
            elif move_type == 'water':
                damage /= 2
        case 'rain':
            if move_type == 'water':
                damage *= 1.5
            elif move_type == 'fire':
                damage /= 2
        case 'hail':
            if move.name == 'blizzard':
                move.accuracy = 100
        case 'sandstorm':
            if 'ground' in defender.type:
                defender.special_defense *= 1.5

    ### Efeito de terreno
    match terrain:
        case 'eletric':
            if move.name == 'Rising Voltage':
                damage *= 2
            if move_type == 'eletric':
                damage *= 1.3
        case 'grassy':
            reduce_damage = ['bulldoze', 'earthquake', 'magnitude']
            if any(typ in move_type for typ in reduce_damage):
                damage /= 2
            if move_type == 'grass':
                damage *= 1.3
        case 'psychic':
            if move.name == 'expanding force':
                damage *= 2
            if move_type == 'psychic':
                damage *= 1.3
        case 'misty':
            if move_type == 'dragon':
                damage /= 2
            elif move.name == 'misty explosion':
                damage *= 2

    ### Efeito de queimadura
    if attacker_effect and move_category == 'physical':
        damage /= 2

    ### Efeito de screen
    if screen == 'reflect' and move_category == 'physical':
        damage /= 2
    elif screen == 'light screen' and move_category == 'special':
        damage /= 2
    elif screen == 'aurora veil':
        damage /= 2

    damage = int(damage)
    ### Roll
    min_damage = int(damage * 85/100)

    ### Habilidades
    pass

    ### Itens
    pass

    defender_hp = hp_calculate(defender, def_hp)
    max_hp_remaing = defender_hp - min_damage if defender_hp - min_damage > 0 else 0
    min_hp_remaing = defender_hp - damage if defender_hp - damage > 0 else 0

    return (100 - int(max_hp_remaing/defender_hp * 100), 100 - int(min_hp_remaing/defender_hp * 100))
    # return (min_damage, damage)


def hp_calculate(pokemon: Pokemon, hp_stat: int):
    base_hp = int(pokemon.hp)
    hp = base_hp + int(hp_stat) + 75
    return int(hp)


if __name__ == '__main__':
    poke1 = Pokemon('greninja')
    poke2 = Pokemon('charizard')
    move1 = Move('flamethrower')
    dano = damage_calculate(move1, poke2, poke1)
    vida = hp_calculate(poke1)