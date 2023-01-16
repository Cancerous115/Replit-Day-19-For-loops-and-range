print("Loan Calc.1000$ loan at 5%APR for 10 years")
total =1000
apr =0.05
for years in range(10):
  total +=(total*apr)
  print("Year",years+1,"is",round(total,2))

  