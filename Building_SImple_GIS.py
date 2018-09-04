import turtle as t #import a module and define it in an easier way
#1) How to define a list and how it does work
firstItem = 0 #define a new variable
#myList[firstItem] #create a new list, starting with number firstItem
#2)Define a state
#Since every city/state has his own name, coordinates and population define:
NAME =0
POINTS=1
POP=2
#Set up now data for Colorado with name, polygons points (a list) and population
state = ["COLORADO", [[-109, 37],[-109, 41],[-102, 41],[-102, 37]], 5187582]
#3)Create a nested list for the cities
cities=[] #emptylist
cities.append(["DENVER", [-104.98, 39.74], 634265]) #Add now cities list to the list
cities.append(["BOULDER", [-105.27, 40.02], 98889])
cities.append(["DURANGO", [-107.88, 37.28], 17069])
#4)Set now the map width and height
map_width = 400
map_height = 300
#5)Scale the map to the geographic canvas, first of all define the bounding box of the largest layer (the state)
minx=180 #longitude min
maxx=-180 #longitude max
miny= 90 # latititude min
maxy = -90 #latitude max
for x,y in state[POINTS]:
    if x < minx: minx=x
    elif x>maxx: maxx=x
    if y < miny: miny=y
    elif y > maxy: maxy=y
#6 scale the map: step 2. Calculate the ratio between actual state and tiny canvas.
    #useful to convert from coordinates to pixel
dist_x= maxx - minx
dist_y = maxy - miny
x_ratio = map_width/dist_x
y_ratio = map_height/dist_y
#7) define a function that transforms point in map coordinates from a data layer to pixels
#plus we compensate some turtle features (centering map)
def convert(point):
    lon = point[0]
    lat = point[1]
    x= map_width -((maxx-lon)*x_ratio)
    y = map_height -((maxy-lat)*y_ratio)
    #Python turtle graphics starts in the middle of the screen
    #so we must offset the points so they are centered
    x = x - (map_width/2)
    y = y - (map_height/2)
    return [x,y]
#8) render our GIS as a thematic map. Idea Turtle work as a pen.
#t.up() pick up the pen and move t.down() draw
t.up()
first_pixel = None
for point in state[POINTS]:
    pixel = convert(point)
    if not first_pixel:
        first_pixel=pixel
    t.goto(pixel)
    t.down()
t.goto(first_pixel)
t.up()
t.goto([0,0])
t.write(state[NAME], align="center", font=("Arial", 16, "bold"))
t.done()