
class Car:
    price = 0

    def set_car_price(self, price):
        self.price = price

    def get_car_price(self):
        return self.price

    def set_car_brand(self, brand):
        self.brand = brand

    def get_car_brand(self):
        return self.brand

    def set_car_model(self, model):
        self.model = model
        # tesla models
        if (self.model == "Model S"):
            self.price += 25000
        elif (self.model == "Model 3"):
            self.price += 40000
        elif (self.model == "Model X"):
            self.price += 55000
        elif (self.model == "Model Y"):
            self.price += 50000
        # toyota car models
        elif (self.model == "2021 Prius"):
            self.price += 24525
        elif (self.model == "2021 Highlander hybrid"):
            self.price += 38410
        elif (self.model == "2021 C-HR"):
            self.price += 21445
        # chevy models
        elif (self.model == "2021 Trail blazer"):
            self.price += 19000
        elif (self.model == "2021 Trax"):
            self.price += 21300
        elif (self.model == "2021 Blazer"):
            self.price += 28800

    def get_car_model(self):
        return self.model

    # features functions
    def features(self, Interrior_leather, convertable, touchscreen):
        self.Interrior_leather = Interrior_leather
        self.convertable = convertable
        self.touchscreen = touchscreen
        if (self.Interrior_leather == 1):
            self.price += 800
        if (self.convertable == 1):
            self.price += 2000
        if (self.touchscreen == 1):
            self.price += 750


