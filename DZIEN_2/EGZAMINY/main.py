from homework import Homework
from exam import Exam
from grade import ExamG

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

print("_________ EXAMG ____________")

fex = ExamG()
fex.math_grade = 34
fex.alg_grade = 46
fex.prog_grade = 12
print(f'egzamin -> matematyka: {fex.math_grade}, algorytmika: {fex.alg_grade}, programowanie: {fex.prog_grade}')

popex = ExamG()
popex.math_grade = 56
popex.alg_grade = 77
popex.prog_grade = 64
print(f'egzamin poprawkowy -> matematyka: {popex.math_grade}, algorytmika: {popex.alg_grade}, programowanie: {popex.prog_grade}')

print(f'dane z archiwum - pierwsze podejście')
print(f'egzamin -> matematyka: {fex.math_grade}, algorytmika: {fex.alg_grade}, programowanie: {fex.prog_grade}')
