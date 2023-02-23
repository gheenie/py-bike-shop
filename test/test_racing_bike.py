from src.component import (Bell, Brakes, Chain, Tyres)
from src.bikes import (RacingBike)


def test_has_a_5_percent_increase_on_tyres():

    new_bell = Bell(0, 10)
    new_brakes = Brakes(0, 20)
    new_chain = Chain(0, 30)
    new_tyres = Tyres(0, 40)

    new_racing_bike = RacingBike(new_bell, new_brakes, new_chain, new_tyres)

    assert new_racing_bike.components['tyres'].current_state == 0
    new_racing_bike.ride()

    assert new_racing_bike.components['tyres'].current_state == 4.2


def test_has_a_5_percent_increase_on_chain():

    new_bell = Bell(0, 10)
    new_brakes = Brakes(0, 20)
    new_chain = Chain(2, 30)
    new_tyres = Tyres(0, 40)

    new_racing_bike = RacingBike(new_bell, new_brakes, new_chain, new_tyres)

    assert new_racing_bike.components['chain'].current_state == 2
    new_racing_bike.ride()

    assert new_racing_bike.components['chain'].current_state == 5.15
