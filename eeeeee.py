class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
         print(f"The name of the train is {self.name}")
         print(f"The total seats available in the train are {self.seats}")

    def fearDetails(self):
        print(f"The pries of the tickets is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print(f"Sorry this train is full!! kindly try tatkal")

rajdhani_expess = Train("Rajdhani Express: 12022",50,2)
rajdhani_expess.getStatus()
rajdhani_expess.bookTicket()
rajdhani_expess.bookTicket()
rajdhani_expess.bookTicket()
rajdhani_expess.getStatus()
