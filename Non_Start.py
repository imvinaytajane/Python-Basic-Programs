# Made by Vinay on 03 Sept 2021
# Problem Statment
# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'

def non_start(a, b):

    print(a.replace(a[0], "") + b.replace(b[0], ""))


non_start('Hello', 'There')
non_start('java', 'code')
non_start('shotl', 'java')

# For general Case

non_start(a=input('Enter First String: '), b=input('Enter Second String: '))
