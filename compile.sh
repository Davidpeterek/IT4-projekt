#!/usr/bin/env bash
#
# BY: chadless1
#
# DESCRIPTION:
#
# skript používající pyinstallet k vytvoření spustitelného souboru
#
pyinstaller --collect-all pyfiglet --onefile --add-data 'style.tcss:.' --name 'sports' sports_tui.py
