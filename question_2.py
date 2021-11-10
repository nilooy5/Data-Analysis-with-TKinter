import utility as util


def my_printing():
    while True:
        input_num = input("Enter a number: ")

        try:
            number = float(input_num)
        except ValueError:
            print("only numbers are accepted")
            continue

        end = util.round_to_closest_int(number)

        arr = list(range(1, end + 1))
        arr = arr[::-1]

        i = 0

        while i != len(arr):
            for j in range(i, len(arr)):
                if number < 0:
                    print(arr[j] * -1, end=" ")
                else:
                    print(arr[j], end=' ')
            print()
            i = i + 1


my_printing()

