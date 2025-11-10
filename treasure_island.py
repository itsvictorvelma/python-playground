def game_over():
    print("\nGAME OVER\n")
    while True:
        choice = input("Try again? (y/n): ").lower()
        if choice == "y":
            treasure()
            break
        elif choice == "n":
            print("Thank you for playing.")
            exit()
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

def treasure():
    
    print("\nWelcome to Treasure Island.\nYour mission is to find the treasure.")
    print("\nPress enter to begin...")
    input()

    print("You wake up on a desolate shore. The moon hangs low, swollen and blood-tinted. Your ship - what's left of it - is scattered across black sand and broken coral. Every wave sounds like its whispering your name...")
    print("You drag yourself to your feet. There’s a faint trail leading left through the jungle, and a jagged path right along the cliffs.")

    prompt1 = input("\nleft or right?: ").lower()
    
    if prompt1 == "right":
        print("\nYou follow the cliffside, ignoring the groans of the tide far below. The wind bites, carrying the scent of rot and metal. The rocks beneath your feet crumble as if the island itself rejects you.\n")
        print("Suddenly the ground gives way - not a hole, but a pit carved unnaturally smooth, like something made it. You fall into the dark, and just before the impact, you hear it breathing beneath you.")
        game_over()

    elif prompt1 == "left":
        print("\nYou push through the jungle. The canopy swallows the moonlight, and strange things scuttle in the leaves. Hours—or maybe minutes—pass before you stumble into a clearing.")
        print("\nIn the center lies a still lake, its surface glassy, perfectly reflecting the stars that shouldn’t exist.")
        print("\nA rickety dock stretches out into the water. Across the lake, you see faint lanterns — a ruined cabin, perhaps. You could swim across… or wait and watch.")
        prompt2 = input("\nswim or wait?: ").lower()

        if prompt2 == "swim":
            print("\nYou strip down and slip into the water. It’s colder than death. Something brushes against your leg - once,\nthen again, harder. You keep going, teeth chattering, when you feel a sharp bite. Then another.")
            print("\nThe water churns red as pale, eyeless trout swarm around you, their mouths filled with tiny, human-like teeth.")
            print("\nYou scream, but the lake only swallows the sound.")
            game_over()

        elif prompt2 == "wait":
            print("\nYou sit by the shore. Time seems to fold in on itself; the stars move too fast, the moon melts into the lake.\nFrom the mist ahead, a stone structure rises - ancient, massive, impossible. Three doors glow faintly in\nits face:")
            print("\nOne red, flickering like molten iron.\nOne blue, cold and shifting like deep water.\nOne yellow, pulsing softly, like candlelight in a tomb.")
            print("\nSomething whispers - choose.")

            prompt3 = input("\nred, blue, or yellow?: ").lower()

            if prompt3 == "red":
                print("\nThe moment your hand touches the red door, it pulses - hot, hungry. It opens on its own, releasing a\nroar of flame. You stumble back, but too late - it clings to you like tar.")
                print("\nThe fire doesn’t consume flesh. It eats memories. You forget your name first, then your purpose, until only\nthe smell of burning remains.")
                game_over()

            elif prompt3 == "blue":
                print("\nCold air floods the room as you step through. The walls drip with condensation. Something breathes in\nthe dark - slow, deliberate.")
                print("\nYou turn, and a dozen yellow eyes open all at once. The beasts emerge, bodies twisted like half-formed\nmen. Their teeth glint with moonlight, and they grin as if they recognize you.")
                print("\nYou never even get to scream.")
                game_over()

            elif prompt3 == "yellow":
                print("\nThe yellow door creaks open, revealing a narrow hall bathed in gold light. The air hums - it feels alive.")
                print("\nYou step forward and find a small chest resting atop a stone pedestal. Inside isn’t gold or jewels, but a\nbeating heart — black, cracked, yet alive.")
                print("\nThe whispers stop. The island exhales.")
                print("\nThe heart dissolves into light and sinks into your chest.")
                print("\nThe treasure was never gold... it was freedom.")
                print("\nYou Win.")

            else:
                print("invalid input")
                treasure()

        else:
            print("invalid input")
            treasure()

    else:
        print("invalid input")
        treasure()

treasure()