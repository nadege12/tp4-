
def on_forever():
    if input.button_is_pressed(Button.B):
        basic.show_number(input.temperature()) 
    elif input.light_level() > 100: 
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.clear_screen()
 
basic.forever(on_forever)