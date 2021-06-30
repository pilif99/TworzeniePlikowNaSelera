
class Informacje:

    def __init__(self, indeks, jezyk, eanyiceny, kolory, tytuly_opisy, ilosc_zdjec):

        self._eanyiceny = eanyiceny
        self._kolory = kolory
        self._tytuly_opisy = tytuly_opisy

        self._indeks = indeks
        self._jezyk = jezyk
        self._plec = self.plec()
        self._ilosc_zdjec = ilosc_zdjec

    def age_range_description(self):

        x = list(self._indeks)
        a = x.index('-', 3) - 3
        for i in range(3):
            del x[0]
        while len(x) > a:
            del x[a]
        bsku = ''.join(x)
        if bsku == 'TJ' or bsku == 'LJ' or bsku == 'JRY' or bsku == 'JJ':
            b = 'coat'
        elif bsku == 'TP' or bsku == 'LP' or bsku == 'JP':
            b = 'pants'
        elif bsku == 'B' or bsku == 'BOT':
            b = 'boot'
        elif bsku == 'GLV':
            b = 'sportactivityglove'
        elif bsku == 'LS1' or bsku == 'LS2':
            b = 'suit'

        if self._jezyk == 'ES' or self._jezyk == 'IT':
            return 'Adulto'
        elif b == 'boot':
            return 'Erwachsene'
        elif b == 'coat':
            return 'Erwachsener'
        elif self._jezyk == 'NL':
            return 'Volwassene'

    def apparel_body_type(self):

        return 'Regular'

    def apparel_height_type(self):

        return 'Regular'

    def apparel_size(self):

        x = list(self._indeks)
        a = x.index('_', x.index('_') + 1) + 1
        if x[a] == 'D':
            a += 1
        for i in range(a):
            del x[0]
        if len(x) > 2:
            if x[2] == '/':
                x[2] = 'W / '
                x.append('L')
        return ''.join(x)

    def apparel_size_class(self):

        slownik = {'DE': 'Alphanumerisch', 'ES': 'Letras', 'IT': 'Testo', 'NL': 'Alphanumerisch'}
        return slownik[self._jezyk]

    def apparel_size_system(self):

        slownik = {'DE': 'DE / NL / SE / PL', 'ES': 'FR / ES', 'IT': 'IT', 'NL': 'DE / NL / SE / PL',}
        return slownik[self._jezyk]

    def brand_name(self):

        slownik = {'BR': 'BROGER', 'OZ': 'OZONE MOTO', 'RH': 'REBELHORN'}
        return slownik[self._indeks[:2]]

    def bullet_point1(self):

        a = self._indeks.index('_')
        parent = self._indeks[:a]
        parent = parent.replace('-LADY', '')

        if self._plec == 'female':
            koncowka = '_L'
        else:
            koncowka = '_P'

        return(self._tytuly_opisy.znajdz_bullet_point(parent + koncowka, self._jezyk, 1))

    def bullet_point2(self):

        a = self._indeks.index('_')
        parent = self._indeks[:a]
        parent = parent.replace('-LADY', '')

        if self._plec == 'female':
            koncowka = '_L'
        else:
            koncowka = '_P'

        return(self._tytuly_opisy.znajdz_bullet_point(parent + koncowka, self._jezyk, 2))

    def bullet_point3(self):

        a = self._indeks.index('_')
        parent = self._indeks[:a]
        parent = parent.replace('-LADY', '')

        if self._plec == 'female':
            koncowka = '_L'
        else:
            koncowka = '_P'

        return(self._tytuly_opisy.znajdz_bullet_point(parent + koncowka, self._jezyk, 3))

    def bullet_point4(self):

        a = self._indeks.index('_')
        parent = self._indeks[:a]
        parent = parent.replace('-LADY', '')

        if self._plec == 'female':
            koncowka = '_L'
        else:
            koncowka = '_P'

        return(self._tytuly_opisy.znajdz_bullet_point(parent + koncowka, self._jezyk, 4))

    def bullet_point5(self):

        a = self._indeks.index('_')
        parent = self._indeks[:a]
        parent = parent.replace('-LADY', '')

        if self._plec == 'female':
            koncowka = '_L'
        else:
            koncowka = '_P'

        return(self._tytuly_opisy.znajdz_bullet_point(parent + koncowka, self._jezyk, 5))

    def color_map(self):

        return self._kolory.znajdz_mape(self._indeks, self._jezyk)

    def color_name(self):

        return self._kolory.znajdz_kolor(self._indeks, self._jezyk)

    def condition_type(self):

        slownik = {'DE': 'Neu', 'ES': 'Nuevo', 'IT': 'Nuovo', 'NL': 'Nieuw'}
        return slownik[self._jezyk]

    def country_of_origin(self):
        
        if self._jezyk == 'ES':
            return 'Pakistán'
        else:
            return 'Pakistan'

    def department_name(self):
        
        Kobiety = {'DE': 'Damen', 'ES': 'Mujer', 'IT': 'Donna', 'NL': 'Vrouwen'}
        Mezczyzni = {'DE': 'Herren', 'ES': 'Hombre', 'IT': 'Uomo', 'NL': 'Mens'}
        if self._plec == 'unisex':
            return 'unisex'
        elif self._plec == 'male':
            return Mezczyzni.get(self._jezyk)
        else:
            return Kobiety.get(self._jezyk)

    def external_product_id(self):

        return self._eanyiceny.znajdz_ean(sku = self._indeks)

    def external_product_id_type(self):

        return 'EAN'

    def feed_product_type(self):

        x = list(self._indeks)
        a = x.index('-', 3) - 3
        for i in range(3):
            del x[0]
        while len(x) > a:
            del x[a]
        bsku = ''.join(x)
        if bsku == 'TJ' or bsku == 'LJ' or bsku == 'JRY' or bsku == 'JJ':
            return 'coat'
        elif bsku == 'TP' or bsku == 'LP' or bsku == 'JP':
            return 'pants'
        elif bsku == 'B' or bsku == 'BOT':
            return 'boot'
        elif bsku == 'GLV' and self._jezyk == 'NL':
            return 'ridinggloves'
        elif bsku == 'GLV':
            return 'sportactivityglove'
        elif bsku == 'LS1' or bsku == 'LS2':
            return 'suit'
        else:
            print('feed_product_type ' + self.parent_sku)

    def footwear_age_group(self):

        if self._jezyk == 'DE' or self._jezyk == 'NL':
            return 'Erwachsene'
        else:
            return 'Adulto'

    def footwear_size(self):

        x = list(self._indeks)
        a = x.index('_', x.index('_') + 1) + 1
        if x[a] == 'D':
            a += 1
        for i in range(a):
            del x[0]
        if len(x) > 2:
            if x[2] == '/':
                x[2] = 'W / '
                x.append('L')
        return ''.join(x)

    def footwear_size_class(self):

        slownik = {'DE': 'Numerisch', 'ES': 'Números', 'IT': 'Numero', 'NL': 'Numerisch'}
        return slownik[self._jezyk]

    def footwear_size_system(self):

        slownik = {'DE': 'EU Schuhgrößensystem', 'ES': 'Sistema tallas calzado EU', 'IT': 'Sistema Taglie Calzature EU', 'NL': 'EU Schuhgrößensystem'}
        return slownik[self._jezyk]

    def footwear_width(self):

        slownik = {'DE': 'Normal', 'ES': 'Estándar', 'IT': 'Normale', 'NL': 'Normal'}
        return slownik[self._jezyk]

    def item_name(self):

        a = self._indeks.index('_')
        parent = self._indeks[:a]
        parent = parent.replace('-LADY', '')

        if self._plec == 'female':
            koncowka = '_L'
        else:
            koncowka = '_P'

        return(self._tytuly_opisy.znajdz_tytul(sku = parent + koncowka, jezyk = self._jezyk))

    def item_sku(self):

        return self._indeks

    def item_type_name(self):

        x = list(self._indeks)
        a = x.index('-', 3) - 3
        for i in range(3):
            del x[0]
        while len(x) > a:
            del x[a]
        bsku = ''.join(x)
        if bsku == 'TJ' or bsku == 'LJ' or bsku == 'JRY' or bsku == 'JJ':
            b = 'coat'
        elif bsku == 'TP' or bsku == 'LP' or bsku == 'JP':
            b = 'pants'
        elif bsku == 'B' or bsku == 'BOT':
            b = 'boot'
        elif bsku == 'GLV':
            b = 'sportactivityglove'
        elif bsku == 'LS1' or bsku == 'LS2':
            b = 'suit'

        lista1 = ['DE', 'ES', 'IT', 'NL']
        lista2 = ['boot', 'coat', 'sportactivityglove', 'pants']
        lista3 = [(x, y) for x in lista2 for y in lista1]
        lista4 = ['Motorradstiefel', 'Botas de moto', 'Stivali da moto', 'Motorlaarzen', 'Motorradjacke', 'chaqueta de moto', 'giacca moto', 'Motorjas', 'Motorradhandschuhe', 'Guantes de moto', 'Guanti da moto', 'Motorhandschoenen', 'Motorradhose', 'pantalones de moto', 'pantaloni da moto', 'Motorbroek']
        slownik = dict(zip(lista3, lista4))
        return slownik[(b, self._jezyk)]

    def main_image_url(self):

        x = self._indeks
        if x[3] == 'T' and x[len(x) - 3] == '/' or x[3] == 'J':
            jeans = 0
        else:
            jeans = 1

        if self._ilosc_zdjec - jeans >= 1:

            slownik1 = {'BR': 'Broger', 'OZ': 'Ozone', 'RH': 'Rebelhorn'}

            a1 = 'https://powerlink.powerbike.pl/AMZPhoto/'
            a2 = slownik1[self._indeks[:2]] + '/'
            b1 = self._indeks.index('_')
            a3 = self._indeks[:b1]
            if self._plec == 'female':
                a4 = ' LADY'
            else:
                a4 = ''
            b2 = self._indeks.index('_', b1 + 1)
            a5 = '/' + self._indeks[:b2] + ' (1)'
            if self._plec == 'female':
                a6 = ' LADY.jpg'
            else:
                a6 = '.jpg'

            aa = a1+a2+a3+a4+a5+a6
            return aa.replace('-LADY', '')

        else:

            return ''

    def manufacturer(self):
        
        slownik = {'BR': 'BROGER', 'OZ': 'OZONE', 'RH': 'REBELHORN'}
        return slownik[self._indeks[:2]].title()

    def material_type(self):
        
        skora = {'DE': 'Leder', 'ES': 'cuero', 'IT': 'pelle', 'NL': 'Leder'}
        return skora.get(self._jezyk)

    def model(self):

        return self._indeks

    def model_name(self):

        a = self._indeks.index('-', 3)
        b = self._indeks.index('_')

        poczatek = self._indeks[a + 1:b]
        poczatek = poczatek.replace('-LADY', '')

        if self._indeks[4] == 'J':
            srodek = ' JACKET'
        elif self._indeks[3:6] == 'JRY':
            srodek = ' SHIRT'
        elif self._indeks[4] == 'P':
            srodek = ' PANTS'
        elif self._indeks[3] == 'B':
            srodek = ' BOOT'
        elif self._indeks[3:6] == 'GLV':
            srodek = ' GLOVES'
        elif self._indeks[3:5] == 'LS':
            srodek = ' SUIT'

        if self._plec == 'female':
            koniec = ' LADY'
        else:
            koniec = ''

        return poczatek + srodek + koniec

    def other_image_url1(self):

        x = self._indeks
        if x[3] == 'T' and x[len(x) - 3] == '/' or x[3] == 'J':
            jeans = 0
        else:
            jeans = 1

        if self._ilosc_zdjec - jeans >= 2:

            slownik1 = {'BR': 'Broger', 'OZ': 'Ozone', 'RH': 'Rebelhorn'}

            a1 = 'https://powerlink.powerbike.pl/AMZPhoto/'
            a2 = slownik1[self._indeks[:2]] + '/'
            b1 = self._indeks.index('_')
            a3 = self._indeks[:b1]
            if self._plec == 'female':
                a4 = ' LADY'
            else:
                a4 = ''
            b2 = self._indeks.index('_', b1 + 1)
            a5 = '/' + self._indeks[:b2] + ' (2)'
            if self._plec == 'female':
                a6 = ' LADY.jpg'
            else:
                a6 = '.jpg'

            aa = a1+a2+a3+a4+a5+a6
            return aa.replace('-LADY', '')

        else:

            return ''

    def other_image_url2(self):

        x = self._indeks
        if x[3] == 'T' and x[len(x) - 3] == '/' or x[3] == 'J':
            jeans = 0
        else:
            jeans = 1

        if self._ilosc_zdjec - jeans >= 3:

            slownik1 = {'BR': 'Broger', 'OZ': 'Ozone', 'RH': 'Rebelhorn'}

            a1 = 'https://powerlink.powerbike.pl/AMZPhoto/'
            a2 = slownik1[self._indeks[:2]] + '/'
            b1 = self._indeks.index('_')
            a3 = self._indeks[:b1]
            if self._plec == 'female':
                a4 = ' LADY'
            else:
                a4 = ''
            b2 = self._indeks.index('_', b1 + 1)
            a5 = '/' + self._indeks[:b2] + ' (3)'
            if self._plec == 'female':
                a6 = ' LADY.jpg'
            else:
                a6 = '.jpg'

            aa = a1+a2+a3+a4+a5+a6
            return aa.replace('-LADY', '')

        else:

            return ''
    
    def other_image_url3(self):

        x = self._indeks
        if x[3] == 'T' and x[len(x) - 3] == '/' or x[3] == 'J':
            jeans = 0
        else:
            jeans = 1

        if self._ilosc_zdjec - jeans >= 4:

            slownik1 = {'BR': 'Broger', 'OZ': 'Ozone', 'RH': 'Rebelhorn'}

            a1 = 'https://powerlink.powerbike.pl/AMZPhoto/'
            a2 = slownik1[self._indeks[:2]] + '/'
            b1 = self._indeks.index('_')
            a3 = self._indeks[:b1]
            if self._plec == 'female':
                a4 = ' LADY'
            else:
                a4 = ''
            b2 = self._indeks.index('_', b1 + 1)
            a5 = '/' + self._indeks[:b2] + ' (4)'
            if self._plec == 'female':
                a6 = ' LADY.jpg'
            else:
                a6 = '.jpg'

            aa = a1+a2+a3+a4+a5+a6
            return aa.replace('-LADY', '')

        else:

            return ''

    def other_image_url4(self):

        x = self._indeks
        if x[3] == 'T' and x[len(x) - 3] == '/' or x[3] == 'J':
            jeans = 0
        else:
            jeans = 1

        if self._ilosc_zdjec - jeans >= 5:

            slownik1 = {'BR': 'Broger', 'OZ': 'Ozone', 'RH': 'Rebelhorn'}

            a1 = 'https://powerlink.powerbike.pl/AMZPhoto/'
            a2 = slownik1[self._indeks[:2]] + '/'
            b1 = self._indeks.index('_')
            a3 = self._indeks[:b1]
            if self._plec == 'female':
                a4 = ' LADY'
            else:
                a4 = ''
            b2 = self._indeks.index('_', b1 + 1)
            a5 = '/' + self._indeks[:b2] + ' (5)'
            if self._plec == 'female':
                a6 = ' LADY.jpg'
            else:
                a6 = '.jpg'

            aa = a1+a2+a3+a4+a5+a6
            return aa.replace('-LADY', '')

        else:

            return ''

    def other_image_url5(self):

        x = self._indeks
        if x[3] == 'T' and x[len(x) - 3] == '/' or x[3] == 'J':
            jeans = 0
        else:
            jeans = 1

        if self._ilosc_zdjec - jeans >= 6:

            slownik1 = {'BR': 'Broger', 'OZ': 'Ozone', 'RH': 'Rebelhorn'}

            a1 = 'https://powerlink.powerbike.pl/AMZPhoto/'
            a2 = slownik1[self._indeks[:2]] + '/'
            b1 = self._indeks.index('_')
            a3 = self._indeks[:b1]
            if self._plec == 'female':
                a4 = ' LADY'
            else:
                a4 = ''
            b2 = self._indeks.index('_', b1 + 1)
            a5 = '/' + self._indeks[:b2] + ' (6)'
            if self._plec == 'female':
                a6 = ' LADY.jpg'
            else:
                a6 = '.jpg'

            aa = a1+a2+a3+a4+a5+a6
            return aa.replace('-LADY', '')

        else:

            return ''

    def other_image_url6(self):

        x = self._indeks
        if (x[3] == 'T' and x[len(x) - 3] == '/') or x[3] == 'J':
            jeans = 0
        else:
            jeans = 1

        if (jeans == 1 or self._ilosc_zdjec == 7) and self._ilosc_zdjec != 0:

            slownik1 = {'BR': 'Broger', 'OZ': 'Ozone', 'RH': 'Rebelhorn'}

            a1 = 'https://powerlink.powerbike.pl/AMZPhoto/'
            a2 = slownik1[self._indeks[:2]] + '/'
            b1 = self._indeks.index('_')
            a3 = self._indeks[:b1]
            if self._plec == 'female':
                a4 = ' LADY'
            else:
                a4 = ''
            b2 = self._indeks.index('_', b1 + 1)
            a5 = '/' + self._indeks[:b2] + ' (7)'
            if self._plec == 'female':
                a6 = ' LADY.jpg'
            else:
                a6 = '.jpg'

            aa = a1+a2+a3+a4+a5+a6
            return aa.replace('-LADY', '')

        else:

            return ''

    def outer_material_type(self):
        syntetyk = {'DE': 'Synthetisch', 'ES': 'sintético', 'IT': 'sintetico', 'NL': 'Synthetik'}
        skora = {'DE': 'Leder', 'ES': 'cuero', 'IT': 'pelle', 'NL': 'Leder'}
        jeans = {'DE': 'Jeans', 'ES': 'denim', 'IT': 'denim', 'NL': 'Denim'}
        if self.feed_product_type == 'sportactivityglove':
            return skora.get(self._jezyk)
        elif self.feed_product_type == 'boot':
            return syntetyk.get(self._jezyk)
        else:
            x = list(self._indeks)
            if x[3] == 'T' and x[len(x) - 3] == '/' or x[3] == 'J':
                return jeans.get(self._jezyk)
            elif x[3] == 'L':
                return skora.get(self._jezyk)
            else:
                return syntetyk.get(self._jezyk)

    def outer_material_type1(self):
        syntetyk = {'DE': 'Synthetisch', 'ES': 'sintético', 'IT': 'sintetico', 'NL': 'Synthetik'}
        skora = {'DE': 'Leder', 'ES': 'cuero', 'IT': 'pelle', 'NL': 'Leder'}
        jeans = {'DE': 'Jeans', 'ES': 'denim', 'IT': 'denim', 'NL': 'Denim'}
        if self.feed_product_type == 'sportactivityglove':
            return skora.get(self._jezyk)
        elif self.feed_product_type == 'boot':
            return syntetyk.get(self._jezyk)
        else:
            x = list(self._indeks)
            if x[3] == 'T' and x[len(x) - 3] == '/' or x[3] == 'J':
                return jeans.get(self._jezyk)
            elif x[3] == 'L':
                return skora.get(self._jezyk)
            else:
                return syntetyk.get(self._jezyk)

    def parent_child(self):

        return 'Child'

    def parent_sku(self):

        a = self._indeks.index('_')
        parent = self._indeks[:a]
        parent = parent.replace('-LADY', '')

        if self._plec == 'female':
            koncowka = '_L'
        else:
            koncowka = '_P'

        return parent + koncowka

    def part_number(self):

        return self._indeks

    def plec(self):
        
        try:
            a = self._indeks.index('_')
            b = self._indeks.index('_', a + 1)
        
            if self._indeks[3] == 'B':
                return 'unisex'
            elif self._indeks[a-4:a] == 'LADY' or self._indeks[b + 1] == 'D':
                return 'female'
            else:
                return 'male'
        except:
            if self._indeks[3] == 'B':
                return 'unisex'
            elif self._indeks[-1] == 'P':
                return 'male'
            elif self._indeks[-1] == 'L':
                return 'female'

    def product_description(self):

        a = self._indeks.index('_')
        parent = self._indeks[:a]
        parent = parent.replace('-LADY', '')

        if self._plec == 'female':
            koncowka = '_L'
        else:
            koncowka = '_P'

        return(self._tytuly_opisy.znajdz_opis(parent + koncowka, self._jezyk))

    def quantity(self):

        return 0

    def relationship_type(self):

        return 'Variation'

    def recommended_browse_nodes(self):

        x = list(self._indeks)
        a = x.index('-', 3) - 3
        for i in range(3):
            del x[0]
        while len(x) > a:
            del x[a]
        bsku = ''.join(x)
        if bsku == 'TJ' or bsku == 'LJ' or bsku == 'JRY' or bsku == 'JJ':
            b = 'coat'
        elif bsku == 'TP' or bsku == 'LP' or bsku == 'JP':
            b = 'pants'
        elif bsku == 'B' or bsku == 'BOT':
            b = 'boot'
        elif bsku == 'GLV':
            b = 'sportactivityglove'
        elif bsku == 'LS1' or bsku == 'LS2':
            b = 'suit'

        lista1 = ['DE', 'ES', 'IT', 'NL']
        lista2 = ['boot', 'coat', 'sportactivityglove', 'pants']
        lista3 = [(x, y) for x in lista2 for y in lista1]
        lista4 = [125852031, 2425309031, 2420951031, 22490070031, 82838031, 2425315031, 2420941031, 16496582031,
                  82835031, 82835031, 82835031, 16496579031, 82837031, 2425320031, 2420943031, 22960681031]

        slownik = dict(zip(lista3, lista4))
        
        return slownik[(b, self._jezyk)]

    def size_map(self):

        x = list(self._indeks)
        a = x.index('_', x.index('_') + 1) + 1
        if x[a] == 'D':
            a += 1
        for i in range(a):
            del x[0]
        if len(x) > 2:
            if x[2] == '/':
                x[2] = 'W / '
                x.append('L')
        return ''.join(x)

    def size_name(self):
        
        x = list(self._indeks)
        a = x.index('_', x.index('_') + 1) + 1
        if x[a] == 'D':
            a += 1
        for i in range(a):
            del x[0]
        if len(x) > 2:
            if x[2] == '/':
                x[2] = 'W / '
                x.append('L')
        return ''.join(x)

    def standard_price(self):

        return self._eanyiceny.znajdz_cene(self._indeks)

    def target_gender(self):

        Kobiety = {'DE': 'Weiblich', 'ES': 'Femenino', 'IT': 'Femmina', 'NL': 'Vrouwelijk'}
        Mezczyzni = {'DE': 'Männlich', 'ES': 'Masculino', 'IT': 'Maschio', 'NL': 'Mannelijk'}
        if self._plec == 'unisex':
            return 'unisex'
        elif self._plec == 'male':
            return Mezczyzni.get(self._jezyk)
        else:
            return Kobiety.get(self._jezyk)

    def update_delete(self):

        return 'Update'

    def variation_theme(self):
        
        return 'SizeName-ColorName'