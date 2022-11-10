#This Python quiz is about music, mainly the 70's and 80's. It asks questions about bands and artists, as well as some movies which have some special music that defines it.
#The user is able to choose the difficulty of the quiz, so it is up to the user, what questions they get
 
#Get user details
score = 0
name = input("Hello user, what is your name? ")
while name == "":
    name = input("Hello user, what is your name? ")
name = name.title()
ready = input("Well {}, are you ready to do this music quiz? ".format(name))
while ready == "":
    ready = input("Well {}, are you ready to do this music quiz? ".format(name))

ready = ready.title()
 
if ready == "Yes":
    print("Okay, let's go!")
else:
    print("Too bad, you're doing it anyway!")
print("")
print("Just want to say that if you want to quit at any point, just type 'Exit' as an answer for a question in the quiz, and it will and the quiz for you.")
#List of questions and answers
#Easy questions and answers
Questions_Easy = ["Who was the lead singer of the British rock band Queen? ", "Which band released the album 'The Dark side of the moon' in 1973? ", "Which rock band was fronted by Jim Morrison? (The) ", "Which of the following singers were NEVER in a mainstream band? \n A: David Byrne \n B: Phil Collins \n C: David Bowie \n D: George Michael  (Answser A, B, C, or D) ",
"Which band released the hit song 'Stairway to heaven'? ", "In which one of his music videos does Michael Jackson transform into a zombie? ", "John Lennon, Paul McCartney, George Harrison, and Ringo Starr were part of which famous English rock band? (The) ", "For which cartoon did Henry Mancini write the famous tune for? (The) ", """Which song begins with the lyrics 'On a dark desert highway, cool wind in my hair'. """, "Reginald Kenneth Dwight is more commonly known by what stage name? ", "Who released the album 'Born in the USA' in 1984? ", "Who was the drummer for the British rock band The Who? ", "Which New Zealand band was brothers Neil and Tim Finn in, before they (Neil) went on to form Crowded House? "]
Answers_Easy = ["Freddie Mercury", "Pink Floyd", "Doors", "C", "Led Zeppelin", "Thriller", "Beatles", "Pink Panther","Hotel California", "Elton John", "Bruce Springsteen","Keith Moon", "Split Enz"]

#Medium questions and answers
Questions_Medium = ["Who was the lead singer of the American rock band Nirvana? ", "Which band released the album in 1986, called 'Slippery when wet?' ", "Which rock band was fronted by Roger Daltrey? (The) ", "Which of the following bands was NOT named after their lead singer? \n A: Bon Jovi \n B: Van Halen \n C: Jimi Hendrix Experience \n D: Santana (Answser A, B, C, or D) ", "Which band released the hit song 'Bohemian Rhapsody'? ", "In which one of Pink Floyd's music videos does school children walk into a meat grinder and become mince? ", "In which blockbuster film was 'The Power of love' by Huey Lewis and the News used in? ", """Which song contains the lyrics 'Every time that I look in the mirror, all these lines on my face getting clearer' """, "Saul Hudson is more commonly known by what stage name? ", "Mick Jagger, Keith Richards, Charlie Watts, Ronnie Wood, Bill Wyman are part of which British rock band? (The) ", "Who released the album 'No jacket required' in 1985? ", "Who was the drummer for the British rock band Led Zeppelin? ", "Which Australian rock band released the album 'Kick' in 1987? "]
Answers_Medium = ["Kurt Cobain", "Bon Jovi", "Who", "B", "Queen", "Another Brick In The Wall", "Back To The Future", "Dream On", "Slash", "Rolling Stones", "Phil Collins", "John Bonham", "Inxs"]

#Hard questions and answers
Questions_Hard = ["Who was the lead singer of the Austrian rock band INXS? ", "Which band released the album 'Heartbeat city' in 1984? (The) ", "Which rock band was fronted by David Lee Roth? ", " What of the following is NOT a New Zealand band? \n A: Split Enz \n B: Cold Chisel \n C: Dragon \n D: The Exponents (Answser A, B, C, or D) ", "Which band released the hit song 'Great Southern Land'? ", "In which one of his music videos does Tom Petty dress up as the Mad Hatter from Alice in Wonderland? ", "David Byrne, Tina Weymouth, Jerry Harrison, and Chris Frantz were part of which famous American rock band? ", "For which famous movie franchise did John Barry write the main theme for? ", """ Which song contains the lyrics 'She's got a smile that it seems to me, reminds me of childhood memories'? """, "Paul David Hewson is more commonly known by what stage name? ", "Who released the album 'Lust for life' in 1977? ", "Who was the drummer for the British rock band Cream? ", "Which band released the album London Calling in 1979? (The) "]
Answers_Hard = ["Michael Hutchence", "Cars", "Van Halen", "B", "Icehouse", "Don't Come Around Here No More", "Talking Heads", "James Bond", "Sweet Child O Mine", "Bono", "Iggy Pop", "Ginger Baker", "Clash"]
 
#Ask user to decide the difficulty of the quiz
difficulty = input("Okay {}, do you want your quiz Easy, Medium, or Hard? ".format(name))
difficulty = difficulty.title()
while difficulty == "":
    difficulty = input("Okay {}, do you want your quiz Easy, Medium, or Hard? ".format(name))
while difficulty != "Easy" and difficulty != "Medium" and difficulty != "Hard":
      difficulty = input("Please choose from easy, medium, or hard")
      difficulty = difficulty.title()

#If user chooses 'Easy', then give easy questions
if difficulty == "Easy":
    i=0
    #Ask questions and compare with answer
    while i < 13:
        response = input(Questions_Easy[i])
        response = response.title()
        while response == "":
          response = input(Questions_Easy[i])
        if response == Answers_Easy[i]:
            print("Correct")
            score += 1
        elif response in Answers_Easy[i]:
          print("Close!!! The answer was " + Answers_Easy[i])
        elif response == "Exit":
          break
        else:
            print("Sorry, correct answer was " + Answers_Easy[i])
        i += 1
        print("")
#If the user chooses 'Medium', then give medium questions
elif difficulty == "Medium":
    i=0
    #Ask questions and compare with answer
    while i < 13:
        response = input(Questions_Medium[i])
        response = response.title()
        while response == "":
          response = input(Questions_Medium[i])
        if response == Answers_Medium[i]:
            print("Correct")
            score += 1
        elif response in Answers_Medium[i]:
          print("Close!!! The answer was " + Answers_Medium[i])
        elif response == "Exit":
          break
        else:
            print("Sorry, correct answer was " + Answers_Medium[i])
        i += 1
        print("")
#If the user chooses 'Hard', then give hard questions
elif difficulty == "Hard":
    i=0
    #Ask questions and compare with answer
    while i < 13:
        response = input(Questions_Hard[i])
        response = response.title()
        while response == "":
          response = input(Questions_Hard[i])
        if response == Answers_Hard[i]:
            print("Correct")
            score += 1
        elif response in Answers_Hard[i]:
          print("Close!!! The answer was " + Answers_Hard[i])
        elif response == "Exit":
          break
        else:
            print("Sorry, correct answer was " + Answers_Hard[i])
        i += 1
        print("")
#Display final score
print("Thank you for playing the quiz {}. Your score was {} out of {}." .format(name, score, i))


