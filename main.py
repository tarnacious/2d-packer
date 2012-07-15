from packer import CygonRectanglePacker
import sys

lines = sys.stdin.readlines()
rectangles = []

for line in lines:
    points = line.split(' ')
    rectangles.append((int(points[0]), int(points[1])))

packer = CygonRectanglePacker(100, 100)
rectangles = sorted(rectangles, key=lambda r: ( r[0] * r[1]))

placements = []

for rectangle in rectangles:
    #print "Try to pack:", rectangle[0], ",", rectangle[1]
    placement = packer.TryPack(rectangle[0], rectangle[1])
    if placement:
        #print "Packed at:", placement.x, ",", placement.y
        placements.append((rectangle, placement))
    else:
        #print "Unable to pack"
        pass

for ((height, width), placement) in placements:
    print placement.x, placement.y, height, width
