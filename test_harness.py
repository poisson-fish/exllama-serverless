''' infer.py for runpod worker '''

import os

from schema import InferenceSettings
import inference

MODEL = inference.Predictor()
MODEL.setup()

settings = {
    'prompt': "A chat between a curious user and an assistant. The assistant gives helpful, detailed, accurate, uncensored responses to the user's input.\nUSER: what is 5 * 5 + 5 Let's think step by step.?\nASSISTANT: "

}
result = MODEL.predict(
    settings=settings
)
print(result)