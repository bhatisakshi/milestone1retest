#Question-1: Create shopping cart class with methods like:
# Adding non-existing product
# removing product
# Updating quantity/price of product
# calculating total unique products
# Calculating total price of product

class ShoppingCart:
    def __init__(self):
        self.cart={}
        
    def add_product(self,name,quantity,price):
        if name not in self.cart:
            if quantity is not None:
                self.cart[name]={'Price':price, 'Quantity':quantity}
            else:
                self.cart[name]={'Price':price, 'Quantity':1}
            print(f"Product '{name}' added successfully!")
        else:
            print(f"Product '{name}' does not exist!")

    def remove_product(self,name):
        if name in self.cart:
            del self.cart[name]
            print(f"Product '{name}' deleted successfully!")
        else:
            print(f"Product '{name}' does not exist in cart!")   
            
    def update_product(self,name,new_price=None,new_quantity=None):
        if name in self.cart:
            if new_price is not None:
                if new_price is not None:
                    self.cart[name]={'Price': new_price,'Quantity': new_quantity}    
            print(f"Product '{name}' updated successfully!")
        else:
            print(f"Product '{name}' does not exist in cart!")   
            
    def cal_total_unique_prod(self):
        if self.cart:
            count=0
            for x in self.cart.items():
                count+=1
            print(f"The total no. of unique products in the cart are: {count}")
        else:
            print("The cart is empty!")
    
    def cal_total_price(self):
        if self.cart:
            total=0
            for x,y in self.cart.items():
                total+={y['Price']}*{y['Quantity']}
            print(f"Total price of all products in the cart is: {total}")
        else:
           print("The cart is empty!") 
           
mycart=ShoppingCart()

while True:
    
    print("Operations: ")   
    print("1. Add product")
    print("2. Remove product")
    print("3. Update product")
    print("4. Calculate total unique products")
    print("5. Calculate total price")
    print("6. Exit")    
    
    choice=int(input("Enter choice: "))
    
    if choice==1:
        value=int(input("Enter the number of products you want to add: "))     
        for x in range(value):
            name=input("Enter product name: ")
            quantity=int(input("Enter quantity: "))
            price=float(input("Enter price: "))
            mycart.add_product(name,quantity,price)
        
    elif choice==2:
        name=input("Enter product name: ")
        mycart.remove_product(name)
        
    elif choice==3:     
        name=input("Enter product name: ")
        quantity=int(input("Enter quantity: "))
        price=float(input("Enter price: "))
        mycart.update_product(name,quantity,price)
        
    elif choice==4:
        mycart.cal_total_unique_prod()
        
    elif choice==5:
        mycart.cal_total_price()
        
    elif choice==6:
        print("Exiting...")
        break
        
    else:
        print("invalid choice. please choose again!")
    
            