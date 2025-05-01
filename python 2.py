// calci

total = 0
n = int(input("enter no. of items: "))

for i in range(n):
     pricve = float(input(f"enter price of item {i+1}: "))
      
    quantity = int(input(f"enter no. of items{i+1}: "))
     
total += price * quantity
gst = total * 0.18
grand_total = total + gst 

print(f"\nSubtotal: {total:.2f}")
print(f"GST (18%): {gst:.2f}")
print(f"Total Bill: {grand_total:.2f}")