class Solution:

    def isValid(self, s: str) -> bool:

        pairs = {')': '(', ']': '[', '}': '{'}
        stk = []

        if len(s) % 2 != 0:
            return False

        for ch in s:

            if ch in '({[':
                stk.append(ch)

            elif ch in pairs:

                if not stk or stk[-1] != pairs[ch]:
                    return False

                stk.pop()

            else:
                return False

        return not stk