from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, value

problem = LpProblem("Shop", LpMaximize)
lathe = LpVariable("lathe", lowBound=0, cat="Integer")
press = LpVariable("press", lowBound=0, cat="Integer")

problem += 100 * press + 150 * lathe
problem += 4000 * lathe + 8000 * press <= 40000
problem += 30 * lathe + 15 * press <= 200
print(problem)

status = problem.solve()
print(LpStatus[status])

print(f"lathes ==> {value(lathe)}; presses ==> {value(press)}; profit ==> {value(problem.objective)}")
