''' infer.py for runpod worker '''

import os

from schema import InferenceSettings
import inference

MODEL = inference.Predictor()
MODEL.setup()

settings = {
    "temperature": 1.31,
    "top_p": 0.14,
    "top_k": 49,
    "early_stopping": False,
    "n": 1,
    "best_of": 1,
    "presence_penalty": 0.0,
    "frequency_penalty": 0.0,
    "use_beam_search": False,
    "length_penalty": 1.0,
    "stop": ['<|im_end|>'],
    "ignore_eos": False,
    "max_tokens": 1024,
    "prompt": "<|im_start|>system\nyou are an expert dolphin trainer<|im_end|>\n<|im_start|>user\nWhat is the best way to train a dolphin to obey me?  Please answer step by step.<|im_end|>\n<|im_start|>assistant"
}

result = MODEL.predict(
    settings=settings
)
print(result)