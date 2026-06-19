
import sys
import os

# Run with python3 -m tests.test_emotion_detection


sys.path.append(os.path.abspath(".."))
from emotion_detector.emotion_detection import run_emotion_detector

print(run_emotion_detector("I am glad this happened."))
print(run_emotion_detector("I am really mad about this."))
print(run_emotion_detector("I feel disgusted just hearing about this."))
print(run_emotion_detector("I am so sad about this."))
print(run_emotion_detector("I am really afraid that this will happen."))