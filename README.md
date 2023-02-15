# TextMate

Launch ocrWindow.py to launch the app <br/>
OCR ML Model is trained in ocr_training/ocrModel.py <br/>
Model is saved in ocr_training/saved_models <br/>
Access model from loadModel() function in backEnd.py

Purpose:
The purpose of this code is to perform Optical Character Recognition (OCR) on an image and extract the text from it. It then provides additional functionalities like saving the text to a file, converting the text to speech, and analyzing the text to generate word frequency charts and word clouds.

Libraries and Tools Used:
easyocr - a python package for performing OCR on images<br/>
pyttsx3 - a python package for converting text to speech<br/>
gtts - a python package for creating audio files from text<br/>
pygame - a python package for playing audio files<br/>
pandas - a python package for data manipulation and analysis<br/>
matplotlib - a python package for visualization<br/>
wordcloud - a python package for creating word clouds<br/>
tensorflow - a python package for machine learning<br/>
opencv - a python package for computer vision<br/>
Functions:
processImage(languageCode) - This function performs OCR on the image provided in the inputPath variable and extracts text from it. The language of the image is determined by the languageCode parameter. If the language is Gujarati, the function includes additional code for character segmentation and extraction. The final extracted text is stored in the outputText variable.
<br/>
saveFile() - This function saves the outputText variable to a file at the path specified in the outputPath variable.<br/>
textToSpeech(languageCode) - This function converts the outputText variable to speech in the language specified by the languageCode parameter, and saves it to an audio file in the tts_audio directory. The audio file is then played using the pygame package.
<br/>
createDataFrame() - This function creates a Pandas dataframe of the words and their frequency in the outputText variable. It returns a tuple containing both a dictionary of the word frequency and the Pandas dataframe.
<br/>
analyseText(language) - This function generates a word frequency chart for the words in the outputText variable. The chart is displayed using the matplotlib package. The language parameter is used to determine the font for the chart.
<br/>
generateWordCloud(language) - This function generates a word cloud for the words in the outputText variable. The cloud is displayed using the matplotlib package. The language parameter is used to determine the font for the cloud.
<br/>loadModel() - This function loads the saved machine learning model for character recognition for the Gujarati language.
<br/>Variables:
inputPath - This variable stores the path to the input image for OCR.<br/>
outputPath - This variable stores the path to the output file for the extracted text.<br/>
inputPathEntered - This variable is used to determine if a valid input path has been entered.<br/>
outputText - This variable stores the extracted text from the OCR process.<br/>
languageCodeDictionary - This dictionary maps language names to their respective language codes used by the OCR package.<br/>
fontDictionary - This dictionary maps language names to their respective font files for creating visualizations.<br/>
