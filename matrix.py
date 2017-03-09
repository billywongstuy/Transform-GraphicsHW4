from __future__ import division
import math

#transformation matrices rows and cols need to be flipped

def transpose(m):
    new_m = [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
    for row in range(4):
        for col in range(4):
            new_m[row][col] = m[col][row]
    return new_m

def make_translate( x, y, z ):
    #
    trans_matrix = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[x,y,z,1]]
    return trans_matrix

def make_scale( x, y, z ):
    scale_matrix = [[x,0,0,0],[0,y,0,0],[0,0,z,0],[0,0,0,1]]
    return scale_matrix

def make_rotX( theta ):
    rotX_matrix = []
    rad = math.radians(theta)
    sin = math.sin(theta)
    cos = math.cos(theta)
    
    '''    
    rotX_matrix.append([1,0,0,0])
    rotX_matrix.append([0,math.cos(theta),-math.sin(theta),0])
    rotX_matrix.append([0,math.sin(theta),math.cos(theta),0])
    rotX_matrix.append([0,0,0,1])
    return transpose(rotX_matrix)
    '''
    
    rotX_matrix.append([1,0,0,0])
    rotX_matrix.append([0,cos,sin,0])
    rotX_matrix.append([0,-sin,cos,0])
    rotX_matrix.append([0,0,0,1])
    return rotX_matrix
    

def make_rotY( theta ):
    rotY_matrix = []
    rad = math.radians(theta)
    sin = math.sin(theta)
    cos = math.cos(theta)

    '''
    rotY_matrix.append([cos,0,sin,0])
    rotY_matrix.append([0,1,0,0])
    rotY_matrix.append([-sin,0,0,cos])
    rotY_matrix.append([0,0,0,1])
    return transpose(rotY_matrix)
    '''

    rotY_matrix.append([cos,0,-sin,0])
    rotY_matrix.append([0,1,0,0])
    rotY_matrix.append([sin,0,0,0])
    rotY_matrix.append([0,0,cos,1])    
    return rotY_matrix


def make_rotZ( theta ):
    rotZ_matrix = []
    rad = math.radians(theta)
    sin = math.sin(theta)
    cos = math.cos(theta)
    
    '''
    rotZ_matrix.append([math.cos(theta),-math.sin(theta),0,0]) #'x-axis'
    rotZ_matrix.append([math.sin(theta),math.cos(theta),0,0]) #'y-axis'
    rotZ_matrix.append([0,0,1,0])
    rotZ_matrix.append([0,0,0,1])
    '''
    
    rotZ_matrix.append([cos,sin,0,0])
    rotZ_matrix.append([-sin,cos,0,0])
    rotZ_matrix.append([0,0,1,0])
    rotZ_matrix.append([0,0,0,1])
    
    return rotZ_matrix

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #print 'm1: ',m1
    #print 'm2: ',m2
    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
            
        point+= 1

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
