
import itertools
import re
def solve(formula):
    return filter(valid, letter_replacements(formula))
def letter_replacements(formula):
    formula = formula.replace(' = ', ' == ') # Allow = or ==
    letters = cat(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        yield formula.translate(str.maketrans(letters, cat(digits)))
def valid(exp):
    try:
        return not leading_zero(exp) and eval(exp) is True
    except ArithmeticError:
        return False
cat = ''.join
leading_zero = re.compile(r'\b0[0-9]').search
str1=input("Enter first string: ")
str2=input("Enter second string: ")
str3=input("Enter third string: ")
str4=str1+' + '+str2+' = '+str3
print("Input string is '",str4,"'")
next(solve(str4))















import constraint

problem = constraint.Problem()

# We're using .addVariables() this time since we're adding
# multiple variables that have the same interval.
# Since Strings are arrays of characters we can write
# "TF" instead of ['T','F'].
problem.addVariables("TF", range(1, 10))
problem.addVariables("WOUR", range(10))

# Telling Python that we need TWO + TWO = FOUR
def sum_constraint(t, w, o, f, u, r):
    if 2*(t*100 + w*10 + o) == f*1000 + o*100 + u*10 + r:
        return True

# Adding our custom constraint. The
# order of variables is important!
problem.addConstraint(sum_constraint, "TWOFUR")

# All the characters must represent different digits,
# there's a built-in constraint for that
problem.addConstraint(constraint.AllDifferentConstraint())

solutions = problem.getSolutions()
print("Number of solutions found: {}\n".format(len(solutions)))

# .getSolutions() returns a dictionary
for s in solutions:
    print("T = {}, W = {}, O = {}, F = {}, U = {}, R = {}"
        .format(s['T'], s['W'], s['O'], s['F'], s['U'], s['R']))
