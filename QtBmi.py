#!/usr/bin/python
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic

import sys


class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('qtbmi.ui', self)
        self.setFixedSize(395, 225)
        peso_iniziale = 50
        altezza_iniziale = 100

        self.hS_peso.setMinimum(0)
        self.hS_peso.setMaximum(300)
        self.hS_altezza.setMinimum(0)
        self.hS_altezza.setMaximum(250)

        self.lE_peso.setText(str(peso_iniziale))
        self.hS_peso.setValue(peso_iniziale)
        self.lE_altezza.setText(str(altezza_iniziale))
        
    
    def cambio_valore_lE(self):
        try:
            peso = float(self.lE_peso.text())
            self.hS_peso.setValue(peso)
            altezza = float(self.lE_altezza.text())
            self.hS_altezza.setValue(altezza)
        except:
            self.lE_peso.setText('')

    
    def cambio_valore_hS(self):
        peso = self.hS_peso.value()
        self.lE_peso.setText(str(peso))
        altezza = self.hS_altezza.value()
        self.lE_altezza.setText(str(altezza))
       
    def calcolo_fun(self):
        try:
            peso = float(self.lE_peso.text())
            alte = float(self.lE_altezza.text())
            altm = alte/100
            bmi = peso/(altm*altm)
            self.lE_bmi.setText(str(format(bmi,'>12.1f')))
            
            bmii = round(bmi)

            if (bmii <= 18):
                self.lE_interpretazione.setText('Sottopeso')
            if (bmii > 19) and (bmii < 24):
                self.lE_interpretazione.setText('Normopeso')
            if (bmii > 25) and (bmii < 29):
                self.lE_interpretazione.setText('Sovrappeso')
            if (bmii >= 30):
                self.lE_interpretazione.setText('Obeso')
        except:
            self.lE_bmi.setText('NaN')
            self.lE_interpretazione.setText('')
    
    def clear_fun(self):
        self.lE_bmi.setText('')
        self.lE_peso
      

app = QApplication(sys.argv)
window = Ui()
window.show()
sys.exit(app.exec())