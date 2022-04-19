def on_forever():
    def on_logo_event_pressed():
        pass
    input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)
basic.show_icon(IconNames.SQUARE) 
def on_logo_event_pressed2():
    basic.pause(100)
    pass
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed2)
basic.show_icon(IconNames.SMALL_SQUARE)            
             
  
 

basic.forever(on_forever)