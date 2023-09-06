def has_bard(villagers) -> bool:
    return "1" in villagers


def read_file():
    with open("python\\bard\\bard_input.txt", "r") as f:
        input_ = []
        for line in f:
            if not line.strip():
                continue
            input_.append(line.replace(" ", "").replace("\n", ""))
    return input_


if __name__ == "__main__":
    input_ = read_file()

    n_total_villagers = int(input_[0])
    n_evenings = int(input_[1])
    current_song = None
    songs_known_by_villagers = {}
    current_song = 0

    for idx in range(n_evenings):
        villagers = input_[idx + 2][1:]

        if has_bard(villagers):
            current_song += 1
            villagers = villagers.replace("1", "")

            known_by_villager = songs_known_by_villagers.get(current_song, None)
            if known_by_villager:
                for villager in villagers:
                    songs_known_by_villagers[current_song].add(villager)
            else:
                songs_known_by_villagers[current_song] = set([v for v in villagers])
        else:
            if current_song == 0:
                continue
            else:
                known_by_villager = songs_known_by_villagers.get(current_song, None)
                if not known_by_villager:
                    continue
                
                for villager in villagers:
                    songs_known_by_villagers[current_song].add(villager)

    songs_and_villagers = []
    for key, val in songs_known_by_villagers.items():
        songs_and_villagers.append(val)
    output = set.intersection(*songs_and_villagers)

    if output:
        output = sorted(output)
        print("1")
        print(*output, sep="\n")
    else:
        print(1)
