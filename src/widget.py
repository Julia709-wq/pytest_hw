def mask_account_card(data: str) -> str:
    """Функция, маскирующая номер карты или счёта"""
    if "Счет" in data:
        return "Счет " + "**" + str(data)[-4:]
    else:
        masked_card = []
        for i in data.split(" "):
            if i.isdigit():
                masked_num = i[:4] + " " + i[4:6] + "** **** " + i[-4:]
                masked_card.append(masked_num)

            else:
                masked_card.append(i)

    return " ".join(masked_card)


def get_data(date_input: str) -> str:
    """Преобразование строки в дату"""
    date_list = date_input.split("-")
    year = date_list[0]
    month = date_list[1]
    day = date_list[2][:2]
    return day + "." + month + "." + year

