def lengthofLongestsubstring(s):
    if not s:
        return 0

    max_length = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i,len(s)):
            if s[j] in seen:
                length = j - i
                max_length = max(max_length, length)
                break
            else:
                seen.add(s[j])
        else:
            length = j - i +1
            max_length = max(max_length, length)
    return max_length
s="pwwkew"
print(lengthofLongestsubstring(s))