import pyttsx3
import sys
import speech_recognition as sr
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QSize

import os

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path("voice.ui")
form_class = uic.loadUiType(form)[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(502, 624)
        self.pushButton.clicked.connect(self.micsay)

    def micsay(self):
        engine.say("사운드테스트")
        engine.runAndWait()

        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            self.textEdit.setText("말하세요")
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio, language='ko-KR')
        ss = f"인식된 음성 : {text}"
        self.textEdit.setText(ss)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()


# 음성으로 말하기 모듈





    # 음성 인식 모듈








