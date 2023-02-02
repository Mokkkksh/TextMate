from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_saveDialog(object):
    def setupUi(self, saveDialog):
        saveDialog.setObjectName("saveDialog")
        saveDialog.resize(390, 150)
        saveDialog.setMinimumSize(QtCore.QSize(390, 150))
        saveDialog.setMaximumSize(QtCore.QSize(390, 150))
        self.label = QtWidgets.QLabel(saveDialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(saveDialog)
        QtCore.QMetaObject.connectSlotsByName(saveDialog)

    def retranslateUi(self, saveDialog):
        _translate = QtCore.QCoreApplication.translate
        saveDialog.setWindowTitle(_translate("saveDialog", "Success"))
        self.label.setText(_translate("saveDialog", "Saved Successfully"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    saveDialog = QtWidgets.QDialog()
    ui = Ui_saveDialog()
    ui.setupUi(saveDialog)
    saveDialog.show()
    sys.exit(app.exec_())
