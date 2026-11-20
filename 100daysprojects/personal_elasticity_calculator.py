def init():
    print("Welcome to your elasticity Calculator")
    print("Here you will know how much elastic is your product")

    price_1 = int(input("What was the initial price of your product:\n"))
    quantity_1 = int(input("How much do you sell with your initial price:\n"))
    price_2 = int(input("What was the final price of your product:\n"))
    quantity_2 = int(input("How much do you sell with your final price:\n"))

    elasticity = -(((quantity_2 - quantity_1) / ((quantity_2 + quantity_1)/ 2)) 
                   /((price_2 - price_1) / ((price_2 + price_1)/ 2)))

    print(f"The elasticity of your product is {elasticity}")



if __name__ == '__main__':
    init()