from src.component import (Bell, Chain, Tyres)
from src.bikes import (BMXBike)


def test_tyres_wear_15_percent_more_per_ride():
    new_bell = Bell(0, 10)
    new_chain = Chain(0, 30)
    new_tyres = Tyres(0, 40)
    new_bmx_bike = BMXBike(
        new_bell, new_chain, new_tyres)

    new_bmx_bike.ride()

    assert new_bmx_bike.components['tyres'].current_state == 4.6

    new_bmx_bike.ride()

    assert new_bmx_bike.components['tyres'].current_state == 9.2


def test_no_brake_component():
    new_bell = Bell(0, 10)
    new_chain = Chain(0, 30)
    new_tyres = Tyres(0, 40)
    new_bmx_bike = BMXBike(
        new_bell, new_chain, new_tyres)

    assert new_bmx_bike.components.get('brakes') == None
