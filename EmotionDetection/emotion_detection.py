import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    
    if response.status_code == 400:
        # Return a dictionary with None for all keys in case of 400 status code
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
    
    formatted_response = json.loads(response.text)
    predictions = formatted_response.get('emotionPredictions', [])
    
    if not predictions:
        raise ValueError("No emotion predictions returned by the API.")
    
    emotions = predictions[0].get('emotion', {})
    if not emotions:
        raise ValueError("No emotion scores found in the prediction.")
    
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }
