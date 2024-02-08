import datetime
class CarManager:
    all_cars = []
    total_cars = 0
    def __init__(self,make,model, year=None, mileage=None,services=[]):
      self._id = CarManager.total_cars
      self._make = make
      self._model = model
      self.year = year
      self._mileage = mileage
      self._services = services
      # Update total_cars and create id for this car
      CarManager.total_cars += 1
      #Update all_cars : power of self
      CarManager.all_cars.append(self)

    @property
    def year(self):
        return self._year  # Accessing the private variable through a getter

    @year.setter
    def year(self, value):
        
        if value is None or (1900 <= value <= datetime.datetime.now().year):
            self._year = value
        else:
            raise ValueError(f"Invalid year: {value}")
     
    
    def __str__(self):
        #removed services output
        return f'ID: {self._id} | MAKE: {self._make} | MODEL: {self._model} | YEAR: {self._year} | MILEAGE: {self._mileage} | SERVICES: (View in Car Details) |'

    def __repr__(self):
       return str(self)
      
    @classmethod
    def set_add_a_car(cls):
        print('-----------------------ADDING NEW VEHICLE --------------------------') 
        n_make  =input("VEHICLE MAKE:")
        n_model =input("VEHICLE MODEL:")
        n_year =int(input("VEHICLE YEAR:"))
        n_milelage =input("VEHICLE MILEAGE:")
        n_services =input("VEHICLE SERVICES:")
        service_order = [{
            'Date Added': str(datetime.datetime.now()),
            'Service Done': n_services
        }]
        # try:
        #      n_year =int(input("VEHICLE YEAR:"))
        # except ValueError as e:
        #     print(f'Error Occured: {e}')
                 
        
        try:
            new_whip = cls(n_make,n_model,n_year,n_milelage,service_order)
        except ValueError as e:
            print(f'Error Occured: {e}')
            return
        #CarManager.all_cars.append(vehicle)
        print('-----------------------VEHICLE ADDED--------------------------------') 
        print(CarManager.all_cars[new_whip._id])
    @classmethod
    def view_all_cars(cls):
         
        print('-----------------------VIEWING ALL VEHICLES ------------------------')
      

        for vehicles in CarManager.all_cars:
            print(vehicles)
      
    @classmethod
    def view_total_number_of_cars(cls):
       
        print('-----------------------TOTAL CAR INVENTORY---------------------------')
        
        return print(CarManager.total_cars)
     
    @classmethod
    def see_car_details(cls):
       
        print('--------------------SEE VEHICLE DETAILS BY ID------------------------')
  
        n_id = int(input("INPUT VEHICLE ID : "))
        print(CarManager.all_cars[n_id])
        for service_records in CarManager.all_cars[n_id]._services:
            print(service_records)

    
    @classmethod
    def service_a_car(cls):
        print('--------------------SEE VEHICLE DETAILS BY ID------------------------')
        
        n_id = int(input("INPUT VEHICLE ID : "))
        service_added = input("SERVICE ADDED : ")
        service_order = {
            'Date Added': str(datetime.datetime.now()),
            'Service Done': service_added
        }
        cls.all_cars[n_id]._services.append(service_order)

    @classmethod
    def update_mileage(cls):
      
        print('---------------UPDATE VEHICLE MILEAGE BY VEHICLE ID------------------')
        
      
        n_id = int(input("INPUT VEHICLE MILEAGE BY ID : "))
        new_mileage = input("NEW MILEAGE : ")
        cls.all_cars[n_id]._mileage = new_mileage
           

class CarData(CarManager):
    
    def __init__(self, make, model, year=None, mileage=None, services=[]):
        super().__init__(make, model, year, mileage, services)

    CarManager("HONDA", "CIVIC", 2010, 150000, 'Tire Rotation')
    CarManager("FORD", "F-150", 2015, 120000, 'Brake Inspection')
    CarManager("CHEVROLET", "IMPALA", 2008, 175000, 'Engine Tune-up')
    CarManager("BMW", "3 SERIES", 2019, 45000, 'Oil Change')
    CarManager("NISSAN", "ALTIMA", 2013, 130000, 'Transmission Flush')
    CarManager("SUBARU", "OUTBACK", 2017, 90000, 'Air Filter Replacement')
    CarManager("TESLA", "MODEL 3", 2020, 25000, 'Battery Check')
    CarManager("VOLKSWAGEN", "GOLF", 2014, 110000, 'Brake Pad Replacement')
    CarManager("JEEP", "WRANGLER", 2018, 70000, 'Suspension Repair')
    CarManager("HYUNDAI", "ELANTRA", 2011, 160000, 'Coolant Flush')




class CarManagerWindow(CarData):

    VIEW_CARS = CarManager.view_all_cars
    ADD_CARS = CarManager.set_add_a_car
    VIEW_TOTAL_CARS = CarManager.view_total_number_of_cars
    SERVICE_CAR = CarManager.service_a_car
    VEHICLE_DETAILS= CarManager.see_car_details
    UPDATE_VEHICLE_MILEAGE = CarManager.update_mileage

    
    def __init__(self, make, model, year=None, mileage=None, services=[]):
        super().__init__(make, model, year, mileage, services)
    
    @classmethod
    def auto_shop(cls):
     
        print('---------------------------WELCOME-----------------------------------')
        print('\n\n')
        print('-----------------SEE AVAILABLE SERVICES BELOW------------------------')
        print('\n')
        print('1. View All Vehicles \n2. Add a Vehicles\n3. View Total Inventory Count\n4. Log Services Done on Vehicle\n5. See Vehicle Details\n6. Update Vehicle Mileage\n7. Quit Management System')
        action = input('Type number to select service: ')
        program_setting = int(action)
        while program_setting != 7:
            match program_setting:
                case 1:
                    cls.VIEW_CARS()
                case 2:
                    cls.ADD_CARS()
                case 3:
                    cls.VIEW_TOTAL_CARS()
                case 4:
                    cls.SERVICE_CAR()
                case 5:
                    cls.VEHICLE_DETAILS()
                case 6:
                    cls.UPDATE_VEHICLE_MILEAGE()
                case _:
                    print("Invalid option, please try again.")
            print('---------------------------------------------------------------------')
            print('1. View All Vehicles \n2. Add a Vehicles\n3. View Total Inventory Count\n4. Log Services Done on Vehicle\n5. See Vehicle Details\n6. Update Vehicle Mileage\n7. Quit Management System')
            print('---------------------------------------------------------------------')
            action = input('Select new action or Quit Management System by pressing 7:  ')
            program_setting = int(action)
        


CarManagerWindow.auto_shop()