import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MiniBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenêtre principale
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)

        # Créer une barre d'outils
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Bouton retour
        back_btn = QAction("Retour", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Bouton avance
        forward_btn = QAction("Avancer", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Bouton recharger
        reload_btn = QAction("Recharger", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Champ pour l'URL
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Afficher l'URL dans le champ
        self.browser.urlChanged.connect(self.update_url)

        # Paramètres de la fenêtre
        self.setWindowTitle("Mini Navigateur")
        self.showMaximized()

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

# Lancer l'application
app = QApplication(sys.argv)
QApplication.setApplicationName("Mini Navigateur Web")
window = MiniBrowser()
app.exec_()
