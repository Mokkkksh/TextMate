from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPlainTextEdit, QPushButton, QComboBox, QFileDialog, QDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import backEnd
import sys
from errorDialog import Ui_errorDialog
from saveDialog import Ui_saveDialog

#Defining the UI Class
class ocrUI(QMainWindow):

    def __init__(self):
        super(ocrUI, self).__init__()

        #Loading the GUI File
        uic.loadUi('ui/ocrWindow.ui', self)


        #Defining Widgets
        self.imageLabel = self.findChild(QLabel, 'imageLabel')
        self.outputTextEdit = self.findChild(QPlainTextEdit, 'outputTextEdit')

        self.inputPathButton = self.findChild(QPushButton, 'inputPathButton')
        self.processButton = self.findChild(QPushButton, 'processButton')
        self.saveButton = self.findChild(QPushButton, 'saveButton')
        self.analyseButton = self.findChild(QPushButton, 'analyseButton')
        self.ttsButton = self.findChild(QPushButton, 'ttsButton')
        self.generateWordCloudButton = self.findChild(QPushButton, 'generateWordCloudButton')

        self.languageComboBox = self.findChild(QComboBox, 'languageComboBox')  


        #Button Functions
        self.inputPathButton.clicked.connect(self.inputPathButtonClicked)
        self.processButton.clicked.connect(self.processButtonClicked)
        self.languageComboBox.addItems(backEnd.languageCodeDictionary.keys())
        self.saveButton.clicked.connect(self.saveButtonClicked)
        self.ttsButton.clicked.connect(self.ttsButtonClicked)
        self.analyseButton.clicked.connect(self.analyseButtonClicked)
        self.generateWordCloudButton.clicked.connect(self.generateWordCloudButtonClicked)
        #Showing the window
        self.show()

    #Defining Button Functions
    def inputPathButtonClicked(self):
        #Grab image path
        backEnd.inputPath = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image Files (*.png *.jpg *.bmp)')[0]
        print(backEnd.inputPath)
        #Display image
        self.imagePixmap = QPixmap(backEnd.inputPath)
        self.imageLabel.setPixmap(self.imagePixmap)
        #Set inputPathEntered to True
        backEnd.inputPathEntered = True

    def processButtonClicked(self):
        if backEnd.inputPathEntered == True:
            backEnd.processImage(backEnd.languageCodeDictionary[self.languageComboBox.currentText()])
            self.outputTextEdit.setPlainText(backEnd.outputText)
        else:
            print('No input path entered')
            self.inputErrorDialog = QDialog()
            self.ui = Ui_errorDialog()
            self.ui.setupUi(self.inputErrorDialog)
            self.inputErrorDialog.show()

    def saveButtonClicked(self):
        backEnd.outputText = self.outputTextEdit.toPlainText()
        backEnd.outputPath = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt)')[0]
        if backEnd.outputPath != '':
            backEnd.saveFile()
            self.saveSuccessDialog = QDialog()
            self.ui = Ui_saveDialog()
            self.ui.setupUi(self.saveSuccessDialog)
            self.saveSuccessDialog.show()

    def ttsButtonClicked(self):
        backEnd.outputText = self.outputTextEdit.toPlainText()
        if backEnd.outputText != '':
            backEnd.textToSpeech(backEnd.languageCodeDictionary[self.languageComboBox.currentText()])


    def analyseButtonClicked(self):
        backEnd.outputText = self.outputTextEdit.toPlainText()
        print(backEnd.outputText)
        if backEnd.outputText != '':
            backEnd.analyseText(self.languageComboBox.currentText())

    def generateWordCloudButtonClicked(self):
        backEnd.outputText = self.outputTextEdit.toPlainText()
        if backEnd.outputText != '':
            backEnd.generateWordCloud(self.languageComboBox.currentText())

app = QApplication(sys.argv)
UIWindow = ocrUI()
app.exec()