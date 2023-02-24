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
        pass

    def service_bike(self):
        pass

    def check_safety(self):
        pass

    def check_up(self):
        pass


