import re
from nltk.tree import Tree

# sentence = 'I like yogurt'
sentence = "I like dogs and cats"

tokens = sentence.split()
length = len(tokens)

# grammar_rules = {
#     'I': ['NP'],
#     'like': ['V', 'PREP'],
#     'dogs': ['NN'],
#     'cats': ['NN'],
#     'and': ['CONJ'],
#     'NP VP': ['S'],
#     'V NP': ['VP'],
#     'CONJ NN': ['NP'],
#     'NN NP': ['NP'],
#     'VP NP': ['S'],
#     'V NN': ['VP'],
# }

# nonterminals = ['PR', 'V', 'NN']

grammar_rules = {
    'I': ['NP'],
    'like': ['V'],
    'dogs': ['NN'],
    'cats': ['NN'],
    'and': ['CONJ'],
    'yogurt': ['NN'],
    'CONJ NN': ['NP'],
    'NN NP': ['NP'],
    # 'V NN': ['VP'],
    'V NP': ['VP'],
    # 'PR VP': ['S'],
    'NP VP': ['S'],
}

# I like dogs and cats


def get_cells(tokens, grammar_rules):

    def apply_rules(t):
        try:
            return grammar_rules[t]
        except KeyError as r:
            return None

    cells = { (1, x+1) : [] for x in range(len(tokens)) }

    for x, t in enumerate(tokens):
       r = apply_rules(t)
       for w in r:
           cells[1, x+1].append((w, (t)))

    #  row; length +1 because the last el in range is not included
    for l in range(2, length + 1):

        # column, smaller by one every iteration;
        # plus 2 because l is bigger by 1 every iteration;
        for s in range(1, length - l + 2):

            # per each cell in l
            for p in range(1, l):

                # (p, s) - current cell;
                # l-p - above
                #  s+p - to the right
                if (p, s) in cells.keys() and (l-p, s+p) in cells.keys():

                    t1 = cells[p, s]
                    t2 = cells[l-p, s+p]

                    for a, _ in t1:
                        for b, _ in t2:
                            r = apply_rules(a + " " + b)
                            if r is not None:
                                if (l, s) not in cells.keys():
                                    cells[l, s] = []
                                for w in r:
                                    cells[l, s].append((w, (a, b)))
    return cells


def get_tree(tokens, cells):

    trees = ['']
    length = len(tokens)

    for l in range(1, length+1):
        for s in range(1, length - l + 2):
            if (l, s) in cells.keys():

                if l == 1:
                    new_trees = []
                    for leaf in cells[l, s]:
                        for lisp_tree in trees:
                            lisp_tree += '(' + leaf[0] + ' ' + leaf[1] + ')'
                            new_trees.append(lisp_tree)
                    trees = new_trees

                else:
                    new_trees = []
                    for leaf in cells[l, s]:
                        child1 = leaf[1][0]
                        child2 = leaf[1][1]
                        parent = leaf[0]
                        print(child1, child2, parent)
                        # if l == length and parent != 'S':
                        #     continue
                        # elif l < length and parent == 'S':
                        #     continue
                        # else:
                        for lisp_tree in trees:
                            match = re.match('(^.*)' + child1 + '(.*)' + child2 + '(.*\))(.*$)', lisp_tree)
                            if match:
                                lisp_tree = match.group(1) + parent + ' (' + child1 + match.group(2) + child2 + match.group(3) + ')' + match.group(4)
                                new_trees.append(lisp_tree)
                    trees = new_trees
    return trees


def cky(tokens, grammar_rules):
    cells = get_cells(tokens, grammar_rules)
    print(cells)
    trees = get_tree(tokens, cells)
    print(trees)
    return trees

trees = cky(tokens, grammar_rules)

for tree in trees:
    parsetree = Tree.fromstring(tree)
    parsetree.pretty_print()
