import torch
from config import model_path
from vllm import LLM, SamplingParams

class Predictor:
    def setup(self):
        # Model moved to network storage  
        print("Loading model...")
        self.llm = LLM(trust_remote_code = True, model=model_path, gpu_memory_utilization=1.0, quantization='awq', dtype="float16")
        self.sampling_params = SamplingParams(temperature=0.4, top_p=0.95)    

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
