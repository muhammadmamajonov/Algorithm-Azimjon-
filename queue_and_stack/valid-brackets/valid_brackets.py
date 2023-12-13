"""
Berilgan qavslar to'g'ri yopilganligini tekshirish.
Qavslar - (), {}, [].
Misol uchun:
    valid_brackets("()()") = True
    valid_brackets("{()[]}") = True
    valid_brackets("{(]}") = False
"""

def valid_brackets(s: str) -> bool:

    stack = []
    brackets = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    for char in s:
        if char not in brackets: # yangi qavs ochyapti
            stack.append(char)
            continue

        if not stack:
            return False
        
        last_opened = stack.pop()
        if last_opened != brackets[char]:
            return False
        
    return not stack