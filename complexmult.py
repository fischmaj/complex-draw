#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graphics import *
from cmath import polar, pi
from ast import literal_eval as make_tuple

def draw_picture(complex, win, color):
    
    radius = 5

    #multiplying by 35 because of the size of the screen
    point = Point( int(complex.real*35), int(complex.imag*35) )
    origin = Point (0,0)
    line= Line(origin, point)
    line.setOutline(color)
    line.setFill(color)
    line.draw(win)

    circle = Circle(point, radius)
    circle.setFill(color)
    circle.draw(win)

    objects=[]
    objects.append(line)
    objects.append(circle)

    return objects

def main():

    complex1 = complex(1)#initially, just use identity matrix
    complex2 = complex(1)    
    result = complex1*complex2

    keep_open= True

    #Open the Canvas window and set the size
    win_height = 700
    win_width = 700
    win = GraphWin("My Window", win_height, win_width)
    win.setBackground(color_rgb(0,0,0))
    win.setCoords(
        int( (win_width/2)*-1  ),
        int( (win_height/2)*-1 ),
        int( (win_width/2)     ),
        int( (win_height/2)    ))

    #Draw the x axis halfway up the window (y=0) and color it red
    x_axis=Line(
        Point( int( (win_width/2) *-1 ),  0),
        Point( int( (win_width/2)     ),  0)  
        )
    x_axis.setFill("red")
    x_axis.draw(win)
    for i in range(20):
        tickmark = Line (
            Point ( int( (-1*win_width/2)+(win_width*i/20)),-10),
            Point ( int( (-1*win_width/2)+(win_width*i/20)), 10)
            )
        tickmark.setFill("red")
        tickmark.draw(win)

    #Draw the y axis halway across the window (x=0) and color it blue
    y_axis=Line(
        Point( 0,  int( (win_height/2) *-1) ),
        Point( 0,  int( (win_height/2) )    )  
        )
    y_axis.setFill("blue")
    y_axis.draw(win)
    for i in range(20):
        tickmark = Line (
            Point (-10, int( (-1*win_height/2)+(win_height*i/20))),
            Point (10, int( (-1*win_height/2)+(win_height*i/20)))
            )
        tickmark.setFill("blue")
        tickmark.draw(win)


    #Draw the "quit" text near the bottom of the window
    exit_text=Text(
        Point(0,  int (win_height*-7/16 ) ),
        "Quit")
    exit_text.setTextColor("white")
    exit_text.setSize(32)
    exit_text.draw(win)


    #Draw the "i" text next to the imaginary input box
    i1_text=Text(
        Point( int (win_width*31/64 ),  int (win_height*7/16 ) ),
        "i")
    i1_text.setTextColor("cyan")
    i1_text.setSize(32)
    i1_text.draw(win)

    #Draw the "i" text next to the imaginary input box
    i2_text=Text(
        Point( int (win_width*31/64 ),  int (win_height*3/8 ) ),
        "i")
    i2_text.setTextColor("yellow")
    i2_text.setSize(32)
    i2_text.draw(win)

    #Draw the "+" text next to the real input box
    plus1_text=Text(
        Point( int (win_width*12/32 ),  int (win_height*7/16 ) ),
        "+")
    plus1_text.setTextColor("cyan")
    plus1_text.setSize(32)
    plus1_text.draw(win)

    #Draw the "+" text next to the real input box
    plus2_text=Text(
        Point( int (win_width*12/32 ),  int (win_height*3/8 ) ),
        "+")
    plus2_text.setTextColor("yellow")
    plus2_text.setSize(32)
    plus2_text.draw(win)


    #Draw the polar form of the complex number text below the input boxes
    polar1 = polar(complex1)
    polar1_text=Text(
        Point( int (win_width*12/32 ),  int (win_height*13/32 ) ),
        "Radius:"+str("%.4f" % polar1[0])+","
        "Theta:"+str("%.1f" % (polar1[1]*180/pi))+"°")
    polar1_text.setTextColor("cyan")
    polar1_text.setSize(12)
    polar1_text.draw(win)

    #Draw the polar form of the complex number text below the input boxes
    polar2 = polar(complex2)
    polar2_text=Text(
        Point( int (win_width*12/32 ),  int (win_height*11/32 ) ),
        "Radius:"+str("%.4f" % polar2[0])+","
        "Theta:"+str("%.1f" % (polar2[1]*180/pi))+"°")
    polar2_text.setTextColor("yellow")
    polar2_text.setSize(12)
    polar2_text.draw(win)

    #Draw the rectilinar form of the result
    result_text=Text(
        Point( int (win_width*12/32 ),  int (win_height*10/32 ) ),
        str("%.4f" % result.real)+  "+" + 
        str("%.4f" % result.imag+"i"))
    result_text.setTextColor("green")
    result_text.setSize(24)
    result_text.draw(win)


    #Draw the polar form of the complex number text below the input boxes
    polar3 = polar(result)
    polar3_text=Text(
        Point( int (win_width*12/32 ),  int (win_height*9/32 ) ),
        "Radius:"+str("%.4f" % polar3[0])+","
        "Theta:"+str("%.1f" % (polar3[1]*180/pi))+"°")
    polar3_text.setTextColor("green")
    polar3_text.setSize(12)
    polar3_text.draw(win)
    

    #These lines place 2 text boxes near the upper left corner of the screen
    #These text boxes are the inputs for the real and imaginary parts of the
    #complex number
    input1_real=Entry(
        Point( int( (win_width*5/16) ) ,  int ( ( win_height*7/16) ) ),
        5)
    input1_real.setText(  str(complex1.real))
    input1_real.draw(win)

    input1_imaginary=Entry(
        Point( int( (win_width*14/32) ) ,  int ( ( win_height*7/16) ) ),
        5)
    input1_imaginary.setText(  str(complex1.imag) )
    input1_imaginary.draw(win)
         

    #These lines place 2 text boxes near the upper left corner of the screen
    #These text boxes are the inputs for the real and imaginary parts of the
    #complex number
    input2_real=Entry(
        Point( int( (win_width*5/16) ) ,  int ( ( win_height*3/8) ) ),
        5)
    input2_real.setText(  str(complex2.real))
    input2_real.draw(win)

    input2_imaginary=Entry(
        Point( int( (win_width*14/32) ) ,  int ( ( win_height*3/8) ) ),
        5)
    input2_imaginary.setText(  str(complex2.imag) )
    input2_imaginary.draw(win)
         

    drawn_objects=[]
    drawn_objects.append(draw_picture(complex1, win, "cyan"))
    drawn_objects.append(draw_picture(complex2, win, "yellow"))
    drawn_objects.append(draw_picture(result, win, "green"))

    # This is the main loop which draws the picture.  The picure is redrawn
    # with each click of the mouse, using the current values in the transform
    # matrix, until the user clicks on "quit"

    while(keep_open):
        clickPoint = win.getMouse()

        #if there is a valid click in a window execute the code below
        if (clickPoint):

            #if the user clicks on "quit" exit the program
            if (
                (clickPoint.getX() > -25) and
                (clickPoint.getX() < 25) and
                (clickPoint.getY() > int(  (win_height/-2) )    ) and
                (clickPoint.getY() < int( (win_height*-3/8))    ) ):
                keep_open = False

            #if the user clicks somewhere other than quit, do the following
            else:

                #remove the old drawing
                for objects in drawn_objects:
                    for object in objects:
                        object.undraw()
                    
                # try to read the elements in the complex number text boxes
                # and redraw the picture using the new values
                try:

                    real_part1 = float( input1_real.getText() )
                    imaginary_part1 = float( input1_imaginary.getText())

                    real_part2 = float( input2_real.getText() )
                    imaginary_part2 = float( input2_imaginary.getText())


                    complex1 = complex(real_part1, imaginary_part1)
                    complex2 = complex(real_part2, imaginary_part2)
                    result = complex1*complex2


                    drawn_objects.append (
                        draw_picture(complex1, win,"cyan"))
                    drawn_objects.append (draw_picture(complex2, win,"yellow"))
                    drawn_objects.append (draw_picture(result, win, "green"))
                    

                    #update the polar text box-- uses "%.4f"% and "%.1f"%
                    #to display 4and 1 decimal places, respectively
                    polar1_text.undraw()
                    polar1 = polar(complex1)
                    polar1_text.setText(
                        "Radius:"+str("%.4f" % polar1[0])+","+
                        "Theta:" +str("%.1f" % (polar1[1]*180/pi))+"°")
                    polar1_text.draw(win)

                    polar2_text.undraw()
                    polar2 = polar(complex2)
                    polar2_text.setText(
                        "Radius:"+str("%.4f" % polar2[0])+","+
                        "Theta:" +str("%.1f" % (polar2[1]*180/pi))+"°")
                    polar2_text.draw(win)

                    result_text.undraw()
                    result_text.setText(
                        str("%.4f" % result.real)+"+"+
                        str("%.4f" % result.imag)+"i")
                    result_text.draw(win)
                  

                    polar3_text.undraw()
                    polar3 = polar(result)
                    polar3_text.setText(
                        "Radius:"+str("%.4f" % polar3[0])+","+
                        "Theta:" +str("%.1f" % (polar3[1]*180/pi))+"°")
                    polar3_text.draw(win)
                  
                    

                # if there is a problem with the read or draw operations,
                # do nothing and wait for the next mouse click. 
                except:
                    print("Unexpected error:", sys.exc_info()[0]) 

#this exception handler doesn't do anything


            
    win.close()


main()
