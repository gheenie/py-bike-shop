from src.component import (Bell)

def test_bell_initializes_with_correct__current_state_max_lifespan():
    new_bell = Bell(4, 10)

    assert new_bell.current_state == 4
    assert new_bell.max_lifespan == 10

    assert new_bell.check_condition() == 'Poor'


def test_bell__use_method_increments_current_state():
    new_bell = Bell(3, 10)
    result = new_bell.use()

    assert new_bell.current_state == 4
    assert result == True


def test_bell_use_method_does_not_allow_use_if_broken():
    new_bell = Bell(10, 10)
    result = new_bell.use()
    assert result == False

    assert new_bell.current_state == 10