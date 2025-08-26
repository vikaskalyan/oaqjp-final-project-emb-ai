# import requests
# import json

# def emotion_detector(text_to_analyse):

#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

#     header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

#     myobj = { "raw_document": { "text": text_to_analyse } }

#     response = requests.post(url, headers=header, json=myobj)

#     response_dict = json.loads(response.text)

#     emotions = response_dict['emotionPredictions'][0]['emotion']

#     anger = emotions['anger']
#     disgust = emotions['disgust']
#     fear = emotions['fear']
#     joy = emotions['joy']
#     sadness = emotions['sadness']

#     dominant_emotion = max(emotions, key=emotions.get)

#     return {
#         'anger': anger,
#         'disgust': disgust,
#         'fear': fear,
#         'joy': joy,
#         'sadness': sadness,
#         'dominant_emotion': dominant_emotion
#     }


import requests
import json

def emotion_detector(text_to_analyse):

    # Handle blank input
    if not text_to_analyse:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, headers=header, json=myobj)

    # Handle server error or bad request
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_dict = json.loads(response.text)

    # Handle missing 'emotionPredictions' key
    if 'emotionPredictions' not in response_dict or not response_dict['emotionPredictions']:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotions = response_dict['emotionPredictions'][0]['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
