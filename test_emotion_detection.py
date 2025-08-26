from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):

        # Test joy
        def test_joy(self):
            result = emotion_detector("I am glad this happened")
            self.assertEqual(result['dominant_emotion'], 'joy')

        # Test anger
        def test_anger(self):
            result = emotion_detector('I am really mad about this')
            self.assertEqual(result['dominant_emotion'], 'anger')

        # Disgust
        def test_disgust(self):
            result = emotion_detector('I feel disgusted just hearing about this')
            self.assertEqual(result['dominant_emotion'], 'disgust')

        # Sadness
        def test_sadness(self):
            result = emotion_detector('I am so sad about this')
            self.assertEqual(result['dominant_emotion'], 'sadness')

        # Fear
        def test_fear(self):
            result = emotion_detector('I am really afraid that this will happen')
            self.assertEqual(result['dominant_emotion'], 'fear') 


if __name__ == '__main__':
    unittest.main()