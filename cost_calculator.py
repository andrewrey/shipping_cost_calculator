import cost_finder as cf
import cost_dictionaries as cd



def cost_finder():
    inputed_weight = float(input("What is the weight of your package? "))
    shipping_cost_dict = cf.cost_finder(cd.ground_shipping_dict, cd.ground_shipping_premium, cd.drone_shipping_dict, inputed_weight)
    cheapest_option = ""
    cheapest_price = 0
    
    for key, value in shipping_cost_dict.items():
        print(value)
    
    
    return shipping_cost_dict


print(cost_finder())