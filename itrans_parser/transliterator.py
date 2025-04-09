from .mappings import MAPPINGS

class Transliterator:
    def __init__(self, script='Devanagari'):
        if script not in MAPPINGS:
            raise ValueError(f"Unsupported script: {script}")
        self.script = script
        self.mapping = MAPPINGS[script]
        # Precompute sorted keys for longest match first
        self.sorted_keys = sorted(self.mapping.keys(), key=len, reverse=True)

    def tokenize(self, text):
        """
        Tokenize the input ITRANS text into a list of tokens.
        Longest match first greedy approach.
        """
        tokens = []
        i = 0
        while i < len(text):
            match = None
            for key in self.sorted_keys:
                if text.startswith(key, i):
                    match = key
                    break
            if match:
                tokens.append(match)
                i += len(match)
            else:
                tokens.append(text[i])
                i += 1
        return tokens

    def transliterate(self, text):
        """
        Convert ITRANS ASCII text to Unicode string in the target script.
        """
        tokens = self.tokenize(text)
        output = []
        for token in tokens:
            unicode_char = self.mapping.get(token, token)
            output.append(unicode_char)
        return ''.join(output)