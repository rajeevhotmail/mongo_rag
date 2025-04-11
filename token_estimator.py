import tiktoken

class TokenEstimator:
    def __init__(self, model_name="gpt-3.5-turbo"):
        try:
            self.encoding = tiktoken.encoding_for_model(model_name)
        except KeyError:
            # Fall back to a default encoding if model name is not recognized
            self.encoding = tiktoken.get_encoding("cl100k_base")

    def estimate(self, text: str) -> int:
        """
        Estimate the number of tokens for a single string.
        """
        return len(self.encoding.encode(text))

    def estimate_list(self, texts: list[str]) -> int:
        """
        Estimate the total number of tokens for a list of strings.
        """
        return sum(self.estimate(text) for text in texts)