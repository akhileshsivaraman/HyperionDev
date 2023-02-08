#==== Define the shoe class ====
class Shoe:

  def __init__(self, country, code, product, cost, quantity):
    self.country = country
    self.code = code
    self.product = product
    self.cost = float(cost)
    self.quantity = int(quantity)

  
  def get_cost(self): # might need to change the input to be the product code
    return self.cost
    
  
  def get_quantity(self): # might need to change the input to be the product code
    return self.quantity
  
  
  def get_code(self):
    return self.code


  def __str__(self):
    return (f"Code: {self.code}\n"
  f"Product: {self.product}\n"
  f"Country: {self.country}\n"
  f"Cost: {self.cost}\n"
  f"Quantity: {self.quantity}\n")
  # using the __str__ method: https://www.educative.io/answers/what-is-the-str-method-in-python


#==== Functions ====
def read_shoes_data():
  # list to store the data
  global shoe_list
  shoe_list = []
  
  while True:
    # ask the user for the file they want to open
    global file_name
    file_name = input("Enter the name of the file you want to open: ")
    
    try:
      # open and read file
      shoe_data = open(f"{file_name}.txt", "r")
      shoe_data_read = shoe_data.read()
      
      # split by line and remove column names
      shoe_data_list = shoe_data_read.split("\n")
      # store column names in a variable
      global colnames
      colnames = shoe_data_list.pop(0)
      
      # close file
      shoe_data.close()
      
      # iterate over the list to take each item, split it into its components and add it to shoe_list
      for i in range(len(shoe_data_list)):
        data = shoe_data_list[i].split(",")
        a_shoe = Shoe(data[0], data[1], data[2], data[3], data[4])
        shoe_list.append(a_shoe)
      
      # break the loop when file is successfully opened
      break
    
    # if the user references an invalid file name, tell them
    except FileNotFoundError:
      print(f"The file `{file_name}` does not exist. Please check the name of the file and try again.")
    continue


def capture_shoes():
  # ask for user inputs
  a_country = input("Enter the country of the stock: ")
  a_code = input("Enter the product code: ")
  a_product = input("Enter the product name: ")
  a_cost = int(input("Enter the cost: "))
  a_quantity = int(input("Enter the quantity of the product stocked: "))
  
  # create Shoe object from the inputs
  a_shoe = Shoe(a_country, a_code, a_product, a_cost, a_quantity)
  
  # append to list
  shoe_list.append(a_shoe)
  
  # write the data to file
  inventory_file = open(f"{file_name}.txt", "w")
  inventory_file.writelines(f"{colnames}\n")
  for shoe in shoe_list:
    country = shoe.country
    code = shoe.code
    product = shoe.product
    cost = shoe.cost
    quantity = shoe.quantity
    inventory_file.write(f"{country},{code},{product},{cost},{quantity}\n")
  inventory_file.close()


def view_all():
  # print details of every shoe in the list
  for shoe in range(len(shoe_list)):
    print(shoe_list[shoe])


def re_stock():
  # iterate over the list, find the quantity of a shoe and if the quantity of this shoe is less than the quantity of the previous shoe, keep this shoe
  quantity_a = shoe_list[0].get_quantity()
  low_stock = shoe_list[0].get_code()
  for shoe in shoe_list:
    quantity_b = shoe.get_quantity()
    if quantity_b < quantity_a:
      quantity_a = quantity_b
      low_stock = shoe.get_code()
  
  # tell the user which shoe has the lowest stock and ask them how many they would like to order
  print(f"The shoe with the lowest stock is {low_stock}. There are only {quantity_a} pairs left.")
  add_stock = int(input(f"How many shoes would you like to order? "))
  
  # calculate the new stock total then find the shoe they have ordered and update the data
  new_stock_total = quantity_a + add_stock
  for shoe in shoe_list:
    if low_stock == shoe.code:
      shoe.quantity = new_stock_total
  
  # write the data to file
  inventory_file = open(f"{file_name}.txt", "w")
  inventory_file.writelines(f"{colnames}\n")
  for shoe in shoe_list:
    country = shoe.country
    code = shoe.code
    product = shoe.product
    cost = shoe.cost
    quantity = shoe.quantity
    inventory_file.write(f"{country},{code},{product},{cost},{quantity}\n")
  inventory_file.close()


def search_shoe():
  # ask the user for the code they are looking for
  search_code = input("Enter the code of the shoe you would like to find: ")
  
  # create boolean switch
  shoe_found_bool = False
  
  # check that the code the user is looking for is valid
  for shoe in shoe_list:
    # if the code is valid, print the data for that shoe, change the switch and break the loop
    if shoe.code == search_code:
      print(shoe)
      shoe_found_bool = True
      break
    
  # if the code is invalid (i.e. the shoe has not been found), tell the user
  if shoe_found_bool is False:
    print("The code you entered does not match any of the shoes in this warehouse.")


def value_per_item():
  for shoe in shoe_list:
    stock_value = shoe.cost * shoe.quantity
    print(f"{shoe}Stock value: {stock_value}\n")


def highest_qty():
  # iterate over the list, find the quantity of a shoe and if the quantity of this shoe is higher than the quantity of the previous shoe, keep this shoe
  quantity_a = shoe_list[0].get_quantity()
  high_stock = shoe_list[0].get_code()
  for shoe in shoe_list:
    quantity_b = shoe.get_quantity()
    if quantity_b > quantity_a:
      quantity_a = quantity_b
      high_stock = shoe.get_code()
  
  print(f"The shoe with the highest stock is {high_stock}. There are {quantity_a} pairs left and they are on sale.")


#==== Main Menu ====
# allow the user to open the file
read_shoes_data()

# allow the user to perform operations
while True:
  
  # user menu selection
  menu = input(f"Select one of the following options:\n"
  f"a: add a new shoe to the inventory\n"
  f"b: view all shoes in the inventory\n"
  f"c: re-stock shoe with the lowest stock\n"
  f"d: search for a shoe\n"
  f"e: view total value of stock per shoe\n"
  f"f: view the shoe with the most stock\n"
  f"Or, enter `quit` to exit\n")
  
  if menu == "a":
    print("\nAdd a new shoe to the inventory\n")
    capture_shoes()
  
  elif menu == "b":
    print("\nView all shoes in the inventory\n")
    view_all()
  
  elif menu == "c":
    print("\nRe-stock shoe with the lowest stock\n")
    re_stock()
  
  elif menu == "d":
    print("\nSearch for a shoe\n")
    search_shoe()
  
  elif menu == "e":
    print("\nView total value of stock per shoe\n")
    value_per_item()
  
  elif menu == "f":
    print("\nView the shoe with the most stock\n")
    highest_qty()
  
  # quit the programme
  elif menu == "quit":
    print("Goodbye.")
    exit()
    
  else:
    print("You selected an invalid option. Please enter the letter of the option you want to select.\n")
