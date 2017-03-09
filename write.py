def line_write(x0,y0,z0,x1,y1,z1):
    return 'line\n%f %f %f %f %f %f\n' % (x0,y0,z0,x1,y1,z1)
def line_write_noz(x0,y0,x1,y1):
    return 'line\n%f %f 0 %f %f 0\n' % (x0,y0,x1,y1)
def scale_write(x,y,z):
    return 'scale\n%f %f %d\n' % (x,y,z)
def move_write(x,y,z):
    return 'move\n%f %f %f\n' % (x,y,z)
def rotate_write(a,t):
    return 'rotate\n%s %s\n' % (a,t)
def save_write(f):
    return 'save\n%s\n' % (f)
def color_write(x,y,z):
    return 'color\n%d %d %d\n' % (x,y,z)

def color_val_move(val,amt):
    val += amt
    val %= 256
    return val

def setup_script(fname, color):
    #setup_book_script(fname, color)
    setup_spiral_script(fname, color)
    #pass


def setup_spiral_script(fname, color):
    f = open(fname,'w')

    color[0] = 132
    color[1] = 183
    color[2] = 78
    
    f.write('ident\n')
    f.write(rotate_write('z',str(-0.5)))
    f.write(scale_write(0.985,0.985,0))

    for r in range(0,1):
        for i in range(0,300):
            f.write('apply\n')
            color[0] = color_val_move(color[0],67)
            color[1] = color_val_move(color[1],10)
            color[2] = color_val_move(color[0],-54)
            
            f.write(line_write(-250,-250,r,250,-250,r))
            f.write(line_write(-250,250,r,250,250,r))
            f.write(line_write(-250,-250,r,-250,250,r))
            f.write(line_write(250,-250,r,250,250,r))
            
    f.write('ident\n')
    f.write(scale_write(2.5,1.5,2))
    f.write(rotate_write('x',180))
    f.write(rotate_write('y',90))
    f.write(move_write(250,250,0))
    f.write('apply\n')
    f.write('display\n')
    f.write(save_write('spiral-3d.png'))
    f.close()




def setup_book_script(fname, color):
    f = open(fname,'w')

    f.write(rotate_write('z','math.pi/36'))
    f.write(scale_write(0.98,0.98,1))
    
    for i in range(0,20):
        f.write('apply\n')
        f.write(line_write(0,0,0,200,0,0))
        f.write(line_write(200,0,0,200,200,0))
        f.write(line_write(0,200,0,200,200,0))
        f.write(line_write(0,0,0,0,200,0))

    f.write('ident\n')
    f.write(move_write(250,200,0))
    f.write(rotate_write('x','45'))
    f.write(rotate_write('y','45'))
    f.write(rotate_write('z','45'))
    
    f.write('apply\n')
    f.write('display\n')
    f.write(save_write('bookthing.png'))
    f.close()
