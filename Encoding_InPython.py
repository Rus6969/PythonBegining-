# im[orting encoding library
import sys
sys.getdefaultencoding()
#The ord() function in Python is used to convert a single Unicode character to its integer equivalent.
# The function accepts any single string character and returns an integer.
print(ord('a'))
print(chr(97))


s = "hello"
enc_ascii=s.encode('ascii')
enc_utf8=s.encode('utf8')
enc_utf16=s.encode('utf16')


print(type(enc_ascii))
print(type(enc_utf8))
print(type(enc_utf16))


print(len(enc_ascii))
print(len(enc_utf8))
print(len(enc_utf16))