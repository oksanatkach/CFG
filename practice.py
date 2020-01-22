import math

probs = {
    'word1': 0.000053124,
    'word2': 0.000000005231524,
    'word3': 0.000000000001523552,
}

# logs = []
# for number in probs:
#     logs.append(math.log(number))
#
# print(logs)

# print( [ math.log(number) for number in probs ] )

# print( { key: math.log(probs[key]) for key in probs } )

# lst = [1, 2, 3]
# print(next(enumerate(lst)))
#
# try:
#     print('string'+4235)
# except:
#     print("Errors!!!")

# for l in range(7, 0, -1):
#     print(l)


# tree_string = "(S (NP I) (VP (V like) (NN dogs)))"
# tree_string = "(S (NP I) (VP (V like) (NN cats)))"

# from nltk.tree import Tree
# parsetree = Tree.fromstring(tree_string)
# parsetree.pretty_print()

import re
lisp_tree = '(NP (NN fruit)(NN fly))(V like)(DET a)(NN banana)'
parent = 'NP'
child1 = 'DET'
child2 = 'NN'
match = re.match('(^.*?)' + child1 + '(.*?)' + child2 + '(.*?\))(.*$)', lisp_tree)

print(match.group(1))
print(match.group(2))
print(match.group(3))
print(match.group(1) + parent + ' (' + child1 + match.group(2) + child2 + match.group(3) + ')' + match.group(4))
