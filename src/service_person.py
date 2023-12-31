from src.component import (Bell, Brakes, Chain, Tyres)


class ServicePerson:
    def __init__(self, bike):
        self.current_bike = bike


    def order_parts(self):
        fresh_parts = {
            'bell': Bell(0, 10),
            'brakes': Brakes(0, 20),
            'chain': Chain(0, 30),
            'tyres': Tyres(0, 40)
        }

        for key, component in self.current_bike.components.items():
            if component.check_condition() == 'Broken':
                self.current_bike.components[key] = fresh_parts[key]


    def service_parts(self):
        for component in self.current_bike.components.values():
            if component.check_condition() in ['Fragile', 'Poor']:
                component.set_current_state('Good')


    def oil(self):
        for key, component in self.current_bike.components.items():
            if component.check_condition() == 'Good' and key.capitalize() in ['Chain', 'Bell', 'Brakes']:
                component.set_current_state('Pristine')


    def pump_wheels(self):
        tyres = self.current_bike.components['tyres']

        if tyres.check_condition() == 'Good':
            tyres.set_current_state('Pristine')


    def service_bike(self):
        self.service_parts()
        self.oil()
        self.pump_wheels()


    def check_safety(self):
        if self.current_bike.ring_bell() == 'The bell fell off!':
            return False

        return self.current_bike.components['brakes'].check_condition() in ['Good', 'Pristine']


    def check_up(self):
        self.order_parts()
        self.service_bike()

        if self.check_safety():
            return self.current_bike.ring_bell()

        return 'there has been an error'
