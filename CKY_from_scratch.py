from nltk.tree import Tree

sentence = "I like dogs"# and cats"
tokens = sentence.split()

grammar_rules = {
    'I': ['NP'],
    'like': ['V', 'PREP'],
    'dogs': ['NN'],
    'cats': ['NN'],
    'and': ['CONJ'],
    'NP VP': ['S'],
    'V NP': ['VP'],
    'V NN': ['VP'],
    'NN NP': ['NP'],
    'CONJ NN': ['NP'],
    'VP NP': ['S'],
}


def get_cells(grammar_rules):

    def apply_rules(rule):
        try:
            return grammar_rules[rule]
        except:
            return None

    cells = { (1, x+1): [] for x in range(len(tokens)) }
    # print(cells)
    for ind, word in enumerate(tokens):
        rule = apply_rules(word)
        for variant in rule:
            cells[1, ind+1].append((variant, (word)))

    length = len(tokens)

    for l in range(2, length+1):

        for s in range(1, length - l + 2):

            for p in range(1, l):
                # print(p, s)
                # print(l-p, s+p)

                if (p, s) in cells.keys() and (l-p, s+p) in cells.keys():
                    t1 = cells[p, s]
                    t2 = cells[l-p, s+p]

                    # print(t1)
                    # print(t2)

                    for pos1, _ in t1:
                        for pos2, _ in t2:
                            rules = apply_rules(pos1 + ' ' + pos2)
                            # print(rules)
                            if rules:
                                if (l, s) not in cells.keys():
                                    cells[l, s] = []

                                for rule in rules:
                                    cells[l, s].append(
                                        (
                                          rule, (pos1, pos2)
                                        )
                                    )
    return cells


def get_trees(tokens, cells):
    trees = ['']
    length = len(tokens)

    for l in range(1, length + 1):
        for s in range(1, length - l + 2):
            if (l, s) in cells.keys():

                if l == 1:
                    new_trees = []

                    ## ?????????????????

                    trees = new_trees

                else:
                    new_trees = []

                    ## ?????????????????

                    trees = new_trees
    return trees


def cky(tokens, grammar_rules):
    cells = get_cells(grammar_rules)
    print(cells)
    trees = get_trees(tokens, cells)
    return trees

trees = cky(tokens, grammar_rules)

for tree in trees:
    parsetree = Tree.fromstring(tree)
    parsetree.pretty_print()
