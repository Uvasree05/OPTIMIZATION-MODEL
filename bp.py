from pulp import LpMaximize, LpProblem, LpVariable, value, LpStatus

# Step 1: Define the problem
model = LpProblem(name="maximize-furniture-profit", sense=LpMaximize)

# Step 2: Define decision variables
tables = LpVariable(name="Tables", lowBound=0, cat="Integer")
chairs = LpVariable(name="Chairs", lowBound=0, cat="Integer")

# Step 3: Objective function
model += 70 * tables + 50 * chairs, "Total_Profit"

# Step 4: Add constraints
model += 4 * tables + 3 * chairs <= 240, "Wood"
model += 2 * tables + 1 * chairs <= 100, "Labor"

# Step 5: Solve the model
model.solve()

# Step 6: Print results
print(f"Status: {model.status}, {LpStatus[model.status]}")
print(f"Produce {tables.value()} Tables")
print(f"Produce {chairs.value()} Chairs")
print(f"Maximum Profit: ₹{value(model.objective)}")
