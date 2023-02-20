from tkinter import *
from PIL import Image , ImageTk
import random
from BlackJack_Simple import card
from BlackJack_Simple import hand
from Music import MP
welcom_screen=Tk()
welcom_screen.iconbitmap('C:\\Users\\HTH\\PycharmProjects\\pythonProject\\'
                            'venv\\Lib\\site-packages\\pygame\\docs\\generated\\_static\\pygame.ico')
welcom_screen.geometry("1000x900")
welcom_screen.config(background='green')
welcom_screen.title('BlackJack_Demo')
temp_image_1=Image.open('C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\intro.jpg')
temp_image_2=temp_image_1.resize((610,610))
global welcom_screen_image
welcom_screen_image=ImageTk.PhotoImage(temp_image_2)
def start_game():
    welcom_screen.destroy()
    welcom_screen.after(700,main_game())
#create welcom screen image
welcom_screen_label=Label(welcom_screen,image=welcom_screen_image,bd=0)
welcom_screen_label.pack(padx=10,pady=10)
#create start game button
start_game_button=Button(welcom_screen,text='Start',command=start_game,font=('Consolas',16))
start_game_button.pack(ipadx=10,ipady=10)
def main_game():
    global root
    root = Tk()
    root.configure(background='green')
    root.title("Balck Jack_Demo")
    root.geometry("1000x900")
    root.iconbitmap('C:\\Users\\HTH\\PycharmProjects\\pythonProject\\'
                    'venv\\Lib\\site-packages\\pygame\\docs\\generated\\_static\\pygame.ico')
    # create global frame
    global my_frame
    my_frame = Frame(root, bg="green")
    my_frame.pack(pady=20)

    # create player and dealer frame
    global dealer_frame,player_frame
    dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0, background="green")
    dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

    player_frame = LabelFrame(my_frame, text="Player", bd=0, background="green")
    player_frame.grid(row=1, column=0, ipadx=20)

    # create button frame
    global button_frame
    button_frame = LabelFrame(my_frame, text='', font=("Consolas", 14), background="green", bd=0)
    button_frame.grid(row=5, column=0, ipadx=20)

    # create result box frame
    global result_frame
    result_frame = LabelFrame(my_frame, text='Annoucement :', font=("Consolas", 14), background="green", bd=0)
    result_frame.grid(row=4, column=0, ipady=1, ipadx=1)

    # create notice box frame
    global notice_frame
    notice_frame = LabelFrame(my_frame, text='Notice :', font=("Consolas", 14), background="green", bd=1)
    notice_frame.grid(row=6, column=0, ipadx=10)

    # create shuffle button
    global shuffle_button
    shuffle_button = Button(button_frame, text="Shuffle", font=("Consolas", 14), command=shuffle)
    shuffle_button.grid(ipadx=5, row=0, column=0)

    # create hit button
    global card_button
    card_button = Button(button_frame, text="Hit", font=("Consolas", 14), command=player_hit)
    card_button.grid(ipadx=5, row=0, column=1)

    # crate stand button
    global stand_button
    stand_button = Button(button_frame, text="Stand", font=("Consolas", 14), command=autoplay_dealer)
    stand_button.grid(ipadx=5, row=0, column=2)

    # create music button
    global music_button
    music_button = Button(button_frame, text="Set Music ", font=("Consolas", 14), command=open_music)
    music_button.grid(ipadx=5, row=0, column=3)

    # create rule button
    global rule_button
    rule_button = Button(button_frame, text="Rule ", font=("Consolas", 14), command=open_rule)
    rule_button.grid(ipadx=5, row=0, column=4)

    # put  cards in card dealer frame and player frame
    global dealer_label_1,dealer_label_2,dealer_label_3,dealer_label_4,dealer_label_5
    global player_label_1,player_label_2,player_label_3,player_label_4,player_label_5
    dealer_label_1 = Label(dealer_frame, text='', background='green')
    dealer_label_1.grid(pady=15, row=0, column=0)

    dealer_label_2 = Label(dealer_frame, text='', background='green')
    dealer_label_2.grid(pady=15, row=0, column=1)

    dealer_label_3 = Label(dealer_frame, text='', background='green')
    dealer_label_3.grid(pady=15, row=0, column=2)

    dealer_label_4 = Label(dealer_frame, text='', background='green')
    dealer_label_4.grid(pady=15, row=0, column=3)

    dealer_label_5 = Label(dealer_frame, text='', background='green')
    dealer_label_5.grid(pady=15, row=0, column=4)

    player_label_1 = Label(player_frame, text='', background='green')
    player_label_1.grid(pady=15, row=1, column=0)

    player_label_2 = Label(player_frame, text='', background='green')
    player_label_2.grid(pady=15, row=1, column=1)

    player_label_3 = Label(player_frame, text='', background='green')
    player_label_3.grid(pady=15, row=1, column=2)

    player_label_4 = Label(player_frame, text='', background='green')
    player_label_4.grid(pady=15, row=1, column=3)

    player_label_5 = Label(player_frame, text='', background='green')
    player_label_5.grid(pady=15, row=1, column=4)

    # create result box label (put in result box frame)
    global result_label
    result_label = Label(result_frame, text="Result : ? ", font=("Consolas", 16), width=60, background='green')
    result_label.pack(padx=20, pady=20)
    # create notice box label (put in notice frame)
    global notice_label
    notice_label = Label(notice_frame, text="", font=("Consolas", 14), width=60, background='green')
    notice_label.pack(padx=20, pady=20)
    notice_label.config(text='  1.Shuffle the deck before playing(very important)\n2.Each side has maximum 5 cards'
                             '\n3.When result is revealed, click shuffle to start again\n4.When you or dealer got blackjack, show all cards both side',
                        anchor='w')
    # root.mainloop()
