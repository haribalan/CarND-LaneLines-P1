
def draw_lines(img, lines, color=[255, 0, 0], thickness=5):
    """
    NOTE: this is the function you might want to use as a starting point once you want to 
    average/extrapolate the line segments you detect to map out the full
    extent of the lane (going from the result shown in raw-lines-example.mp4
    to that shown in P1_example.mp4).  
    
    Think about things like separating line segments by their 
    slope ((y2-y1)/(x2-x1)) to decide which segments are part of the left
    line vs. the right line.  Then, you can average the position of each of 
    the lines and extrapolate to the top and bottom of the lane.
    
    This function draws `lines` with `color` and `thickness`.    
    Lines are drawn on the image inplace (mutates the image).
    If you want to make the lines semi-transparent, think about combining
    this function with the weighted_img() function below
    """
    for line in lines:
        for x1,y1,x2,y2 in line:
            #cv2.line(img, (x1, y1),(x2,y2), color, thickness) 
            #return
            slope = ((y2-y1)/(x2-x1))
            theta = np.arctan(slope)
            #ext=18
            #this ignores extrapolating the lines on road that are not lanes e.g. road markings 
            if slope>-0.4 and slope<0.4: #they are almost perpendicular
                continue 
            if(slope<0): #Left lane
                #cv2.line(img, (x1 - int(ext * (np.cos(theta))), y1 + int(ext * (np.sin(theta)))), 
                         #(x2 + int(ext * (np.cos(theta))), y2 - int(ext * (np.sin(theta)))), color, thickness)   
                b = y1 - slope*x1
                y1 = 540 #starting from the bottom of the image
                if math.isinf((y1-b)/slope):
                    continue
                else:
                    x1 = int(round((y1-b)/slope))
                
                b = y2 - slope*x2
                y2 = y2-5 #mid of the image
                if math.isinf((y2-b)/slope):
                    continue
                else:
                    x2 = int(round((y2-b)/slope))
                                
                
                cv2.line(img, (x1, y1),(x2,y2), color, thickness) 
            else: #right lane
                #cv2.line(img, (x1- int(ext * (np.cos(theta))), y1 - int(ext * (np.sin(theta)))), 
                         #(x2 + int(ext * (np.cos(theta))), y2 + int(ext * (np.sin(theta)))), color, thickness)     
                b = y1 - slope*x1
                y1 = y1-10
                if math.isinf((y1-b)/slope):
                    continue
                else:
                    x1 = int(round((y1-b)/slope))
                
                b = y2 - slope*x2
                y2 = 540 
                if math.isinf((y2-b)/slope):
                    continue
                else:
                    x2 = int(round((y2-b)/slope))  
                
                cv2.line(img, (x1, y1),(x2,y2), color, thickness) 
