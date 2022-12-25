purchase = int(300)


if purchase > 100:
    discountRate = float(int(0.25))  
    shipCost = float(int(10.00))
    TotalBill = (purchase) - (purchase * 0.25) + 10.00
    print ("TotalBill =", TotalBill)
    
else:
    discountRate = float(int(0.15))  
    shipCost = float(int(5.00))
    TotalBill = (purchase) - (purchase * 0.25) + 10.00
    print ("TotalBill =", TotalBill)
    
    
    
   