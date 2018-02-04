import os
import sys

from PyQt5 import QtWidgets

from main_ui import Ui_MainWindow
import encrypt
import decrypt


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.browse_btn.clicked.connect(self.get_filepath)
        self.encrypt_btn.clicked.connect(self.encrypt_file)

        self.browse_btn_tab2.clicked.connect(self.get_filepath)
        self.decrypt_btn_tab2.clicked.connect(self.decrypt_file)

        self.show()

    def get_filepath(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'File', os.getenv('HOME'))
        if self.tabWidget.currentIndex() == 0:
            self.filepath_ledit.setText(filename[0])
        elif self.tabWidget.currentIndex() == 1:
            self.filepath_ledit_tab2.setText(filename[0])

    def encrypt_file(self):
        pub_key = self.pubkey_textedit.toPlainText().encode()
        result = encrypt.encrypt(pub_key, self.filepath_ledit.text())
        QtWidgets.QMessageBox.about(self, "Result", result)

    def decrypt_file(self):
        priv_key = self.privkey_textedit_tab2.toPlainText().encode()
        result = decrypt.decrypt(priv_key, self.filepath_ledit_tab2.text())
        QtWidgets.QMessageBox.about(self, "Result", result)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
