from src.component import (Chain)


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
