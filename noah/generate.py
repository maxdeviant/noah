import re
import json

dictionary = []

with open('../raws/2of12id.txt') as wordlist:
    for line in wordlist:
        # Remove newline characters
        line = line.replace('\n', '')

        # Split line at spaces
        split = line.split(' ')

        # Filter out empty strings
        split = filter(None, split)

        dictionary.append({
            'word': split[0],
            'part_of_speech': split[1].replace(':', ''),
            'dump': split[2:len(split)]
        })

with open('../dictionaries/english.json', 'w') as output:
    json.dump(dictionary, output, indent=4, separators=(',', ': '))