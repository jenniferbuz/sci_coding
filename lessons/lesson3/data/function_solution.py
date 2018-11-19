def likes_fruit(answer):
    """Return True if answer is 'yes'
    
    Parameters
    ----------
    answer: str
        A 3 character string of 'yes' or 'nah'.

    Returns
    -------
    bool
        True iff answer is 'yes'.

    Examples
    --------
    >>> likes_fruit('yes')
    True
    >>> likes_fruit('nah')
    False
    """
    return answer == 'yes'

def is_adult(age):
    """Return True if age is greater than 20.
    
    Parameters
    ----------
    answer: int
        A positive integer age.

    Returns
    -------
    bool
        True iff age is larger than 20.

    Examples
    --------
    >>> is_adult(5)
    False
    >>> is_adult(20)
    False
    >>> is_adult(21)
    True
    >>> is_adult(82)
    True
    """
    return age > 20

def is_match(apples, oranges, age):
    """Return True if likes_fruit(apples), likes_fruit(oranges) and is_adult(age).
    
    Parameters
    ----------
    apples: str
        A 3 character string of whether a person likes apples.
    oranges: str
        A 3 character string of whether a person likes oranges.
    age: int
        A positive integer age.
    """
    return likes_fruit(apples) and likes_fruit(oranges) and is_adult(age)


def all_match(person1, person2, person3):
    """Return True if all people like apples and oranges and are older than 20.
    
    Parameters
    ----------
    person1: str
        A string of whether person1 likes apples and oranges followed by their age.
    person2: str
        A string of whether person2 likes apples and oranges followed by their age.
    person3: str
        A string of whether person3 likes apples and oranges followed by their age.
    """
    if (is_match(person1[0:3], person1[4:7], int(person1[8:])) and
        is_match(person2[0:3], person2[4:7], int(person2[8:])) and
        is_match(person3[0:3], person3[4:7], int(person3[8:]))):
        print("It's a match!")
    else:
        print("It's not a match!")
    
all_match(person1, person2, person3)