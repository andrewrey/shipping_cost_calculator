# import cost_dictionaries as dc

def cost_finder(ground,g_premium, drone, weight):
    key_finder = 0
    if weight > 10:
        key_finder = "10_lbs_plus"
    elif weight > 6:
        key_finder = "over_6_to_10_lbs"
    elif weight > 2:
        key_finder = "over_2_to_6_lbs"
    else:
        key_finder = "2_and_less_lbs"
        
        
    # Ground shipping price
    
    ground_price = (weight * ground[key_finder][0]) + ground[key_finder][-1]
    
    # Premium shipping price

    premium_price = g_premium
    
    
    
    # Drone shipping price
    
    drone_price = weight * drone[key_finder][0]


    return {
        "ground": ground_price,
        "premium": premium_price,
        "drone": drone_price
    }



# price = cost_finder(dc.ground_shipping_dict,dc.ground_shipping_premium, dc.drone_shipping_dict, 15)

# print (price)