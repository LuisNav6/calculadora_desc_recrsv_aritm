class RecursiveDescentParser:
    def __init__(self, expr):
        # Inicialización del objeto con la expresión y el índice actual
        self.expr = expr
        self.index = 0

    def parse(self):
        # Método para analizar la expresión de entrada
        result = self.expression()
        if self.index < len(self.expr): # revisamos si ya hemos revisado toda la expresión
            raise Exception("Error de sintaxis")
        return result

    def expression(self):
        # Método para analizar una expresión que contiene términos separados por '+' o '-' llamada exp en la regla
        result = self.term()
        while self.index < len(self.expr) and self.expr[self.index] in '+-':
            if self.expr[self.index] == '+':
                self.index += 1
                result += self.term()
            else:
                self.index += 1
                result -= self.term()
        return result

    def term(self):
         # Método para analizar un término que contiene factores separados por '*', '/', o '%' llamada term en la regla
        result = self.exponent()
        while self.index < len(self.expr) and self.expr[self.index] in '*/%':
            if self.expr[self.index] == '*':
                self.index += 1
                result *= self.exponent()
            elif self.expr[self.index] == '/':
                self.index += 1
                result /= self.exponent()
            else:
                self.index += 1
                result %= self.exponent()
        return result

    def exponent(self):
        # Método para analizar un exponente, que puede ser un factor elevado a una potencia, regla añadida por decisión propia
        result = self.factor()
        while self.index < len(self.expr) and self.expr[self.index] == '^':
            self.index += 1
            result **= self.factor()
        return result

    def factor(self):
        # Método para analizar un factor, que puede ser un número entero o una expresión entre paréntesis llamada factor en la regla
        if self.expr[self.index].isdigit():
            # Si el próximo carácter es un dígito, analiza un número entero
            start = self.index
            while self.index < len(self.expr) and self.expr[self.index].isdigit():
                self.index += 1
            return int(self.expr[start:self.index])
        elif self.expr[self.index] == '(':
            # Si el próximo carácter es '(', analiza una expresión entre paréntesis esto nos ayuda a identificar precedencias
            self.index += 1
            result = self.expression()
            if self.expr[self.index] == ')':
                # Verifica si la expresión entre paréntesis está cerrada correctamente, sino mandamos un error
                self.index += 1
                return result
            else:
                raise Exception("Error de sintaxis: se esperaba ')'")
        else:
            # Si el próximo carácter no es un dígito, '(' o '^', se produce un error de sintaxis
            raise Exception("Error de sintaxis: se esperaba un dígito, '(' o '^'")

# Llamamos a la clase, para poder realizar el proceso de "calculadora descendente recursiva aritmética entera simple EBNF"
expresion_usuario = input("Ingresa una expresión matemática: ")
parser = RecursiveDescentParser(expresion_usuario)
print(f"El resultado de la expresión es: {parser.parse()}")