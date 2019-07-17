import sys

from PyQt5 import Qt
from PyQt5.uic import loadUi

class Konver (Qt.QMainWindow):
        def __init__(self, parent=None):
            super(). __init__(parent)
            self.ui = loadUi ("konvers.ui", self) #memanggil konversny
            self.angka1.clicked.connect(self.satu1)
            self.angka2.clicked.connect(self.dua)
            self.angka3.clicked.connect(self.tiga)
            self.angka4.clicked.connect(self.empat)
            self.angka5.clicked.connect(self.lima)
            self.angka6.clicked.connect(self.enam)
            self.angka7.clicked.connect(self.tuju)
            self.angka8.clicked.connect(self.lapan)
            self.angka9.clicked.connect(self.mbilan)
            self.angka0.clicked.connect(self.noll)
            self.titik.clicked.connect(self.titik1)
            self.AC1.clicked.connect(self.AC)
            self.apus.clicked.connect(self.hapus)
            self.pilihan1.addItem('us') #memilih
            self.pilihan1.addItem('indo')
            self.pilihan2.addItem('us')
            self.pilihan2.addItem('indo')

        @Qt.pyqtSlot() #parameter
        def satu1(self): #method
            hhm = self.line1.text() +'1'
            self.line1.setText (hhm )
            self.hitung1()

        @Qt.pyqtSlot()
        def dua (self):
            hhm = self.line1.text() +'2'
            self.line1.setText(hhm )
            self.hitung1()

        @Qt.pyqtSlot()
        def tiga (self):
            hhm = self.line1.text() + '3'
            self.line1.setText(hhm )
            self.hitung1()

        @Qt.pyqtSlot()
        def empat(self):
            hhm = self.line1.text()  + '4'
            self.line1.setText(hhm)
            self.hitung1()

        @Qt.pyqtSlot()
        def lima(self):
            hhm = self.line1.text() + '5'
            self.line1.setText(hhm )
            self.hitung1()

        @Qt.pyqtSlot()
        def enam(self):
            hhm = self.line1.text() + '6'
            self.line1.setText(hhm )
            self.hitung1()

        @Qt.pyqtSlot()
        def tuju(self):
            hhm = self.line1.text() + '7'
            self.line1.setText(hhm )
            self.hitung1()

        @Qt.pyqtSlot()
        def lapan(self):
            hhm = self.line1.text() + '8'
            self.line1.setText(hhm )
            self.hitung1()

        @Qt.pyqtSlot()
        def mbilan(self):
            hhm = self.line1.text()  + '9'
            self.line1.setText(hhm)
            self.hitung1()

        @Qt.pyqtSlot()
        def noll(self):
            hhm = self.line1.text() + '0'
            self.line1.setText(hhm )
            self.hitung1()

        @Qt.pyqtSlot()
        def titik1(self):
            hhm = self.line1.text()  + '.'
            self.line1.setText(hhm)

        @Qt.pyqtSlot()
        def AC(self):
            self.line1.setText('')
            self.line2.setText('')

        @Qt.pyqtSlot()
        def hapus(self):
            hhm = self.line1.text()
            self.line1.setText(hhm[0:-1])
            self.hitung1()

        @Qt.pyqtSlot()
        def hitung1(self):
            hhm = self.line1.text()
            hm = eval (hhm)

            apaaja = self.pilihan1.currentText()
            kepodeh = self.pilihan2.currentText()

            if apaaja == 'us':  #perhitungan
                if kepodeh == 'us':
                    kepodeh1 = hm * 1
                    self.line2.setText(str(kepodeh1))
                elif kepodeh == 'indo':
                    kepodeh1 = hm * 14000
                    self.line2.setText(str(kepodeh1))
            elif apaaja == 'indo':
                if kepodeh == 'us':
                    kepodeh1 = hm / 14000
                    self.line2.setText(str(kepodeh1))
                elif kepodeh == 'indo':
                    kepodeh1 = hm * 1
                    self.line2.setText(str(kepodeh1))


app = Qt.QApplication(sys.argv)

watch = Konver()
watch.show()

app.exec_()