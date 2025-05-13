sentances = ["My name is Ram", "He is good person", "You should be careful while coding", "He can do better", "The person is mysterious", "Jay shree ram", "It is my pen"]

def sentance_split(sentance):
    return sentance.lower().split()

word_trees = []
for sentance in sentances:
    word = sentance_split(sentance)
    word_trees.append(word)

print("Word_tree", word_trees)

word_count = {}
for word in word_trees:
    for i in word:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1
        
print("Word count : ", word_count)
