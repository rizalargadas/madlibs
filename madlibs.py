import stories
import random

adj_1 = input("Adjective: ")
adj_2 = input("Adjective: ")
verb_1 = input("Verb: ")
verb_2 = input("Verb: ")
verb_3 = input("Verb: ")
person = input("Famous Person: ")

randomizer = random.randint(1, 10)

if randomizer == 1:
    print(stories.madlibs1.format(adj_1=adj_1, adj_2=adj_2, verb_1=verb_1,
                                  verb_2=verb_2, verb_3=verb_3, person=person))

elif randomizer == 2:
    print(stories.madlibs2.format(adj_1=adj_1, adj_2=adj_2, verb_1=verb_1,
                                  verb_2=verb_2, verb_3=verb_3, person=person))

elif randomizer == 3:
    print(stories.madlibs3.format(adj_1=adj_1, adj_2=adj_2, verb_1=verb_1,
                                  verb_2=verb_2, verb_3=verb_3, person=person))

elif randomizer == 4:
    print(stories.madlibs4.format(adj_1=adj_1, adj_2=adj_2, verb_1=verb_1,
                                  verb_2=verb_2, verb_3=verb_3, person=person))

elif randomizer == 5:
    print(stories.madlibs5.format(adj_1=adj_1, adj_2=adj_2, verb_1=verb_1,
                                  verb_2=verb_2, verb_3=verb_3, person=person))

elif randomizer == 6:
    print(stories.madlibs6.format(adj_1=adj_1, adj_2=adj_2, verb_1=verb_1,
                                  verb_2=verb_2, verb_3=verb_3, person=person))

elif randomizer == 7:
    print(stories.madlibs7.format(adj_1=adj_1, adj_2=adj_2, verb_1=verb_1,
                                  verb_2=verb_2, verb_3=verb_3, person=person))

elif randomizer == 8:
    print(stories.madlibs8.format(adj_1=adj_1, adj_2=adj_2, verb_1=verb_1,
                                  verb_2=verb_2, verb_3=verb_3, person=person))

elif randomizer == 9:
    print(stories.madlibs9.format(adj_1=adj_1, adj_2=adj_2, verb_1=verb_1,
                                  verb_2=verb_2, verb_3=verb_3, person=person))

else:
    print(stories.madlibs10.format(adj_1=adj_1, adj_2=adj_2, verb_1=verb_1,
                                   verb_2=verb_2, verb_3=verb_3, person=person))
