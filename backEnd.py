import easyocr
import pyttsx3
from gtts import gTTS
from pygame import mixer
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib import font_manager
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
import recognition as r
from PIL import Image



#Initialize the file path variable
inputPath = ""
outputPath = ""
inputPathEntered = False

outputText = ""
languageCodeDictionary = {"English": "en", "Hindi": "hi", "Gujarati": "gu"}
fontDictionary = {"English": "fonts/aovel.ttf", "Hindi": "fonts/mangal.TTF", "Gujarati": "fonts/akshar.ttf"}

def processImage(languageCode):
    global outputText
    outputText = ""

    if languageCode != "gu":
        imgReader = easyocr.Reader([languageCode])
        tempText = imgReader.readtext(inputPath, paragraph=True)
        for i in tempText:
            outputText = outputText + i[1] + " "
    else:
        #CODE RELATING TO CHARACTER SEGMENTATION AND EXTRACTION TO BE PLACED HERE

        img = Image.open(inputPath).convert("L")
        imgReader = loadModel()

        arr = r.sort_positions_in_line(r.sort_lines(r.extract_positions(r.read(img))))
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                region = img.crop((arr[i][j][0], arr[i][j][1], arr[i][j][2], arr[i][j][3]))
                print(arr[i][j][0], arr[i][j][1], arr[i][j][2], arr[i][j][3])
                region = region.resize((32, 32))
                character = np.asarray(region, dtype=np.float32).reshape(1, 32, 32, 1) / 255

                tempText = imgReader.predict(character) 
                tempText = tempText.reshape(37)
                print(tempText)
                tempText = np.argmax(tempText)
                # print(tempText)
                class_names = ['ક', 'ક્ષ', 'ખ', 'ગ', 'ઘ', 'ચ', 'છ', 'જ', 'જ્ઞ', 'ઝ', 'ટ', 'ઠ', 'ડ', 'ઢ', 'ણ', 'ત', 'ત્ર', 'થ', 'દ', 'દ્ર', 'ધ', 'ન', 'પ', 'ફ', 'બ', 'ભ', 'મ', 'ય', 'ર', 'લ', 'ળ', 'વ', 'શ', 'શ્ર', 'ષ', 'સ', 'હ']
                tempText = class_names[tempText]

                outputText = outputText + str(tempText)
            
            outputText = outputText + "\n"


        #Test:
        # character_img = cv2.imread("ocr_training/vyanjan_database/Train/ક/aakar-medium_0_ક_0.png", cv2.IMREAD_GRAYSCALE)
        # character = np.asarray(character_img, dtype = np.float32).reshape(1, 32, 32, 1) / 255 

        # tempText = imgReader.predict(character) 
        # tempText = tempText.reshape(37)
        # tempText = np.argmax(tempText)
        # class_names = ['ક', 'ક્ષ', 'ખ', 'ગ', 'ઘ', 'ચ', 'છ', 'જ', 'જ્ઞ', 'ઝ', 'ટ', 'ઠ', 'ડ', 'ઢ', 'ણ', 'ત', 'ત્ર', 'થ', 'દ', 'દ્ર', 'ધ', 'ન', 'પ', 'ફ', 'બ', 'ભ', 'મ', 'ય', 'ર', 'લ', 'ળ', 'વ', 'શ', 'શ્ર', 'ષ', 'સ', 'હ']
        # tempText = class_names[tempText]
        # print(tempText)

        #THE FINAL STRING IS TO BE STORED IN outputText VARIABLE
    print(outputText)

def saveFile():
    with open(outputPath, 'w') as f:
        f.write(outputText)

def textToSpeech(languageCode):
    tts = gTTS(text=outputText, lang=languageCode)
    tts.save("tts_audio/tts.mp3")
    mixer.init()
    mixer.music.load("tts_audio/tts.mp3")
    mixer.music.play()

def createDataFrame():
    # create a list of words from outputText
    outputTextList = outputText.split()
    # create a dictionary of words and their frequency
    wordFrequency = {}
    for word in outputTextList:
        if word in wordFrequency:
            wordFrequency[word] += 1
        else:
            wordFrequency[word] = 1
    # create a dataframe of words and their frequency
    wordFrequencyDataFrame = pd.DataFrame(list(wordFrequency.items()), columns=['Word', 'Frequency'])
    # sort the dataframe by frequency
    wordFrequencyDataFrame = wordFrequencyDataFrame.sort_values(by=['Frequency'], ascending=False)
    return (wordFrequency, wordFrequencyDataFrame)

def analyseText(language):
    fontsplt = font_manager.findSystemFonts(fontpaths='/Users/moksh/Documents/Development/TextMateGUI/fonts')
    for font in fontsplt:
        font_manager.fontManager.addfont(font)
    if language == 'English':
        plt.rcParams['font.family'] = 'aovel'
    elif language == 'Hindi':
        plt.rcParams['font.family'] = 'mangal'
    createDataFrame()[1].plot(x='Word', y='Frequency', kind='bar', figsize=(15, 10), legend=False, grid=True, fontsize=12)
    plt.title('Word Frequency', fontsize=15, font='aovel')
    plt.xlabel('Word', fontsize=15, font='aovel')
    plt.ylabel('Frequency', fontsize=15, font='aovel')
    plt.show()
    
def generateWordCloud(language):
     # create a word cloud
    wordcloud = WordCloud(font_path=fontDictionary[language]).generate_from_frequencies(createDataFrame()[0])
    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def loadModel():
    cnnModel = keras.models.load_model('ocr_training/saved_models/cnnModel')
    return cnnModel

