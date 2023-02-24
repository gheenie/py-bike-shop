from src.component import (Brakes)


def test_brakes_initializes_with_correct__current_state_max_lifespan():
    new_brakes = Brakes(4, 10)

    assert new_brakes.current_state == 4
    assert new_brakes.max_lifespan == 10

    assert new_brakes.check_condition() == 'Poor'


def test_brakes__use_method_increments_current_state():
    new_brakes = Brakes(3, 10)

    new_brakes.use()

    assert new_brakes.current_state == 5


# def test_brakes_use_method_does_not_allow_use_if_broken():
#     new_brakes = Brakes(10, 10)

#     new_brakes.use()

#     assert new_brakes.current_state == 10
