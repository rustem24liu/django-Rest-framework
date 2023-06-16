import re

s=input()
match = re.match(r'(\b(\w+)\w*\b)(,?\2\w*)+$', s)
print(match.group(2) if match else '')