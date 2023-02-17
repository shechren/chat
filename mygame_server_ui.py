import traceback

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QTextBrowser, QApplication
import sys

class UI(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 600, 400)

        #Layout
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox_bl1 = QHBoxLayout()
        self.hbox_bl2 = QHBoxLayout()

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox_bl1)
        self.vbox.addLayout(self.hbox_bl2)

        #Widgets
        self.line = QLineEdit()
        self.view = QTextBrowser()
        self.connect = QPushButton()
        self.send = QPushButton()
        self.dice = QPushButton()
        self.draw = QPushButton()
        self.myinf = QPushButton()
        self.inf_view = QLineEdit()


        #addWidget
        self.hbox.addWidget(self.view)
        self.hbox_bl1.addWidget(self.connect)
        self.hbox_bl1.addWidget(self.line)
        self.hbox_bl1.addWidget(self.send)
        self.hbox_bl2.addWidget(self.dice)
        self.hbox_bl2.addWidget(self.draw)
        self.hbox_bl2.addWidget(self.myinf)
        self.hbox_bl2.addWidget(self.inf_view)
        self.inf_view.setDisabled(True)

        #SetLayout
        self.setLayout(self.vbox)

        #ButtonName
        self.connect.setText("연결")
        self.send.setText("전송")
        self.dice.setText("주사위")
        self.draw.setText("카드")
        self.myinf.setText("정보")
        self.view.append("이건 작동함")

        #Connection
        self.connect.clicked.connect(self.btn_server)

    def btn_server(self):
        from mygame_server import Connection
        try:
            c = Connection()
            c.start()
        except Exception as e:
            err = traceback.format_exc()
            print(e, err)

    def button_send(self):
        pass

    def view_append(self, msg):
        print(msg)
        self.view.append(msg)
        # 연결을 누르면 안녕이 뜨는데 self.view.append(msg)가 작동을 안함

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())