from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    
    def test_emotion_detection(self):
        # Test cases
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]
        
        # Iterate through test cases and check if the dominant emotion is as expected
        for text, expected_emotion in test_cases:
            result = emotion_detector(text)  # Call the emotion_detector method
            dominant_emotion = result['dominant_emotion']
            self.assertEqual(
                dominant_emotion, expected_emotion, 
                f"Expected '{expected_emotion}' but got '{dominant_emotion}' for text: {text}"
            )

if __name__ == '__main__':
    unittest.main()
