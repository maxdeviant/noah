import json
import random
import pprint

class Noah(object):
    def __init__(self, dictionary_file):
        self.dictionary = json.load(dictionary_file)

    def list(self):
        return [entry['word'] for entry in self.dictionary]

    def list_filter(self, query):
        return filter(lambda x: x['word'].startswith(query), self.dictionary)

    def define(self, word):
        return filter(lambda x: x['word'] == word, self.dictionary)

    def random(self):
        return random.choice(self.dictionary)