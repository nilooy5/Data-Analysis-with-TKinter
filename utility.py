def round_to_closest_int(number):
    if number < 0:
        number = -number

    rounded_dec_2 = round(number, 2)
    decimals = (rounded_dec_2 * 100) % 100

    if decimals <= 50:
        if rounded_dec_2 < 0:
            return int(rounded_dec_2) - 1
        else:
            return int(rounded_dec_2)

    else:
        if rounded_dec_2 < 0:
            return int(rounded_dec_2) - 1
        else:
            return int(rounded_dec_2) + 1

