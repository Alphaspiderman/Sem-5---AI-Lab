from itertools import permutations


def convert(word, subs):
    val = 0
    for idx, ch in enumerate(word[::-1]):
        val += subs[ch] * pow(10, idx)
    return val


def cryptic(w1, w2, w3):
    found = False
    letters = list(set(w1) | set(w2) | set(w3))
    digits = [i for i in range(10)]
    if len(letters) > len(digits):
        print("Combination is not possible")
        return

    for perm in permutations(digits, len(letters)):
        mapping = {letters[i]: perm[i] for i in range(len(letters))}
        val1 = convert(w1, mapping)
        val2 = convert(w2, mapping)
        val3 = convert(w3, mapping)
        if val1 + val2 == val3:
            found = True
            print(f"Solution - {mapping}")
            print(f"First Word:  {w1} with Value: {val1}")
            print(f"Second Word: {w2} with Value: {val2}")
            print(f"Result Word: {w3} with Value: {val3}")
    if not found:
        print("No Solutions Found")

print("Enter the equation in the format --> WORD1 + WORD2 = WORD3")
eqn = input("Equation - ")
temp, word3 = eqn.lower().replace(" ", "").split("=")
word1, word2 = temp.split("+")

cryptic(word1, word2, word3)
