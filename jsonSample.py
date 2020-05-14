import json

totalValue = 0
zipcode = int(input("Please confirm the property's zipcode: "))
#AC TYPE        
AC_type = int(input("Choose the AC type\n(0) Window Units\n(1) House Fan\n(2) Central Air\n(3) Ductless Mini-Split AC\n(4) Geothermal\n(5) Other\n\n"))         
if(AC_type == 5):
   AC_other = input("Enter the AC type that the property contains: ")
def switch_AC(AC_type):
    switcher_AC = {
            0: -500,
            1: -400,
            2: 0,
            3: 0,
            4: 500,
            5: 0
    }.get(AC_type,"Invalid, will not be considered")
    return switcher_AC
totalValue = totalValue + switch_AC(AC_type)
print(totalValue)
#END AC TYPE


#HEAT TYPE
heat_type = int(input("Choose the heat type\n(0) Boiler\n(1) Furnace\n(2) Standard Heat Pump\n(3) Mini Split Heat Pump\n(4) Geothermal\n(5) Other\n\n"))
if(heat_type == 5):
   heat_other = input("Enter the heat type that the property contains: ")
def switch_Heat(heat_type):
    totalValue_switch = {
        0: -500,
        1: -350,
        2: 0,
        3: 0,
        4: 500,
        5: 0
    }.get(heat_type,"Invalid, will not be considered")
    return totalValue_switch 
totalValue = totalValue + switch_Heat(heat_type)
print(totalValue)
#END HEAT TYPE   
   
 
#FIREPLACES  
fireplaces = int(input("Enter the number of fireplaces if installed and 0 if not: \n"))
totalValue = totalValue+(fireplaces*800)
print(totalValue)
#END FIREPLACES
data = {}
data['Results'] = []
data['Results'].append({
    "zipcode" : zipcode,
    "AC type": AC_type,
    "heat type": heat_type,
    "fireplaces": fireplaces
    })
with open("results.json", "w") as outfile:
    json.dump(data, outfile)

# data['Results'] = []
# data['Results'].append({
#     "zipcode" : zipcode,
#     "property type": prop_type,
#     "year built": year_built,
#     "property value": prop_value,
#     "property sqft": prop_sqft,
#     "lot sqft": lot_sqft,
#     "bedrooms": bedrooms,
#     "full bathrooms": full_bathrooms,
#     "half_bathrooms": half_bathrooms,
#     "kitchen sqft": kitchen_sqft,
#     "basement": basement,
#     "roof type": roof_type,
#     "washer" : washer,
#     "dryer" : dryer,
#     "dishwasher" : dishwasher,
#     "fridge": fridge,
#     "microwave":microwave,
#     "stove":stove,
#     "kicthen match": kitchen_match,
#     "washer dryer match":washer_dryer_match,
#     "pool":pool,
#     "pool install":pool_install,
#     "hot tub":hot_tub,
#     "driveway" : driveway,
#     "garage" : garage,
#     "garage install" : garage_install,
#     "AC type": AC_type,
#     "heat type": heat_type,
#     "fireplaces": fireplaces,
#     "electric system": electric_system,
#     "water type": water_type,
#     "foundation material" : foundation_material,
#     "porch" : porch,
#     "patio" : patio,
#     "yard" : yard,
#     "additional factors" : additional_factors,
#     "Total Value" : totalValue


    
