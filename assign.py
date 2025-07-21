Datatypes and variables

# Paints = {-------------------------------------------------------------------1
#     "AsianPaints": {
#         "Types": {
#             'Apex':{"20ltprice": 7400, "10ltprice": 4700},
#             'Ace' :{"20ltprice": 6200, "10ltprice": 4100},
#             'Royale' :{"20ltprice": 9600, "10ltprice": 6900},
#             'Tractor Emulsion' :{"20ltprice": 4800, "10ltprice":2250}
#             },
        
#     },
#     "nerolac" :{
#          "Types":[
#                     {
#                         'name':'Super Clean', 
#                         '20ltprice': 6200, 
#                         '10ltprice': 4100
#                     },
#                       {
#                         'name':'Beauty Gold', 
#                         '20ltprice': 8000, 
#                         '10ltprice': 5500
#                      },
                  
#                   {
#                       'name':'Beauty Velvet',
#                       '20ltprice': 7500, 
#                       '10ltprice': 5200
#                   },
                  
#                   {
#                       'name':'Tractor Emulsion',
#                       '20ltprice': 3800,
#                       '10ltprice': 1700
#                   }
#                 ]

#     }

# }

# final = Paints["AsianPaints"]["Types"]['Royale']["20ltprice"]
# print("The price of Royale 20lt is: ", final)

# total = Paints["nerolac"]["Types"][2]['20ltprice'] + Paints["nerolac"]["Types"][1]['20ltprice']
# print("The total price of Super Clean and Beauty Gold 20lt is: ", total)


# paintbrand = input("Enter the paint brand: ")------------------------------2
# painttype = input("Enter the paint type: ")
# quantity = input("Enter the quantity in liters: ")
# is_available = input("Is the paint available? (yes/no): ")

# painttype = int(painttype)
# quantity = float(quantity)
# is_available = is_available.lower() == 'yes'

# print("\n Paints Requirements")
# print(f"paint brand: {paintbrand} (Type:{type(paintbrand).__name__})")
# print(f"paint type: {painttype} (Type:{type(painttype).__name__})")
# print(f"quantity: {quantity} (Type:{type(quantity).__name__})")
# print(f"is_available: {is_available} (Type:{type(is_available).__name__})")

# def input_values(*args,**kwargs):-------------------3
#     result = {}

#     for value in args:
#         dtype = type(value).__name__
#         if dtype not in result:
#             result[dtype] = []
#         result[dtype].append(value)
#     for value in kwargs:
#         value = kwargs[value]
#         dtype = type(value).__name__
#         if dtype not in result:
#             result[dtype] = []
#         result[dtype].append(value)
    
#     for v in result:
#       print(f"{v}: {result[v]}")

# input_values(7900, 15.5, "Asian paints", 69.99, True, "Red", 44.0, False)


Controlstructures

# def paint_budjet():------------------------------------1
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")

#     choice = input("Enter your choice (add/subtract/multiply/divide): ").lower()
#     a = float(input("Enter the first quantity: "))
#     b = float(input("Enter the second quantity: "))

#     match choice:
#         case "add":
#             c = float(input("Enter the third quantity: "))
#             print(f"Result: {a + b + c}")
#         case "subtract":
#             d= float(input("Enter the third quantity: "))
#             print(f"Result: {a - b - d}")
#         case "multiply":
#             c = float(input("Enter the third quantity: "))
#             print(f"Result: {a * b * c}")
#         case "divide":
#             if b != 0:
#                 print(f"Result: {a / b}")
#             else:
#                 print("Error: Division by zero.")
#         case _:
#             print("Invalid choice.")
# paint_budjet()

# def value_check():--------------------------------------------------------2
#     a = (input("Enter the color code:"))
#     b = (input("Enter the color quantity:"))

#     if b.isdigit():
#         b = int(b)
#     else:
#         print("Invalid quantity. Please enter a number.")
#         return
    
#     c = 1000

