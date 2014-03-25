import string
from collections import defaultdict
from nltk.corpus import stopwords

text = """
The fear of the pending ritual is more memorable than the pain inflicted during it. Thirty-five years ago, inside a high school football locker room, I was a 14-year-old stripped down to a jock strap preparing to crawl on hands and knees through a gantlet of upperclassmen fixing to strike my backside with the cleats and wet, coiled-up towels in their hands.

This was freshman orientation, minus the faculty lectures, and I can still picture the eager looks on the seniors' faces as they waited for the next man (or boy) up. It was a frightening scene for a 140-pounder about to be hazed by much bigger, older teammates, but at the other end of that procession waited a shower to cool your wounds and, more important, full acceptance into the club.
"""

# extract out extras
extras = ['!','.',',',':',';','\n']
for c in extras:
    if c == '\n':
        text = text.replace(c,' ')
    else:
        text = text.replace(c,'')

# new array
text_array = text.split(' ')
print "Array size: " + str(len(text_array))

#noise = ['the','in','are','we','i','can','in','and','his','their',
#         'of','one','he','was','which','is','at','to','on','by','1',
#         '','a','as','two','him','has','that','get','it','had','gone',
#         'when']

noise = set(stopwords.words('english'))

f = open("stopwords.txt", "w")
[f.write(n+'|') for n in noise]
f.close()

filtered_array = []
freq_array = defaultdict(int)

for data in text_array:
    data = data.lower()
    if data not in noise:
        filtered_array.append(data)
        freq_array[data] += 1


print "Filtered array size: " + str(len(filtered_array))

sorted(freq_array.iteritems(),key=lambda (k,v): v,reverse=True)
#print filtered_array
#print freq_array
#print text

for k,v in freq_array.iteritems():
    print "%s - %s" % (str(k), str(v))
