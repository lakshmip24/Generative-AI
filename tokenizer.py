import re
def tokenize(text):
  return re.findall(r'\w+|[^\w\s]', text)

input_text=input("Enter a string to tokenize: ")
print(tokenize(input_text))