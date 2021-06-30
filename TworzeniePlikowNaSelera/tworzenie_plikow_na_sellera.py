
from openpyxl import Workbook
import baza_danych
import eanyiceny
import tytuly_opisy
import kolory
import informacje
import poi
import os
import pandas as pd
import shutil

class Tworzenie_Plikow_Na_Sellera:

    def __init__(self, parent, ilosc_zdjec):

        slownik = {'RH': 'Rebelhorn', 'OZ': 'Ozone', 'BR': 'Broger'}

        for i in ['NL']:

            bd = baza_danych.Baza_Danych(informacje.Informacje, eanyiceny.EanyiCeny(), kolory.Kolory(), tytuly_opisy.Tytuly_Opisy(), i, poi.POI(parent), ilosc_zdjec)

            os.chdir("\\\\192.168.1.111\\Wymiana\\Filip Lorenz\\" + slownik[parent[:2]])
            writer = pd.ExcelWriter(parent + ' ' + i + '.xlsx', engine='xlsxwriter')
            bd.to_excel(writer, sheet_name = 'Arkusz1', header = None, index = None)
            writer.save()

lista_parentow = ['RH-LJ-REBEL_P']

for parent in lista_parentow:

    a = Tworzenie_Plikow_Na_Sellera(parent, 0)