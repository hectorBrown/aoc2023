PATH = "data.txt"

translation = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

input = [line[:-1] for line in open(PATH).readlines()]
for translation_row in translation:
    input = [
        line.replace(
            translation_row,
            translation_row + translation[translation_row] + translation_row,
        )
        for line in input
    ]

print(
    sum(
        [
            int(line[0] + line[-1])
            for line in [
                [x for x in line if x in [str(y) for y in range(10)]] for line in input
            ]
        ]
    )
)
