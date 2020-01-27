"""Пейзаж из как минимум 5 статических фигур"""
import graphics as gr

def draw_land(color_land):
    print("5")
    return 0

def draw_land(color_land):
    print("6")
    return 0

def draw_sky(horizon_height , color_sky):
    print("7")
    return 0

def draw_moon(moon_center_x, moon_center_y, moon_r, color_moon):
    print("8")
    return 0

def draw_clouds(cloud_centers_x, cloud_centers_y,
              cloud_part_r, color_cloud):
    print("9")
    return 0

def draw_forest(horizon_height, number_of_trees):
    print("10")
    return 0

def draw_Night(
               color_land, color_sky, color_moon,
               horizon_height, 
               moon_center_x, moon_center_y,
               cloud_centers_x, cloud_centers_y, cloud_part_r,
               numbers_of_trees):
    print("4")
    draw_land(color_land)
    i+=draw_sky(horizon_height , color_sky)
    i+=draw_moon(moon_center_x, moon_center_y, moon_r, color_moon)
    i+=draw_clouds(cloud_centers_x, cloud_centers_y,
               cloud_part_r, color_cloud)
    i+=draw_forest(horizon_height, number_of_trees)
    print("Narisovano chastey: ", i)
    return i

def main():
    print("1")
    draw = True
    color_land="black"
    color_sky="black"
    color_moon="black"
    
    horizon_height=0

    moon_center_x=0
    moon_center_y=0
    
    cloud_centers_x = [0]
    cloud_centers_y = [0]
    cloud_part_r = 0
    print (len(cloud_centers_x))
    number_of_trees = 0
    
    
    if len(cloud_centers_x) == len(cloud_centers_y):
        number_of_clouds = len(cloud_centers_x)
        print("2")
    else:
        print("error")
        draw = False
    
    if draw == True:
        print("3")
        window = gr.GraphWin("Night", 500, 500)
        draw_Night(
               color_land, color_sky, color_moon,
               horizon_height, 
               moon_center_x, moon_center_y,
               cloud_centers_x, cloud_centers_y, cloud_part_r,
               numbers_of_trees)
    
    
    window.getMouse()
    window.close()

main()
