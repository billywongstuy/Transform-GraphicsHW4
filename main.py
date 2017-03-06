from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
ident(transform)

#'script' contains the list of arguments
#parse_file( 'script', edges, transform, screen, color )
parse_file( 'myscript', edges, transform, screen, color )
