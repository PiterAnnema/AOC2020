import re

pattern = re.compile(r'^(\d*)-(\d*) (.): ([a-z]*)$')
with open('data/day2.txt') as f:
    count1 = 0
    count2 = 0
    for line in f:
        a, b, ch, pw = pattern.search(line).groups()
        a = int(a)
        b = int(b)
        count1 += a <= sum(map(lambda c: c == ch, pw)) <= b
        count2 += b <= len(pw) and (pw[a-1] == ch) != (pw[b-1] == ch)


print(count1)
print(count2)