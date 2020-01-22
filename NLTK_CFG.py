import nltk

grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  """)

sent = "Mary saw Bob".split()
parser = nltk.ChartParser(grammar)
rd_parser = nltk.RecursiveDescentParser(grammar)
sr_parser = nltk.ShiftReduceParser(grammar)
trace_sr_parser = nltk.ShiftReduceParser(grammar1, trace=2)

for tree in sr_parser.parse(sent):
    print(tree)
    tree.pretty_print()
