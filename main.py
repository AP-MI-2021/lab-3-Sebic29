from typing import List
from math import sqrt


def show_menu():
    print("1.Citire date")
    print("2.Determinati cea mai lunga subsecventa in care toate numerele sunt patrate perfecte.")
    print("3.Determinati cea mai lunga subsecventa in care toate numerele sunt prime")
    print("4.Determinati cea mai lunga subsecventa in care toate numerele sunt palindrome")
    print("5.Exit.")


def get_perfect_squares(number):
    """
    Verifica daca un numar este patrat perfect
    :param number: Un numar introdus
    :return: Returneaza True sau False,respectiv daca numarul este patrat perfect sau daca nu este
    """
    # Returneaza daca un numar este patrat perfect(True) iar in caz contrar(False)
    if sqrt(number) == int(sqrt(number)):
        return True
    return False


def convert_list_str_to_int(lst):
    """
    Converteste elementele de tip str in elemente de tipp int
    :param lst: Lista de convertit
    :return: Returneaza lista cu elementele convertite in int
    """
    list_int = []
    for i in lst:
        list_int.append(int(i))

    return list_int


def read_list():
    lst = []
    lst_str = input("Introduceti numerele separate printr-un spatiu: ")
    lst_str_split = lst_str.split(' ')
    for number in lst_str_split:
        lst.append(number)

    return lst


def get_longest_all_perfect_squares(lst):
    """
    Determina cea mai lunga subsecventa in care numerele sunt patrate perfecte
    :param lst: Lista de numere introdusa de la tastatura(numere naturale)
    :return: Returneaza cea mai lunga subsecventa in care numerele sunt patrate perfecte(o lista)
    """
    length = 0
    list_copy = []
    rezult_list = []
    mx_length = 0
    for i in range(len(lst)):
        if get_perfect_squares(lst[i]) == True:
            list_copy.append(lst[i])
            length = length + 1
        elif length > mx_length:
            mx_length = length
            rezult_list = list_copy[:]
            length = 0
            list_copy.clear()
        else:
            list_copy.clear()
    if length > mx_length:
        rezult_list = list_copy[:]
    return rezult_list


def test_longest_perfect_squares():
    assert get_longest_all_perfect_squares([5, 4, 9, 16, 3, 232, 36, 49, 81, 9]) == [36, 49, 81, 9]
    assert get_longest_all_perfect_squares([5, 7, 8, 4, 4, 9, 100, 121]) == [4, 4, 9, 100, 121]
    assert get_longest_all_perfect_squares([7, 8, 9, 9, 81, 121, 36, 7, 5, 5, 4, 4, 4, 9, 81, 36, 9]) == [4, 4, 4, 9,
                                                                                                          81, 36, 9]


def is_prime(n):
    # Aceasta functie returneaza daca un numar este prim
    # parametrul n este numarul dat pentru care se returneaza daca este prim
    if n < 2:
        return False
    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def get_longest_all_primes(lst: List[int]):
    """
    Determina cea mai lunga subsecventa in care numerele sunt prime
    :param lst: Lista de numere introdusa de la tastatura(numere naturale)
    :return: Returneaza cea mai lunga subsecventa in care numerele sunt prime(o lista)
    """

    length = 0
    list_copy = []
    rezult_list = []
    mx_length = 0
    for i in range(len(lst)):
        if is_prime(lst[i]) == True:
            list_copy.append(lst[i])
            length = length + 1
        elif length > mx_length :
            mx_length = length
            rezult_list = list_copy[:]
            length = 0
            list_copy.clear()
        else:
            list_copy.clear()
    if length > mx_length:
            rezult_list = list_copy[:]
    return rezult_list


def test_primes_subsec():
    assert get_longest_all_primes([9, 5, 3, 7, 4, 7, 5]) == [5, 3, 7]
    assert get_longest_all_primes([10, 5, 3, 7, 2, 9, 9, 4]) == [5, 3, 7, 2]
    assert get_longest_all_primes([11, 5, 3, 7, 2, 9, 4, 4]) == [11, 5, 3, 7, 2]


def is_palindrome(n):
    #Determina daca un numar este palindrom dau sau nu
    copie_n = n
    oglindit = 0
    while n:
        oglindit = oglindit * 10 + n % 10
        n = n // 10
    if( copie_n == oglindit ):
        return True
    return False


def get_longest_all_palindromes(lst: List[int]):
    """
    Determina cea mai lunga subsecventa in care numerele sunt palindrome
    :param lst: Lista de numere introdusa de la tastatura(numere naturale)
    :return: Returneaza cea mai lunga subsecventa in care numerele sunt palindrome(o lista)
    """

    length = 0
    list_copy = []
    rezult_list = []
    mx_length = 0
    for i in range(len(lst)):
        if is_palindrome(lst[i]) == True:
            list_copy.append(lst[i])
            length = length + 1
        elif length > mx_length :
            mx_length = length
            rezult_list = list_copy[:]
            length = 0
            list_copy.clear()
        else:
            list_copy.clear()
    if length > mx_length:
            rezult_list = list_copy[:]
    return rezult_list


def test_get_longest_all_palindromes() :
    assert get_longest_all_palindromes([11,232,122,5,7,9,121]) == [5,7,9,121]
    assert get_longest_all_palindromes([1333,44,55,345,1,11,121,232,131]) == [1,11,121,232,131]
    assert get_longest_all_palindromes([34,56,999,121,131,12334,1221]) == [999,121,131]


def main():
    lst = []
    while True:
        show_menu()
        optiune = (input("Optiunea: "))
        if optiune == '1':
            lst = read_list()
        if optiune == '2':
            int_list = convert_list_str_to_int(lst)
            squares = get_longest_all_perfect_squares(int_list)
            print(f"Cea mai lunga subsecventa de patrate perfecte este: {squares}")
        if optiune == '3':
            int2_list = convert_list_str_to_int(lst)
            print(f"Cea mai lunga subsecventa de numere prime este: {get_longest_all_primes(int2_list)}")
        if optiune == '4':
            int3_list = convert_list_str_to_int(lst)
            print(f"Cea mai lunga subsecventa de numere palindrome este: {get_longest_all_palindromes(int3_list)}")
        if optiune == '5':
            break


if __name__ == '__main__':
    test_primes_subsec()
    test_longest_perfect_squares()
    test_get_longest_all_palindromes()
    main()
