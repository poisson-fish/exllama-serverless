import torch
from config import repo_name, model_name
from huggingface_hub import snapshot_download
import logging, os, glob
from vllm import LLM, SamplingParams
from schema import InferenceSettings

class Predictor:
    def setup(self):
        # Model moved to network storage
        model_directory = f"/runpod-volume/{model_name}"  
        # model_directory = f"./models/{model_name}"
        print("Loading model...")
        self.llm = LLM(model=model_directory, gpu_memory_utilization=0.7, quantization='awq')
        self.sampling_params = SamplingParams(temperature=0.8, top_p=0.95)    

    def predict(self, settings):
        self.sampling_params = SamplingParams(temperature=settings["temperature"], 
                                              top_p=settings["top_p"],
                                              top_k=settings["top_k"],
                                              early_stopping=settings["early_stopping"],
                                              n=settings["n"],
                                              best_of=settings["best_of"],
                                              presence_penalty=settings["presence_penalty"],
                                              frequency_penalty=settings["frequency_penalty"],
                                              use_beam_search=settings["use_beam_search"],
                                              length_penalty=settings["length_penalty"],
                                              stop=settings["stop"],
                                              ignore_eos=settings["ignore_eos"],
                                              max_tokens=settings["max_tokens"]
                                              ) 
        return self.generate_to_eos(settings["prompt"])
    
    def generate_to_eos(self, prompt):
        return self.llm.generate(prompt, self.sampling_params)[0].outputs[0].text
