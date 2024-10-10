import math
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QDate

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("untitled.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.func1)
        self.pushButton_2.clicked.connect(self.func2)
        self.pushButton_add.clicked.connect(self.func3)
        self.pushButton_3.clicked.connect(self.funcx2)
        self.pushButton_4.clicked.connect(self.funcn2)

        self.add = 1
        self.number = 0
        self.label.setText(f"카운트된 숫자 : {self.number}")

        now = QDate.currentDate()
        self.label_2.setText(now.toString("yyyy년 MMMM dd일"))
    def func1(self):
        self.number += self.add
        self.label.setText(f"카운트된 숫자 : {self.number}")
        print(f"{self.add} 만큼 증가")
    def func2(self):
        self.number -= self.add
        self.label.setText(f"카운트된 숫자 : {self.number}")
        print(f"{self.add} 만큼 감소")
    def func3(self):
        self.add += 1
        self.label_3.setText(f"더하거나 감소되는 양 : {self.add}")
    def funcx2(self):
        self.number = self.number * 2
        self.label.setText(f"카운트된 숫자 : {self.number}")
    def funcn2(self):
        self.number = self.number // 2
        self.label.setText(f"카운트된 숫자 : {self.number}")

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
