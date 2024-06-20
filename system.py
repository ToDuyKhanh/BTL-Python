from PyQt6 import QtCore, QtGui, QtWidgets
from adminlogin import Ui_MainWindow as AdminWindow
from member import Ui_MainWindow as MemberWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create a QLabel for the background image
        self.background = QtWidgets.QLabel(parent=self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.background.setPixmap(QtGui.QPixmap("img/mau-thiet-ke-noi-that-showroom-ao-cuoi.jpg"))
        self.background.setScaledContents(True)

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 60, 400, 61))
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # Set the color and bold style for the label text
        self.label.setStyleSheet("QLabel {color: white; font-weight: bold; font-size: 35px;}")

        # Apply styles to buttons to round the corners and set bold text
        button_style = """
            QPushButton {
                border-radius: 20px;
                background-color: rgba(255, 255, 255, 200);
                font-weight: bold;
            }
            QPushButton:pressed {
                background-color: rgba(200, 200, 200, 255);
            }
        """

        self.admin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.admin.setGeometry(QtCore.QRect(110, 182, 191, 41))
        self.admin.setObjectName("admin")
        self.admin.setStyleSheet(button_style)

        self.member = QtWidgets.QPushButton(parent=self.centralwidget)
        self.member.setGeometry(QtCore.QRect(110, 280, 191, 41))
        self.member.setObjectName("member")
        self.member.setStyleSheet(button_style)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the ADMIN button click to open the admin form
        self.admin.clicked.connect(self.openAdminForm)

        # Connect the MEMBER button click to open the member login form
        self.member.clicked.connect(self.openMemberLoginForm)

        # Connect the REGISTER MEMBER button click to open the register member form
      

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main System"))
        self.label.setText(_translate("MainWindow", "Welcome to the Wedding Store"))
        self.admin.setText(_translate("MainWindow", "ADMIN"))
        self.member.setText(_translate("MainWindow", "NHÂN VIÊN"))
        

    def openAdminForm(self):
        self.adminWindow = QtWidgets.QMainWindow()
        self.ui = AdminWindow()
        self.ui.setupUi(self.adminWindow)
        self.adminWindow.show()
        MainWindow.close()
        

    def openMemberLoginForm(self):
        self.memberWindow = QtWidgets.QMainWindow()
        self.ui = MemberWindow()
        self.ui.setupUi(self.memberWindow)
        self.memberWindow.show()
        MainWindow.close()
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
