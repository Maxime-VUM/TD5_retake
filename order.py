lass Order:

    def __init__(self, quantity, price, is_a_buy, name):
        self.quantity = quantity
        self.price = price
        self.is_a_buy = is_a_buy
        self.name = name

    # method o1 == o2
    def __eq__(self, other):

        if(self.is_a_buy == other.is_a_buy):

            if(self.price == other.price):
                message = f"{self.name} and {other.name} are equal"

            else:
                message = f"{self.name} and {other.name} are not equal"

            print(message)
            file = open("output.txt", "a")
            file.write(message + "\n")
            file.close()

        else :
            print("ERROR : Impossible to compare a buy order with a sell order")
            file = open("output.txt", "a")
            file.write("ERROR : Impossible to compare a buy order with a sell order\n")
            file.close()

    # method o1 >= o2
    def __ge__(self, other):

        if(self.is_a_buy == other.is_a_buy):

            if(self.price > other.price):
                message = f"{self.name} is greater than {other.name}"
        
            elif(self.price == other.price):
                message = f"{self.name} and {other.name} are equal"

            else :
                message = f"{self.name} is lower than {other.name}"

            print(message)
            file = open("output.txt", "a")
            file.write(message + "\n")
            file.close()

        else :
            print("ERROR : Impossible to compare a buy order with a sell order")
            file = open("output.txt", "a")
            file.write("ERROR : Impossible to compare a buy order with a sell order\n")
            file.close()

    # method o1 <= o2
    def __le__(self, other):

        if(self.is_a_buy == other.is_a_buy):

            if(self.price < other.price):
                message = f"{self.name} is lower than {other.name}"

            elif(self.price == other.price):
                message = f"{self.name} and {other.name} are equal"

            else:
                message = f"{self.name} is greater than {other.name}"

            print(message)
            file = open("output.txt", "a")
            file.write(message + "\n")
            file.close()

        else :
            print("ERROR : Impossible to compare a buy order with a sell order")
            file = open("output.txt", "a")
            file.write("ERROR : Impossible to compare a buy order with a sell order\n")
            file.close()

    # method to add o1 and o2
    def __add__(self, other):
        
        if(self.is_a_buy == other.is_a_buy):
            new_quantity = self.quantity + other.quantity
            new_price = (self.quantity * self.price + other.quantity * other.price) / (self.quantity + other.quantity)
            message = f"New quantity = {new_quantity}\nNew price = {new_price}"
            print(message)
            file = open("output.txt", "a")
            file.write(message + "\n")
            file.close()

        else :
            print("ERROR : Impossible to add a buy order to a sell order")
            file = open("output.txt", "a")
            file.write("ERROR : Impossible to add a buy order to a sell order\n")
            file.close()

    # method to display properties, we overload the str method
    def __str__(self):

        if(self.is_a_buy == True):
            order_type = "Buy"

        else :
            order_type = "Sell"

        message = f"Properties of the order :\nQuantity = {self.quantity}\nPrice = {self.price}\nType = " + order_type
        file.open("output.txt", "a")
        file.write(message + "\n")
        file.close()
        return message
