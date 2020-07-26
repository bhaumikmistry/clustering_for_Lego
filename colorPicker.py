# This file holds the information about the colors

##
#		notes:		A dict for the colors 
#					and the pixel information
#
#		modified:	bm	03 06 17	created
#						created the function to get the color dictionary
#
############- LEGO list of colors -##############
# family		color    			R 	G 	B 	#
# Grey 											#
# 			Dark stone Grey			91	103	112	#
# 			medium stone Grey		162	170	173	#
# Black											#
# 			Black					39	37	31	#
# Green											#
# 			Dark Green				0	132	61	#
# Yellow 										#
# 			Bright Yellow			255	205	0	#
# Reddish Brown									#
# 			Reddish Brown			122	62	58	#
# 			Brick Yellow			211	188	141	#
# Blue											#
# 			Bright Blue				0	61	165	#
# 			Earth Blue				0	56	101	#
# White		White								#
# Bright Orange  								#
# 			Bright Orange			255	130	0	#
# Lilac											#
# 			Medium Lavender			160	94	181	#
# Red 											#
# 			Bright Red 				239	51	64	#
#################################################

Dark_stone_Grey	=[91,103,112]	
Medium_stone_Grey =[162,170,173]
Black =[39,	37,31]	
Dark_Green =[0,	132,61]	
Bright_Yellow =[255,205,0]	
Reddish_Brown =[122,62,58]	
Brick_Yellow =[211,	188,141]	
Bright_Blue =[0,61,165]	
Earth_Blue =[0,	56,101]
Bright_Orange =[255,130,0]
White =[217,217,214]	
Medium_Lavendel	=[160,94,181]	
Bright_Red =[239,51,64]	

def getColorList():
    colors = ['Dark stone grey', 'Medium stone grey', 'Black', 'Dark Green', 'Bright yellow', 'Reddish Brown', 'Brick Yellow', 'Bright Blue', 'Earth Blue', 'White', 'Bright Orange', 'Medium Lavender'];
    return colors

# def getColorAndValue():
#     colors = {'Dark stone grey':Dark_stone_Grey, 'Medium stone grey':Medium_stone_Grey, 'Black':Black, 'Dark Green':Dark_Green, 'Bright yellow':Brick_Yellow, 'Reddish Brown':Reddish_Brown, 'Brick Yellow':Brick_Yellow, 'Bright Blue':Bright_Blue, 'Earth Blue':Earth_Blue, 'White':White, 'Bright Orange':Bright_Orange, 'Medium Lavender':Medium_Lavendel}
#     return colors

def getColorAndValue():
    colors = {
        'Black':Black, 
        'Bright yellow':Brick_Yellow,
        'Bright Blue':Bright_Blue,
        'Bright Orange':Bright_Orange,
        'Brick Yellow':Brick_Yellow,
        'Dark Green':Dark_Green,
        'Dark stone grey':Dark_stone_Grey,
        'Earth Blue':Earth_Blue,
        'Medium Lavender':Medium_Lavendel,
        'Medium stone grey':Medium_stone_Grey,
        'Reddish Brown':Reddish_Brown,
        'White':White
        }
    return colors