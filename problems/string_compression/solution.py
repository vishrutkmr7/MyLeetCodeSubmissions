class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) < 2:
            return len(chars)
        c, n, k = chars[0], 1, 0  # char, number of char, index
        for i in range(1, len(chars)):
            if chars[i] == c:
                n += 1
            else:
                s = [c] + list(str(n)) if n > 1 else [c]
                chars[k : k + len(s)] = s
                k += len(s)
                c, n = chars[i], 1
        s = [c] + list(str(n)) if n > 1 else [c]
        chars[k : k + len(s)] = s
        k += len(s)
        return k