import pygame
import math
from datetime import datetime
import time

def main():

    pygame.init() 

    window_size = (600, 600)

    screen = pygame.display.set_mode((window_size)) #Create a window of 640x600 pixels

    black = (0, 0, 0)
    white = (255, 255, 255)

    center = ((window_size[0]/2, window_size[1]/2))

    print(f"Time: {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}")

    run_flag = True
    while run_flag is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_flag = False

        screen.fill((black)) #Fill with black
        pygame.draw.circle(screen, (white), (center), 160, 10) #Draw circle
        for i in range(12): #draw clock hours
            angle_h = math.radians(i * (360/12)) #Split 360 degress in 12, change to radians

            start_point_x = center[0] + 125 * math.cos(angle_h) #Calculate start point for x coordinate 
            start_point_y = center[1] + 125 * math.sin(angle_h) #Calculate start point for y coordinate

            end_point_x = center[0] + 150 * math.cos(angle_h) #Calculate end point for x coordinate 
            end_point_y = center[1] + 150 * math.sin(angle_h) #Calculate end point for y coordinate
            
            #maybe use loop to draw the numbers for each hour (need to set start angle not cos 1)
            pygame.draw.line(screen, (white), (start_point_x, start_point_y), (end_point_x, end_point_y), 2) # Draw the line

        for i in range(60): #Draw clock minutes 
            angle_h = math.radians(i * (360/60)) #Split 360 degress in 60, change to radians

            start_point_x = center[0] + 140 * math.cos(angle_h) #Calculate start point for x coordinate 
            start_point_y = center[1] + 140 * math.sin(angle_h) #Calculate start point for y coordinate

            end_point_x = center[0] + 150 * math.cos(angle_h) #Calculate end point for x coordinate 
            end_point_y = center[1] + 150 * math.sin(angle_h) #Calculate end point for y coordinate
            
            pygame.draw.line(screen, (white), (start_point_x, start_point_y), (end_point_x, end_point_y)) # Draw line
        
        counter_minutes(screen, center)
        counter_hours(screen, center)
        counter_seconds(screen, center)

        pygame.display.flip() #Refresh the screen
        time.sleep(1)


def counter_seconds(screen, center):
    angle = math.radians(360/60*(datetime.now().second + 45))
    x_end = center[0] + 100 * math.cos(angle)
    y_end = center[1] + 100 * math.sin(angle)
    pygame.draw.line((screen), (255, 0, 0), (center[0], center[1]), (x_end, y_end))
    
def counter_minutes(screen, center):
    angle = math.radians(360/60*(datetime.now().minute + 45))
    x_end = center[0] + 100 * math.cos(angle)
    y_end = center[1] + 100 * math.sin(angle)
    pygame.draw.line((screen), (255, 255, 255), (center[0], center[1]), (x_end, y_end),2)

def counter_hours(screen, center):
    angle = math.radians(360/12*(datetime.now().hour + 45))
    x_end = center[0] + 75 * math.cos(angle)
    y_end = center[1] + 75 * math.sin(angle)
    pygame.draw.line((screen), (255, 255, 255), (center[0], center[1]), (x_end, y_end),3)

if __name__ == "__main__":
    main()