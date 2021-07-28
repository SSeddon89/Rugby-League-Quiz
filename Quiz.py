from Question import Question

question_prompts = [
    "What Rugby League team playes their home games at AJ Bell Stadium?\n(a) St Helens\n(b) Salford Red Devils\n(c) Leigh Centurions\n\n",
    "As of 2020 Who has won the most Grand Finals?\n(a) St Helens & Leeds Rhinos\n(b) Wigan Warriors\n (c) Warrington Wolves\n\n",
    "Which Rugby League player become the first ever to be sent off in a Grand Final?\n(a) Jamie Foster\n(b) Gareth Hock\n(c) Ben Flower\n\n",
    "Who scored the most tries in Super League since its 1996 inception?\n(a) Danny Maguire\n(b) Kieron Cunningham\n(c) Joshua Charnley\n\n",
    "Who is the record point scorer in Super League?\n(a) Luke Gale\n(b) Pat Richards\n(c) Kevin Sinfield\n\n",
    "Which Rugby League team is known as the Chery & Whites?\n(a) Warrington Wolves\n(b) Wigan Warriors\n(c) Widnes Vikings\n\n",
    "Which Rugby League club is owned by Russell Crowe?\n(a) Newcastle Knights\n(b) Sydney Roosters\n(c) South Sydney Rabbitohs\n\n",
    "What colour kit do Melbourne Storm wear for home games?\n(a) Blue\n(b) Purple\n(c) Green\n\n",
    "Which team was the last to win the treble in the Super League?\n(a) Leeds Rhinos\n(b) St Helens\(c) Bradford Bulls\n\n",
    "Who holds the record for most appearances in the famous Red Vee?\n(a) Paul Wellens\n(b) Kel Coslett\n(c) Mal Meninga"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "c"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "b"),
]



def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer: 
            score +=1
        print("you got" + str (score) + "/"  + str(len(questions)) + "correct" )



run_test(questions)



