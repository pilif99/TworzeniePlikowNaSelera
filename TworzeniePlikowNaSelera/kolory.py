
import pandas as pd

class Kolory(pd.DataFrame):

    def __init__(self):
        
        super().__init__()
        df = pd.read_excel(r"TEMPLATES\kolory.xlsx")
        df_dict = df.to_dict()
        self.append(super().__init__(df_dict))

    def znajdz_kolor(self, sku, jezyk):

        slownik = {'DE': 'Kolor niemiecki', 'ES': 'Kolor hiszpański', 'IT': 'Kolor włoski', 'NL': 'Kolor holenderski'}
        try:
            return list(self.loc[self['SKU'] == sku, slownik[jezyk]].values)[0]
        except:
            pass

    def znajdz_mape(self, sku, jezyk):

        slownik = {'DE': 'Kolor mapa DE', 'ES': 'Kolor mapa ES', 'IT': 'Kolor mapa IT', 'NL': 'Kolor mapa NL'}
        try:
            return list(self.loc[self['SKU'] == sku, slownik[jezyk]].values)[0]
        except:
            return ''

# a = Kolory()