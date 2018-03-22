import re
from collections import Counter

text = "hello,Crise! How are you? It's nice day I'm very happy to meet you!"

text = text.lower()
result = re.findall('[a-zA-Z]', text)
count = Counter(result)
print(count)
count_list = list(count.values())
#print(count_list)
max_value = max(count_list)
max_list = []
for k, v in count.items():
    if v == max_value:
        max_list.append(k)
    max_list = sorted(max_list)
print(max_list)
