def guess_a_number():
    name = raw_input("Greetings, earthling, what are you called? ")
    print name + ", we aliens can read minds, can you?"
    replay = "yes"
    while replay == "yes":  
        import random
        x = random.randint(1, 101)
        answer = raw_input("I'm thinking of a number between 1 and 100.  Try to read my mind. ")
        print type(answer)
        if x == answer:
            print "WOW, humans CAN read minds!"
        else:
            while x != answer:
                if x < answer:
                    answer = int(raw_input("That number is astronomical, try again. Earthlings are not very impressive so far. "))
                elif x > answer:
                    answer = int(raw_input("That number is miniscule like the size of your brain.  Try again. "))
                else:
                    answer = int(raw_input("I am speaking English, correct?  That is not a number, I asked for a number, tiny human! "))
            print "Congratulations! Maybe you Earthlings aren't as dumb as I thought."
        replay = raw_input("Would you like to fail again? YES or NO? ").lower()
        if replay != "yes" or "no":
            replay = raw_input("I am speaking English, correct? I asked a YES or NO question. Answer appropriately!!!! ").lower()



guess_a_number()
#ord