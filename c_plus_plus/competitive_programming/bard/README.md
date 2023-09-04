Every evening villagers in a small village gather around a big fire and sing songs.

A prominent member of the community is the bard. Every evening, if the bard is present, he sings a brand new song that no villager has heard before, and no other song is sung that night. In the event that the bard is not present, other villagers sing without him and exchange all songs that they know.

Given the list of villagers present for

consecutive evenings, output all villagers that know all songs sung during that period.
Input

The first line of input contains an integer
, , the number of villagers. The villagers are numbered to . Villager number

is the bard.

The second line contains an integer
,

, the number of evenings.

The next
lines contain the list of villagers present on each of the evenings. Each line begins with a positive integer , , the number of villagers present that evening, followed by

positive integers separated by spaces representing the villagers.

No villager will appear twice in one night and the bard will appear at least once across all nights.
Output

Output all villagers that know all songs, including the bard, one integer per line in ascending order.

https://open.kattis.com/problems/bard