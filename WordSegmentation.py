# Dictionary building

text = "The study of the vaccine produced by U.S. firm Pfizer and German partner BioNTech was conducted by scientists " \
       "from the two companies and researchers at the University of Texas Medical Branch. It comes as public health " \
       "experts warn that the more transmissible variant could drive yet another surge in covid  cases particularly " \
       "as restrictions are lifted across the United States.The variant known as P.1 has spread rapidly across Brazil " \
       "since emerging in early January, reinfecting people who already had covid and leaving  tidal wave of misery " \
       "and death in it wake. According to the U.S. Centers for Disease Control and Prevention just 15 cases of the " \
       "Brazil variant have been identified in nine states. "
text = text.lower()
tokens = []
dictionary = list(set(text.split(" ")))

# Word Segmentation
spaceFreeText = "vaccinewasproducedbypfizerforcovid"

'''WORD SEGMENTATION LOGIC'''
word = ""
for i in range(0, len(spaceFreeText)):
    word += spaceFreeText[i]
    if word in dictionary:
        tokens.append(word)
        word = ""


print(tokens)
