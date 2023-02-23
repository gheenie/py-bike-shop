from src.component import (Brakes)

def test_brakes_initializes_with_correct__current_state_max_lifespan():
    newbrakes = Brakes(4, 10)

    assert newbrakes.current_state == 4
    assert newbrakes.max_lifespan == 10

    assert newbrakes.check_condition() == 'Poor'


def test_brakes__use_method_increments_current_state():
    newbrakes = Brakes(3, 10)
    result = newbrakes.use()

    assert newbrakes.current_state == 5
    assert result == True


def test_brakes_use_method_does_not_allow_use_if_broken():
    newbrakes = Brakes(10, 10)
    result = newbrakes.use()
    assert result == False

    assert newbrakes.current_state == 10