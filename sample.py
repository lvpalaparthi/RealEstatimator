#DRIVEWAY
driveway = input("Is there a driveway? (yes or none): ")
if(driveway == "yes"):
    driveway_sqft = int(input("Enter the driveway square footage: "))
    while True:
        try:
            driveway_material = int(input("Choose the driveway material\n(0) Concrete\n(1) Brick\n(2) Rock\n(3) Asphalt\n\n"))
            if driveway_material in range(4):
                break
        except:
            pass
        print('\nIncorrect input, try again!')
    while True:
        try:
            driveway_condition = int(input("Choose the current driveway condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n"))
            if driveway_condition in range(4):
                break
        except:
            pass
        print('\nIncorrect input, try again!')
else:
    totalValue = totalValue
def switch_driveway_material(driveway_material):
    drive_mat_switcher = {
        0: driveway_sqft * 5,
        1: driveway_sqft * 2,
        2: driveway_sqft * 1,
        3: driveway_sqft * 3,
    }.get(driveway_material, "Invalid, will not be considered")
    return drive_mat_switcher

def switch_driveway_value(driveway_condition):
    driveway_val_switch = {
        0: driveway_value *0.8,
        1: driveway_value *1,
        2: driveway_value *1.1,
        3: driveway_value *1.2
    }.get(driveway_condition, "Invalid, will not be considered")
    return driveway_val_switch
driveway_value = switch_driveway_material(driveway_material)
driveway_value =  switch_driveway_value(driveway_condition)
totalValue = totalValue + driveway_value
print(totalValue)
#END OF DRIVEWAY
