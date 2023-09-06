import pygame
import cv2
import numpy as np

video=cv2.VideoCapture(0)

faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


pygame.init()



window=pygame.display.set_mode((1400,1500))

pygame.display.set_caption("Face Detection App")

img=pygame.image.load("cat.jpeg").convert()

start=True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start=False
            pygame.quit()
            
    ret,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(frame,1.3,5)
    for(x,y,w,h) in faces:
        x1,y1=x+w,y+h
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),1)
        cv2.line(frame,(x,y),(x+30,y),(0,0,255),6)
        cv2.line(frame,(x,y),(x,y+30),(0,0,255),6)
        
        cv2.line(frame,(x1,y),(x1-30,y),(0,0,255),6)
        cv2.line(frame,(x1,y),(x1,y+30),(0,0,255),6)
        
        cv2.line(frame,(x,y1),(x+30,y1),(0,0,255),6)
        cv2.line(frame,(x,y1),(x,y1-30),(0,0,255),6)
        
        cv2.line(frame,(x1,y1),(x1-30,y1),(0,0,255),6)
        cv2.line(frame,(x1,y1),(x1,y1-30),(0,0,255),6)
        
        
        
    
    imgRGB=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgRGB=np.rot90(imgRGB)
    imgRGB=pygame.surfarray.make_surface(imgRGB).convert()
    
    font=pygame.font.Font(None,50)
    text=font.render("Face Detection :  {} Face Detected".format(len(faces)),True,(255,255,255))
    
    
    
    
    window.blit(img,(0,0))
    window.blit(imgRGB,(70,70))
    
    
    pygame.draw.rect(window,(144,238,144),(100,30,1200,50),border_top_left_radius=10, border_top_right_radius=10)
    pygame.draw.rect(window,(144,238,144),(100,800,1200,50),border_bottom_left_radius=10,border_bottom_right_radius=10)
    window.blit(text,(320,50))
    pygame.display.update()
    
    
    