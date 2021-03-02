import shutil
import datetime
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app_copy.ui', self)
        self.source_name = ''
        self.dest_name = ''
        self.btn_source.clicked.connect(self.give_source)
        self.btn_dest.clicked.connect(self.give_dest)
        self.btn_archive.clicked.connect(self.make_reserve_arc)

    def give_source(self):
        self.source_name = QFileDialog.getExistingDirectory()
        text_source = self.source_name.split('/')
        self.line_source.setText('/'.join(text_source[len(text_source) - 2:len(text_source)]))

    def give_dest(self):
        self.dest_name = QFileDialog.getExistingDirectory()
        text_dest = self.dest_name.split('/')
        self.line_dest.setText('/'.join(text_dest[len(text_dest) - 2:len(text_dest)]))

    def make_time(self, time: str):
        self.time_name = time.split('.')[0].replace('-', '_')
        self.time_name = '--'.join(self.time_name.replace(':', '-').split())
        return self.time_name

    def make_reserve_arc(self):
        try:
            shutil.make_archive('archive' + self.make_time(str(datetime.datetime.now())), 'zip',
                                root_dir=self.source_name)
            shutil.move('archive' + self.time_name + '.zip.', self.dest_name)
            self.statusBar().showMessage('Каталог успешно архивирован')
            self.statusBar().setStyleSheet("color : green")
        except Exception:
            self.statusBar().setStyleSheet("color : grey")
            self.statusBar().showMessage('Что-то пошло не так')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())