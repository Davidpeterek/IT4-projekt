
# Sportovní aplikace v terminálu

sportovni aplikace napsaná v pythonu používající [textual](https://textual.textualize.io/).

Po spuštění se zobrazí následující data:

- Program 
- Tabulka
- Zranění

Pro daný sport:
- MLB
- NBA
- NFL
- NHL

Všechna data jsou sbírána z [CBS Sports](https://cbssports.com).


## Jak spustit:

#### Spustit pomocí pythonu
instalovat balíčky lokálně nebo do virtuálního prostředí.
```
$ pip install -r requirements.txt
$ python sports_tui.py
```

#### Vytvořít spustitelný soubor
Pomocí PyInstalleru vytvořte spustitelný soubor pro váš operační systém. 
Spusťte soubor přímo ve složce nebo umístěte spustitelný soubor do cesty a spusťte kdekoli. 
Skript vytvoří spustitelný soubor pro sport. To lze změnit úpravou příznaku '--name' ve skriptu.
```
$ ./compile.sh
$ cd dist
$ ./sports
```
