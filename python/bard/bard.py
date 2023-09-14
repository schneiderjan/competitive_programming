from sys import stdin, stdout


def has_bard(villagers):
    return "1" in villagers

def read_file():
    with open("python\\bard\\bard_input.txt", "r") as f:
        input_ = []
        for line in f:
            if not line.strip():
                continue
            input_.append(line.replace(" ", "").replace("\n", ""))
    return input_

# input_ = []
# [input_.append(line) for line in stdin]
input_ = read_file()

n_total_villagers = int(input_[0])
n_evenings = int(input_[1])
current_song = None
songs_known_by_villagers = {}
villager_knows_song = {}
current_song = 0

for idx in range(n_evenings):
    villagers = input_[idx + 2][1:]

    if has_bard(villagers):
        current_song += 1
        villagers = villagers.replace("1", "")

        known_by_villager = songs_known_by_villagers.get(current_song, None)
        songs_known_by_villagers[current_song] = set([v for v in villagers])
        for villager in villagers:
            # villager in map already
            if villager_knows_song.get(villager, None):
                villager_knows_song[villager].add(current_song)
            else:
                villager_knows_song[villager] = set([current_song])

    else:
        known_by_villager = songs_known_by_villagers.get(current_song, None)
        if not known_by_villager:
            continue

        for villager in villagers:
            songs_known_by_villagers[current_song].add(villager)

            if not villager_knows_song.get(villager, None):
                print
                # must check if villager has a set already if not we add one.
                # otherwise can add.

                # if villager_knows_song:
                # villager_knows_song = set([current_song])
            
                # add something to populate all songs for every villager.
                # villagers share all songs

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

