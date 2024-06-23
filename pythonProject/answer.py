class Car(object):
    def __init__(self,model = None):
        self.model = model
    def run(self):
        print('running')

class Toyota_car(Car):
    def run(self):
        print('Toyota')

class Tesla_car(Car):
    def __init__(self,model = 'Model S',enable_auto_run = False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

    def run(self,ai):
        print(f'super fast {ai}')

    def auto_run(self):
        print('auto run')


car = Car()
car.run()
print(car.model)
print('##############################################')
toyota_car = Toyota_car('す')
print(toyota_car.model)
toyota_car.run()
print('##############################################')
tesla = Tesla_car()
print(tesla.model)

tesla.run('aiko')
tesla.auto_run()