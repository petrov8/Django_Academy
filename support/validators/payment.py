

def check_card_number(number):
    card_number = int(number)
    if card_number == int(number[0]):
        raise Exception("Card number is invalid")



