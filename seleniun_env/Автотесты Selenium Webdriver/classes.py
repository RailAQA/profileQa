class AutoMobile:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year


class Engine(AutoMobile):
    def __init__(self, name, model, year, enmodel, price):
        super().__init__(name, model, year)
        self.enmodel = enmodel
        self.price = price

    
    def calculate_price_eng(self):
        if self.enmodel[0] == 'Б':
            return self.price + 500000
        
GLE = Engine('Мерс', 'Гелик', 2025, 'Брабус', 20000000)
print(GLE.calculate_price_eng())
        

