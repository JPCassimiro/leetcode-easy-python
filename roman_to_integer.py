class Solution:
    def romanToInt(self, s: str) -> int:
        romanTable = {
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M": 1000
        }  

        letterConversion = []
        
        idx = 0

        while (idx < len(s)):
            current_letter = s[idx]
            if idx + 1 >= len(s):
                letterConversion.append(romanTable.get(current_letter))
            elif current_letter == "I":
                if ((s[idx+1] == "V") or (s[idx+1] == "X")):
                    letterConversion.append(romanTable.get(current_letter+s[idx + 1]))
                    idx += 1
                else:
                    letterConversion.append(romanTable.get(current_letter))
            elif current_letter == "X":
                if ((s[idx+1] == "L") or (s[idx+1] == "C")):
                    letterConversion.append(romanTable.get(current_letter+s[idx + 1]))
                    idx += 1
                else:
                    letterConversion.append(romanTable.get(current_letter))
            elif current_letter == "C":
                if ((s[idx+1] == "D") or (s[idx+1] == "M")):
                    letterConversion.append(romanTable.get(current_letter+s[idx + 1]))
                    idx += 1
                else:
                    letterConversion.append(romanTable.get(current_letter))
            else:
                letterConversion.append(romanTable.get(current_letter))
            idx += 1
        
        return sum(letterConversion)