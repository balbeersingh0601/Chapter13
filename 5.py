products={}
n= int(input("ENter the no. of products to want to add in dictionary"))
for a in range(n):
    product,price = eval(input("Enter the products and the associated price"))
    products[product]=price
print("Created a dictionary",products)
item = input("Now enter to be searched ")
for a in products:
    if a == item:
        print(products[item])
