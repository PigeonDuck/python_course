print("hellp")
triplets = [
    ['t','u','p'],
    ['w','h','i'],
    ['t','s','u'],
    ['a','t','s'],
    ['h','a','p'],
    ['t','i','s'],
    ['w','h','s']
]
letters = {letter for triplet in triplets for letter in triplet }
letters_or=[triplet for triplet in triplets for triplet in triplet]
print(letters_or)
print(triplets[0][1])
print(letters)
length = len(letters)
    