class Codec_unicode:
    separator = chr(257)

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """

        return self.separator.join(strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        return s.split(self.separator)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))