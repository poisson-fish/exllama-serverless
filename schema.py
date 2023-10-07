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
        self.use_beam_search = True
        self.max_tokens = 1024
        self.presence_penalty = 0.0
        self.frequency_penalty = 0.0
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
    'n': {
        'type': int,
        'required': False,
        'default': 1
    },
    'stop': {
        'type': list,
        'required': False,
        'default': ["###"]
    },
    'ignore_eos': {
        'type': bool,
        'required': False,
        'default': False
    },
    'temperature': {
        'type': float,
        'required': False,
        'default': 1.31
    },
    'early_stopping': {
        'type': bool,
        'required': False,
        'default': True
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
    'use_beam_search': {
        'type': bool,
        'required': False,
        'default': False
    },
    'max_tokens': {
        'type': int,
        'required': False,
        'default': 1024
    },
    'presence_penalty': {
        'type': float,
        'required': False,
        'default': 0.0
    },
    'frequency_penalty': {
        'type': float,
        'required': False,
        'default': 0.0
    },
    'best_of': {
        'type': int,
        'required': False,
        'default': 1
    },
    'length_penalty': {
        'type': float,
        'required': False,
        'default': 1.0
    },
    
}
