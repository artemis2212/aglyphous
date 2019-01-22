psittacosauridae = list(range(87, 101))  # list of porcupine-like dinos
pachycephalosauria = list(range(75, 84))  # list of headbutting dinos
megalosauridae = list(range(294, 309))  # list of dorsalfinned carnivorous dinos
compsognathidae = list(range(332, 340))  # list of tiny carnivorous dinos <=1ft is height
maniraptora = list(range(374, 387))  # list of dinos with big hands
dromaeosauridae = list(range(431, 456))  # list of raptors(like velocirptors)
x = 1  # sets up x for random number generator loop
potentials = psittacosauridae + pachycephalosauria + megalosauridae + compsognathidae + maniraptora + dromaeosauridae
from random import randint  # imports number generator

while x != 0:
    y = (randint(87, 457))  # selects random number, and ensures that its in a/
    if potentials.count(y) == 1:  # family I like
        print("Done", y)
        x = 0
    else:
        print("rerun", y)

