from src.component import (Bell, Brakes, Chain, Tyres)


class Bike:
    def __init__(self, bell, brakes, chain, tyres):
        self.components = {
            'bell': bell,
            'brakes': brakes,
            'chain': chain,
            'tyres': tyres
        }

    def ride(self):
        all_component_states = [
            self.components[key].check_condition() for key in self.components]

        if 'Broken' in all_component_states:
            message = 'bike is broken'
            print(message)
            return message

        for key in self.components:
            self.components[key].use()

        if 'Fragile' in all_component_states:
            message = 'fragile ride'

        elif 'Poor' in all_component_states:
            message = 'poor ride'

        else:
            message = 'perfect ride'

        print(message)
        return message

    def ring_bell(self):
        pass