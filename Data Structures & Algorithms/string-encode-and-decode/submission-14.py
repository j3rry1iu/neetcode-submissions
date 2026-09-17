class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: 
            return " "
        elif strs == [""]: 
            return ""
        joinWord = "😭".join(strs)
        return joinWord


    def decode(self, s: str) -> List[str]:
        if s == " ":
            return []
        elif s == "":
            return [""]
        return s.split("😭")

