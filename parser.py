from display import *
from matrix import *
from draw import *
from write import *
import math, random

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 yrotate: create an y-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 zrotate: create an z-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""


def parse_file( fname, points, transform, screen, color ):
    setup_script(fname, color)

    f = open(fname,'r+')
    lines = f.readlines()
    i = 0
    end = len(lines)

    one_line = ['display','apply','ident','']
    
    while i < end:
        command = lines[i].rstrip('\n')
        if i != len(lines)-1:
            args = lines[i+1].rstrip('\n').split(' ')
        else:
            args = []
        if command == 'line':
            add_edge(points,float(args[0]),float(args[1]),float(args[2]),float(args[3]),float(args[4]),float(args[5]))
        elif command == 'ident':
            ident(transform)
        elif command == 'scale':
            scale_matrix = make_scale(float(args[0]),float(args[1]),float(args[2]))
            matrix_mult(scale_matrix,transform)
        elif command == 'move':
            move_matrix = make_translate(float(args[0]),float(args[1]),float(args[2]))
            matrix_mult(move_matrix,transform)
        elif command == 'rotate':
            theta = float(args[1])
            if args[0] == 'x':
                rotate_matrix = make_rotX(theta)
            elif args[0] == 'y':
                rotate_matrix = make_rotY(theta)
            else:
                rotate_matrix = make_rotZ(theta)
            matrix_mult(rotate_matrix,transform)
        elif command == 'apply':
            matrix_mult(transform,points)
        elif command == 'display':
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
        elif command == 'save':
            clear_screen(screen)
            draw_lines(points,screen,color)
            save_extension(screen, args[0])
        elif command == 'color':
            color[0] = int(args[0])
            color[1] = int(args[1])
            color[2] = int(args[2])
        elif command == "":
            i+=0
        else:
            print 'Error occurred'
            exit

        if command in one_line:
            i+=1
        else:
            i+=2



