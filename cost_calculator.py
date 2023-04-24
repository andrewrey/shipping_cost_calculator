import cost_finder as cf
import cost_dictionaries as cd



def cost_finder():
    inputed_weight = float(input("What is the weight of your package? "))
    shipping_cost_dict = cf.cost_finder(cd.ground_shipping_dict, cd.ground_shipping_premium, cd.drone_shipping_dict, inputed_weight)
    cheapest_option = ""
    cheapest_price = 0
    
    for key, value in shipping_cost_dict.items():
        if cheapest_price == 0:
            cheapest_price = value
            cheapest_option = key
        else:
            if value < cheapest_price:
                cheapest_price = value
                cheapest_option = key 
    
    output_message = f"Weight of item: {inputed_weight}\nGround Shipping Price: {shipping_cost_dict['ground']}\nGround Shipping Premium Price: {shipping_cost_dict['premium']}\nDrone Shipping Price: {shipping_cost_dict['drone']}"
    if cheapest_option == "ground":
        output_message += f"\nThe cheapest option is Ground shipping at a price of ${cheapest_price}."
    elif cheapest_option == "premium":
        output_message += f"\nThe cheapest option is Premium Ground Shipping at a price of ${cheapest_price}."
    else:
        output_message += f"\nThe cheapest option is Drone Shipping at a price of ${cheapest_price}."
    return output_message


print(cost_finder())