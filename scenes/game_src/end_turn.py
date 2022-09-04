


def end_turn():
    global is_own_turn, energy
    
    # for card in cards, enemy_cards:
    #     if card.re_event != None:
    #         card.re_event()

    def set_hand_pos(obj, pos):
        obj.set_hand_pos(pos)
        obj.set_original_pos(pos)

    def add_card_to_hand(card_count):

        global hand_cards

        rand_card = deck_cards[random.randint(0, len(deck_cards) - 1)]
        
        rand_card.set_pos((deck_image.x, deck_image.y,))

        temp_card_list = []
        for i in range(len(hand_cards) + 1):
            temp_card_list.append(Square(0, 0, card_width, card_height, COL.black.value))

        

        hand_cards.append(rand_card)
        deck_cards.remove(rand_card)

        hand_cards = align_x(card_combined_width, hand_cards)
        hand_cards = align_center_x(WIN.width, hand_cards)
        hand_cards = move_bottom(WIN.height, hand_cards)

        # positions = get_x_centered_positions(WIN.width, get_x_aligned_positions(card_combined_width, temp_card_list))
        # positions = positions[len(positions) - 1]

        # target_pos = (positions.x, WIN.height - positions.height)
        target_pos = (rand_card.x, rand_card.y)
        rand_card.attach_animation(Animation(rand_card, (deck_image.x, deck_image.y), target_pos, Animation_Type.ease__in__out.value, 0.75, set_hand_pos, [rand_card, target_pos]))
        
        # rand_card.place_bot(WIN)

    #! checks if own turn 

    if is_own_turn:
        is_own_turn = False

        energy = 3

        if len(hand_cards) < 3:
            add_card_to_hand(3 - len(hand_cards))
                

        def get_random_card():
            match random.randint(0, 2):
                case 0:
                    return enemy_card1
                case 1:
                    return enemy_card2
                case 2:
                    return enemy_card3
        
        def use_random_card():

            global enemy_attacking, is_own_turn

            temp_card = get_random_card()

            if active_card1.value == None and active_card2.value == None and active_card3.value == None:
                is_own_turn = True
                return None

            match random.randint(0, 2):
                case 0:
                    if active_card1.value != None and temp_card.current_state == 1:
                        enemy_attacking = True
                        attack(active_card1.value, temp_card)
                        
                    else: use_random_card()
                case 1:
                    if active_card2.value != None and temp_card.current_state == 1:
                        enemy_attacking = True
                        attack(active_card2.value, temp_card)

                    else: use_random_card()
                case 2:
                    if active_card3.value != None and temp_card.current_state == 1:
                        enemy_attacking = True
                        attack(active_card3.value, temp_card)
                        
                    else: use_random_card()
                        
                        

        def put_random_card():

            global enemy_active_card1, enemy_active_card2, enemy_active_card3, is_own_turn

            temp_card = get_random_card()

            match random.randint(0, 2):

                case 0:

                    if enemy_active_card1.value == None and temp_card.current_state == 0:
                        # temp_card.x = enemy_drop_area1.x
                        # temp_card.y = enemy_drop_area1.y

                        place(enemy_drop_area1, temp_card)

                        # temp_card.current_state = 1

                        enemy_active_card1.value = temp_card

                        # temp_card.set_original_pos((temp_card.x, temp_card.y))

                        # is_own_turn = True
                        
                        return True
                    else:
                        put_random_card()
                case 1:
                    
                    if enemy_active_card2.value == None and temp_card.current_state == 0:
                        # temp_card.x = enemy_drop_area2.x
                        # temp_card.y = enemy_drop_area2.y

                        place(enemy_drop_area2, temp_card)
                        enemy_active_card2.value = temp_card

                        # temp_card.current_state = 1

                        # temp_card.set_original_pos((temp_card.x, temp_card.y))

                        # is_own_turn = True
                        

                        return True
                    else:
                        put_random_card()
                case 2:
                    if enemy_active_card3.value == None and temp_card.current_state == 0:
                        # temp_card.x = enemy_drop_area3.x
                        # temp_card.y = enemy_drop_area3.y

                        place(enemy_drop_area3, temp_card)
                        enemy_active_card3.value = temp_card

                        # temp_card.current_state = 1

                        # temp_card.set_original_pos((temp_card.x, temp_card.y))

                        # is_own_turn = True
                        
                        return True
                    else:
                        put_random_card()

        def set_own_turn():
            global is_own_turn, enemy_attacking, enemy_energy
            is_own_turn = True
            enemy_attacking = False
            enemy_energy = 3
            

        def check_attack():
            if not enemy_energy <= 0:
                active_count = 0
                for card in enemy_cards:
                    if card.current_state == 1:
                        active_count += 1

                if active_count == len(enemy_cards):
                    use_random_card()
                elif active_count == 0:
                    put_random_card()
                else:
                    match random.randint(0, 1):
                        case 0:
                            use_random_card()
                        case 1:
                            put_random_card()
            else:
                set_own_turn()
                current_round.add_number(1)

        def attack_finished(attacker, victim):
            global enemy_energy
            victim.health -= attacker.damage
            enemy_energy -= attacker.cost
            attacker.attach_animation(Animation(attacker, (attacker.x, attacker.y), (attacker.get_original_pos()[0], attacker.get_original_pos()[1]), 4, 1, None))

            wait_and_call(1.5, check_attack)

        def set_op(card):
            print("NOGGER BLACK")
            card.set_original_pos((card.x, card.y))

        def place(area, card):
            card.current_state = 1
            card.attach_animation(Animation(card, (card.x, card.y), (area.x, area.y), Animation_Type.ease__in__out.value, 0.5, set_op, [card]))
            wait_and_call(2, check_attack)

        def attack(victim_card, attacker_card):
            attacker_card.attach_animation(Animation(attacker_card, (attacker_card.x, attacker_card.y), (victim_card.x, victim_card.y), 2, 0.5, attack_finished, (attacker_card, victim_card)))

        if not enemy_energy <= 0:
            active_count = 0
            for card in enemy_cards:
                if card.current_state == 1:
                    active_count += 1

            if active_count == len(enemy_cards):
                use_random_card()
            elif active_count == 0:
                put_random_card()
            else:
                match random.randint(0, 1):
                    case 0:
                        use_random_card()
                    case 1:
                        put_random_card()


                # use_random_card()