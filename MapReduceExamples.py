from functools import reduce

def count_words(doc):
    normalised_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequency = {}
    for word in normalised_doc.split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def combine_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + 1
    return d

print(count_words("An argumentative essay is just what it sounds like: an essay where you argue. "))

document = [
    "An argumentative essay is just what it sounds like: an essay where you argue.", 
    "You pick a topic, take a stance, research information to support your opinion, state your claims, and voilà!", 
    "You’ve got your essay.", 
    "As simple as that may sound, writing a persuasive essay can be quite difficult for even very experienced writers.", 
    "It takes excellent organization and planning to clearly address your thoughts and requires stellar research skills to find valid arguments that support your claim.",
    "But before you can state your case, you first need to come up with the topic you’re going to argue about."
]

counts = map(count_words, document)
total_counts = reduce(combine_counts, counts)
print(total_counts)
