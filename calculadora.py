from models.moves import Move
from models.pokemons import Pokemon
from lists import types_relations

def damage_calculate(
        move: Move,
        attacker: Pokemon,
        defender: Pokemon,

        def_hp: int,
        def_def: int,
        def_sp_def: int,

        weather: str,
        terrain: str,
        screen: str,
        attacker_effect: bool,
        att_attack: int,
        att_sp_atk: int,

        ) -> int:


    power = move.power
    move_category = move.damage_class
    move_type = move.type
    crit = False

    if move_category == 'physical':
        attack_points = int(attacker.attack) + int(att_attack) + 20
        defense_points = int(defender.defense) + int(def_def) + 20

    else:
        attack_points = int(attacker.special_attack) + int(att_sp_atk) + 20
        defense_points = int(defender.special_defense) + int(def_sp_def) + 20

    ### Cálculo base
    damage = int((22 * power * attack_points/defense_points)/50) + 2


    ### Cálculo de STAB
    if move.type in attacker.type:
        damage *= 1.5

    for tipo in defender.type:
    ### Cálculo de super efetividade
        for supereff_type in types_relations[move_type]['double_damage_to']:
            if tipo in supereff_type:
                damage *= 2
                print('superef')

    ### Cálculo de resistência
        for resist_type in types_relations[move_type]['half_damage_to']:
            if resist_type in tipo:
                damage /= 2
                print('Resiste')

    ### Cálculo de imunidade
        for imunity_type in types_relations[move_type]['no_damage_to']:
            if tipo in imunity_type:
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


def hp_calculate(pokemon: Pokemon, hp_stat: int):
    base_hp = int(pokemon.hp)
    hp = base_hp + int(hp_stat) + 75
    return int(hp)


if __name__ == '__main__':
    poke1 = Pokemon('greninja')
    poke2 = Pokemon('charizard')
    move1 = Move('flamethrower')
    dano = damage_calculate(move1, poke2, poke1, 100, 50, 50)
    vida = hp_calculate(poke1, 100)
    print(dano)