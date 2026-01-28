class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in mapping.values():  # opening bracket
                stack.append(ch)
            else:  # closing bracket
                if not stack or stack.pop() != mapping[ch]:
                    return False

        return not stack
