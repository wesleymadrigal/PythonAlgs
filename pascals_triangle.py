#!usr/bin/env python

def triangle(n):
    triangle_l = []
    if n == 0:
        return []
    else:
        for i in range(n):
            triangle_l.append([])
    for e in range(len(triangle_l)):
        if e == 0 or e == 1:
            for i in range(e+1):
                triangle_l[e].append(1)
        else:
            for i in range(e+1):
                if i == 0 or i == e:
                    triangle_l[e].append(1)
                else:
                    val = triangle_l[e-1][i-1]+triangle_l[e-1][i]
                    triangle_l[e].append(val)  
    return triangle_l

if __name__ == '__main__':
  pascal_size = raw_input('Enter a pascal triangle size: ')
  pascals_triangle = triangle(int(pascal_size))
  for i in pascals_triangle:
    print i
