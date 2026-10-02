class Solution(object):
    def frequencySort(self, s):
        if len(s) <= 1:
            return s
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        x = ""
        while freq:
            max_key = max(freq, key=freq.get)
            if freq[max_key] == 0:
                return x
            while freq[max_key]:
                x += max_key
                freq[max_key] -= 1
            del freq[max_key]
        return x


        