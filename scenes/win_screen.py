import main


import sys
sys.path.append("..")

from cls.Colors import COL
from cls.Text import Text



def load_scene(winner):
    
    while True:
        match winner:
            case "enemy":
                main.WIN.fill(COL.red.value)

                text = Text(0, 0, COL.black.value, 70, "oh NO! enemy won?! why you so bad man????")
                text.place_center(main.WIN) # okan hat mir bei diesem Projekt geholfen!
                
                text.draw(main.WIN)
            case "player":
                main.WIN.fill(COL.blue.value)

                text = Text(0, 0, COL.black.value, 60, "WOW omg !!! you won you so good now you can die peacefully")
                text.place_center(main.WIN)

                text.draw(main.WIN)
        