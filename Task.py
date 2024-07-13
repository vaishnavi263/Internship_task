def hex_pattern(rows, cols): 
     
    hex_top = "___ " 
    hex_mid_top = " /   \\" 
    hex_mid_bot = " \\___/" 
    hex_spacing = "  " 
 
    #  top row of hexagons 
    for col in range(cols): 
        print(hex_spacing + hex_top, end='') 
    print() 
 
    # middle and bottom parts of hexagons 
    for row in range(rows): 
        for col in range(cols): 
            print(hex_mid_top, end='') 
        print() 
        for col in range(cols): 
            print(hex_mid_bot, end='') 
        print() 
 
# Calling 
rows = 3 
cols = 5 
hex_pattern(rows, cols) 
 
rows = 4 
cols = 7 
hex_pattern(rows, cols)
