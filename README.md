# Projeto: Calculadora com Testes Unitários

Este projeto implementa uma calculadora com operações matemáticas básicas em Python, acompanhada de testes unitários utilizando o framework `pytest`.

## 🧮 Funcionalidades da Calculadora

A calculadora possui os seguintes métodos:

- `soma(a, b)`
- `subtracao(a, b)`
- `multiplicacao(a, b)`
- `divisao(a, b)` — com tratamento para divisão por zero
- `fatorial(n)` — com tratamento para número negativo
- `potencia(base, expoente)`

## ✅ Testes Unitários

Os testes cobrem os seguintes casos:

- Operações básicas com números positivos e negativos
- Divisões com números decimais e erro ao dividir por zero
- Fatorial com valores válidos e inválidos
- Potência com expoentes positivos e negativos

## 🚀 Como executar

### 1. Instale o pytest
```bash
pip install pytest
```

### 2. Execute os testes
No terminal, digite:
```bash
python -m pytest test_calculadora.py
```

Você deverá ver uma saída parecida com esta:
```
test_calculadora.py ...... [100%]
```

## 👩‍💻 Desenvolvido por

Jessica — para a disciplina de Qualidade de Software
