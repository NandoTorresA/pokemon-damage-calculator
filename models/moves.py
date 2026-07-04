import pandas as pd


moves_df = pd.read_csv('movimentos_info.csv', sep=';', index_col='name')
class Move:

    def __init__(self, name):
        data = moves_df.loc[name]
        self.name = name
        self.power = data['power']
        self.accuracy = data['accuracy']
        self.damage_class = data['damage_class']
        self.priority = data['priority']
        self.type = data['type']