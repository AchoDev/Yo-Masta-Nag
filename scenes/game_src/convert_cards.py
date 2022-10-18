from cards.blue_cards import *
from cards.red_cards import *

def convert_card(selectable_card):
    name = selectable_card.card_values[1] 
    return globals()[name](False)

    # match(name):
    #     #* cnd -> card not done yet

        # #> red
        # case "broken_tank":
        #     return broken_tank()
        # case "goblin":
        #     return goblin()
        # case "junkie":
        #     return junkie()
        # case "lost_ghost":
        #     return lost_ghost()
        # case "missing_transition":
        #     return missing_transition()
        # case "passionate_icecream_eater":
        #     return goblin()             #* cnd
        # case "sleep_paralysis_demon":
        #     return goblin()             #* cnd
        
        # #> blue 
        # case "bubblegum_dealer":
        #     return bubblegum_dealer()
        # case "kuba_colognalo":
        #     return kuba_colognalo()
        # case "mario":
        #     return goblin()             #* cnd
        # case "sad_rejection":
        #     return goblin()             #* cnd
        # case "stand_up_comedian":
        #     return goblin()             #* cnd
        
        # #> green
        # case "cameraman":
        #     return goblin()             #* cnd
        # case "desert_bandit":
        #     return goblin()             #* cnd
        # case "hell_demon":
        #     return goblin()             #* cnd
        # case "no_way":
        #     return goblin()             #* cnd
        # case "x_rayvren":
        #     return goblin()             #* cnd