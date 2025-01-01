class car:   
    def __init__(self, brand: str, fuel_type: str) -> None:
        self.brand = brand
        self.fuel_type = fuel_type
    
    def drive(self, distance: float)  -> None: 
        print(f"Driving {self.brand} for {distance} km [{self.fuel_type}]")

vovle: car = car(brand="volve", fuel_type = "Diesel"  )

print(vovle.brand)
print(vovle.fuel_type)
