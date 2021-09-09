import Random

def DrawMulti():
  Multiplier_options=[1,1,1,1,1,2,2,2,5]
  Multiplier=(random.choice(Multiplier_options))
  print("Multiplier: "+str(Multiplier))
  global Total_Power
  Total_Power=(Power*Multiplier)
  print("Total Power: "+str(Total_Power))
  print('__________________')
