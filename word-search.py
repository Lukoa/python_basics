import re

def search(*args):
    pattern = r'\b{}\b'.format(args[0])
    match = re.search(pattern, ' '.join(args[1:]))
    if match is not None:
        return match.group()

word = input('Enter a word to search: ')
phrase = input('Enter the phrase: ')

print(search(word, phrase))