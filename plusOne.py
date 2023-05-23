class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        new_list = []
        for i in range(len(digits) - 1, -1, -1):
            new_element = digits[i] + carry
            print(new_element)
            carry = new_element // 10
            print(carry)
            new_list.append(new_element % 10)
        if carry > 0:
            new_list.append(carry)
        return new_list[::-1]

if __name__ == "__main__":
    s1 = Solution()
    digits = [9, 9,2]
    new_list = s1.plusOne(digits)
    print(new_list)

