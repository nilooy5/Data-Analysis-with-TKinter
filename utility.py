def round_to_closest_int(number):
    rounded_dec_2 = round(number, 2)
    print(rounded_dec_2)
    decimals = (rounded_dec_2 * 100) % 100

    if decimals <= 50:
        return int(rounded_dec_2)
    else:
        return int(rounded_dec_2) + 1

