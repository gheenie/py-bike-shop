from src.component import (Bell)

def test_bell_initializes_with_correct__current_state_max_lifespan():
    newBell = Bell(4, 10)

    assert newBell.current_state == 4
    assert newBell.max_lifespan == 10

    assert newBell.check_condition() == 'Poor'


def test_bell__use_method_increments_current_state():
    newBell = Bell(3, 10)
    result = newBell.use()

    assert newBell.current_state == 4
    assert result == True


def test_bell_use_method_does_not_allow_use_if_broken():
    newBell = Bell(10, 10)
    result = newBell.use()
    assert result == False

    assert newBell.current_state == 10