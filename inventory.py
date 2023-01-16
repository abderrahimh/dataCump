import os
import itertools
import sys

#========The Shoe class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        cost = self.cost * self.quantity
        return(cost)

    def get_quantity(self):
        return(self.quantity)

    def __str__(self):
        print(f"country origin = {self.country} \ncode = {self.code} \nproduct name = {self.product}")
        print(f"We have {self.quantity} in stock at {self.cost} cost each.")
        return('')



#==========Functions outside the class ==============

#------------ read shoes data lines and store header and data in two objects
def read_shoes_data(data_path, inventory_file, header):
    temp_list = []
    try:
        with open(data_path + inventory_file, 'r+') as f:
            for line in f:
                lines_list.append(line)
        header = lines_list.pop(0)
    except:
        print(f"{data_path + inventory_file} can not be found.")
        input("")
    finally:
        f.close()
    return([header, lines_list])

#-------------------- declaire each data line as a class instance and store in a shoe list
def capture_shoes(lines_list, shoe_list):
    for i in range(len(lines_list)):
        temp_list = lines_list[i].split(',')
        temp_class = Shoe(temp_list[0], temp_list[1], temp_list[2], int(temp_list[3]), int(temp_list[4].replace('\n', '')))
        shoe_list.append(temp_class)
        temp_list = None
        temp_class = None
    return(shoe_list)

#----------------------- print all shoes variables including cost and quantity
def view_all_shoes(shoe_list):
    for i in range(len(shoe_list)):
        print(shoe_list[i].__str__())
        print('\n')

#------------------- returns the index of the minimus stock shoe in the shoe list
def minimum_stock(shoe_list):
  ind = 0
  min_s = shoe_list[0].quantity
  for i in range(1,len(shoe_list),1):
    if shoe_list[i].quantity < min_s:
      min_s = shoe_list[i].quantity
      ind = i
  return(ind)

#------------------- returns the index of the maximus stock shoe in the shoe list
def maximum_stock(shoe_list):
  ind = 0
  max_s = shoe_list[0].quantity
  for i in range(1,len(shoe_list),1):
    if shoe_list[i].quantity > max_s:
      max_s = shoe_list[i].quantity
      ind = i
  return(ind)

#---------------------- print a table of shoes and value in stock
def print_value_per_item(shoe_list):
  print("Product                Value")
  print("---------------------------\n")
  for i in range(len(shoe_list)):
    space = "".join(itertools.repeat(' ', 20 - len(shoe_list[i].product)))
    print(f"{shoe_list[i].product}: {space} {shoe_list[i].get_cost()}")

#---------------- print shoe details given the shoe code.   
def by_code_shoe_print(shoe_list, code):
  for i in range(len(shoe_list)):
    if shoe_list[i].code == code:
      shoe_list[1].__str__()
      break

#----------------------------- main process
while True:
  
  #============= variables ===========
  header = []
  lines_list = []
  shoe_list = []
  
  def get_path():
    return(os.path.dirname(os.path.realpath(sys.argv[0])))
  
  data_path = get_path()
  inventory_file = '\\inventory.txt'
  #----------------- read data and populate instances of the Shoe class
  
  shoes_data = read_shoes_data(data_path, inventory_file, header)
  header = shoes_data[0]
  lines_list = shoes_data[1]
  shoe_list = capture_shoes(lines_list, shoe_list)
  os.system('cls')
  print("This program manages shoes stock.\n")
  menu = input('''Please select one of the following Options:
                  r  - Rebuild low stock
                  d  - display stock levels
                  m  - show maximum stock
                  i  - display inventory
                  c  - by code print item
                  e  - Exit
                  : ''').lower()
                  #os.system('cls')
  
  if menu == 'r':
    print('We have minimum stock at:\n')
    min_index = minimum_stock(shoe_list)
    shoe_list[min_index].__str__()
    quantity_added = input(f"\nPlease type in the quantity to be added or press enter to skip: ")
    if quantity_added.isdecimal():
      shoe_list[min_index].quantity += int(quantity_added)
    
    with open(data_path + inventory_file, 'w') as f:
      f.write(header.replace('\n', ''))
      for i in range(len(shoe_list)):
        f.write('\n' + shoe_list[i].country + ',' + shoe_list[i].code + ',' + shoe_list[i].product +','+ str(shoe_list[i].cost) +','+  str(shoe_list[i].quantity))

  elif menu == 'd':
    os.system('cls')
    view_all_shoes(shoe_list)
  elif menu == 'e':
    break
  elif menu == 'm':
    os.system('cls')
    max_index = maximum_stock(shoe_list)
    print("This stock is for sale.\n")
    shoe_list[max_index].__str__()
  elif menu == 'i':
    os.system('cls')
    print_value_per_item(shoe_list)
  elif menu == 'c':
    code_s = input("Please type the product code eg SKU90000: ")
    os.system('cls')
    by_code_shoe_print(shoe_list, code_s)
  else:
    input("")
    continue

  input("")



