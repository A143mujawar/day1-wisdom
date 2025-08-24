from collections import defaultdict

def Day10(strs):
    anagrams = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        anagrams[tuple(count)].append(word)
    return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Day10(strs))
