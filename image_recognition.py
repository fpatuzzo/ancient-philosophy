# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:03:57 2022

@author: Fabrizio
"""

# We install the FER() library to perform facial recognition
# This installation will also take care of any of the above dependencies if they are missing
# pip install FER

from fer import FER
import matplotlib.pyplot as plt 
%matplotlib inline
import numpy as np

#test_image_one = plt.imread("images/morto.jpg")
test_image_one = plt.imread("aprile_2022.jpg")

emo_detector = FER(mtcnn=True)
# Capture all the emotions on the image
captured_emotions = emo_detector.detect_emotions(test_image_one)
# Print all captured emotions with the image
print(captured_emotions[0]["emotions"])
emotions = np.array(list(captured_emotions[0]["emotions"].values()))
emotions2 = list(captured_emotions[0]["emotions"].keys())
main_em = emotions2[np.argmax(emotions)]
main_value = np.max(emotions)
print(main_em, type(emotions))
plt.title("%s %.2f" %(main_em, main_value))
# plt.text(200, 200, "main emotion:")
# plt.text(200, 350, "%s %.2f" %(main_em, main_value))
# plt.text(200, 350, "anger: %.2f" %captured_emotions[0]["emotions"]["angry"])
# plt.text(200, 500, "happy: %.2f" %captured_emotions[0]["emotions"]["happy"])
plt.axis('off')
plt.imshow(test_image_one)

# Use the top Emotion() function to call for the dominant emotion in the image
# dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
# print(dominant_emotion, emotion_score)