"""Пейзаж из как минимум 5 статических фигур"""
import graphics as gr

def draw_land(window, color_land, weight, height):
    
    my_land = gr.Rectangle(gr.Point(0, height) , gr.Point(weight, 0))
    my_land.draw(window)
    my_land.setFill(color_land)
    
    return 0

def draw_sky(window, horizon_height , weight,  color_sky):
    
    my_sky = gr.Rectangle(gr.Point(0, horizon_height) , gr.Point(weight, 0))
    my_sky.draw(window)
    my_sky.setFill(color_sky)
    return 0

def draw_moon(window, moon_center_x, moon_center_y, moon_r, color_moon):
    
    my_moon = gr.Circle(gr.Point(moon_center_x, moon_center_y), moon_r)
    my_moon.draw(window)
    my_moon.setFill(color_moon)
    return 0

def draw_clouds(window, cloud_centers_x, cloud_centers_y,
              cloud_part_r, color_cloud, number_of_clouds):
    for j in range(number_of_clouds):
        for i in range (3):
            my_cloud_part = gr.Circle(gr.Point(cloud_centers_x[j]+50*i, cloud_centers_y[j]),
                                      cloud_part_r)
            my_cloud_part.draw(window)
            my_cloud_part.setFill(color_cloud)
        
    return 0

def draw_forest(window, horizon_height, number_of_trees):
    for i in range (number_of_trees):
        my_tree = gr.Rectangle(gr.Point(20*i, horizon_height-20) ,
                               gr.Point(20+20*i, horizon_height+20) )
        my_tree.draw(window)
        my_tree.setFill("green")
    
    return 0
#test commit

def draw_Night(window,
               weight, height,
               color_land, color_sky, color_moon, color_cloud,
               horizon_height, 
               moon_center_x, moon_center_y, moon_r,
               cloud_centers_x, cloud_centers_y, cloud_part_r, number_of_clouds,
               number_of_trees):
    
    draw_land(window, color_land, weight, height)
    draw_sky(window, horizon_height , weight, color_sky)
    draw_moon(window, moon_center_x, moon_center_y, moon_r, color_moon)
    draw_clouds(window, cloud_centers_x, cloud_centers_y,
               cloud_part_r, color_cloud, number_of_clouds)
    draw_forest(window, horizon_height, number_of_trees)
    
    return 

def main():
    print("1")
    draw = True
    weight = 600
    height = 600
    color_land="grey"
    color_sky="blue"
    color_moon="yellow"
    color_cloud="white"
    
    horizon_height=240

    moon_center_x=50
    moon_center_y=50
    moon_r = 20
    
    cloud_centers_x = [70, 480]
    cloud_centers_y = [70, 80]
    cloud_part_r = 40
    
    
    number_of_trees = 10
    
    
    if len(cloud_centers_x) == len(cloud_centers_y):
        number_of_clouds = len(cloud_centers_x)
        
    else:
        print("error in list of cloud senters")
        draw = False
    
    if draw == True:
        
        window = gr.GraphWin("Night", weight, height)
        draw_Night(window,
               weight, height,
               color_land, color_sky, color_moon, color_cloud,
               horizon_height, 
               moon_center_x, moon_center_y, moon_r,
               cloud_centers_x, cloud_centers_y, cloud_part_r, number_of_clouds,
               number_of_trees)
        window.getMouse()
        window.close()     
    

main()
