#main routine
from urllib.request import urlopen
curf=input("please enter the currency you want to change from:")
curt=input("please enter the currency you want to convert to:")
am=float(input("please enter the amount of currency you want to convert"))

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    trans={'source':'currency_from','target':'currency_to','amount':'amount_to'}
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={source}&to={target}&amt={amount}'.format(**trans))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr = jstr[0:-34]+"}"
    dic=eval(jstr)
    ed=dic['"to"']
    a=ed.split(' ')
    res=float(a[0])
    return res


def get_from(currency_from, currency_to, amount_from):
    """To judge whether the input parametre is available or not."""
    trans={'source':'currency_from','target':'currency_to','amount':'amount_to'}
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={source}&to={target}&amt={amount}'.format(**trans))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    j =[',','.',';','?','!',' ']
    for i in range(0,len(j)):
        s1=jstr.split('j[i]')
        s2=''.join(s1)
    if sr[-7:]!='invalid':
        l=True
    else:
        l=False
    return l 

        
get_from(curf,curt,am)
if l==True:
    exchange(curf,curt,am)
    print(res)
else:
    print("your input is invalid!")
    

#test routine
"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""
#test for module get_from
def test1():
    assert('USD' == get_from(json))
    assert('EUR' == get_from(json))
    assert("FFF" != get_from(json))
#test for module exchange
def test2():
    assert(exchange(USD,EUR,2.5) == 2.0952375)
    assert(exchange(HKD,SOS,12.9) == 955.28082055764)
    assert(exchange(ILS,XOF,1.5) != 4364.8927)
    assert(exchange(BBD,MVR,7.6) != 29.735451)
#test for all modules
def testAll()
    """test all cases"""
    test1()
    test2()
    print("All tests passed")

testAll()


    
