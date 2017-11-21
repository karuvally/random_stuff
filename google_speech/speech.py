#!/usr/bin/env python3
# Speech recognition experiment (alpha release)
# Kaavilamme Sakthi tharoo!

# import some serious stuff
import sys
import speech_recognition as speech
from PyQt5.QtWidgets import (QApplication, QPushButton, QLineEdit,
    QMainWindow)


# set up the main window
class MainWindow(QMainWindow):
    # call some weird constructors
    def __init__(self):
        super().__init__()
        self.initUI()
    
    
    # function to recognize audio
    def recognize_audio(self):
        recognize = speech.Recognizer()
        
        # this is where actual listening takes place
        with speech.Microphone() as source:
            self.statusBar().showMessage('listening...')
            audio = recognize.listen(source)
            
        self.statusBar().showMessage('recognizing...')
        speech_string =  recognize.recognize_google(audio)
        self.statusBar().showMessage(speech_string)
        
    
    # define the window
    def initUI(self):
        button = QPushButton('Listen', self)
        button.resize(button.sizeHint())
        button.move(108, 95)
        button.clicked.connect(self.recognize_audio)
        
        self.statusBar()
        
        self.resize(300, 220)
        self.setWindowTitle('Speech')
        self.statusBar().showMessage('Speech, alpha release')
        self.show()
        

# create application and window object
application = QApplication(sys.argv)
windowObject = MainWindow()
sys.exit(application.exec_())
