import re

#checks if a word is in a sentence, prints it out and replace it with another word
'''word=r'cow'
text='Your life is more intresting'

match=re.search(word, text)
print(match)

new_text=re.sub(word, 'farm', text)

print(new_text)
'''
def is_valid_email(emails):
    pattern=r'^[a-zA-Z0-9+%_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, emails) is not None

#max_emails=5
emails=input('Enter an email address: ')
#separator=r'/'
#email=re.split(separator, emails)

#if len(email)<max_emails:
if is_valid_email(emails):
    print(f'{emails} email address is valid.')
else:
    print(f'{emails} email address is not valid')
#else:
 #   print('The emails exceeded the maximum number!')


'''
re.search(pattern, string): Searches the string for the first occurrence of the pattern and returns a match object if found.

re.match(pattern, string): Matches the pattern at the beginning of the string and returns a match object if found.

re.findall(pattern, string): Returns a list of all non-overlapping matches of the pattern in the string.

re.sub(pattern, repl, string): Replaces all occurrences of the pattern in the string with the replacement string repl.

re.split(pattern, string): Splits the string into a list of substrings using the pattern as a delimiter.

re.compile(pattern): Compiles the pattern into a regular expression object, which can be used to perform multiple searches on different strings.

re.escape(string): Escapes special characters in the string so that they can be used as literal characters in a regular expression.

re.fullmatch(pattern, string): Matches the entire string against the pattern and returns a match object if the string matches the pattern.

re.finditer(pattern, string): Returns an iterator over all non-overlapping matches of the pattern in the string.
'''