rdef weight_on_planets():
   earthstr = input("What do you weigh on earth?")
   earth = float(earthstr)
   mars = earth * 0.38
   jupitar = earth * 2.34
   print("\nOn Mars you would weigh %.2f pounds\nOn Jupiter you would weigh %.2f pounds." % (mars, jupiter))
   
   
   
   
if __name__ == '__main__':
   weight_on_planets()
