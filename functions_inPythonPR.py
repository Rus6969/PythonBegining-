def greeting():
    '''
    Doc String info about this function 
    '''
    
    print("Hello")





greeting()
#help(greeting)


def find_sum(x,y):
    return x+y

print(find_sum(5,5))



def is_palindrome(word):


    return word == word[::-1]


print(is_palindrome("alla"))  


def calc_taaxes(*args):
    for x in args:
     print(f'Got paymentn = {x}')
    return print(sum(args)*0.6)

calc_taaxes(14,58)


def addPlayerInDictionary(**kwargs):
    for k,v in kwargs.items():
        print(f'Player {k} has raiting {v}')
 



addPlayerInDictionary(Yanis=5,Lillard=8)
        