class Bike:
    def __init__(self, bell, brakes, chain, tyres): #alternative would be to pass in components as dictionary
        self.components = {
            'bell': bell,
            'brakes': brakes,
            'chain': chain,
            'tyres': tyres
        }


    def use_components(self):
        for key in self.components:
            self.components[key].use()


    def ride(self):
        all_component_states = [
            self.components[key].check_condition() for key in self.components]

        if 'Broken' in all_component_states:
            message = 'bike is broken'
            print(message)
            return message

        self.use_components()

        if 'Fragile' in all_component_states:
            message = 'fragile ride'

        elif 'Poor' in all_component_states:
            message = 'poor ride'

        else:
            message = 'perfect ride'

        print(message)
        return message


    def ring_bell(self):

        all_component_states = [
            self.components[key].check_condition() for key in self.components]

        if 'Broken' in all_component_states:
            message = 'The bell fell off!'
            print(message)
            return message

        if 'Fragile' in all_component_states:
            message = 'Ring! cling...'

        else:
            message = 'Ring! Ring! Ring!'

        print(message)
        return message

    # def __eq__(self?):
    # def __str__(self?):


class RacingBike(Bike):
    def __init__(self, bell, brakes, chain, tyres):
        super().__init__(bell, brakes, chain, tyres)


    def use_components(self):
        self.components['chain'].use(1.05)
        self.components['brakes'].use()
        self.components['bell'].use()
        self.components['tyres'].use(1.05)


class BMXBike(Bike):
    def __init__(self, bell, chain, tyres):
        super().__init__(bell, None, chain, tyres)
        del self.components['brakes']


    def use_components(self):
        self.components['chain'].use()
        self.components['bell'].use()
        self.components['tyres'].use(1.15)


class MountainBike(Bike):
    def __init__(self, bell, brakes, chain, tyres):
        super().__init__(bell, brakes, chain, tyres)


    def use_components(self):
        self.components['chain'].use(0.85)
        self.components['brakes'].use()
        self.components['bell'].use()
        self.components['tyres'].use()


class StreetBike(Bike):
    def __init__(self, bell, brakes, chain, tyres):
        super().__init__(bell, brakes, chain, tyres)


    def use_components(self):
        self.components['chain'].use()
        self.components['brakes'].use(1.05)
        self.components['bell'].use()
        self.components['tyres'].use()
