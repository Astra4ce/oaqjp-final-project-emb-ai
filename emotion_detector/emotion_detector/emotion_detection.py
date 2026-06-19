import requests
import json

def run_emotion_detector(text_to_analyze): 
    
    # returns text attribute of response object
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = { "grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock" }

    payload = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=payload)
    status_code = response.status_code

    if status_code == 400:
        return {
            "anger": "None",
            "disgust": "None",
            "fear": "None",
            "joy": "None",
            "sadness": "None",
            "dominant_emotion" : "Invalid text! Please try again!"
        }

  
    response_json = response.json()

    #print(status_code)
    emotion = response_json["emotionPredictions"][0]["emotion"]

    result = {
        "anger": emotion["anger"],
        "disgust": emotion["disgust"],
        "fear": emotion["fear"],
        "joy": emotion["joy"],
        "sadness": emotion["sadness"],
        "dominant_emotion" : max(emotion, key=emotion.get)
    }
    
    return result

# import json
# import urllib.request

# def run_emotion_detector(text_to_analyze):
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

#     headers = { "grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock" }

#     payload = { "raw_document": { "text": text_to_analyze } }

#     # Convert dict to JSON string to bytes
#     data = json.dumps(payload).encode("utf-8")

#     req = urllib.request.Request(
#         url,
#         data=data,
#         headers=headers,
#         method="POST"
#     )

#     with urllib.request.urlopen(req) as response:
#         result = json.loads(response.read().decode("utf-8"))

#     return result

# result = run_emotion_detector("I am so happy doing this.")
# print(result)