def main():
    
    user_car = Car()
    user_file1 = open('user_choice', 'r')
    last_line = ""
    try:
        last_line = user_file1.readlines()[-1]
    except IndexError:
        print()
    if (last_line == ""):
        print("hi welcome to the car shop you are our first customer")
    else:
        print(f"the file exist and the last selection was {last_line}")

    # asking for users car make
    user_name = input("Please enter your name here: ")
    user_file1.close()
    user_file1 = open("user_choice", 'a')
    try:
        user_make = int(input(
            "Please enter the following numbers for a make,\n1.) Tesla\n2.) Toyota\n3.) Chevy\nPlease enter your selection here:"))
        if (user_make == 1):
            user_car.set_car_brand("Tesla")  # setting the users car make in the set car make function
            # assuming user chose tesla brand they are now choosing the what model they want
            user_tesla_model = int(input(
                "Please enter the model of tesla you want,\n1.) Model S-$25000,\n2.) Model 3-$40000,\n3.) Model X-$55000,\n4.) Model Y-$50000\nPlease enter your selection here:"))
            if (user_tesla_model == 1):
                user_car.set_car_model("Model S")  # storing the model the user wants in the set car model function
                user_interior_input = int(
                    input("Please enter if you would like interior leather,\n1.) for yes($800)\n2.for no\nEnter selection: "))
                user_convertable_input = int(
                    input("Please enter if you would like a convertible car,\n1.)for yes($2000)\n2.)for no\nEnter selection: "))
                user_touchscreen_input = int(
                    input("Please enter if you would like a touch screen dashboard,\n1.)for yes($750)\n2.)for no\nEnter selection: "))
            if (user_tesla_model == 2):
                user_car.set_car_model("Model 3")  # storing the model the user wants in the set car model function
                user_interior_input = int(
                    input("Please enter if you would like interior leather,\n1.for yes($800)\n2.for no\nEnter selection: "))
                user_convertable_input = int(
                    input("Please enter if you would like a convertible car,\n1.for yes($2000)\n2.for no\nEnter selection: "))
                user_touchscreen_input = int(
                    input("Please enter if you would like a touch screen dashboard,\n1.for yes($750)\n2.for no\nEnter selection: "))
            if (user_tesla_model == 3):
                user_car.set_car_model("Model X")  # storing the model the user wants in the set car model function
                user_interior_input = int(
                    input("Please enter if you would like interior leather,\n1.)for yes($800)\n2.)for no\nEnter selection: "))
                user_convertable_input = int(
                    input("Please enter if you would like a convertible car,\n1.)for yes($2000)\n2.)for no\nEnter selection: "))
                user_touchscreen_input = int(
                    input("Please enter if you would like a touch screen dashboard,\n1.)for yes($750)\n2.)for no\nEnter selection: "))
            if (user_tesla_model == 4):
                user_car.set_car_model("Model Y")  # storing the model the user wants in the set car model function
                user_interior_input = int(
                    input("Please enter if you would like interior leather,\n1.)for yes($800)\n2.)for no\nEnter selection: "))
                user_convertable_input = int(
                    input("Please enter if you would like a convertible car,\n1.)for yes($2000)\n2.)for no\nEnter selection: "))
                user_touchscreen_input = int(
                    input("Please enter if you would like a touch screen dashboard,\n1.)for yes($750)\n2.)for no\nEnter selection: "))
        #toyota models
        if (user_make == 2):
            user_car.set_car_brand("Toyota")  # setting the users car make in the set car make function
            # assuming user chose tesla brand they are now choosing the what model they want
            user_chevy_model = int(input(
                "Please enter the model of Toyota you want,\n1.) for 2021 Prius-$24525,\n2.) for 2021 Highlander Hybrid-$38410,\n3.) for 2021 CH-R($21445)\nPlease enter your selection here:"))
            if (user_chevy_model == 1):
                user_car.set_car_model("2021 Prius")  # storing the model the user wants in the set car model function
                user_interior_input = int(
                    input("Please enter if you would like interior leather,\n1)for yes($800) \n2.)for no\nEnter selection: "))
                user_convertable_input = int(
                    input("Please enter if you would like a convertible car,\n1.)for yes($2000)\n2.)for no\nEnter selection: "))
                user_touchscreen_input = int(
                    input("Please enter if you would like a touch screen dashboard,\n1.)for yes($750)\n2).for no\nEnter selection: "))
            if (user_chevy_model == 2):
                user_car.set_car_model("2021 Highlander hybrid")  # storing the model the user wants in the set car model function
                user_interior_input = int(
                    input("Please enter if you would like interior leather,\n1.)for yes($800)\n2.)for no\nEnter selection: "))
                user_convertable_input = int(
                    input("Please enter if you would like a convertible car,\n1.)for yes($2000)\n2.)for no\nEnter selection: "))
                user_touchscreen_input = int(
                    input("Please enter if you would like a touch screen dashboard,\n1.)for yes($750)\n2.)for no\nEnter selection: "))
            if (user_chevy_model == 3):
                user_car.set_car_model("2021 C-HR")  # storing the model the user wants in the set car model function
                user_interior_input = int(
                    input("Please enter if you would like interior leather,\n1.)for yes($800)\n2.)for no\nEnter selection: "))
                user_convertable_input = int(
                    input("Please enter if you would like a convertible car,\n1.)for yes($2000)\n2.)for no\nEnter selection: "))
                user_touchscreen_input = int(
                    input("Please enter if you would like a touch screen dashboard,\n1.)for yes($750)\n2.)for no\nEnter selection: "))
        #Chevy models
        if (user_make == 3):
            user_car.set_car_brand("Chevy")  # setting the users car make in the set car make function
            # assuming user chose tesla brand they are now choosing the what model they want
            user_chevy_model = int(input(
                "Please enter the model of Chevy you want,\n1.) for 2021 Trail blazer-$19000,\n2.) for 2021 Trax-$21300,\n3.) for 2021 Blazer-$28800\nPlease enter your selection here:"))
            if (user_chevy_model == 1):
                user_car.set_car_model("2021 Trail blazer")  # storing the model the user wants in the set car model function
                user_interior_input = int(
                    input("Please enter if you would like interior leather,\n1.)for yes($800)\n2.)for no\nEnter selection: "))
                user_convertable_input = int(
                    input("Please enter if you would like a convertible car,\n1.)for yes($2000)\n2.)for no\nEnter selection: "))
                user_touchscreen_input = int(
                    input("Please enter if you would like a touch screen dashboard,\n1.)for yes($750)\n2.)for no\nEnter selection: "))
            if (user_chevy_model == 2):
                user_car.set_car_model("2021 Trax")  # storing the model the user wants in the set car model function
                user_interior_input = int(
                    input("Please enter if you would like interior leather,\n1.)for yes($800)\n2.)for no\nEnter selection: "))
                user_convertable_input = int(
                    input("Please enter if you would like a convertible car,\n1.)for yes($2000)\n2.)for no\nEnter selection: "))
                user_touchscreen_input = int(
                    input("Please enter if you would like a touch screen dashboard,\n1.)for yes($750)\n2.)for no\nEnter selection: "))
            if (user_chevy_model == 3):
                user_car.set_car_model("2021 Blazer")  # storing the model the user wants in the set car model function
                user_interior_input = int(
                    input("Please enter if you would like interior leather,\n1.)for yes($800)\n2.)for no\nEnter selection: "))
                user_convertable_input = int(
                    input("Please enter if you would like a convertible car,\n1.)for yes($2000)\n2.)for no\nEnter selection: "))
                user_touchscreen_input = int(
                    input("Please enter if you would like a touch screen dashboard,\n1.)for yes($750)\n2.)for no\nEnter selection: "))
    except ValueError:
        print("Please enter one of the options given")
        quit()


    user_car.features(user_interior_input, user_convertable_input, user_touchscreen_input)
    user_selection = user_name + ", " + user_car.get_car_brand() + " " + user_car.model + ", " + str(
    user_interior_input) + ", " + str(user_convertable_input) + ", " + str(user_touchscreen_input) + ", " + str(
    user_car.get_car_price()) + '\n'
    user_file1.write(user_selection)
    user_file1.close()

main()
