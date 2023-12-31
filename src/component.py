class Component:
    def __init__(self, current_state, max_lifespan):
        self.current_state = current_state
        self.max_lifespan = max_lifespan
    
    
    def set_current_state(self, desired_state):
        if desired_state == 'Pristine':
            self.current_state = 0

        if desired_state == 'Good':
            self.current_state = self.max_lifespan * 0.11
        

    def check_condition(self):
        percentage_lifespan = self.current_state / self.max_lifespan * 100
        condition = ''

        if percentage_lifespan <= 10:
            condition = 'Pristine'

        if 10 < percentage_lifespan <= 30:
            condition = 'Good'

        if 30 < percentage_lifespan <= 60:
            condition = 'Poor'

        if 60 < percentage_lifespan < 100:
            condition = 'Fragile'

        if percentage_lifespan >= 100:
            condition = 'Broken'

        print(f'The condition of the {type(self)} is {condition}.')

        return condition


class Bell(Component):
    def __init__(self, current_state, max_lifespan):
        super().__init__(current_state, max_lifespan)


    def use(self, multiplier=1):
        self.current_state += 1 * multiplier


class Brakes(Component):
    def __init__(self, current_state, max_lifespan):
        super().__init__(current_state, max_lifespan)


    def use(self, multiplier=1):
        self.current_state += 2 * multiplier


class Chain(Component):
    def __init__(self, current_state, max_lifespan):
        super().__init__(current_state, max_lifespan)


    def use(self, multiplier=1):
        self.current_state += 3 * multiplier


class Tyres(Component):
    def __init__(self, current_state, max_lifespan):
        super().__init__(current_state, max_lifespan)


    def use(self, multiplier=1):
        self.current_state += 4 * multiplier
