import os
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

        # If the word is a noun
        if pos == 'N':
            plurals = ''

            # Check for plurals
            if len(split) > 0:
                plurals = split.pop(0)

            # Add word to dictionary
            dictionary.append({
                'word': word,
                'plurals': plurals,
                'part_of_speech': pos,
                'dump': split[0:len(split)]
            })
        # If the word is a verb
        elif pos == 'V':
            verbs = []

            # Check for verb forms
            if len(split) > 2:
                for v in split[:]:
                    i = split.index(v)
                    if not '(' in split[i]:
                        verbs.append(split.pop(i))

                # Add word to dictionary
                dictionary.append({
                    'word': word,
                    'verb_forms': {
                        'past': verbs[0],
                        'present': verbs[1],
                        'plural': verbs[2]
                    },
                    'part_of_speech': pos,
                    'dump': split[0:len(split)]
                })
            else:
                # Add word to dictionary
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
        elif pos == 'A':
            forms = []

            if len(split) > 1:
                for a in split[:]:
                    i = split.index(a)
                    forms.append(split.pop(i))

                # Add word to dictionary
                dictionary.append({
                    'word': word,
                    'forms': {
                        'comparative': forms[0],
                        'superlative': forms[1]
                    },
                    'part_of_speech': pos,
                    'dump': split[0:len(split)]
                })
            else:
                # Add word to dictionary
                dictionary.append({
                    'word': word,
                    'forms': {
                        'comparative': '',
                        'superlative': ''
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

output_dir = '../dictionaries/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(os.path.join(output_dir, 'english.json'), 'w') as output:
    json.dump(dictionary, output, indent=4, separators=(',', ': '))