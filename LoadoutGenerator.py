import random

#TRAITS - at the moment item rarity is 


guns=['556 AR Rifle','556 AR Pistol','308 AR Rifle','308 AR Pistol','556 Bullpup Rifle',
     'Pump Action 12 GA Shotgun','Semi-Auto 12GA Shotgun','30-06 Bolt Action Rifle','45 Submachine Gun',
      '9mm Submachine Gun','762 AK Rifle','762 AK Pistol','556 AK Rifle','45 Lever Action Rifle']

optics=['Holographic Sight', 'Flip-up Sights', 'Iron Sights', 'Low Powered Variable Optic', 'Red Dot Sight',
        'Red Dot Sight + Magnifier', 'Thermal Scope', '5-50x Scope', 'Night Vision Gear', 'Red Laser', 'Green Laser']

trigger=['Standard Semi', 'Binary Trigger', 'Full Auto','Forced Reset Trigger']

camo=['Black','Desert Tan','Digital Camo','Golden','Woodland Camo']

character=['Hunter','Range Larp','Special Ops','Recruit','Double Agent','Guerrilla','Cowboy','Maverick']

alignment=['Saint', 'Criminal', 'Family Oriented', 'Money Motivated', 'Evil']

heal=['Bandage', 'Medkit', 'Ibuprofen', 'Acetaminophin', 'Box of Tissues']




def Gen_Loadout():
  print(random.choice(camo))
  print(random.choice(guns))
  print(random.choice(trigger))
  print(random.choice(optics))
  print(random.choice(character))
  print(random.choice(alignment))
  print(random.choice(heal))
  global power
  power=(random.randint(45,100))
  print("Power: "+str(power))
  print('__________________')
  
  
i=1
while i < 15:
  Gen_Loadout()
  i +=1
  
  
  

