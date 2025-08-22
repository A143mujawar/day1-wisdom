class Day8: 
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        return " ".join(words[::-1])

sol = Day8() 
input_str = "  the   sky   is blue  "
print("Reversed:", '"' + sol.reverseWords(input_str) + '"')
