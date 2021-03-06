import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5 import uic


def translite_func(stro, desh, reverse=False):
    if not desh:
        dic = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
               "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
               "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
               "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
               "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
               "б": "b", "ю": "ju", "ё": "jo", "ву": "w", "ку": "q"}
    else:
        dic = {"q": "й", "`": "ё", "w": "ц", "e": "у", "r": "к", "t": "е",
               "y": "н", "u": "г", "i": "ш", "o": "щ", "p": "з", "[": "х",
               "]": "ъ", "a": "ф", "s": "ы", "d": "в", "f": "а", "g": "п",
               "'": "э", ";": "ж", "l": "д", "k": "л", "j": "о", "h": "р",
               "z": "я", "x": "ч", "c": "с", "v": "м", "b": "и", "n": "т",
               ".": "ю", ",": "б", "m": "ь"}
    if reverse:
        dic = dict([[i[1], i[0]] for i in dic.items()])
    res = []
    for i in stro:
        try:
            if i.isupper():
                res.append(dic[i.lower()].capitalize())
            else:
                res.append(dic[i])
        except KeyError:
            res.append(i)
    return ''.join(res)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.initUI()

    def initUI(self):
        self.func = [False, True]
        self.perevesti.clicked.connect(self.translite)
        self.S_Russk.triggered.connect(self.S_Russk_func)
        self.S_Angl.triggered.connect(self.S_Angl_func)
        self.Na_Angl.triggered.connect(self.Na_Angl_func)
        self.Na_Russk.triggered.connect(self.Na_Russk_func)

    def S_Russk_func(self):
        self.label.setText('Перевод с русского языка на транслит')
        self.func = [False, False]
        self.text_for_translite.clear()
        self.result.clear()

    def S_Angl_func(self):
        self.label.setText('Перевод с транслита на русский язык')
        self.func = [False, True]
        self.text_for_translite.clear()
        self.result.clear()

    def Na_Angl_func(self):
        self.label.setText('Дешифровка с русской раскладки')
        self.func = [True, True]
        self.text_for_translite.clear()
        self.result.clear()

    def Na_Russk_func(self):
        self.label.setText('Дешифровка с английской раскладки')
        self.func = [True, False]
        self.text_for_translite.clear()
        self.result.clear()

    def translite(self):
        txt = self.text_for_translite.text()
        res = translite_func(txt, self.func[0], self.func[1])
        self.result.setText(res)

    def keyPressEvent(self, event):
        if event.key() == 16777221 or event.key() == 16777220:
            self.translite()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
