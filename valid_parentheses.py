class Solution:
    def isValid(self, s: str) -> bool:
        _valid_char_hash = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        openers = []
        closers = []
        for idx, char in enumerate(s):
            if char in _valid_char_hash.keys():
                #get latest opener
                openers.append(char)
            else:
                #get latest closer
                closers.append(char)
                if len(openers) == 0:
                    return False
                latest_opener = openers[-1]
                latest_closer = closers[-1]
                expected_closer = _valid_char_hash.get(latest_opener)
                if latest_closer != expected_closer:
                    return False
                else:
                    openers.pop()
                    closers.pop()

        if (len(closers) != 0) or (len(openers) != 0):
            return False

        return True