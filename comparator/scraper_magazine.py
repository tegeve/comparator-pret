from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


class ScraperAltexEmag:

    def __init__(self, cod_produs):
        self.descriere_emag = None
        self.descriere_altex = None
        self.pret_produs_emag = None
        self.cod_produs = cod_produs
        self.pret_emag = self.scraper_emag()
        self.pret_altex = self.scraper_altex()

    def scraper_emag(self):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get('https://www.emag.ro/#opensearch')
        get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
        get_element.send_keys(f'{self.cod_produs}')
        get_element.submit()
        try:
            descriere_produs_emag = browser.find_element(by=By.ID, value="card_grid")
            self.descriere_emag = descriere_produs_emag.text.split('\n')
            self.pret_produs_emag = browser.find_element(by=By.XPATH,
                                                         value=f'//*[@id="card_grid"]/div/div/div/div[4]/div[1]/p[2]')
            self.pret_emag = self.pret_produs_emag.text.removesuffix(' Lei')
            return self.descriere_emag[0], self.pret_emag
        except NoSuchElementException:
            pass

    def scraper_altex(self):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(f'https://altex.ro/cauta/?q={self.cod_produs}')
        pret_produs_altex = browser.find_element(by=By.XPATH,
                                                 value=f'//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div['
                                                       f'2]/div/ul[2]/li/a/div[5]/div/div[2]')
        descriere_produs_altex = browser.find_element(by=By.XPATH,
                                                      value='//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div['
                                                            '2]/div/ul[2]/li/a')
        self.descriere_altex = descriere_produs_altex.text.split('\n')[0]
        self.pret_altex = pret_produs_altex.text.removesuffix(' lei')
        return self.descriere_altex, self.pret_altex

    # afisare in DATAFRAME

    def __str__(self):
        try:
            dictionar = {'cod produs': f'{self.cod_produs}',
                         'descriere': f'{self.descriere_altex[0]}',
                         'pret': f'{self.pret_altex}',
                         'magazin': 'altex'
                         }, {'cod produs': f'{self.cod_produs}',
                             'descriere': f'{self.descriere_emag[0]}',
                             'pret': f'{self.pret_emag}',
                             'magazin': 'emag'}
        except TypeError:
            dictionar = {'cod produs': f'{self.cod_produs}',
                         'pret': f'{self.pret_altex}',
                         'magazin': 'altex'
                         }, {'cod produs': f'{self.cod_produs}',
                             'descriere': 'nu este}',
                             'pret': 'Produsul nu este in stoc',
                             'magazin': 'emag'}

        df = pd.DataFrame(dictionar, columns=('cod produs', 'pret', 'magazin'))
        self.df_sortat_pret = df.sort_values(by=['pret'], ascending=False)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.expand_frame_repr', False)
        pd.set_option('max_colwidth', None)
        return f'{self.df_sortat_pret}'





