from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_errorDialog(object):
    def setupUi(self, errorDialog):
        errorDialog.setObjectName("errorDialog")
        errorDialog.resize(390, 150)
        errorDialog.setMinimumSize(QtCore.QSize(390, 150))
        errorDialog.setMaximumSize(QtCore.QSize(390, 150))
        self.label = QtWidgets.QLabel(errorDialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(errorDialog)
        QtCore.QMetaObject.connectSlotsByName(errorDialog)

    def retranslateUi(self, errorDialog):
        _translate = QtCore.QCoreApplication.translate
        errorDialog.setWindowTitle(_translate("errorDialog", "Dialog"))
        self.label.setText(_translate("errorDialog", "Please select Image"))
