import re
def dehtml(text):
    L = re.split(r'\s+|<.*?>', text)
    return ' '.join(L)
#if __name__ == '__main__':
html_text = input()
print(dehtml(html_text))
