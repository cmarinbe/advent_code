# coding: utf-8


# define global params
vowels = ["a", "e", "i", "o", "u"]
bad_strings = ["ab", "cd", "pq", "xy"]


# part 1 functions
def has_3_vowels(test):
    counter = 0
    for l in test:
        if l in vowels: counter += 1
    return counter>=3

def has_double_letter(test):
    for i in range(len(test)-1):
        if test[i]==test[i+1]: return True
    return False

def has_bad_strings(test):
    for bs in bad_strings:
        if bs in test:
            return True
    return False

# part 2 functions
def get_letterPairs(test):
    return ["{}{}".format(test[i], test[i+1]) for i in range(len(test)-1)]

def has_two_letterPairs(test):
    letter_pairs = get_letterPairs(test)
    for pair in letter_pairs:
        if test.count(pair) >= 2:
            return True
    return False

def has_inbetween_pair(test):
    for i in range(len(test)-2):
        if test[i]==test[i+2]: return True
    return False

def is_nice_string(test):
    return (has_two_letterPairs(test) and
            has_inbetween_pair(test))


# main
if __name__=="__main__":
    nice_strings = 0

    with open("instructions5.txt") as input:
        string_list = input.readlines()
        for s in string_list:
            if is_nice_string(s.strip()):
                nice_strings += 1

    print nice_strings


#EOF