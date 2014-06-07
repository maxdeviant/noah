import json
import random
import pprint

class Noah(object):
    def __init__(self, dictionary_file):
        self.dictionary = json.load(dictionary_file)

    def list(self):
        return '\n'.join([entry['word'] for entry in self.dictionary])

    def define(self, word):
        return self.output(filter(lambda x: x['word'] == word, self.dictionary))

    def random(self):
        return self.output(random.choice(self.dictionary))

    def output(self, data):
        return json.dumps(data, indent=4)

def main():
    with open('../dictionaries/english.json') as dictionary:
        n = Noah(dictionary)

    print n.list()
    print n.define('run')
    print n.random()

if __name__ == '__main__':
    main()