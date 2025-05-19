#Import the Random Number Generator
import p1_random as p1
rng = p1.P1Random()

#Initialize variables
game_num = 0
player_win = 0
dealer_win = 0
game_ties = 0
in_progress = True


#Ensures that while the game is in progress the following code is executed
while in_progress:
    #New game loop
    print(f'START GAME #{game_num + 1}')
    #makes sure that a number between 1 and 13 is generated
    card = rng.next_int(13) + 1
    #Accounts for the fact that Jack, Queen, and King are 11,12, and 13 but hold a value of 10
    if card == 1:
        hand = 1
        print(f'Your card is a ACE!')
    elif 2 <= card <= 10:
        hand = card
        print(f'Your card is a {card}!')
    else:
        hand = 10
        if card == 11:
            print(f'Your card is a JACK!')
        if card == 12:
            print(f'Your card is a QUEEN!')
        if card == 13:
            print(f'Your card is a KING!')

    print(f'Your hand is: {hand}')
    while True:
        choice = int(input("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n\nChoose an option: "))
        #Adds the corresponding value to the player's hand
        if choice == 1:
            card = rng.next_int(13) + 1
            if card == 1:
                hand += 1
                print(f'Your card is a ACE!')
                print(f'Your hand is: {hand}')
            elif 2 <= card <= 10:
                hand += card
                print(f'Your card is a {card}!')
                print(f'Your hand is: {hand}')
            elif card == 11:
                hand += 10
                print(f'Your card is a JACK!')
                print(f'Your hand is: {hand}')
            elif card == 12:
                hand += 10
                print(f'Your card is a QUEEN!')
                print(f'Your hand is: {hand}')
            elif card == 13:
                hand += 10
                print(f'Your card is a KING!')
                print(f'Your hand is: {hand}')
            if hand == 21:
                player_win += 1
                print("BLACKJACK! You win!")
                break
            elif hand > 21:
                dealer_win += 1
                print("You exceeded 21! You lose.")
                break

        elif choice == 2:
            #Dealer's draw
            #Generates a random number between 16 and 26
            dealer_hand = rng.next_int(11) + 16
            print("Dealer's hand:", dealer_hand)
            print("Your hand is:", hand)
            if dealer_hand == 21:
                dealer_win += 1
                print("Dealer wins!")
                break
            elif dealer_hand > 21:
                player_win += 1
                print("You win!")
                break
            elif hand == dealer_hand:
                print("It's a tie! No one wins!")
                game_ties += 1
                break
            elif hand > dealer_hand:
                player_win += 1
                print("BLACKJACK! You win!")
                break
            elif dealer_hand > hand:
                dealer_win += 1
                print("Dealer wins!")
                break
        elif choice == 3:
            #Print stats
            average = (player_win/game_num) * 100
            print(f'Number of Player wins: {player_win}')
            print(f'Number of Dealer wins: {dealer_win}')
            print(f'Number of tie games: {game_ties}')
            print(f'Total # of games played is: {game_num}')
            print(f'Percentage of Player wins: {average:.1f}%')
        elif choice == 4:
            #Exit
            in_progress = False
            break
        else:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")
            continue
    game_num += 1







