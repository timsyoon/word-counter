# Author: Timothy Yoon
# Date: August 27, 2020

# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap


# Regular expression used to capture words
rgx = re.compile("(\w[\w']*\w|\w)")


def hash_function_2(key):
    """
    Hash function to use for the hash map.
    """
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


def get_count(tup):
    """
    Helper function for top_words() that returns the second element in a tuple.
    The function is used as a key in sort() to sort a list of tuples by the
    second element of each tuple, that is, by word count.

    The idea for this function is courtesy of Programiz's Python List sort()
    page: https://www.programiz.com/python-programming/methods/list/sort

    :return: the second element of the tuple parameter
    """
    return tup[1]


def top_words(source, number):
    """
    Take a plain text file and count the number of occurrences of case insensitive words.
    Return the top `number` of words in a list of tuples of the form (word, count).

    :param source: the file name containing the text
    :param number: the number of top results to return (e.g. 5 would return the 5 most common words)
    :return: a list of tuples of the form (word, count), sorted by most common word (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """
    keys = set()

    ht = HashMap(2500,hash_function_2)

    # Read the file one word at a time and put the word in `w`
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                # Convert the word to lowercase to enforce case insensitivity
                word_lower = w.lower()

                # If the word already exists in the table, get and update its
                # current count
                if ht.contains_key(word_lower):
                    cur_count = ht.get(word_lower)  # Get current count
                    ht.put(word_lower, cur_count + 1)  # Update current count

                # If the word does not exist in the table, add it and set its
                # count to 1
                else:
                    ht.put(word_lower, 1)

    # Get a list of tuples consisting of all the key-value pairs in the table
    tuple_list = ht.get_tuples()

    # Sort the list of tuples in descending order by word count
    tuple_list.sort(key=get_count, reverse=True)
    # print("sorted tuple_list:", tuple_list)

    # Slice the list of tuples to contain `number` amount of tuples
    sliced_list = tuple_list[0:number]

    # Return the sliced list of tuples
    return sliced_list


print(top_words("alice.txt", 10))
