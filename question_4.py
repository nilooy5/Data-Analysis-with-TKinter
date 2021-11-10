import math


def my_formula(rate, depth):
    return 4 * (rate / (math.pi * (depth ** 2)))


def meter_to_feet(meter):
    return meter * 3.28084


def meterCube_to_feetCube(meterCube):
    return meterCube * 35.3147


while True:
    Vt = float(input("Enter the rate of water (in cubic meters/minutes):"))
    d = float(input("Enter the specific depth (in meters):"))
    # Vt = 0.25
    # d = 1.8
    is_SI = input("Do you wish the results using the International System of Units?:")

    if is_SI == "Yes" or is_SI == "yes":
        try:
            result = my_formula(Vt, d)
        except ZeroDivisionError:
            print("Error: Zero Division Error")
            continue
        result = round(result, 3)
        result = str(result) + " m/min"
    else:
        Vt = meterCube_to_feetCube(Vt)
        d = meter_to_feet(d)
        try:
            result = my_formula(Vt, d)
        except ZeroDivisionError:
            print("Error: Zero Division Error")
            continue
        result = round(result, 3)
        result = str(result) + " feet/min"

    print(result)

    # 35.3147
    # 3.28084
