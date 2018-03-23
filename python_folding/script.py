from matplotlib import pyplot as plt
from shapely.geometry.polygon import LinearRing, Polygon
from numpy import linalg as la

if __name__ == "__main__":
    # Towel
    bottom_left = (1,1)
    top_left = (1,7)
    top_right = (12,7)
    bottom_right = (12,1)
    towel = Polygon([bottom_left,top_left,top_right,bottom_right])
    
    # Pant
    left_leg_right = (4,1)
    left_leg_left = (1,1.2)
    top_left = (2,18)
    top_right = (10,18)
    right_leg_right = (11,1.2) 
    right_leg_left = (8,1)
    crotch = (6,14)
    pant = Polygon([left_leg_right,left_leg_left,top_left,top_right,right_leg_right,right_leg_left,crotch])

     
    # Short-sleeved Shirt
    bottom_left = (5,1)
    left_armpit = (5,11)
    left_sleeve_bottom = (3,9)
    left_sleeve_top = (1,11)
    left_shoulder_top = (5,15)
    left_collar = (7,16.8)
    spine_top = (11,16)
    right_collar = (15,16.8)
    right_shoulder_top = (17,15)
    right_sleeve_top = (21,11)
    right_sleeve_bottom = (19,9)
    right_armpit = (17,11)
    bottom_right = (17,1)
    tee = Polygon([bottom_left,left_armpit,left_sleeve_bottom,left_sleeve_top,left_shoulder_top,left_collar,spine_top
               ,right_collar,right_shoulder_top,right_sleeve_top,right_sleeve_bottom,right_armpit,bottom_right])
    
    # Long-sleeved Shirt
    bottom_left = (9,1)
    left_armpit = (9,11)
    left_sleeve_bottom = (3,5)
    left_sleeve_top = (1,7)
    left_shoulder_top = (9,15)
    left_collar = (11,16.8)
    spine_top = (15,16)
    right_collar = (19,16.8)
    right_shoulder_top = (21,15)
    right_sleeve_top = (29,7)
    right_sleeve_bottom = (27,5)
    right_armpit = (21,11)
    bottom_right = (21,1)
    long_shirt = Polygon([bottom_left,left_armpit,left_sleeve_bottom,left_sleeve_top,left_shoulder_top,left_collar,spine_top
               ,right_collar,right_shoulder_top,right_sleeve_top,right_sleeve_bottom,right_armpit,bottom_right])    
    
    x,y = long_shirt.exterior.xy
    fig = plt.figure(1, figsize=(5,5), dpi=90)
    ax = fig.add_subplot(111)
    ax.plot(x, y, color='#6699cc', alpha=0.7,
    linewidth=3, solid_capstyle='round', zorder=2)
    ax.set_title('Shirt')
    

    plt.xlim(0,30)
    plt.ylim(0,30)
    plt.show()
