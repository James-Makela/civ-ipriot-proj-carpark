from string import ascii_letters
import random

letters = []
for letter in ascii_letters:
    letters.append(letter)


def create_plate():
    rnd = random.Random()
    plate_number = '1'
    plate_number += letters[rnd.randint(0, 7)].upper()
    for _ in range(2):
        plate_number += letters[rnd.randint(0, len(letters) - 1)].upper()
    for _ in range(3):
        plate_number += str(rnd.randint(0, 9))

    return plate_number


def main():
    plates = []
    for i in range(100):
        plate = create_plate()
        if plate not in plates:
            plates.append(plate)
        else:
            i -= 1

    print(len(plates))
    for plate in plates:
        print(plate)


if __name__ == "__main__":
    main()


