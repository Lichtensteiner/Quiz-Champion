#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quiz Champion - Sélecteur d'Interface
CLI pour choisir entre GUI ou Interface Ligne de Commande
"""

import sys
import os
import argparse
from pathlib import Path

# Configure UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Ajouter src au path
sys.path.insert(0, str(Path(__file__).parent / "src"))


def launch_gui():
    """Lance l'interface graphique"""
    try:
        from PyQt6.QtWidgets import QApplication
        from quiz_champion.gui.main_window import MainWindow
        from quiz_champion.gui.styles import get_stylesheet
        from quiz_champion.models.database import db
        from quiz_champion.services import CategoryService
        
        # Initialiser BD
        db.init_db()
        session = db.get_session()
        CategoryService.get_or_create_categories(session)
        session.close()
        
        # Créer app PyQt
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        app.setStyle('Fusion')
        app.setStyleSheet(get_stylesheet())
        
        window = MainWindow()
        window.show()
        
        sys.exit(app.exec())
    
    except ImportError:
        print("❌ PyQt6 n'est pas installé!")
        print("Installez avec: pip install PyQt6")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        sys.exit(1)


def launch_cli():
    """Lance l'interface ligne de commande"""
    try:
        from quiz_champion.main import QuizChampionApp
        
        app = QuizChampionApp()
        app.init()
        app.run()
    
    except Exception as e:
        print(f"❌ Erreur: {e}")
        sys.exit(1)


def launch_demo():
    """Lance la démo des composants GUI"""
    try:
        from PyQt6.QtWidgets import QApplication
        from gui_demo import GuiDemoWindow
        from quiz_champion.gui.styles import get_stylesheet
        
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        app.setStyle('Fusion')
        app.setStyleSheet(get_stylesheet())
        
        window = GuiDemoWindow()
        window.show()
        
        sys.exit(app.exec())
    
    except ImportError:
        print("❌ PyQt6 n'est pas installé!")
        print("Installez avec: pip install PyQt6")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        sys.exit(1)


def main():
    """Point d'entrée principal"""
    parser = argparse.ArgumentParser(
        description="Quiz Champion - Testez vos connaissances!",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python run_app.py               # Lance la GUI (par défaut)
  python run_app.py --cli         # Lance l'interface CLI
  python run_app.py --demo        # Affiche la démo des composants
        """
    )
    
    parser.add_argument(
        '--cli',
        action='store_true',
        help='Lancer l\'interface en ligne de commande'
    )
    
    parser.add_argument(
        '--demo',
        action='store_true',
        help='Lancer la démo des composants GUI'
    )
    
    args = parser.parse_args()
    
    # Sélectionner l'interface
    if args.cli:
        print("🎮 Lancement de l'interface CLI...")
        launch_cli()
    elif args.demo:
        print("🎨 Lancement de la démo GUI...")
        launch_demo()
    else:
        print("🎮 Lancement de l'interface graphique...")
        launch_gui()


if __name__ == "__main__":
    main()