def open_music():
    player_music=Toplevel()
    player_music.title('Music Settings')
    player_music.iconbitmap('C:\\Users\\HTH\\PycharmProjects\\pythonProject\\'
                    'venv\\Lib\\site-packages\\pygame\\docs\\generated\\_static\\pygame.ico')
    MP(player_music)
    player_music.mainloop()
def open_rule():
    rule=Toplevel()
    rule.title('Rule')
    rule.iconbitmap('C:\\Users\\HTH\\PycharmProjects\\pythonProject\\'
                            'venv\\Lib\\site-packages\\pygame\\docs\\generated\\_static\\pygame.ico')
    rule.geometry('1000x1000')
    rule.config(background='white')
    global rule_image_1,rule_image_2
    temp_image_1=Image.open('C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\bodoi.jpg')
    temp_image_2= temp_image_1.resize((400,300))
    rule_image_1=ImageTk.PhotoImage(temp_image_2)
    rule_image_2=ImageTk.PhotoImage(Image.open('C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\rule.jpg'))
    rule_image_label_1=Label(rule,image=rule_image_1)
    rule_image_label_1.pack(padx=10, pady=10)
    rule_image_label_2 = Label(rule, image=rule_image_2)
    rule_image_label_2.pack(padx=10, pady=10)
def shuffle():
    card_button.config(state="normal")
    stand_button.config(state="normal")
    result_label.config(text='Result : ? ')
    dealer_label_1.config(image='')
    dealer_label_2.config(image='')
    dealer_label_3.config(image='')
    dealer_label_4.config(image='')
    dealer_label_5.config(image='')
    player_label_1.config(image='')
    player_label_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')
    global deck,dealer,player
    deck=[]
    suits = ['Spades', 'Club', 'Diamond', 'Hearts']
    ranks = [
        {"rank": "A", "value": 11},
        {"rank": "2", "value": 2},
        {"rank": "3", "value": 3},
        {"rank": "4", "value": 4},
        {"rank": "5", "value": 5},
        {"rank": "6", "value": 6},
        {"rank": "7", "value": 7},
        {"rank": "8", "value": 8},
        {"rank": "9", "value": 9},
        {"rank": "10", "value": 10},
        {"rank": "J", "value": 10},
        {"rank": "Q", "value": 10},
        {"rank": "K", "value": 10}
    ]
    for suit in suits:
        for rank in ranks:
            deck.append(card(suit, rank))
    player=hand()
    dealer=hand(dealer=True)
    dealer_hit()
    dealer_hit()
    player_hit()
    player_hit()
    check_if_blackJack("player")
    check_if_blackJack("dealer")
def resize_card(card):
    card_img = Image.open(card)
    card_resize_image = card_img.resize((160,190))
    global card_image
    card_image = ImageTk.PhotoImage(card_resize_image)
    return card_image
