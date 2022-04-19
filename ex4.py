bearing = 0

def on_forever():
    global bearing
    bearing = input.compass_heading()
    if bearing < 45 or bearing > 315:
        basic.show_string("N")
        basic.show_string("S")
    else:
        
        bearing = input.compass_heading()
    if bearing > 45 or bearing > 315:
        basic.show_string("W")
        basic.show_string("E")
basic.forever(on_forever)