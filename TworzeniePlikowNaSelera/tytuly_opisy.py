
import pandas as pd

class Tytuly_Opisy(pd.DataFrame):

    def __init__(self):

        super().__init__()
        df = pd.read_excel(r"TEMPLATES\tytuły, opisy, bullet pointy.xlsx")
        df_dict = df.to_dict()
        self.append(super().__init__(df_dict))

    def znajdz_tytul(self, sku, jezyk):

        return list(self.loc[self['Unnamed: ' + str(0)] == sku, jezyk].values)[0]

    def znajdz_opis(self, sku, jezyk):

        slownik = {'DE': '9', 'ES': '16', 'IT': '23', 'NL': '30'}
        return list(self.loc[self['Unnamed: ' + str(0)] == sku, 'Unnamed: ' + slownik[jezyk]].values)[0]

    def znajdz_bullet_point(self, sku, jezyk, nr):

        slownik = {'DE': 9, 'ES': 16, 'IT': 23, 'NL': 30}
        return list(self.loc[self['Unnamed: ' + str(0)] == sku, 'Unnamed: ' + str(slownik[jezyk] + nr)].values)[0]