def dealer_hit():
    if len(dealer.cards)<=5:
        try:
            card=random.choice(deck)
            deck.remove(card)
            dealer.cards.append(card)
            global dealer_image_1, dealer_image_3, dealer_image_4, dealer_image_5
            if  len(dealer.cards)==1:
                dealer_image_1=resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
                dealer_label_1.config(image=dealer_image_1)
            elif len(dealer.cards)==2:
                global replace_image_2,temp_image_2
                replace_image_2=resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
                temp_image_2=resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\back.jpg')
                dealer_label_2.config(image=temp_image_2)
            elif len(dealer.cards) == 3:
                dealer_image_3 = resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
                dealer_label_3.config(image=dealer_image_3)
            elif len(dealer.cards) == 4:
                dealer_image_4 = resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
                dealer_label_4.config(image=dealer_image_4)
            elif len(dealer.cards) == 5:
                dealer_image_5 = resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
                dealer_label_5.config(image=dealer_image_5)
                del dealer_image_1,dealer_image_3, dealer_image_4
                play_game(player,dealer,game_over=True)
            if dealer.get_value()>21:
                print("\tDealer lost, you win :) ")
                result_label.config(text='Dealer lost, you win :)')
                card_button.config(state="disabled")
                stand_button.config(state="disabled")
            root.title(f"Balck Jack_Demo /{len(deck)} cards remaining")
        except:
            root.title(f"Balck Jack_Demo /No more cards remaining")
            root.quit()
            print("Out of cards , quit game ")
    #check_if_blackJack("dealer")
    #play_game(player,dealer,game_over=True)
def player_hit():
    if len(player.cards)<=5:
        try :
            card = random.choice(deck)
            deck.remove(card)
            player.cards.append(card)
            global player_image_1, player_image_2, player_image_3, player_image_4, player_image_5
            if len(player.cards)==1:
                player_image_1 = resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
                player_label_1.config(image=player_image_1)
            elif len(player.cards)==2:
                player_image_2 = resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
                player_label_2.config(image=player_image_2)
            elif len(player.cards) == 3:
                player_image_3 = resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
                player_label_3.config(image=player_image_3)
            elif len(player.cards) == 4:
                player_image_4 = resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
                player_label_4.config(image=player_image_4)
            elif len(player.cards) == 5:
                player_image_5 = resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
                player_label_5.config(image=player_image_5)
                card_button.config(state="disabled")
            if player.get_value()>21:
                result_label.config(text='You lost, dealer wins :(')
                print('\tYou lost, dealer wins :(')
                dealer_label_2.config(image=replace_image_2)
                card_button.config(state="disabled")
                stand_button.config(state="disabled")
            root.title(f"Balck Jack_Demo /{len(deck)} cards remaining")
        except:
            root.title(f"Balck Jack_Demo /No more cards remaining")
            root.quit()
            print("Out of cards , quit game ")
    check_if_blackJack("player")
def check_if_blackJack(hand):
    '''check_if_blackJack function can be cleaned by erasing comemnt sections ? '''
    if hand=="player":
        if (player.is_blackjack() and not dealer.is_blackjack()):
            print('\tYou got blackjack, you win, dealer lost :)')
            result_label.config(text='You got blackjack, you win, dealer lost :)')
            dealer_label_2.config(image=replace_image_2)
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            return True
        # elif (not player.is_blackjack() and dealer.is_blackjack()):
        #     print('\tDealer got blackjack, dealer wins, you lost :(')
        #     result_label.config(text='Dealer got blackjack, dealer wins, you lost :(')
        #     dealer_label_2.config(image=replace_image_2)
        #     card_button.config(state="disabled")
        #     stand_button.config(state="disabled")
        #     return True
        elif (dealer.is_blackjack() and player.is_blackjack()):
            print("\tBoth sides got blackjack, tie ! ")
            result_label.config(text='Both sides got blackjack, tie !')
            dealer_label_2.config(image=replace_image_2)
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            return True
    elif hand=="dealer":
        if (dealer.is_blackjack() and not player.is_blackjack()):
            print('\tDealer got blackjack, dealer wins, you lost :( ')
            result_label.config(text='Dealer got blackjack, dealer wins, you lost :(')
            dealer_label_2.config(image=replace_image_2)
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            return True
        # elif (not dealer.is_blackjack() and player.is_blackjack()):
        #     print('\tYou got blackjack, you win, dealer lost :)')
        #     result_label.config(text='You got blackjack, you win, dealer lost :)')
        #     dealer_label_2.config(image=replace_image_2)
        #     card_button.config(state="disabled")
        #     stand_button.config(state="disabled")
        #     return True
        elif (dealer.is_blackjack() and player.is_blackjack()):
            print("\tBoth sides got blackjack, tie ! ")
            result_label.config(text='Both sides got blackjack, tie !')
            dealer_label_2.config(image=replace_image_2)
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            return True
    return False
