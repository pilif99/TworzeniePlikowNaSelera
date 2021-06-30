
import pandas as pd

class EanyiCeny(pd.DataFrame):

    def __init__(self):

        super().__init__()
        df = pd.read_excel(r"TEMPLATES\eany ceny.xlsx")
        df = df.astype('str')
        df['g_EANCode'] = df["g_EANCode"].apply(lambda x: x.replace(x, x[:-2]))
        df['f_RRPCurr'] = df["f_RRPCurr"].apply(lambda x: x.replace(x, x[:-2]))
        df_dict = df.to_dict()
        self.append(super().__init__(df_dict))

    def znajdz_ean(self, sku):

        return list(self.loc[self['b_Indeks'] == sku, 'g_EANCode'].values)[0]

    def znajdz_cene(self, sku):

        return list(self.loc[self['b_Indeks'] == sku, 'f_RRPCurr'].values)[0]