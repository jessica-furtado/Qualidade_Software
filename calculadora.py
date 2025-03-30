import math

class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b

    def fatorial(self, n):
        if n < 0:
            raise ValueError("Fatorial de número negativo não é permitido.")
        return math.factorial(n)

    def potencia(self, base, expoente):
        return base ** expoente
