import json
import os

FILE_PATH = os.path.join("memory", "history.json")

def save_history(topic, confidence):

    os.makedirs("memory", exist_ok=True)

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)

    with open(FILE_PATH, "r") as f:
        history = json.load(f)

    history.append({
        "topic": topic,
        "confidence": round(confidence, 2)
    })

    with open(FILE_PATH, "w") as f:
        json.dump(history, f, indent=4)


def get_history():

    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        return json.load(f)