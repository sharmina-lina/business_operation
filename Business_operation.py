import json

class Wares:
    def __init__(self,name,buy_price):
        self.name = name
        self.buy_price = buy_price
class Business:
    def __init__(self,name, money = 0):
        self.name = name
        self.wares = {}
        self.deals = {}
        self.money = money

    def restock_wares(self, ware_name, ware_quatity,buy_price):
        
        cost = ware_quatity * buy_price
        print(self.money)
        if self.money < cost:
           print(f"Not have enough money to restock {ware_name}")
        else:
           if ware_name in self.wares:
            self.wares[ware_name]['quantity'] += ware_quatity
           else:
            self.wares[ware_name] = {'quantity': ware_quatity, 'buy_price': buy_price}
            self.money -= cost
            print(f"Restocked {ware_quatity} {ware_name} for ${cost:.2f}.")
            
        


    def check_price(self,ware_name):
       if ware_name in self.wares:
          if ware_name in self.deals:
             discount_percent = self.deals[ware_name]
             price = self.wares[ware_name]['buy_price']*(1-discount_percent/100)
             return price
          else:
            price = self.wares[ware_name]['buy_price']
            return price
          
       return None
    
    def check_availability(self, ware_name):
       if ware_name in self.wares:
          quantity = self.wares[ware_name]['quantity']
          return quantity
       return 0
     

    def sell_wares(self,ware_name,quantity):
       if ware_name in self.wares:
          if self.wares[ware_name]['quantity'] >= quantity:
             price = self.check_price(ware_name)
             if price:
                revenue = price*quantity
                self.wares[ware_name]['quantity'] -= quantity
                self.money += revenue
                print(f"Sold {quantity} {ware_name} for ${revenue:.2f}")
             else:
                print(f"No Price information available for  {ware_name}")
          else:
             print(f" {quantity} {ware_name} is not in the stock")
       else:
          print(f"{ware_name} is not available in the inventory.")
             
                

    def add_deals(self,ware_name,discount_percent):
       if ware_name in self.wares:
          self.deals[ware_name] = discount_percent
          print(f"New deal for {ware_name}: {discount_percent}% off")
       else:
          print(f"{ware_name} not found in inventory. cannot add a deal")

    def remove_deals(self,ware_name):
       if ware_name in self.wares:
          del self.deals[ware_name]
          print(f"Deals for {ware_name} removed.")
       else:
          print(f"No deal found for {ware_name} ")


def save_business_data(businesses):
   data = {}

   for business in businesses:
      data[business.name] = {
         "money" : business.money,
         "wares" : business.wares,
         "deals" : business.deals
         
      }

   with open("business_data.json", "w") as file:
        json.dump(data,file)
      

def load_business_data():
    try:
        with open("business_data.json","r") as file:
            data = json.load(file)
        businesses = []
        for name, info in data.items():
            business = Business (name, info["money"])   
            business.wares = info["wares"]
            business.deals = info["deals"]
            businesses.append(business)

        return businesses
    except FileNotFoundError:
       return []
    



def main():
   businesses = load_business_data()
   while True:
      print("1. Create a new business")
      print("2. Manage your existing business")
      print("3. Exit")

      choice = input("Enter Your Choice? ")


      if choice == "1":
         name = input("Enter your business name? ")
         money = int(input("Enter your Initial deposit: "))
         business = Business(name,money)
         businesses.append(business)
         print(f"New Business {name} created with initial deposit ${money}")
      
      elif choice == "2":
         if not businesses:
            print("No Business found. Creat a new Business ")
            continue
         print("Please select a business to manage")

         for i, business in enumerate(businesses):
            print(f"{i+1}. {business.name}")

         try:
            business_number = int(input("Please Enter the number of Business: ")) -1
            if 0 <= business_number < len(businesses):
               current_business = businesses[business_number]
            
               while True:
                print(f"Selected Business name: {current_business.name}")
                print("1. Restock Wares")
                print("2. Check Price")
                print("3. Check Availability")
                print("4. Sell Wares")
                print("5. Add Deal")
                print("6. Remove Deal")
                print("7. Exit to the Main Menu")

                menu_choice = input("Enter Your Choice: ")

                if menu_choice == "1":
                   ware_name = input("Enter the name of the ware: ")
                   ware_quantity = int(input("Enter the quantity of restock: "))
                   ware_price = float(input("Enter the buy price of the ware: "))
                   current_business.restock_wares(ware_name,ware_quantity,ware_price)
                elif menu_choice == "2":
                   ware_name = input("Enter the name of ware: ")
                   price = current_business.check_price(ware_name)
                   if price:
                      print(f"Price of {ware_name}: {price:.2f}")
                   else:
                      print(f" No Price Information available for {ware_name}")
                elif menu_choice == "3":
                   ware_name = input("Enter the name of the ware : ")
                   availability = current_business.check_availability(ware_name)
                   print(f"Availability of {ware_name}: {availability}")
                elif menu_choice == "4":
                   ware_name = input("Enter the name of the ware: ")
                   quantity = int(input("Enter the quantity of sell: "))
                   current_business.sell_wares(ware_name,quantity)
                elif menu_choice == "5":
                   ware_name = input("Enter the name of the ware: ")
                   discount_percent = float(input("Enter the discount percent: "))
                   current_business.add_deals(ware_name,discount_percent)
                elif menu_choice == "6":
                   ware_name = input("Enter the name of the ware: ")
                   current_business.remove_deals(ware_name)
                elif menu_choice == "7":
                   save_business_data(businesses)
                   break
                else:
                   print("Invalid Selection.Please select a valid number for managing your Business")

         except ValueError:
            print("Invalid input. Please enter a number.")
            
        
      
      elif choice == "3":
         save_business_data(businesses)
         print("Existing the program")
         break
      
      else:
         print("Invalid Number! Please Enter a valid choice:")


if __name__ == "__main__":
   main()
   
         







        