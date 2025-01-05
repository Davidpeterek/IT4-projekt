import os
import sys
import itertools
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
from tabulate import tabulate
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListView, ListItem
from textual.widgets import Label, Pretty, Rule, TabbedContent
from textual.binding import Binding
from textual.screen import Screen
from textual.reactive import reactive
from textual.containers import Container, ScrollableContainer

__version__ = 1.0

# Třída pro kontejner a posouvání tabulek
class SportsTableContainer(ScrollableContainer):
    BINDINGS = [
        Binding("k", "scroll_up", "Posun nahoru", show=False),
        Binding("j", "scroll_down", "Posun dolů", show=False),
        Binding("h", "scroll_left", "Posun vlevo", show=False),
        Binding("l", "scroll_right", "Posun vpravo", show=False),
    ]

# Obrazovka pro zobrazení sportovních dat
class SportsScreen(Screen):
    BINDINGS = [
        ("backspace", "app.pop_screen", "Zpět"),  # Umožňuje uživateli vrátit se na předchozí obrazovku
        ("escape", "app.pop_screen", "Zpět")       # Další zkratka pro návrat
    ]

    sport_name = reactive('sport', recompose=True)  # Reaktivní vlastnost pro sledování vybraného sportu

    def compose(self):
        # Šablony URL pro získávání dat
        url = 'https://www.cbssports.com/{}/schedule/'.format(self.sport_name)
        df = pd.read_html(url)  # Načtení rozpisu do DataFrame

        # Získání dat o rozpisu pomocí BeautifulSoup
        url_date = get('https://www.cbssports.com/{}/schedule/'.format(self.sport_name))
        soup = BeautifulSoup(url_date.content, 'html.parser')
        dates = soup.find_all('h3', {'class': 'TableBase-title TableBase-title--large'})
        dates_list = [d.text.strip() for d in dates]

        # Načtení tabulky pořadí
        url_standings = 'https://www.cbssports.com/{}/standings/'.format(self.sport_name)
        df_standings = pd.read_html(url_standings)

        # Načtení dat o zraněních
        url_injury = 'https://www.cbssports.com/{}/injuries/'.format(self.sport_name)
        df_injury = pd.read_html(url_injury)

        # Získání názvů týmů pomocí BeautifulSoup
        url_team_name = get('https://www.cbssports.com/{}/injuries/'.format(self.sport_name))
        soup = BeautifulSoup(url_team_name.content, 'html.parser')
        team_name = soup.find_all('span', {'class': 'TeamName'})

        # Zobrazení hlavičky
        yield Header()
        with Container(classes='top'):
            yield Label(self.sport_name.upper(), id='sportTitle')  # Zobrazení názvu vybraného sportu
            yield Rule(line_style='ascii')

        # Zobrazení obsahu v kartách
        with Container(classes='bottom'):
            with TabbedContent('Schedule', 'Standings', 'Injury', classes='bottom'):
                # Zobrazení rozpisu zápasů
                with SportsTableContainer(classes='bottom'):
                    for date, table in itertools.zip_longest(dates_list, df, fillvalue=' '):
                        table = table.iloc[:, 0:3]  # Výběr prvních 3 sloupců tabulky
                        yield Label(f'[bold purple]{date}[/bold purple]')
                        yield Label('')
                        yield Pretty(table)  # Zobrazení tabulky rozpisu
                        yield Label('')

                # Zobrazení tabulky pořadí
                with SportsTableContainer(classes='bottom'):
                    if self.sport_name == 'mlb':
                        # Zpracování tabulky pořadí pro MLB
                        df1 = df_standings[1]
                        df1 = df1.iloc[:, 0:3]
                        df1 = df1.droplevel(0, axis=1)
                        df1 = df1.dropna()
                        df2 = df_standings[3]
                        df2 = df2.iloc[:, 0:3]
                        df2 = df2.droplevel(0, axis=1)
                        df2 = df2.dropna()
                        yield Pretty(df1)
                        yield Pretty(df2)
                        yield Label('')
                    elif self.sport_name == 'nba':
                        # Zpracování tabulky pořadí pro NBA
                        df1 = df_standings[0]
                        df1 = df1.iloc[:, 1:5]
                        df1 = df1.droplevel(0, axis=1)
                        df1 = df1.dropna()
                        df2 = df_standings[1]
                        df2 = df2.iloc[:, 1:5]
                        df2 = df2.droplevel(0, axis=1)
                        df2 = df2.dropna()
                        yield Label('[bold purple]Východní[/bold purple]')
                        yield Pretty(df1)
                        yield Label('[bold purple]Západní[/bold purple]')
                        yield Pretty(df2)
                        yield Label('')
                    elif self.sport_name == 'nhl':
                        # Zpracování tabulky pořadí pro NHL
                        df1 = df_standings[0]
                        df1 = df1.iloc[:, 0:6]
                        df1 = df1.droplevel(0, axis=1)
                        df1 = df1.dropna()
                        df2 = df_standings[1]
                        df2 = df2.iloc[:, 0:6]
                        df2 = df2.droplevel(0, axis=1)
                        df2 = df2.dropna()
                        yield Label('[bold purple]Východní[/bold purple]')
                        yield Pretty(df1)
                        yield Label('[bold purple]Západní[/bold purple]')
                        yield Pretty(df2)
                        yield Label('')
                    elif self.sport_name == 'nfl':
                        # Zpracování tabulky pořadí pro NFL
                        df1 = df_standings[0]
                        df1 = df1.iloc[:, 0:4]
                        df1 = df1.droplevel(0, axis=1)
                        df1 = df1.dropna()
                        df2 = df_standings[1]
                        df2 = df2.iloc[:, 0:4]
                        df2 = df2.droplevel(0, axis=1)
                        df2 = df2.dropna()
                        yield Label('[bold purple]AFC[/bold purple]')
                        yield Pretty(df1)
                        yield Label('[bold purple]NFC[/bold purple]')
                        yield Pretty(df2)
                        yield Label('')

                # Zobrazení zranění
                with SportsTableContainer(classes='bottom'):
                    for name, table in zip(team_name, df_injury):
                        # Zpracování jmen hráčů pro zobrazení
                        table['first_name'] = table['Player'].str.split().str[0]
                        table['last_name'] = table['Player'].str.split().str[2]
                        table['Player'] = table['first_name'] + table['last_name']
                        table = table.drop(['first_name', 'last_name'], axis=1)
                        yield Label(f'[bold purple][u]{name.text.strip()}[/u][/bold purple]')
                        yield Label('')
                        yield Label(tabulate(table, headers='keys', showindex=False))
                        yield Label('')
        yield Footer()

