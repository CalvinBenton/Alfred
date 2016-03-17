import re
num = [int(s) for s in re.findall(r'\b\d+\b', '10:41')]
print num