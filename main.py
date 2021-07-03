import sys

#PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout 
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel

# class Login(QDialog):

#     def __init__(self, parent = None):

#         super().__init__(parent)
#         self.setWindowTitle('Login/SignIn')
#         dlgLayout  = QVBoxLayout()
#         formLayout = QFormLayout()

#         formLayout.addRow('Username: ', QLineEdit)
#         formLayout.addRow('Passowrd: ', QLineEdit)

#         dlgLayout.addLayout(formLayout)

#         btns = QDialogButtonBox()
#         btns.setStandardButtons(
#             QDialogButtonBox.Cancel | QDialogButtonBox.Ok
#         )


class Dialog(QDialog):


    def __init__(self, parent = None):
        #"__Initializer__"
        super().__init__(parent)
        self.setWindowTitle('LogIn')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()

        formLayout.addRow('Username: ', QLineEdit())
        formLayout.addRow('Password: ', QLineEdit())
        # formLayout.addRow('Name:     ', QLineEdit())
        # formLayout.addRow('Mob.Num:  ', QLineEdit())
        # formLayout.addRow('DOB:      ', QLineEdit())
        
        dlgLayout.addLayout(formLayout)
        
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok
        )
        dlgLayout.addWidget(btns)
        

        self.setLayout(dlgLayout)

        

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())