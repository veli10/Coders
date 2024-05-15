def samitleri_al(sentence):
    samitler = set()
    for i in sentence:
        if i not in 'aeiou' and i.isalpha():
            samitler.add(i.lower())
    
    return samitler