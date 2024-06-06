print("Welcome to Are You Smarter than a Middle Schooler?")

playing = input("Do you want to play? ")
points = 0

if(playing.lower() != "yes"):
    quit

answer = input("Is apple a fruit or color?... ")
if(answer.lower() == "fruit"):
    print('Correct\n')
    points = points +1
else:
    print('Wrong :C\n')

answer = input("What is 12 x12?... ")
if(answer.lower() == "144"):
    print('Correct\n')
    points = points +1
else:
    print('Wrong :C\n')

answer = input("Are insects invertebrae?... ")
if(answer.lower() == "yes" or answer.lower() == "true"):
    print('Correct\n')
    points = points +1
else:
    print('Wrong :C\n')

answer = input("The number of degrees in a triangle adds up to?... ")
if(answer.lower() == "180"):
    print('Correct\n')
    points = points +1
else:
    print('Wrong :C\n')

answer = input("Glaciers are mainly made of which frozen form of liquid?... ")
if(answer.lower() == "fruit"):
    print('Correct\n')
    points = points +1
else:
    print('Wrong :C\n')

answer = input("Who wrote the play Romeo and Juliet?... ")
if(answer.lower() == "william shakespeare" or answer.lower() == "shakespeare"):
    print('Correct\n')
    points = points +1
else:
    print('Wrong :C\n')

answer = input("What is the largest planet in the solar system?... ")
if(answer.lower() == "jupiter"):
    print('Correct\n')
    points = points +1
else:
    print('Wrong :C\n')

answer = input("What metal is best conductor of electricity?... ")
if(answer.lower() == "silver"):
    print('Correct\n')
    points = points +1
else:
    print('Wrong :C\n')

print('Thank you for playing! You have earned', points, ' out of 8 avaliable points.')