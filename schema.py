class InferenceSettings:
    def __init__(self, **kwargs):
        # Set the default values for all settings
        self.prompt = "output EOS token"
        self.n = 1
        self.stop = ['###']
        self.ignore_eos = False
        self.temperature = 1.31
        self.early_stopping = True
        self.top_p = 0.14
        self.top_k = 49
        self.max_tokens = 1024
        self.presence_penalty = 0
        self.frequency_penalty = 0
        self.best_of = 1
        self.length_penalty = 1.0

        # Overwrite the default values with any provided in kwargs
        for key, value in kwargs.items():
            # Check if the key is a valid setting name
            if hasattr(self, key):
                # Check if the value matches the expected type
                if isinstance(value, type(getattr(self, key))):
                    # Set the attribute to the value
                    setattr(self, key, value)
                else:
                    # Raise an exception if the type is wrong
                    raise TypeError(f"Expected {type(getattr(self, key))} for {key}, got {type(value)}")
            else:
                # Raise an exception if the key is invalid
                raise AttributeError(f"Invalid setting name: {key}")

INPUT_SCHEMA = {
    'prompt': {
        'type': str,
        'required': True,
    },
    'reverse_prompt': {
        'type': list,
        'required': False,
        'default': ["###"]
    },
    'temperature': {
        'type': float,
        'required': False,
        'default': 1.31
    },
    'top_p': {
        'type': float,
        'required': False,
        'default': 0.14
    },
    'top_k': {
        'type': int,
        'required': False,
        'default': 49
    },
    'typical_p': {
        'type': float,
        'required': False,
        'default': 1.0
    },
    'max_new_tokens': {
        'type': int,
        'required': False,
        'default': 1024
    },
    'token_repetition_penalty': {
        'type': float,
        'required': False,
        'default': 1.17
    },
    'tail_free_sampling': {
        'type': float,
        'required': False,
        'default': 1.0
    },
    'num_beams': {
        'type': int,
        'required': False,
        'default': 1
    },
    'length_penalty': {
        'type': float,
        'required': False,
        'default': 1.0
    }
}
