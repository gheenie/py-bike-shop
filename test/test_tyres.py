from src.component import (Tyres)


def test_tyres_initializes_with_correct__current_state_max_lifespan():
    new_tyres = Tyres(15, 20)

    assert new_tyres.current_state == 15
    assert new_tyres.max_lifespan == 20

    assert new_tyres.check_condition() == 'Fragile'


def test_tyres__use_method_increments_current_state():
    new_tyres = Tyres(3, 10)
    result = new_tyres.use()

    assert new_tyres.current_state == 7
    assert result == True


def test_tyres_use_method_does_not_allow_use_if_broken():
    new_tyres = Tyres(10, 10)
    result = new_tyres.use()
    assert result == False

    assert new_tyres.current_state == 10
