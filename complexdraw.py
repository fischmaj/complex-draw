#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graphics import *
from cmath import polar, pi
from ast import literal_eval as make_tuple


# This function takes a complex number and a graphics window and draws
# green lines on the graphics window in relation to the points in a file
# called "data.txt"  The points in data.txt must be entered as (x,y) followed
# by a newline.  A line will be drawn between each successive point in the
# "data.txt" file, dot-to-dot style unless a blank line (newline character) 
# is the only entry on a line of the file.  This is the signal to end the 
# previous line or "pick the pen off the paper" and begin the next line at 
# a new point.  Each point in "data.txt" will treated as a number in the
# complex plane, and before it is graphed, it will be multiplied by the given 
# complex number, and the resulting points and lines will be displayed on
# the screen.   To display the points of "data.txt" in their original form, use
# the complex number 1. 
def draw_picture(compl, window):
    
    myfile = open('data.txt', 'r')
    line_list = []
    new_object = True

    for text_line in myfile:
        if text_line[0] == "(":
            if new_object:
                tuple = make_tuple(text_line)
                old_point = complex(tuple[0], tuple[1])
                old_point = compl * old_point
                new_object = False

            tuple = make_tuple(text_line)
            point = complex(tuple[0], tuple[1])
            point = compl * point

            # complex mult returns floats, so they must be explicitly cast
            # to ints before they are valid graphics points
            line = Line(Point( int (old_point.real), int(old_point.imag) ), 
                        Point( int(point.real), int(point.imag)  )       )
            line.setOutline(color_rgb(0,255,0))
            line.draw(window)
            line_list.append(line)
            old_point= point

        else:
            new_object = True
    
    return line_list


def main():

    complex_number = complex(1)#initially, just use identity matrix

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



    #Draw the y axis halway across the window (x=0) and color it blue
    y_axis=Line(
        Point( 0,  int( (win_height/2) *-1) ),
        Point( 0,  int( (win_height/2) )    )  
        )
    y_axis.setFill("blue")
    y_axis.draw(win)


    #Draw the "quit" text near the bottom of the window
    exit_text=Text(
        Point(0,  int (win_height*-7/16 ) ),
        "Quit")
    exit_text.setTextColor("white")
    exit_text.setSize(32)
    exit_text.draw(win)


    #Draw the "i" text next to the imaginary input box
    i_text=Text(
        Point( int (win_width*31/64 ),  int (win_height*7/16 ) ),
        "i")
    i_text.setTextColor("white")
    i_text.setSize(32)
    i_text.draw(win)

    #Draw the "+" text next to the real input box
    plus_text=Text(
        Point( int (win_width*12/32 ),  int (win_height*7/16 ) ),
        "+")
    plus_text.setTextColor("white")
    plus_text.setSize(32)
    plus_text.draw(win)


    #Draw the polar form of the complex number text below the input boxes
    polar_number = polar(complex_number)
    polar_text=Text(
        Point( int (win_width*12/32 ),  int (win_height*3/8 ) ),
        "Radius:"+str("%.4f" % polar_number[0])+","
        "Theta:"+str("%.1f" % (polar_number[1]*180/pi))+"°")
    polar_text.setTextColor("white")
    polar_text.setSize(12)
    polar_text.draw(win)




    #These lines place 2 text boxes near the upper left corner of the screen
    #These text boxes are the inputs for the real and imaginary parts of the
    #complex number
    input_real=Entry(
        Point( int( (win_width*5/16) ) ,  int ( ( win_height*7/16) ) ),
        5)
    input_real.setText(  str(complex_number.real))
    input_real.draw(win)

    input_imaginary=Entry(
        Point( int( (win_width*14/32) ) ,  int ( ( win_height*7/16) ) ),
        5)
    input_imaginary.setText(  str(complex_number.imag) )
    input_imaginary.draw(win)
         

    drawn_objects=[]
    drawn_objects.append(draw_picture(complex_number, win) )




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
                    for element in objects:
                        element.undraw()
                    
                # try to read the elements in the complex number text boxes
                # and redraw the picture using the new values
                try:

                    real_part = float( input_real.getText() )
                    imaginary_part = float( input_imaginary.getText())
                    complex_number = complex(real_part, imaginary_part)
                    drawn_objects.append (draw_picture(complex_number, win))

                    #update the polar text box-- uses "%.4f"% and "%.1f"%
                    #to display 4and 1 decimal places, respectively
                    polar_text.undraw()
                    polar_number = polar(complex_number)
                    polar_text.setText(
                        "Radius:"+str("%.4f" % polar_number[0])+","+
                        "Theta:" +str("%.1f" % (polar_number[1]*180/pi))+"°")
                    polar_text.draw(win)
                  
                # if there is a problem with the read or draw operations,
                # do nothing and wait for the next mouse click. 
                except:
                    None  #this exception handler doesn't do anything


            
    win.close()


main()
