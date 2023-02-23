class Component:
    def __init__(self, current_state, max_lifespan):
        self.current_state = current_state
        self.max_lifespan = max_lifespan

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
        
        print(f'The condition of the bike is {condition}.')

        return condition
    