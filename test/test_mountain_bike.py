from src.component import (Bell, Brakes, Chain, Tyres)
from src.bikes import (MountainBike)


def test_has_a_15_percent_stronger_chain():

    new_bell = Bell(0, 10)
    new_brakes = Brakes(0, 20)
    new_chain = Chain(0, 30)
    new_tyres = Tyres(0, 40)

    new_mountain_bike = MountainBike(
        new_bell, new_brakes, new_chain, new_tyres)

    assert new_mountain_bike.components['chain'].current_state == 0

    new_mountain_bike.ride()
    assert new_mountain_bike.components['chain'].current_state == 2.55

    new_mountain_bike.ride()
    assert new_mountain_bike.components['chain'].current_state == 5.1
