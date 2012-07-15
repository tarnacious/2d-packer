2D Packing
----------

After chatting about programming my flatmate wanted to know how you would solve a glass cutting problem with Programming.

We are doing it as two programs. The first takes a list of heights and widths and returns thier placement position, width and height.

    $ echo "10 10
    > 20 20" | python2 pack.py
    0 0 20 20
    20 0 10 10

The second draws the boxes.

    $ cat rectangles.txt | python2 pack.py | python2 draw.py

![screenshot](https://github.com/tarnacious/2d-packer/blob/master/screenshot.png)

The problem we want to solve is a little more complex but this is a nice start.
