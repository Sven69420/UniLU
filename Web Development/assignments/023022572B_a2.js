let parkingManager = {
    drivers: [], //Array to store driver objects
    
    //List parked Cars
    listParkedCars() {
      const parkedCars = []; //Array to store parked car objects
      for (const driver of this.drivers) {
        for (const car of driver.cars) {
          if (car.checkOutTime === null) { //Cecks if the car is still parked
            parkedCars.push(car);
          }
        }
      }
      return parkedCars;
    },
  
    //Park Car Module
    parkCar(driverName, driverLicense, carNumber, checkInTime) {
      const existingDriver = this.drivers.find((driver) => driver.driverLicense === driverLicense);
      if (existingDriver) {
        //Check if the driver already has a parked car or if the car plate (carNumber) has already been parked
        if (existingDriver.cars.find((car) => car.checkOutTime === null) || this.listParkedCars().find((car) => car.carNumber === carNumber)) {
          return false; //Car can't be parked
        }
        existingDriver.cars.push({ carNumber, checkInTime, checkOutTime: null });
      } else {
        //Create a new driver and park the car
        this.drivers.push({
          driverName,
          driverLicense,
          cars: [{ carNumber, checkInTime, checkOutTime: null }],
        });
      }
      return true;
    },
  
    //Unpark Car Module
    unparkCar(carNumber, unparkDateTime) {
      const foundCar = this.listParkedCars().find((car) => car.carNumber === carNumber && car.checkOutTime === null);
      if (foundCar) {
        //Updates the check out time for the unparked car
        foundCar.checkOutTime = unparkDateTime;
        return true; //car is succesfully unparked
      } else {
        return false; //car cannot be found / already unparked
      }
    },
  
    //Get the cars history by drivers license
    historyByDriver(driverLicense) {
      const driver = this.drivers.find((driver) => driver.driverLicense === driverLicense);
      //returns false if the driver is not found, otherwise returns the cars history
      return driver ? driver.cars : false; 
    },
  
    //Get the cars history by plate number
    historyByCarNumber(carNumber) {
      const history = [];
      for (const driver of this.drivers) {
        for (const car of driver.cars) {
          if (car.carNumber === carNumber) {
            history.push(car);
          }
        }
      }
      //Same as above just with plate number method instead of divers license
      return history.length === 0 ? false : history;
    },
  
    //Calculates total hours a car has been parked
    totalHoursByCar(carNumber) {
      const carHistory = this.historyByCarNumber(carNumber);
      if (!carHistory) {
        return false; //Car not found
      }
      
      let totalHours = 0;
      for (const car of carHistory) {
        if (car.checkOutTime === null) {
          if (carHistory.length === 1) {
            return false; //Car is still parked
          }
          continue; //Skip currently parked cars
        }
        totalHours += (car.checkOutTime - car.checkInTime);
      }
      
      return (totalHours / 36e5); //Conversion to total hours with 2 decimals
    }
  };
  