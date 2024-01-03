class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # defining the length of the input strings
        result = ""
        acount = len(a)-1
        bcount = len(b)-1
        carry = 0

        while acount>=0 or bcount>=0:
            totalSum = carry
            if acount>=0:
                totalSum += int(a[acount])
                acount -= 1
            if bcount>=0:
                totalSum += int(b[bcount])
                bcount -= 1
            result = str(totalSum%2) + result 
            carry = totalSum//2
        if carry > 0:
            result = str(1) + result
        return result 