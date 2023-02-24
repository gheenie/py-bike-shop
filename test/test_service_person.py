from src.bikes import (Bike, RacingBike, BMXBike, MountainBike, StreetBike)
from src.component import (Bell, Brakes, Chain, Tyres)
from src.service_person import (ServicePerson)


def test_has_current_bike_property_with_bike_instance():

    new_bell = Bell(0, 10)
    new_brakes = Brakes(0, 20)
    new_chain = Chain(0, 30)
    new_tyres = Tyres(0, 40)

    new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres)

    john = ServicePerson(new_bike)

    assert john.current_bike is new_bike


def test_order_parts_should_replace_any_broken_parts_to_pristine():

    new_bell = Bell(0, 10)
    new_brakes = Brakes(20, 20)
    new_chain = Chain(0, 30)
    new_tyres = Tyres(41, 40)

    new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres)

    john = ServicePerson(new_bike)
    john.order_parts()

    assert new_bike.components['brakes'].current_state == 0
    assert new_bike.components['tyres'].current_state == 0

    assert new_bike.components['brakes'] is not new_brakes
    assert new_bike.components['tyres'] is not new_tyres


def test_service_parts_should_change_any_fragile_poor_parts_to_good():

    new_bell = Bell(2, 10)
    new_brakes = Brakes(10, 20)
    new_chain = Chain(26, 30)
    new_tyres = Tyres(40, 40)

    new_bike = MountainBike(new_bell, new_brakes, new_chain, new_tyres)

    john = ServicePerson(new_bike)
    john.service_parts()

    assert new_bike.components['bell'].current_state == 2
    assert new_bike.components['chain'].current_state == 3.3
    assert new_bike.components['brakes'].current_state == 2.2
    assert new_bike.components['tyres'].current_state == 40

    assert new_bike.components['bell'] is new_bell
    assert new_bike.components['chain'] is new_chain
    assert new_bike.components['brakes'] is new_brakes
    assert new_bike.components['tyres'] is new_tyres


def test_oil_should_change_brake_chain_bell_from_good_to_pristine():

    new_bell = Bell(2, 10)
    new_brakes = Brakes(12, 20)
    new_chain = Chain(1, 30)
    new_tyres = Tyres(40, 40)

    new_bike = MountainBike(new_bell, new_brakes, new_chain, new_tyres)

    john = ServicePerson(new_bike)
    john.oil()

    assert new_bike.components['bell'].current_state == 0
    assert new_bike.components['chain'].current_state == 1
    assert new_bike.components['brakes'].current_state == 12
    assert new_bike.components['tyres'].current_state == 40

    assert new_bike.components['bell'] is new_bell
    assert new_bike.components['chain'] is new_chain
    assert new_bike.components['brakes'] is new_brakes
    assert new_bike.components['tyres'] is new_tyres


def test_pump_wheels_tyres_from_good_to_pristine():

    new_bell = Bell(2, 10)
    new_brakes = Brakes(12, 20)
    new_chain = Chain(1, 30)
    new_tyres = Tyres(6, 40)

    new_bike = RacingBike(new_bell, new_brakes, new_chain, new_tyres)

    john = ServicePerson(new_bike)
    john.pump_wheels()

    assert new_bike.components['bell'].current_state == 2
    assert new_bike.components['chain'].current_state == 1
    assert new_bike.components['brakes'].current_state == 12
    assert new_bike.components['tyres'].current_state == 0

    assert new_bike.components['bell'] is new_bell
    assert new_bike.components['chain'] is new_chain
    assert new_bike.components['brakes'] is new_brakes
    assert new_bike.components['tyres'] is new_tyres

    second_tyres = Tyres(10, 10)
    new_bike.components['tyres'] = second_tyres

    john.pump_wheels()
    assert new_bike.components['tyres'].current_state == 10

def test_service_bike_should_invoke_service_parts_oil_pump_wheels_methods():

    new_bell = Bell(10, 10)
    new_brakes = Brakes(18, 20)
    new_chain = Chain(1, 30)
    new_tyres = Tyres(6, 40)

    new_bike = StreetBike(new_bell, new_brakes, new_chain, new_tyres)

    john = ServicePerson(new_bike)
    john.service_bike()

    assert new_bike.components['bell'].current_state == 10
    assert new_bike.components['chain'].current_state == 1
    assert new_bike.components['brakes'].current_state == 0
    assert new_bike.components['tyres'].current_state == 0

    assert new_bike.components['bell'] is new_bell
    assert new_bike.components['chain'] is new_chain
    assert new_bike.components['brakes'] is new_brakes
    assert new_bike.components['tyres'] is new_tyres

def test_check_safety_ring_bell_and_check_brakes_are_good_or_pristine():

    new_bell = Bell(2, 10)
    new_brakes = Brakes(15, 20)
    new_chain = Chain(1, 30)
    new_tyres = Tyres(6, 40)

    new_bike = RacingBike(new_bell, new_brakes, new_chain, new_tyres)

    john = ServicePerson(new_bike)
    result = john.check_safety()

    assert result == False


    new_bell = Bell(9, 10)
    new_brakes = Brakes(2, 20)
    new_chain = Chain(19, 30)
    new_tyres = Tyres(40, 40)

    new_bike = RacingBike(new_bell, new_brakes, new_chain, new_tyres)

    john = ServicePerson(new_bike)
    result = john.check_safety()

    assert result == False

    new_bell = Bell(9, 10)
    new_brakes = Brakes(5, 20)
    new_chain = Chain(19, 30)
    new_tyres = Tyres(25, 40)

    new_bike = RacingBike(new_bell, new_brakes, new_chain, new_tyres)

    john = ServicePerson(new_bike)
    result = john.check_safety()

    assert result == True


   

    
