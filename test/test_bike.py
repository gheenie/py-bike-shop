from src.component import (Bell, Brakes, Chain, Tyres)
from src.bikes import (Bike)

def test_initialising_bike():
    new_bell = Bell(0, 10)
    new_brakes = Brakes(0, 20)
    new_chain = Chain(0, 30)
    new_tyres = Tyres(0, 40)
    new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres)

    assert len(new_bike.components) == 4
    assert new_bike.components['bell'] is new_bell
    assert new_bike.components['brakes'] is new_brakes
    assert new_bike.components['chain'] is new_chain
    assert new_bike.components['tyres'] is new_tyres

    new_bell.use()
    assert new_bike.components['bell'].current_state == 1
    new_bike.components['bell'].use()
    assert new_bell.current_state == 2

    # another_bell = Bell(0, 10)
    # assert new_bike.components['bell'] == another_bell

def test_ride_when_no_components_are_broken():
    new_bell = Bell(0, 10)
    new_brakes = Brakes(0, 20)
    new_chain = Chain(0, 30)
    new_tyres = Tyres(0, 40)
    new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres)

    message = new_bike.ride()

    assert message == 'perfect ride'
    assert new_bike.components['bell'].current_state == 1
    assert new_bike.components['brakes'].current_state == 2
    assert new_bike.components['chain'].current_state == 3
    assert new_bike.components['tyres'].current_state == 4

def test_ride_when_at_least_1_component_is_broken():
    new_bell = Bell(0, 10)
    new_brakes = Brakes(0, 20)
    new_chain = Chain(0, 30)
    new_tyres = Tyres(40, 40)
    new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres)

    message = new_bike.ride()

    assert message == 'bike is broken'
    assert new_bike.components['bell'].current_state == 0
    assert new_bike.components['brakes'].current_state == 0
    assert new_bike.components['chain'].current_state == 0
    assert new_bike.components['tyres'].current_state == 40