#     if a == 'bryo':
#         d = 280
#         if b + d <= c:
#             print(f"Color code {a} with quantity {b+d} is within the quantity range.")
#         else:   
#             print(f"Color code {a} with quantity {b+d} exceeds the quantity range.")

#     elif a == 'wtbk':
#         e = 320
#         if b + e <= c:
#             print(f"Color code {a} with quantity {b+e} is within the quantity range.")
#         else:   
#             print(f"Color code {a} with quantity {b+e} exceeds the quantity range.")

#     elif a == 'bryl':
#         f = 435
#         if b + f <= c:
#             print(f"Color code {a} with quantity {b+f} is within the quantity range.")
#         else:   
#             print(f"Color code {a} with quantity {b+f} exceeds the quantity range.")

#     elif a == 'dprd':
#         g = 480
#         if b + g <= c:
#             print(f"Color code {a} with quantity {b+g} is within the quantity range.")
#         else:   
#             print(f"Color code {a} with quantity {b+g} exceeds the quantity range.")

#     elif a == 'dpord':
#         h = 690
#         if b + h <= c:
#             print(f"Color code {a} with quantity {b+h} is within the quantity range.")
#         else:   
#             print(f"Color code {a} with quantity {b+h} exceeds the quantity range.")
# value_check()


# a ={12, 33, 15, 9, 87, 99, 108, 45,97, 897, 84, 44, 94, 54, 22}------------------3

# multiples_of_5 = 0
# lessthan_50 = 0
# even_numbers = 0

# passed_multiple = set()

# for num in a:
#     pass_count = 0

#     if num % 5 == 0:
#         multiples_of_5 += 1
#         pass_count += 1
#     if num < 50:
#         lessthan_50 += 1
#         pass_count += 1
#     if num % 2 == 0:
#         even_numbers += 1
#         pass_count += 1

#     if pass_count > 0:
#         passed_multiple.add(num)

# print("Multiples of 5:", multiples_of_5)
# print("Less than 50:", lessthan_50)
# print("Even numbers:", even_numbers)
# print("Passed multiple:", passed_multiple)

Functions and loops

# def sum_arg(*args):----------------------------------------1
#     total = 0
#     for num in args:
#         if type(num) in (int, float):
#             total += num
#         else:
#             print(f"Skipping non-numeric argument: {num}")
#     return total

# result = sum_arg(66, 'apex emulsion', 15.5, 3.06, [1, 2], False)
# print("Sum of numeric values:", result)

# def analyze_text(**kwargs):--------------------------------------2
#     result = {}

#     if "text" not in kwargs:
#         return {"error": "No text provided."}

#     text = kwargs["text"]

#     if kwargs.get("count_words"):
#         words = text.split()
#         result["word_count"] = len(words)

#     if kwargs.get("count_vowels"):
#         vowels = "aeiouAEIOU"
#         count = 0
#         for char in text:
#             if char in vowels:
#                 count += 1
#         result["vowel_count"] = count

#     if kwargs.get("count_uppercase"):
#         count = 0
#         for char in text:
#             if char.isupper():
#                 count += 1
#         result["uppercase_count"] = count

#     if kwargs.get("count_lowercase"):
#         count = 0
#         for char in text:
#             if char.islower():
#                 count += 1
#         result["lowercase_count"] = count

#     return result

# report = analyze_text(text="This report Is to Analyze the Earliest product Specifications", count_words=True, count_vowels=True, count_uppercase=True, count_lowercase=True)
# print(report)

# def open_list(list):------------------------------------------------------3
#      Flist = []

#      for a in list:
#          if type(a) == list:
#              nlist = open_list(a)
#              for value in nlist:
#                  Flist.append(value)
#          else:
#              Flist.append(a)
#      return Flist

# list = [9600, 4700, [4500, 5200, [7900, 2700], 2200], 3200, 2900]
# result = open_list(list)
# print("Flattened list:", result)


