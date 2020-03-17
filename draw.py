from display import *
from matrix import *

  # ====================
  # add the points for a rectagular prism whose
  # upper-left corner is (x, y, z) with width,
  # height and depth dimensions.
  # ====================
def add_box( points, x, y, z, width, height, depth ):
    top_y = y
    bottom_y = y - height
    left_x = x
    right_x = x + width
    front_z = z
    back_z = z - depth
    add_edge(points, left_x, top_y, back_z, right_x, top_y, back_z)
    add_edge(points, right_x, top_y, back_z, right_x, bottom_y, back_z)
    add_edge(points, right_x, bottom_y, back_z, left_x, bottom_y, back_z)
    add_edge(points, left_x, bottom_y, back_z, left_x, top_y, back_z)

    add_edge(points, left_x, top_y, front_z, right_x, top_y, front_z)
    add_edge(points, right_x, top_y, front_z, right_x, bottom_y, front_z)
    add_edge(points, right_x, bottom_y, front_z, left_x, bottom_y, front_z)
    add_edge(points, left_x, bottom_y, front_z, left_x, top_y, front_z)

    add_edge(points, left_x, top_y, front_z, left_x, top_y, back_z)
    add_edge(points, right_x, top_y, front_z, right_x, top_y, back_z)
    add_edge(points, right_x, bottom_y, front_z, right_x, bottom_y, back_z)
    add_edge(points, left_x, bottom_y, front_z, left_x, bottom_y, back_z)

  # ====================
  # Generates all the points along the surface
  # of a sphere with center (cx, cy, cz) and
  # radius r.
  # Returns a matrix of those points
  # ====================
def generate_sphere( points, cx, cy, cz, r, step ):
    sphere = new_matrix(0,0)
    rot = 0
    circ = 0
    pi2 = 2 * math.pi
    while (rot < 2):
        while (circ < 2):
            cpi = math.pi * circ
            rpi = math.pi * rot
            x = r * math.cos(cpi) + cx
            y = r * math.sin(cpi) * math.cos(rpi) + cy
            z = r * math.sin(cpi) * math.sin(rpi) + cz
            add_point(sphere, x, y, z)
            circ += step
        rot += step
        circ = 0

    return sphere

  # ====================
  # adds all the points for a sphere with center
  # (cx, cy, cz) and radius r to points
  # should call generate_sphere to create the
  # necessary points
  # ====================
def add_sphere( points, cx, cy, cz, r, step ):
    print("sphere")
    sphere = generate_sphere(points, cx, cy, cz, r, step)
    for point in sphere:
        add_edge(points, point[0], point[1], point[2], point[0], point[1], point[2])


  # ====================
  # Generates all the points along the surface
  # of a torus with center (cx, cy, cz) and
  # radii r0 and r1.
  # Returns a matrix of those points
  # ====================
def generate_torus( points, cx, cy, cz, r0, r1, step ):
    torus = new_matrix(0,0)
    rot = 0
    circ = 0
    pi2 = 2 * math.pi
    while (rot < 2):
        while (circ < 2):
            cpi = math.pi * circ
            rpi = math.pi * rot
            x = math.cos(rpi) * (r0 * math.cos(cpi) + r1) + cx
            y = r0 * math.sin(cpi) + cy
            z =-math.sin(rpi) * (r0 * math.cos(cpi) + r1) + cz
            # print ([x, y, z])
            add_point(torus, x, y, z)
            circ += step
        rot += step
        circ = 0
    # print_matrix(torus)
    return torus


  # ====================
  # adds all the points for a torus with center
  # (cx, cy, cz) and radii r0, r1 to points
  # should call generate_torus to create the
  # necessary points
  # ====================
def add_torus( points, cx, cy, cz, r0, r1, step ):
    print("torus")
    torus = generate_torus( points, cx, cy, cz, r0, r1, step )
    for point in torus:
        add_edge(points, point[0], point[1], point[2], point[0], point[1], point[2])



def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    pi2 = 2 * math.pi
    x = r * math.cos(pi2 * t) + cx
    y = r * math.sin(pi2 * t) + cy
    while t < 1:
        t = t + step
        newx = r * math.cos(pi2 * t) + cx
        newy = r * math.sin(pi2 * t) + cy
        add_edge(points, x, y, cz, newx, newy, cz)
        x = newx
        y = newy

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    x_coef = generate_curve_coefs(x0, x1, x2, x3, curve_type)
    y_coef = generate_curve_coefs(y0, y1, y2, y3, curve_type)

    x = x0
    y = y0
    t = 0
    while t < 1:
        t = t + step
        t3 = t * t * t
        t2 = t * t
        newx = x_coef[0][0] * t3 + x_coef[0][1] * t2 + x_coef[0][2] * t + x_coef[0][3]
        newy = y_coef[0][0] * t3 + y_coef[0][1] * t2 + y_coef[0][2] * t + y_coef[0][3]
        add_edge(points, x, y, 0, newx, newy, 0)
        x = newx
        y = newy


def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
