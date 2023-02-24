from src.component import (Bell, Brakes, Chain, Tyres)
from src.bikes import (StreetBike)


def test_has_a_5_percent_increase_on_brakes():
    new_bell = Bell(0, 10)
    new_brakes = Brakes(0, 20)
    new_chain = Chain(0, 30)
    new_tyres = Tyres(0, 40)
    new_street_bike = StreetBike(new_bell, new_brakes, new_chain, new_tyres)

    new_street_bike.ride()

    assert new_street_bike.components['brakes'].current_state == 2.1

    new_street_bike.ride()

    assert new_street_bike.components['brakes'].current_state == 4.2
