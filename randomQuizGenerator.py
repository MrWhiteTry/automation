#! python3
# randomQuizGenerator.py - creating exam tickets with questions and answers in random order with keys of answers

import random
# the tickets date. Keys - Name of states, values - capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
            'Areizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California':
            'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford',
            'Deleware': 'Dover', 'Florida': 'Tallahassee', 'Georgia':
            'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
            'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana':
            'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota':
            'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jufferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada': 'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma':
            'Oklahoma city', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas':
            'Austin', 'Utah': 'Salt Lake Cite', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'}

# Generate 35 files with tickets.
for quizNum in range(35):
    # creating file of tickets and answer keys
    quizFile = open('capitalsqriz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answer%s.txt' % (quizNum + 1), 'w')
    # Write heading of tickets
    quizFile.write('Name:\n\nDate:\n\n')
    quizFile.write((' ' * 15) + 'Test knowledge about capitals of states (Ticket %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    # randomizaite nomerite capitals of states
    states = list(capitals.keys())
    random.shuffle(states)

    # create cycle for all 50 states and create the questions for all of them.
    for questionNum in range(50):

        # Take wrong and correct answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write question and answers options in file
        quizFile.write('%s. Chose capital of state %s.\n' %
                       (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))

        quizFile.write('\n')

        # Write key of answer in file
        answerKeyFile.write('%s. %s\n' % (questionNum +1, 'ABCD' [answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()

