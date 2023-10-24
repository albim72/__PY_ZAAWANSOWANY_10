from homework import Homework

print("_________ HOMEWORK ____________")
g = Homework()
g.grade = 95
assert g.grade == 95
print(f'ocena za projekt: {g.grade}')
