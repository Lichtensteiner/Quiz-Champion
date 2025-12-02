"""
Quiz Champion - Démonstration GUI Moderne
Écran de démonstration des composants PyQt6
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QLabel, QScrollArea
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QColor

from quiz_champion.gui.styles import COLORS, get_stylesheet
from quiz_champion.gui.widgets import (
    Card, RoundedButton, TimerWidget, ScoreDisplay, ProgressIndicator
)


class GuiDemoWindow(QMainWindow):
    """Fenêtre de démonstration des composants GUI"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz Champion - Démo Composants GUI")
        self.setGeometry(100, 100, 1400, 900)
        
        # Appliquer stylesheet
        QApplication.instance().setStyle('Fusion')
        QApplication.instance().setStyleSheet(get_stylesheet())
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configure l'interface de démo"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Titre
        title = QLabel("🎨 Galerie de Composants GUI")
        title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        title.setStyleSheet(f"color: {COLORS['primary']};")
        main_layout.addWidget(title)
        
        # Scroll area pour tous les composants
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet(f"background-color: {COLORS['light']};")
        
        components_widget = QWidget()
        components_layout = QVBoxLayout()
        components_layout.setSpacing(20)
        components_layout.setContentsMargins(0, 0, 0, 0)
        
        # Section: Boutons
        components_layout.addWidget(self._create_buttons_demo())
        
        # Section: Cartes
        components_layout.addWidget(self._create_cards_demo())
        
        # Section: Chronomètre
        components_layout.addWidget(self._create_timer_demo())
        
        # Section: Indicateurs
        components_layout.addWidget(self._create_indicators_demo())
        
        # Section: Couleurs
        components_layout.addWidget(self._create_colors_demo())
        
        components_layout.addStretch()
        
        components_widget.setLayout(components_layout)
        scroll.setWidget(components_widget)
        
        main_layout.addWidget(scroll)
        central_widget.setLayout(main_layout)
    
    def _create_buttons_demo(self):
        """Démo des boutons"""
        card = Card()
        layout = QVBoxLayout()
        
        # Titre
        title = QLabel("📌 Boutons (Styles)")
        title.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Boutons
        buttons_row = QHBoxLayout()
        buttons_row.setSpacing(10)
        
        styles = [
            ("Primary", "primary"),
            ("Secondary", "secondary"),
            ("Success", "success"),
            ("Danger", "danger"),
        ]
        
        for text, style_type in styles:
            btn = RoundedButton(text, style_type=style_type)
            btn.setMinimumHeight(40)
            buttons_row.addWidget(btn)
        
        layout.addLayout(buttons_row)
        card.layout.addLayout(layout)
        
        return card
    
    def _create_cards_demo(self):
        """Démo des cartes"""
        card = Card()
        layout = QVBoxLayout()
        
        # Titre
        title = QLabel("🎴 Cartes (Cards)")
        title.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Grille de cartes
        cards_row = QHBoxLayout()
        cards_row.setSpacing(15)
        
        for i in range(3):
            demo_card = Card()
            demo_layout = QVBoxLayout()
            
            card_title = QLabel(f"Carte {i+1}")
            card_title.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
            card_title.setStyleSheet(f"color: {COLORS['primary']};")
            
            card_content = QLabel(
                "Contenu de démonstration\navec plusieurs lignes\nd'exemple"
            )
            card_content.setStyleSheet(f"color: {COLORS['text_muted']};")
            card_content.setWordWrap(True)
            
            demo_layout.addWidget(card_title)
            demo_layout.addWidget(card_content)
            demo_layout.addStretch()
            
            demo_card.layout.addLayout(demo_layout)
            cards_row.addWidget(demo_card)
        
        layout.addLayout(cards_row)
        card.layout.addLayout(layout)
        
        return card
    
    def _create_timer_demo(self):
        """Démo du chronomètre"""
        card = Card()
        layout = QVBoxLayout()
        
        # Titre
        title = QLabel("⏱️ Chronomètre (Timer)")
        title.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Timers
        timers_row = QHBoxLayout()
        timers_row.setSpacing(20)
        
        for seconds in [10, 20, 30]:
            timer = TimerWidget(seconds)
            timer.start_timer()
            timers_row.addWidget(timer)
        
        layout.addLayout(timers_row)
        card.layout.addLayout(layout)
        
        return card
    
    def _create_indicators_demo(self):
        """Démo des indicateurs"""
        card = Card()
        layout = QVBoxLayout()
        
        # Titre
        title = QLabel("📊 Indicateurs")
        title.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Indicateurs en ligne
        demo_layout = QHBoxLayout()
        demo_layout.setSpacing(20)
        
        # Score Display
        score_label = QLabel("Score Display:")
        score_label.setMinimumWidth(120)
        score = ScoreDisplay()
        score.set_score(2450)
        demo_layout.addWidget(score_label)
        demo_layout.addWidget(score)
        
        # Progress Indicator
        demo_layout.addSpacing(30)
        progress_label = QLabel("Progression:")
        progress_label.setMinimumWidth(120)
        progress = ProgressIndicator(10)
        progress.set_progress(7)
        demo_layout.addWidget(progress_label)
        demo_layout.addWidget(progress)
        
        demo_layout.addStretch()
        layout.addLayout(demo_layout)
        
        card.layout.addLayout(layout)
        
        return card
    
    def _create_colors_demo(self):
        """Démo de la palette de couleurs"""
        card = Card()
        layout = QVBoxLayout()
        
        # Titre
        title = QLabel("🎨 Palette de Couleurs")
        title.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Grille de couleurs
        colors_layout = QHBoxLayout()
        colors_layout.setSpacing(10)
        
        color_items = [
            ("Primary", COLORS['primary']),
            ("Secondary", COLORS['secondary']),
            ("Success", COLORS['success']),
            ("Danger", COLORS['danger']),
            ("Warning", COLORS['warning']),
            ("Dark", COLORS['dark']),
        ]
        
        for color_name, color_hex in color_items:
            color_widget = QWidget()
            color_widget.setStyleSheet(f"""
                background-color: {color_hex};
                border-radius: 8px;
            """)
            color_widget.setMinimumSize(80, 80)
            
            # Container pour le label
            container_layout = QVBoxLayout()
            container_layout.setContentsMargins(0, 0, 0, 0)
            
            color_label = QLabel(color_name)
            color_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            color_label.setStyleSheet(f"""
                color: white;
                font-weight: bold;
                font-size: 10px;
            """)
            
            container_layout.addWidget(color_label)
            color_widget.setLayout(container_layout)
            
            colors_layout.addWidget(color_widget)
        
        colors_layout.addStretch()
        layout.addLayout(colors_layout)
        
        card.layout.addLayout(layout)
        
        return card


def run_demo():
    """Exécute la démonstration GUI"""
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    
    window = GuiDemoWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    run_demo()