# play_game function can be optimized by erasing section if statement when game_over variable is False ?
def play_game(player,dealer,game_over=False):
    '''play_game function can be optimized by erasing section if statement when game_over variable is False ?'''
    if (not game_over):
        if (player.get_value() > 21):
            print("\tYou lost, dealer wins :( ")
            result_label.config(text='You lost, dealer wins :(')
            dealer_label_2.config(image=replace_image_2)
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            return True
        elif (dealer.get_value() > 21):
            print("\tDealer lost, you win :) ")
            result_label.config(text='Dealer lost, you win :)')
            dealer_label_2.config(image=replace_image_2)
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            return True
        elif (dealer.is_blackjack() and player.is_blackjack()):
            print("\tBoth player got blackjack, tie ! ")
            result_label.config(text='Both player got blackjack, tie ! ')
            dealer_label_2.config(image=replace_image_2)
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            return True
        elif (player.is_blackjack()):
            print('\tYou got blackjack, you win, dealer lost :) ')
            result_label.config(text='You got blackjack, you win, dealer lost :)')
            dealer_label_2.config(image=replace_image_2)
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            return True
        elif (dealer.is_blackjack()):
            print('\tDealer got blackjack, dealer wins, you lost :( ')
            result_label.config(text='Dealer got blackjack, dealer wins, you lost :(')
            dealer_label_2.config(image=replace_image_2)
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            return True
    else:
        if (player.get_value() > dealer.get_value()):
            print('\tYou win, dealer lost :) ')
            result_label.config(text='You win, dealer lost :)')
            dealer_label_2.config(image=replace_image_2)
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
        elif (player.get_value() < dealer.get_value()):
            print('\tDealer wins, you lost :( ')
            result_label.config(text='Dealer wins, you lost :(')
            dealer_label_2.config(image=replace_image_2)
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
        elif (player.get_value() == dealer.get_value()):
            result_label.config(text='Tie !')
            dealer_label_2.config(image=replace_image_2)
            print('\tTie ! ')
        return True
    return False
def autoplay_dealer():
    while len(dealer.cards)<=5 and dealer.get_value()<17:
        card=random.choice(deck)
        deck.remove(card)
        dealer.cards.append(card)
        global dealer_img_1, dealer_img_2, dealer_img_3, dealer_img_4, dealer_img_5
        if  len(dealer.cards)==1:
            dealer_img_1=resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
            dealer_label_1.config(image=dealer_img_1)
        elif len(dealer.cards)==2:
            dealer_img_2 = resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
            dealer_label_2.config(image=dealer_img_2)
        elif len(dealer.cards) == 3:
            dealer_img_3 = resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
            dealer_label_3.config(image=dealer_img_3)
        elif len(dealer.cards) == 4:
            dealer_img_4 = resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
            dealer_label_4.config(image=dealer_img_4)
        elif len(dealer.cards) == 5:
            dealer_img_5 = resize_card(f'C:\\Users\\HTH\\PycharmProjects\\pythonProject\\Game\\52_poker_Cards\\{card}.jpg')
            dealer_label_5.config(image=dealer_img_5)
            check_if_blackJack("dealer")
            play_game(player,dealer,game_over=True)
        if dealer.get_value()>21:
            print("\tDealer lost, you win :) ")
            result_label.config(text='Dealer lost, you win :)')
            dealer_label_2.config(image=replace_image_2)
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            return
        if check_if_blackJack("dealer")==True :
            return
        root.title(f"Balck Jack_Demo /{len(deck)} card remaining")
    play_game(player,dealer,game_over=True)
    dealer_label_2.config(image=replace_image_2)
    card_button.config(state="disabled")
    stand_button.config(state="disabled")
mainloop()