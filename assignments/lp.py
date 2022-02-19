from pulp import LpProblem, LpVariable, LpMaximize, LpMinimize, LpStatus, value

problem = LpProblem("Giapetto", LpMinimize)
y1 = LpVariable("y1", lowBound=0)
y2 = LpVariable("y2", lowBound=0)
y3 = LpVariable("y3", lowBound=0)

problem += 100 * y1 + 2400 * y2 + 800 * y3
problem += 1 * y1 + 20 * y2 + 4 * y3 >= 80
problem += 1 * y1 + 40 * y2 + 16 * y3 >= 100
print(problem)

status = problem.solve()
print(LpStatus[status])

print(f"y1 ==> {value(y1)}; y2 ==> {value(y2)};y2 ==> {value(y3)}; z ==> {value(problem.objective)}")
