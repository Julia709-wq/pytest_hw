def get_mask_card_number(card_number: int):
    if len(str(card_number)) != 16:
        return '*' * len(str(card_number))
    elif type(card_number) != int:
        return None
    else:
        return (str(card_number)[:4] + " " + str(card_number)[4:6] + "** **** "
                + str(card_number)[12:])


def get_mask_account(account_number: int):
    return "**" + str(account_number)[-4:]
