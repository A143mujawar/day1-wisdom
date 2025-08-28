def atMostK(s, k):
    freq = {}
    i = 0
    ans = 0

    for j in range(len(s)):
        freq[s[j]] = freq.get(s[j], 0) + 1

        while len(freq) > k:
            freq[s[i]] -= 1
            if freq[s[i]] == 0:
                del freq[s[i]]
            i += 1

        ans += j - i + 1
    return ans

def countSub(s, k):
    return atMostK(s, k) - atMostK(s, k - 1)


s = "pqpqs"
k = 2
print(countSub(s, k))
