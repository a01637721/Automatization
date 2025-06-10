import pytest
from area_triangulo import calcular_area

def test_area_valores_correctos():
    assert calcular_area(5, 7) == 17.5

def test_base_negativa():
    with pytest.raises(ValueError, match="La base debe ser mayor a cero."):
        calcular_area(-3, 5)

def test_altura_negativa():
    with pytest.raises(ValueError, match="La altura no puede ser negativa."):
        calcular_area(4, -2)

def test_base_cero():
    with pytest.raises(ValueError, match="La base debe ser mayor a cero."):
        calcular_area(0, 6)
