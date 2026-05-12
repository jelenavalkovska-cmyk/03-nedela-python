
def capitalize(text):
    """Pārtaisa visus burtus tekstā par lielājiem (UPPER CASE)

        Args:
        text: ievades teksts

        Returns: String

        Example: 

        >>> capitalize("Hello World!")

        HELLO WORLD!

        >>> capitalize("Beautiful DAY")

        BEAUTIFUL DAY 
              
    """ 
    return(text.upper())


def truncate(text, max_len=20):
    """Apgriež un pievieno "..." 

        Args:
        text: ievades teksts
        max_len: maksimālais pieļaujāmais teksta garums

        Returns: String

        Example: 

        >>> truncate("Hello World!", 5)

        Hello

        >>> truncate("Beautiful", 15)

        Beautiful...
              
    """ 
    if len(text) > max_len:
        return text[:max_len]
    return text + "..."



def count_words(text):
    """Saskaita vārdus

        Args:
        text: ievades teksts

        Returns: int

        Example: 

        >>> count_words("Hello my beautiful day!")

        4

        >>> count_words(7776666)

        AttributeError: 'int' object has no attribute 'split'
              
    """ 
    return(len(text.split()))





def clamp(num, low, high): 

    """Ierobežo skaitli norādītajā diapazonā. 

        Args: 

        num: skaitlis, ko ierobežot 

        low: minimālā robeža 

        high: maksimālā robeža 

 

    Returns: 

        int vai float: ierobežotā vērtība 

 

    Example: 

        >>> clamp(15, 0, 10) 

        10 

        >>> clamp(-5, 0, 10) 

        0 

    """ 

    return max(low, min(num, high)) 


def is_prime(num):
    """Pārbauda Vai ir pirmskaitlis (atgriež bool) 

        Args:
        num: skaitlis

        Returns: Boolean

        Example: 

        >>> is_prime(5)

        True

        >>> is_prime(36)

        False 

        >>> is_prime(36.98)

        True

        >>> is_prime("Hello")

        TypeError: '<=' not supported between instances of 'str' and 'int'
              
    """ 
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        return True
    

    
def factorial(n):
    """n! (ar validāciju: n >= 0)

        Args:
        n: skaitlis

        Returns: int

        Example: 

        >>> factorial(2)

        2

        >>> factorial(3)

        6 

        >>> factorial(0)

        "Faktoriāls nav definēts negatīviem skaitļiem vai 0!"

        >>> factorial("hello")

        TypeError: '<=' not supported between instances of 'str' and 'int'
              
    """ 
    if n <= 0:
        return "Faktoriāls nav definēts negatīviem skaitļiem vai 0!"
    rezultats = 1
    for i in range(1, n + 1):
        rezultats *= i
    return rezultats
    

def total(numbers):
    """Saraksta summa (ar for, ne sum())

        Args:
        numbers: saraksts

        Returns: int vai float

        Example: 

        >>> total([1, 2, 5, "hello", 2])

        10

        >>> total((1, 2, 5, "hello", 2))

        10 

        >>> total(("hello", "bye", "end"))

        0
              
    """ 
    summa = 0
    for elements in numbers:
        if isinstance(elements, (int, float)):
            summa += elements
    return(summa)


def average(numbers):
    """Vidējais aritmētiskais

        Args:
        numbers: saraksts

        Returns: int vai float

        Example: 

        >>> average([1, 2, 5, "hello", 2])

        2.5

        >>> average((1, 2, 5, "hello", 2))

        2.5

        >>> average(("hello", "bye", "end"))

        ZeroDivisionError: division by zero
              
    """ 
    summa = 0
    skaits = 0
    for elements in numbers:
        if isinstance(elements, (int, float)):
            skaits += 1
            summa += elements
    return(summa/skaits)




if __name__ == "__main__":
    print(capitalize("Hello World!"))
    print(truncate("Hello my be", 5))
    print(truncate("Beautiful", 15))
    print(count_words("Hello my beautiful day!"))
    #print(count_words(7776666))
    print(is_prime(5))
    print(is_prime(36))
    print(is_prime(36.98))
    #print(is_prime("Hello!"))
    print(factorial(2))
    print(factorial(3))
    print(factorial(0))
    #print(factorial("hello"))
    print(total([1, 2, 5, "hello", 2]))
    print(total((1, 2, 5, "hello", 2)))
    print(total(("hello", "bye", "end")))
    print(average([1, 2, 5, "hello", 2]))
    print(average((1, 2, 5, "hello", 2)))
    print(average(("hello", "bye", "end")))


