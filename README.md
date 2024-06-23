Webová aplikace pro zobrazování sportovních zpráv
Popis projektu

-Tento projekt je webová aplikace, která zobrazuje nové sportovní zprávy z různých internetových stránek, jako jsou tn.cz a blesk.cz. Aplikace bude mít vyhledávací menu, kde uživatel zadá konkrétní sport a zobrazí se mu zprávy z různých zdrojů.

Klíčové vlastnosti--
Sledování sportovních zpráv z různých zdrojů:

Automatické získávání a zobrazování sportovních zpráv z webových stránek jako tn.cz, blesk.cz a dalších.
Vyhledávací funkce:

Uživatel může zadat konkrétní sport do vyhledávacího pole a zobrazí se mu relevantní zprávy z různých zdrojů.
Podrobné statistiky:

Aplikace poskytuje přehledy a statistiky o sportovních zprávách, které uživatel čte nejčastěji.
Upozornění a notifikace:

Upozornění na nové zprávy nebo důležité události ve světě sportu.
Historie a export dat:

Ukládání historie čtení sportovních zpráv a možnost exportu dat do CSV nebo jiných formátů pro další analýzu.
Technologie
Vývoj webové aplikace
Backend:

Python a Flask: Pro vytvoření serverové části aplikace, která bude zpracovávat požadavky a získávat data z webových stránek.
BeautifulSoup a Requests: Pro web scraping a získávání sportovních zpráv z různých webových zdrojů.
Frontend:

HTML5, CSS3 a JavaScript: Pro strukturování a stylizaci uživatelského rozhraní.
React.js: Pro vytváření dynamických a interaktivních uživatelských prvků.
Databáze:

SQLite: Pro ukládání uživatelských dat a historie čtení zpráv lokálně na serveru.
Nasazení:

Heroku nebo Vercel: Pro nasazení aplikace na web.
Funkcionalita
Backend
Scraping: Automatické získávání sportovních zpráv z různých zdrojů pomocí knihoven BeautifulSoup a Requests.
API: Vytvoření API pomocí Flask pro poskytování dat frontendu.
Frontend
Uživatelské rozhraní:

Vyhledávací pole pro zadání konkrétního sportu.
Zobrazení seznamu relevantních zpráv.
Grafy a statistiky čtenosti zpráv.
Interaktivita:

Dynamické aktualizace seznamu zpráv na základě vyhledávání.
Notifikace o nových zprávách.
Nasazení
Heroku nebo Vercel: Pro nasazení a hostování aplikace online.
Příklad použití
Uživatel otevře aplikaci a zadá do vyhledávacího pole "fotbal".
Aplikace zobrazí seznam nejnovějších zpráv o fotbalu z různých zdrojů.
Uživatel si může zobrazit podrobnosti o každé zprávě a přejít na původní zdroj.
Aplikace ukládá historii čtení a poskytuje statistiky o nejčtenějších zprávách.