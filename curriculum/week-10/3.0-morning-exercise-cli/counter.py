import re
import sys
regex = re.compile('[^a-zA-Z]')
out = dict()
for line in sys.stdin:
    line = line.split(" ")
    line = filter(lambda item: regex.sub('', item), line)
    for word in line:
        word = word.lower()
        word = regex.sub('', word)
        if word in out.keys():
            out[word] +=1
        else:
            out[word] = 1

for key in sorted(out):
    print "%s: %s" % (key, out[key])