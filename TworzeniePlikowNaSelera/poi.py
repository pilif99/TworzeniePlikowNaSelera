
import os
import pandas as pd
from openpyxl import load_workbook

class POI(list): # Pobranie Odpowiednich Indeksów

    def __init__(self, parent):

        self.parent = parent

        os.chdir("Katalogi")
        a_sku = ''.join(list(self.parent)[:2])
        if a_sku == 'BR':
            df = pd.read_excel('Catalog Broger.xlsx')
        elif a_sku == 'OZ':
            df = pd.read_excel('Catalog Ozone.xlsx')
        elif a_sku == 'RH':
            df = pd.read_excel('Catalog Rebelhorn.xlsx')

        df = df[['b_Indeks', 'Parent']]
        df = df[df['Parent'].isin([self.parent])]

        df = df.drop(columns = ['Parent'])
        df = df.squeeze()
        self.extend(df.values.tolist())