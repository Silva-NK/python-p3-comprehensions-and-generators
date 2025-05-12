#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = [num for num in num_list if num % 2 == 0]
    return even_nums
print(return_evens([0, 3, 8, 15, 24, 35, 48, 63, 80, 99]))


def make_exclamation(sentence_list):
    new_sentences = [f"{sentence}!" for sentence in sentence_list]
    return new_sentences
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))