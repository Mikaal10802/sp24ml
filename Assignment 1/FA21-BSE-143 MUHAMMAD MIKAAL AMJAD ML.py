# 12TH MARCH,2024
# CSC354 – Assignment1 – ML – Concept Learning
# MUHAMMAD MIKAAL AMJAD
# FA21-BSE-143
# IMPLEMENTING CANDIDATE ELIMINATION ALGORITHM
def update_hypotheses(concepts, target, specific_h, general_h):
    for i, h in enumerate(concepts):
        if target[i] == "yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        elif target[i] == "no":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?' if general_h[x][x] != specific_h[x] else specific_h[x]
    return specific_h, general_h
def init(concept):
    specific_h = concept[0].copy()
    general_h = [['?' for _ in specific_h] for _ in specific_h]
    return specific_h, general_h

data = [
    ['small', 'red', 'circle'],
    ['big', 'red', 'circle'],
    ['small', 'red', 'triangle'],
    ['big', 'blue', 'circle'],
    ['small', 'blue', 'circle'],
]

output = ["yes", "no", "no", "no", "yes"]

specific_h, general_h = init(data)
specific_h, general_h = update_hypotheses(data, output, specific_h, general_h)

print("\nFinal Specific Hypothesis:")
print(specific_h)
print("\nFinal General Hypothesis:")
print(general_h)
