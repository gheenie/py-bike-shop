from src.component import (Component)

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