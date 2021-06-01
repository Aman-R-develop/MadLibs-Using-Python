import random

ran = random.randint(1, 2)
points = 0

if ran == 1:
    story = '''
    Today I went to the zoo. I saw a/an)
    ___________(adjective)
    _____________(Noun) jumping up and down in its tree.
    He _____________(verb, past tense) __________(adverb)
    through the large tunnel that led to its _______(adjective)
    __________(noun). I got some peanuts and passed
    them through the cage to a gigantic gray _______(noun)
    towering above my head. Feeding that animal made
    me hungry. I went to get a __________(adjective) scoop
    of ice cream. It filled my stomach. Afterwards I had to
    __________(verb) __________ (adverb) to catch our bus.
    When I got home I __________(verb, past tense) my
    mom for a __________(adjective) day at the zoo. '''
    print(story)
    print("\n\033[1mStart guessing only after reading the story")

    a = input(
        "\nEnter your guesses:- Today I went to the zoo. I saw a/an ___________ (adjective): ").lower()
    b = input(
        "\nEnter your guesses:- _____________ (Noun) jumping up and down in its tree: ").lower()
    c = input(
        "\nEnter your guesses:- He _____________ (verb, past tense): ").lower()
    c1 = input(
        "\nEnter your guesses:-  __________ (adverb): ").lower()
    d = input(
        "\nEnter your guesses:- through the large tunnel that led to its _______ (adjective): ").lower()
    e = input(
        "\nEnter your guesses:- __________ (noun). I got some peanuts and passed: ").lower()
    f = input(
        "\nEnter your guesses:- them through the cage to a gigantic gray _______ (noun) me hungry: ").lower()
    g = input(
        "\nEnter your guesses:-  I went to get a __________ (adjective) scoop of ice cream: ").lower()
    h = input(
        "\nEnter your guesses:- It filled my stomach. Afterwards I had to __________ (verb): ").lower()
    h1 = input(
        "\nEnter your guesses:- __________ (adverb) to catch our bus: ").lower()
    i = input(
        "\nEnter your guesses:- When I got home I __________ (verb, past tense) my: ").lower()
    j = input(
        "\nEnter your guesses:- mom for a __________ (adjective) day at the zoo: \033[0m").lower()

    if a == "naughty":
        points = points + 1

    if b == "monkey":
        points = points + 1

    if c == "jumped":
        points = points + 1

    if c1 == "frequently":
        points = points + 1

    if d == "small":
        points = points + 1

    if e == "cage":
        points = points + 1

    if f == "monkey":
        points = points + 1

    if g == "creamy":
        points = points + 1

    if h == "run":
        points = points + 1

    if h1 == "quickly":
        points = points + 1

    if i == "thanked":
        points = points + 1

    if j == "remarkable":
        points = points + 1

    print(f"\nYou scored {points}/12")
    actualstory = '''
    Today I went to the zoo. I saw a naughty monkey jumping up and down in its tree. He jumped 
    frequently through large tunnel that led to it's small cage. I got some peanuts and passed 
    them through the cage to a gigantic gay monkey towering above my head. Feeding that animal
    made me hungry. I went to get a creamy scoop of ice cream. I filled my stomach. Afterwards 
    I had to run quickly to catch our bus. When I got home I thanked my mom for a remarkable day at the zoo.
    '''
    print(actualstory)

elif ran == 2:
    story = '''
    Last month, I went to Disney World with __________ (friend's name) . We
    traveled for __________ hours (number in text) by __________ (vehicle). Finally, we
    arrived and it was very __________ (adjective). There were
    __________ (adjective) people __________ (-ing verb) everywhere. There
    were also people dressed up in __________ (animal) costumes.
    I wish it had been more __________ (adjective), but we __________ (past
    tense verb) anyway. We also went on a/an __________ (adjective) ride
    called Magic. _____ (Friends name) nearly fell off a ride and had to be
    __________ (past tense verb). Later, we went to the hotel and
    __________ (past tense verb). Next year, I want to go to __________(place),
    where we can ________ (verb).'''

    print(story)
    print("\n\033[1mStart guessing only after reading the story")

    a = input(
        "\nEnter your guesses:- Last month, I went to Disney World with __________ (friend's name): ").lower()
    b = input(
        "\nEnter your guesses:- We traveled for __________ hours (number in text): ").lower()
    c = input(
        "\nEnter your guesses:- by __________ (vehicle): ").lower()
    d = input(
        "\nEnter your guesses:- Finally, we arrived and it was very __________ (adjective):").lower()
    e = input(
        "\nEnter your guesses:- There were __________ (adjective): ").lower()
    f = input(
        "\nEnter your guesses:- people __________(-ing verb) everywhere: ").lower()
    g = input(
        "\nEnter your guesses:- There were also people dressed up in __________(animal) costumes: ").lower()
    h = input(
        "\nEnter your guesses:- I wish it had been more __________ (adjective): ").lower()
    i = input(
        "\nEnter your guesses:- but we __________ (past tense verb) anyway: ").lower()
    j = input(
        "\nEnter your guesses:- We also went on a/an __________ (adjective) ride called Magic: ").lower()
    k = input(
        "\nEnter your guesses:- _____ (Friends name) nearly fell off a ride and: ").lower()
    l = input(
        "\nEnter your guesses:- had to be __________ (past tense verb): ").lower()
    m = input(
        "\nEnter your guesses:- Later, we went to the hotel and __________ (past tense verb): ").lower()
    n = input(
        "\nEnter your guesses:- Next year, I want to go to __________(place): ").lower()
    o = input(
        "\nEnter your guesses:- where we can ________ (verb): \033[0m").lower()

    if a == "ethan":
        points = points + 1

    if b == "six":
        points = points + 1

    if c == "bus":
        points = points + 1

    if d == "exicting":
        points = points + 1

    if e == "a lot of":
        points = points + 1

    if f == "roaming":
        points = points + 1

    if g == "girrafe":
        points = points + 1

    if h == "dangerous":
        points = points + 1

    if i == "managed":
        points = points + 1

    if j == "amazing":
        points = points + 1

    if k == "ethan":
        points = points + 1

    if l == "bandaged":
        points = points + 1

    if m == "slept":
        points = points + 1

    if n == "tokyo":
        points = points + 1

    if o == "enjoy":
        points = points + 1

    print(f"\nYou scored {points}/14")
    actualstory = '''
    Last month, I went to Disney World with Ethan. We
    traveled for six hours by bus . Finally, we arrived and it was very exiting. 
    There were a lot of people roaming everywhere. 
    There were also people dressed up in girrafe costumes.
    I wish it had been more dangerous, but we managed anyway. We also went on a/an amazing ride
    called Magic. Ethan nearly fell off a ride and had to be bandaged. 
    Later, we went to the hotel and slept. 
    Next year, I want to go to Tokyo,
    where we can enjoy.
    '''
    print(actualstory)
