from matplotlib import pyplot as plt
from shapely.geometry.polygon import LinearRing, Polygon
from numpy import linalg as la

if __name__ == "__main__":
    bottom_left = (5,1)
    left_armpit = (5,11)
    left_sleeve_bottom = (3,9)
    left_sleeve_top = (1,11)
    left_shoulder_top = (5,15)
    left_collar = (7,17)
    spine_top = (11,16)
    right_collar = (15,17)
    right_shoulder_top = (17,15)
    right_sleeve_top = (21,11)
    right_sleeve_bottom = (19,9)
    right_armpit = (17,11)
    bottom_right = (17,1)
        
    shirt = Polygon([bottom_left,left_armpit,left_sleeve_bottom,left_sleeve_top,left_shoulder_top,left_collar,spine_top
               ,right_collar,right_shoulder_top,right_sleeve_top,right_sleeve_bottom,right_armpit,bottom_right])
    x,y = shirt.exterior.xy
     
    fig = plt.figure(1, figsize=(5,5), dpi=90)
    ax = fig.add_subplot(111)
    ax.plot(x, y, color='#6699cc', alpha=0.7,
    linewidth=3, solid_capstyle='round', zorder=2)
    ax.set_title('Shirt')
    

    plt.xlim(0,22)
    plt.ylim(0,22)
    plt.show()