from src.component import (Component, Bell, Brake, Chain, Tyres)


def test_initialise_component():
    newComponent = Component(9, 10)

    assert newComponent.current_state == 9
    assert newComponent.max_lifespan == 10


def test_check_condition():
    newComponent = Component(0, 10)
    assert newComponent.check_condition() == 'Pristine'
    newComponent = Component(1, 10)
    assert newComponent.check_condition() == 'Pristine'

    newComponent = Component(3, 10)
    assert newComponent.check_condition() == 'Good'

    newComponent = Component(6, 10)
    assert newComponent.check_condition() == 'Poor'

    newComponent = Component(9, 10)
    assert newComponent.check_condition() == 'Fragile'

    newComponent = Component(10, 10)
    assert newComponent.check_condition() == 'Broken'

    newComponent = Component(9, 100)
    assert newComponent.check_condition() == 'Pristine'

    newComponent = Component(99, 100)
    assert newComponent.check_condition() == 'Fragile'


def test_check_condition_errors():
    newComponent = Component(11, 10)
    assert newComponent.check_condition() == 'Broken'


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


def test_brakes_initializes_with_correct__current_state_max_lifespan():
    newbrake = Brake(4, 10)

    assert newbrake.current_state == 4
    assert newbrake.max_lifespan == 10

    assert newbrake.check_condition() == 'Poor'


def test_brakes__use_method_increments_current_state():
    newbrake = Brake(3, 10)
    result = newbrake.use()

    assert newbrake.current_state == 5
    assert result == True


def test_brakes_use_method_does_not_allow_use_if_broken():
    newbrake = Brake(10, 10)
    result = newbrake.use()
    assert result == False

    assert newbrake.current_state == 10

def test_chain_initializes_with_correct__current_state_max_lifespan():
    new_chain = Chain(15, 20)

    assert new_chain.current_state == 15
    assert new_chain.max_lifespan == 20

    assert new_chain.check_condition() == 'Fragile'


def test_chain__use_method_increments_current_state():
    new_chain = Chain(3, 10)
    result = new_chain.use()

    assert new_chain.current_state == 6
    assert result == True


def test_chain_use_method_does_not_allow_use_if_broken():
    new_chain = Chain(10, 10)
    result = new_chain.use()
    assert result == False

    assert new_chain.current_state == 10

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

