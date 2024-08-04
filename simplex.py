import numpy as np

class Simplex:
    def __init__(self, num_constraints, num_variables, A, b, c):
        self.num_constraints = num_constraints
        self.num_variables = num_variables
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
        self.c = np.array(c, dtype=float)
        self.solution = None
        self.iterations = []
        
        # Crear la tabla inicial del método Simplex
        self.table = self.create_initial_table()

    def create_initial_table(self):
        """
        Crear la tabla inicial del método Simplex
        """
        tableau = np.zeros((self.num_constraints + 1, self.num_variables + self.num_constraints + 1))
        
        # Coeficientes de las restricciones
        tableau[:self.num_constraints, :self.num_variables] = self.A
        
        # Variables de holgura
        np.fill_diagonal(tableau[:self.num_constraints, self.num_variables:self.num_variables + self.num_constraints], 1)
        
        # Coeficientes de la función objetivo
        tableau[-1, :self.num_variables] = -self.c
        
        # Términos independientes
        tableau[:self.num_constraints, -1] = self.b
        
        return tableau
    
    def solve(self):
        """
        Ejecutar el método Simplex
        """
        while not self.is_optimal():
            pivot_col = self.select_pivot_column()
            pivot_row = self.select_pivot_row(pivot_col)
            self.pivot(pivot_row, pivot_col)
            self.iterations.append(self.table.copy())
        
        self.solution = self.extract_solution()
        return self.solution

    def is_optimal(self):
        """
        Verificar si la solución actual es óptima
        """
        return np.all(self.table[-1, :-1] >= 0)

    def select_pivot_column(self):
        """
        Seleccionar la columna pivote
        """
        return np.argmin(self.table[-1, :-1])

    def select_pivot_row(self, pivot_col):
        """
        Seleccionar la fila pivote
        """
        ratios = np.divide(self.table[:-1, -1], self.table[:-1, pivot_col], out=np.full_like(self.table[:-1, -1], np.inf), where=self.table[:-1, pivot_col] > 0)
        return np.argmin(ratios)
    
    def pivot(self, pivot_row, pivot_col):
        """
        Realizar la operación de pivoteo
        """
        self.table[pivot_row, :] /= self.table[pivot_row, pivot_col]
        for i in range(self.table.shape[0]):
            if i != pivot_row:
                self.table[i, :] -= self.table[i, pivot_col] * self.table[pivot_row, :]

    def extract_solution(self):
        """
        Extraer la solución óptima y los valores de las variables
        """
        solution = {'variables': {}, 'optimal_value': self.table[-1, -1]}
        for i in range(self.num_variables):
            col = self.table[:, i]
            if np.count_nonzero(col[:-1]) == 1 and np.count_nonzero(col) == 1:
                row = np.where(col[:-1] == 1)[0][0]
                solution['variables'][f'x{i+1}'] = self.table[row, -1]
            else:
                solution['variables'][f'x{i+1}'] = 0
        return solution