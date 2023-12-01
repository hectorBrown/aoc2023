PATH = "data.txt"

print(
    sum(
        [
            int(line[0] + line[-1])
            for line in [
                [x for x in line[:-1] if x in [str(y) for y in range(10)]]
                for line in open(PATH).readlines()
            ]
        ]
    )
)
