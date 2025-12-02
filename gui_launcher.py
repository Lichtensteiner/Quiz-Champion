#!/usr/bin/env python3
"""
Quiz Champion - Application principale GUI
Lance l'interface graphique moderne PyQt6
"""

import sys
from pathlib import Path

# Ajouter le répertoire src au path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import Qt

from quiz_champion.models.database import db
from quiz_champion.services import CategoryService
from quiz_champion.gui.main_window import MainWindow
from quiz_champion.gui.styles import get_stylesheet, COLORS


def initialize_database():
    """Initialise la base de données"""
    try:
        db.init_db()
        session = db.get_session()
        CategoryService.get_or_create_categories(session)
        session.close()
        return True
    except Exception as e:
        print(f"Erreur lors de l'initialisation de la BD: {e}")
        return False


def main():
    """Point d'entrée principal"""
    # Initialiser la BD
    if not initialize_database():
        print("Impossible d'initialiser la base de données")
        sys.exit(1)
    
    # Créer l'application PyQt
    app = QApplication(sys.argv)
    
    # Configuration globale
    app.setStyle('Fusion')
    app.setStyleSheet(get_stylesheet())
    
    # Créer et afficher la fenêtre principale
    try:
        window = MainWindow()
        window.show()
    except Exception as e:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Erreur")
        msg_box.setText(f"Erreur lors du lancement de l'application:\n{str(e)}")
        msg_box.exec()
        sys.exit(1)
    
    # Démarrer la boucle d'événements
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
