class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        pre = [s.replace("#", "##") for s in strs]
        pre = [s.replace(",", ",,") for s in pre]
        return "#,#".join(pre)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        k = s.split("#,#")
        k = [r.replace("##", "#") for r in k]
        return [r.replace(",,", ",") for r in k]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))