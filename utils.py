def get_constraints(entries, num_constraints, num_variables):
    constraints = []
    for i in range(num_constraints):
        row = []
        for j in range(num_variables):
            value = float(entries[i][j].get())
            row.append(value)
        constraints.append(row)
    return constraints

def get_vector(entries, size):
    vector = []
    for i in range(size):
        value = float(entries[i].get())
        vector.append(value)
    return vector

def save_solution(solution, iterations):
    with open("output/solution.txt", "w") as f:
        for i, iteration in enumerate(iterations):
            f.write(f"Iteración {i+1}:\n")
            f.write(str(iteration))
            f.write("\n\n")
        f.write("Solución Óptima: " + str(solution['optimal_value']) + "\n")
        for var, value in solution['variables'].items():
            f.write(f"{var} = {value}\n")
        f.write(f"\nNúmero de Iteraciones: {iterations}\n\n")
        
        for i, interaction in enumerate(interactions):
            f.write(f"Iteración {i + 1}:\n")
            f.write(f"  Pivote: {interaction['pivot']}\n")
            f.write(f"  Variable que entra: {interaction['entering_var']}\n")
            f.write(f"  Variable que sale: {interaction['leaving_var']}\n")
            f.write("\n")

def save_interaction(interactions, pivot, entering_var, leaving_var):
    interactions.append({
        'pivot': pivot,
        'entering_var': entering_var,
        'leaving_var': leaving_var
    })
