class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = "" 
        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                digit1 = int(num1[i])
                i -= 1
            else:
                digit0 = 0
                digit1 = 0
            if j >= 0:
                digit2 = int(num2[j])
                j -= 1
            else:
                digit2 = 0
            total = digit1 + digit2 + carry
            current_digit = total % 10
            result += str(current_digit)
            carry = total // 10
        return result[::-1]
        