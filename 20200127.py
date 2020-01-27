"""Пейзаж из как минимум 5 статических фигур"""
import graphics as gr

def draw_land(window, color_land, weight, height):
    print("6")
    my_land = gr.Rectangle(gr.Point(0, height) , gr.Point(weight, 0))
    my_land.draw(window)
    my_land.setFill(color_land)
    print("6")
    return 0

def draw_sky(window, horizon_height , weight,  color_sky):
    print("7")
    my_sky = gr.Rectangle(gr.Point(0, horizon_height) , gr.Point(weight, 0))
    my_sky.draw(window)
    my_sky.setFill(color_sky)
    return 0

def draw_moon(window, moon_center_x, moon_center_y, moon_r, color_moon):
    print("8")
    my_moon = gr.Circle(gr.Point(moon_center_x, moon_center_y), moon_r)
    my_moon.draw(window)
    my_moon.setFill(color_moon)
    return 0

def draw_clouds(window, cloud_centers_x, cloud_centers_y,
              cloud_part_r, color_cloud):
    print("9")
    return 0

def draw_forest(window, horizon_height, number_of_trees):
    print("10")
    return 0
#test commit

def draw_Night(window,
               weight, height,
               color_land, color_sky, color_moon,
               horizon_height, 
               moon_center_x, moon_center_y, moon_r,
               cloud_centers_x, cloud_centers_y, cloud_part_r,
               number_of_trees):
    print("4")
    draw_land(window, color_land, weight, height)
    draw_sky(window, horizon_height , weight, color_sky)
    draw_moon(window, moon_center_x, moon_center_y, moon_r, color_moon)
    draw_clouds(window, cloud_centers_x, cloud_centers_y,
               cloud_part_r, color_cloud)
    draw_forest(window, horizon_height, number_of_trees)
    print("Narisovano chastey: ")
    return 

def main():
    print("1")
    draw = True
    weight = 600
    height = 600
    color_land="grey"
    color_sky="blue"
    color_moon="white"
    
    horizon_height=240

    moon_center_x=50
    moon_center_y=50
    moon_r = 20
    
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
        window = gr.GraphWin("Night", weight, height)
        draw_Night(window,
               weight, height,
               color_land, color_sky, color_moon,
               horizon_height, 
               moon_center_x, moon_center_y, moon_r,
               cloud_centers_x, cloud_centers_y, cloud_part_r,
               number_of_trees)
    
    
    window.getMouse()
    window.close()

main()
