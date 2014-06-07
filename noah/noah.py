import json

class Noah(object):
    def __init__(self, dictionary_file):
        self.dictionary = json.load(dictionary_file)

    def list(self):
        return '\n'.join([entry['word'] for entry in self.dictionary])

    def define(self, word):
        entry = next((x for x in self.dictionary if x['word'] == word), None)

        if not entry is None:
            return '%s (%s)' % (entry['word'], entry['part_of_speech'])

def main():
    with open('../dictionaries/english.json') as dictionary:
        n = Noah(dictionary)

    print n.list()
    print n.define('aardvark')

if __name__ == '__main__':
    main()