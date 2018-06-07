Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> key="abcdefghijklmnopqrstuvwxyz"
>>> 
>>> 
>>> def encrypt(txt,shift):
	result = ' '
	for char in txt.lower():
		result+=key[i]

		
>>>     return result
SyntaxError: unexpected indent
>>>      return result
SyntaxError: unexpected indent
>>> return result
SyntaxError: 'return' outside function
>>>          return result
SyntaxError: unexpected indent
>>> def encrypt(txt,shift):
	result = ' '
	for char in txt.lower():
		result+=key[i]
	return result
def decrypt(ct, shift):
	
SyntaxError: invalid syntax
>>> 
>>> def decrypt(ct,shift):
	result=''
	for char in ct:
		i=(key.index(char)-shift)%26
		result+=key[i]

		
>>>     return result
SyntaxError: unexpected indent
>>> def decrypt(ct,shift):
	result=''
	for char in ct:
		i=(key.index(char)-shift)%26
		result+=key[i]
	return result

>>> 
>>> txt=input("enter the string")
enter the string
>>> shift=3
>>> print("plain text is:",txt)
plain text is: 
>>> ct=encrpyt(txt,shift)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    ct=encrpyt(txt,shift)
NameError: name 'encrpyt' is not defined
>>> ct=encrypt(txt,shift)
>>> print("encrypted text is:",ct)
encrypted text is: None
>>> print("decypted text is:",decrypt(ct,shift))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print("decypted text is:",decrypt(ct,shift))
  File "<pyshell#25>", line 3, in decrypt
    for char in ct:
TypeError: 'NoneType' object is not iterable
>>> ct=decrypt(txt,shift)
>>> print("decrypted text is:",decrypt(ct,shift))
decrypted text is: 
>>> 
# python