# Zobrazení seznamu sportů
class SportsListView(ListView):
    BINDINGS = [
        Binding("enter", "select_cursor", "Vybrat", show=False),
        Binding("k", "cursor_up", "Nahoru", show=False),
        Binding("j", "cursor_down", "Dolů", show=False),
    ]

# Hlavní třída aplikace
class Sports(App):
    CSS_PATH = 'style.tcss'

    SCREENS = {'sport': SportsScreen}

    BINDINGS = [
        ('q', 'close_window', 'Konec aplikace'),  # Ukončení aplikace
        ('escape', 'close_window', 'Konec aplikace'),
        ('d', 'toggle_dark', 'Přepnout tmavý režim'),  # Přepínání tmavého režimu
    ]

    def compose(self):
        # Hlavička a seznam sportů pro výběr
        yield Header()
        yield Label(' Vyber SPORT ...')
        yield SportsListView(
            ListItem(Label(':ice_hockey: NHL'), name='nhl'),
            ListItem(Label(':baseball: MLB'), name='mlb'),
            ListItem(Label(':basketball: NBA'), name='nba'),
            ListItem(Label(':football: NFL'), name='nfl'),

        )
        yield Footer()

    def action_toggle_dark(self):
        self.dark = not self.dark  # Přepínání tmavého režimu

    def action_close_window(self):
        self.exit()  # Ukončení aplikace

    @on(SportsListView.Selected)
    def show_sport(self, event):
        # Zobrazení obrazovky vybraného sportu
        self.push_screen('sport')
        self.query_exactly_one(SportsScreen).sport_name = event.item.name

##########################

# Vstupní bod aplikace
if __name__ == '__main__':
    app = Sports()
    if len(sys.argv) < 2:
        app.run()
    elif sys.argv[1] in ['-v', '--version']:
        print(f'Sports  version {__version__}')
