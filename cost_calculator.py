import cost_finder as cf
import cost_dictionaries as cd


print(cf.cost_finder(cd.ground_shipping_dict, cd.ground_shipping_premium, cd.drone_shipping_dict, 15))

def cost_finder():
    inputed_weight = float(input("What is the weight of your package? "))
    return inputed_weight



print(type(cost_finder()))