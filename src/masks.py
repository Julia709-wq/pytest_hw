def get_mask_card_number(card_number: int):
    return (str(card_number)[:4] + " " + str(card_number)[4:6] + "** **** "
            + str(card_number)[12:])


def get_mask_account(account_number: int):
    return "**" + str(account_number)[-4:]
