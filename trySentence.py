from Sentence import Sentence

sentence = Sentence('爱的可能')
arcs = sentence.arcs

print(sentence.words)
print(sentence.postags)
print(sentence.personNames)
print('\t'.join ('%s,%s' % (arc.head,arc.relation)for arc in arcs))
