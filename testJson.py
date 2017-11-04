import json
r = open('NASDAQ_MSFT.json', 'r')
line = json.load(r)
# r.readline()
# line = r.readline()
print(line)