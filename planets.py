def weight_on_planets():
   earthstri = input("What do you weigh on earth? ")
   earth = float(earthstri)
   mars = earth * 0.38
   jupiter = earth * 2.34
   print("\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds." % (mars, jupiter))
   
   
   
   
if __name__ == '__main__':
   weight_on_planets()
