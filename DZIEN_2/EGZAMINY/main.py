from homework import Homework
from exam import Exam

print("_________ HOMEWORK ____________")
g = Homework()
g.grade = 95
assert g.grade == 95
print(f'ocena za projekt: {g.grade}')

print("_________ EXAM ____________")
ex = Exam()
ex.part_a_grade = 88
ex.part_b_grade = 65

assert ex.part_a_grade == 88
assert ex.part_b_grade == 65

print(f'egzamin -> część a: {ex.part_a_grade} punktów, część b: {ex.part_b_grade} punktów')
