print(" Welcome to the going to practice destiny simulator!")
print(" This isn't just practice! This is a crossroad of desity!")
print(" This could either lead to the teams glory or the collapes of civilization itself...")

q1 = input(" Your alarm shrieks. Do you'get up' or 'sleep in'?").lower()

if q1 == "get up":
    q2 = input(" You stumble to your practice bag. Do you pack your 'shoes', 'water bottle', or 'forget something'?").lower()
    if q2 == "shoes":
        q3 = input(" You notice your shoes have a glow to them. Do you 'wear them' or 'be scared of them'").lower()
        if q3 == "wear them":
            q4 = input(" The shoes whisper: 'Go through the woods... it's faster' Do you listen? 'yes or 'no'?").lower()
            if q4 == "yes":
                q5 = input(" The raccon come out of their trees in the woods and challenge you to a fight. Do you use 'karate' or use a 'bride'?").lower()
                if q5 == "karate":
                    print(" You unleash your amazing karate and win. The woods name you the Ruler. You arrive at practice 4 hours late but you are now worshiped as a god.")
                else:
                    print(" You bribe the raccons with cotton candy. The raccons now crown you are there king. Practice was canceled in your honor!!!")
            else:
                q5 = input("You reject the shoes advice. Do you take the 'main road' or 'ride a dragon'?").lower()
                if q5 == "main road":
                    print("You hit traffic... your road rage unlocks a monster. You defeat it and unlock super speed.")
                else:
                    print("You summon a dragon. It drops you directly on the field. You make it to practice on time!!!") 
        else: 
            print(" You fear the shoes. They abandon you! You are now forced to play barefoot, but your toughness has earned you respect.")
    elif q2 == "water bottle":
        q3 = input(" The water bottle glows. is it filled with 'Gatorade' or 'Mystery liquid'?").lower()
        if q3 == "Gatorade":
            q4 = input(" You take a sip. Do you choose 'blue' or 'red'?").lower()
            if q4 == "blue":
                print("Blue grants you super speed. You outrun the coachs whistle and stop time itself.")
            else:
                print("Red grants you super strength. You crush the ball, ending practice... FOREVER!")
        else:
             q4 = input("It tastes odd. Do you 'spit it out' or 'drink it'?").lower()
             if q4 == "spit it out":
                 print(" You spit it out and it dissolves the ground, revealing a secret portal to Atlantis. The Mermaids recruit you to be in a undersea practice.")
             else:
                 print(" You drinking it sand you get the power of the sun, but you accidently melt the field.")
    else:
        q3 = input(" You forgot your gear. Do you go back 'home' or 'borrow'?").lower()
        if q3 == "home":
            print(" You go back home but time jumps forward and you appear 1000 years in the future. You are now benched cause you are playing on a team of robots.")
        else:
            print(" You borrow shoes from a teammate but they make you gain super powers. That is against the rules and you get banned from practice due to unfair playing advantage.")
elif q1 == "sleep in":
    q2 = input(" You hit snooze on your alarm. Your coach appears in your dream. Do you 'apologize' or 'run'?").lower()
    if q2 == "apologize":
        q3 = input(" Your coach demands that you do pushups or give them snacks. Do you 'do pushups' or 'give them snacks'?").lower()
        if q3 == "do pushups":
            print("You do 10 pushups and pass out in your dream. You wake up to embarrassed and quit the team.")
        else:
            print(" You give your coach a snack. Your coach devours them and promotes you to captain.")
    else:
        q3 = input(" You run, but the dream turns into a chase. Are you chased by 'a pack of wolves' or 'the school mascot'?").lower()
        if q3 == "a pack of wolves":
            print(" You manage to tame the wolves mid-chase. They lead you to practice as your new pack. Your coaches now fear you and you become coach.")
        else:
            q4 = input(" The mascot corners you. Do you 'fight the mascot' or 'dance battle'")
            if q4 == "fight the mascot":
                print(" You fight the mascot. You win, but the school bans you.")
            else:
                print(" You have a ultimate dance battle and destroy them. That was such a weird event pract was forgotten.")
else:
    print(" You do nothing. The universe collapes from severe boredom.")