#!/usr/bin/python3
listt = [chr(i) for i in range(97, 123) if chr(i) not in ['q', 'e']]
alphabet_string = ''.join(listt)
print(alphabet_string,end='')
