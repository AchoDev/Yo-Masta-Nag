


def drop_card(card):

    global active_card1, active_card2, active_card3, enemy_active_card1, enemy_active_card2, enemy_active_card3, energy

    match card.current_state:
        case 0:
            collision_count = 0
            for area in areas:
                if check_collision(card, area):
                    collision_count = collision_count + 1
                
            if collision_count <= 0 or collision_count > 1:
                card.return_to_original_position()
                return None

            if energy <= 0:
                return None

            for i in range(len(areas)):
                if check_collision(card, areas[i]):
                    if active_cards[i].value == None:
                        active_cards[i].value = card
                        hand_cards.remove(card)

                        card.x = areas[i].x
                        card.y = areas[i].y
                        card.set_original_pos((card.x, card.y))

                        card.current_state = 1

                        energy -= 1
                    else:
                        card.return_to_original_position()
                        


            # if check_collision(card, drop_area1):
            #     if active_card1.value == None:
            #         active_card1.value = card

            #         card.x = drop_area1.x
            #         card.y = drop_area1.y
            #         card.set_original_pos((card.x, card.y))

            #         card.current_state = 1

            #         energy -= 1

            #         # card.is_draggable = False
            #     else:
            #         card.return_to_original_position()
            # elif check_collision(card, drop_area2):
            #     if active_card2.value == None:
            #         active_card2.value = card

            #         card.x = drop_area2.x
            #         card.y = drop_area2.y

            #         card.set_original_pos((card.x, card.y))

            #         card.current_state = 1

            #         energy -= 1

            #         # card.is_draggable = False
            #     else:
            #         card.return_to_original_position()
            # elif check_collision(card, drop_area3):
            #     if active_card3.value == None:
            #         active_card3.value = card

            #         card.x = drop_area3.x
            #         card.y = drop_area3.y

            #         card.set_original_pos((card.x, card.y))

            #         card.current_state = 1

            #         energy -= 1

            #         # card.is_draggable = False
            #     else:
            #         card.return_to_original_position()
        case 1:

            collision_count = 0

            if card.range == attackable.enemy_cards.value or card.range == attackable.all_cards.value:
                for area in enemy_areas:
                    if check_collision(card, area):
                        collision_count = collision_count + 1

            if card.range == attackable.own_cards.value or card.range == attackable.all_cards.value:
                for area in areas:
                    if check_collision(card, area):
                        collision_count = collision_count + 1
                

            if collision_count <= 0 or collision_count > 1:
                card.return_to_original_position()
                return None

            if card.range == attackable.enemy_cards.value or card.range == attackable.all_cards.value:
                if check_collision(card, enemy_drop_area1):
                    if enemy_active_card1.value != None:
                        # enemy_active_card1.current_state = 0
                        # enemy_active_card1.return_to_original_position()

                        # enemy_active_card1 = None

                        if card.range == attackable.enemy_cards.value or card.range == attackable.all_cards.value:
                            enemy_active_card1.value.health -= card.damage
                            if card.effect != None:
                                card.effect(card, enemy_active_card1.value)
                            energy -= card.cost

                    card.return_to_original_position()
                elif check_collision(card, enemy_drop_area2):
                    if enemy_active_card2.value != None:
                        # enemy_active_card2.current_state = 0
                        # enemy_active_card2.return_to_original_position()

                        # enemy_active_card2 = None

                        if card.range == attackable.enemy_cards.value or card.range == attackable.all_cards.value:
                            enemy_active_card2.value.health -= card.damage
                            if card.effect != None:
                                card.effect(card, enemy_active_card2.value)
                            energy -= card.cost

                    card.return_to_original_position()
                elif check_collision(card, enemy_drop_area3):
                    if enemy_active_card3 != None:
                        # enemy_active_card3.current_state = 0
                        # enemy_active_card3.return_to_original_position()

                        # enemy_active_card3 = None
                        if card.range == attackable.enemy_cards.value or card.range == attackable.all_cards.value:
                            enemy_active_card3.value.health -= card.damage
                            if card.effect != None:
                                card.effect(card, enemy_active_card3.value)
                            energy -= card.cost

                    card.return_to_original_position()
                
                
            # checking own zones for blue cards
            if card.range == attackable.own_cards.value or card.range == attackable.all_cards.value:
                if check_collision(card, drop_area1):
                    if active_card1.value != None and active_card1.value != card:
                        if card.range == attackable.own_cards.value:
                            card.effect(card, active_card1.value)
                            energy -= card.cost
                    card.return_to_original_position()

                elif check_collision(card, drop_area2):
                    if active_card2.value != None and active_card2.value != card:
                        if card.range == attackable.own_cards.value:
                            card.effect(card, active_card2.value)
                            energy -= card.cost
                    card.return_to_original_position()

                elif check_collision(card, drop_area1):
                    if active_card3.value != None and active_card3.value != card:
                        if card.range == attackable.own_cards.value:
                            card.effect(card, active_card3.value)
                            energy -= card.cost
                    card.return_to_original_position()

                else:
                    card.return_to_original_position()