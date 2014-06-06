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

        word = split.pop(0)

        # Get part of speech
        pos = split.pop(0).replace(':', '')

        if pos == 'N':
            plurals = ''

            if len(split) > 0:
                plurals = split.pop(0)

            dictionary.append({
                'word': word,
                'plurals': plurals,
                'part_of_speech': pos,
                'dump': split[0:len(split)]
            })
        elif pos == 'V':
            verbs = []
            if len(split) > 2:
                for v in split[:]:
                    i = split.index(v)
                    if not '(' in split[i]:
                        verbs.append(split.pop(i))

                dictionary.append({
                    'word': word,
                    'verb_forms': {
                        'past': verbs[0] ,
                        'present': verbs[1],
                        'plural': verbs[2]
                    },
                    'part_of_speech': pos,
                    'dump': split[0:len(split)]
                })
            else:
                dictionary.append({
                    'word': word,
                    'verb_forms': {
                        'past': '' ,
                        'present': '',
                        'plural': ''
                    },
                    'part_of_speech': pos,
                    'dump': split[0:len(split)]
                })
        else:
            dictionary.append({
                'word': word,
                'part_of_speech': pos,
                'dump': split[0:len(split)]
            })

with open('../dictionaries/english.json', 'w') as output:
    json.dump(dictionary, output, indent=4, separators=(',', ': '))