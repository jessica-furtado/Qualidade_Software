import pytest
from calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_soma(calc):
    assert calc.soma(3, 5) == 8
    assert calc.soma(-2, 7) == 5

def test_subtracao(calc):
    assert calc.subtracao(10, 5) == 5
    assert calc.subtracao(-2, -2) == 0

def test_multiplicacao(calc):
    assert calc.multiplicacao(3, 4) == 12
    assert calc.multiplicacao(-2, 3) == -6

def test_divisao(calc):
    assert calc.divisao(10, 2) == 5
    assert calc.divisao(7, 2) == 3.5
    with pytest.raises(ValueError):
        calc.divisao(10, 0)

def test_fatorial(calc):
    assert calc.fatorial(5) == 120
    assert calc.fatorial(0) == 1
    with pytest.raises(ValueError):
        calc.fatorial(-3)

def test_potencia(calc):
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(2, -2) == 0.25
