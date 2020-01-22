import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    VP -> V NP
    VP -> NP V
    NP -> NN NP
    NP -> CONJ NN
    NP -> "I"
    V -> "like"
    NN -> "dogs"
    NN -> "cats"
    CONJ -> "and"
""")

sentence = "I like dogs and cats"
tokens = sentence.split()

# chart_parser = nltk.ChartParser(grammar)
# rd_parser = nltk.RecursiveDescentParser(grammar)
# sr_parser = nltk.ShiftReduceParser(grammar)
# trace_sr_parser = nltk.ShiftReduceParser(grammar, trace=2)

# for tree in chart_parser.parse(tokens):
#     tree.pretty_print()
#
# for tree in rd_parser.parse(tokens):
#     tree.pretty_print()

# for tree in trace_sr_parser.parse(tokens):
#     print(tree)

import spacy

#python -m spacy download en_core_web_sm

parser = spacy.load("en_core_web_sm")

doc = parser('Fruit flies like a banana.')

for token in doc:
    print(token.text,
          token.lemma_,
          token.pos_,
          token.tag_,
          token.dep_,
          token.shape_,
          token.is_alpha,
          token.is_stop
          )

from spacy import displacy

displacy.serve(doc, style='dep')