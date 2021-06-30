
import pandas as pd
import os
import eanyiceny
import tytuly_opisy
import kolory
import informacje
import poi

class Baza_Danych(pd.DataFrame):

    def __init__(self, informacje, eanyiceny, kolory, tytuly_opisy, jezyk, lista_indeksow, ilosc_zdjec):

        os.chdir("..")
        super().__init__()

        slownik = {'coat': 'Kurtka', 'boot': 'Buty', 'sportactivityglove': 'Rękawice', 'pants': 'Spodnie', 'ridinggloves': 'Rękawice'}

        aa = slownik[informacje(lista_indeksow[0], jezyk, eanyiceny, kolory, tytuly_opisy, ilosc_zdjec).feed_product_type()]

        df = pd.read_excel('TEMPLATES\\' + aa + ' Nowe\\' + aa +' DE.xlsx', header = None)
        df = df.loc[[0, 1, 2]]
        df = df.drop(df.columns[len(df.columns) - 1], axis=1)

        lista = df.iloc[[2]].values.tolist()[0]

        def get_lista(info):

            lista1 = []
            for i in range(len(lista)):
                if lista[i] in dir(informacje):
                    lista1.append(getattr(info, lista[i])())
                else:
                    lista1.append('')
            return lista1

        lista2 = ['feed_product_type', 'item_sku', 'brand_name', 'item_name', 'parent_child', 'variation_theme', 'update_delete', 'manufacturer', 'condition_type', 'country_of_origin',
                  'product_description', 'model_name', 'item_type_name', 'bullet_point1', 'bullet_point2', 'bullet_point3', 'bullet_point4', 'bullet_point5', 'recommended_browse_nodes']

        def get_lista2(info):

            lista1 = []
            for i in range(len(lista)):
                if lista[i] in lista2:
                    if lista[i] == 'parent_child':
                        lista1.append('Parent')
                    else:
                        lista1.append(getattr(info, lista[i])())
                else:
                    lista1.append('')
            return lista1

        df.loc[len(df.index)] = get_lista2(informacje(informacje(lista_indeksow[0], jezyk, eanyiceny, kolory, tytuly_opisy, ilosc_zdjec).parent_sku(), jezyk, eanyiceny, kolory, tytuly_opisy, ilosc_zdjec))

        for i in lista_indeksow:

            df.loc[len(df.index)] = get_lista(informacje(i, jezyk, eanyiceny, kolory, tytuly_opisy, ilosc_zdjec))
            
        df = df.astype('str')
        df_dict = df.to_dict()
        self.append(super().__init__(df_dict))