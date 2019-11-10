#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random 
import os

# The quiz data. Keys are states and values are their capitals. 
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'} 

if os.path.exists('.\\quiz'):
    pass
else:
    os.makedirs('.\\quiz')
# Generate 35 quiz files. 
for quizNum in range(35):
    #create the quiz and answer key files
    quizfile = open('.\\quiz\\capitalsquiz%s.txt' % (quizNum + 1),'w')
    answerfile = open('.\\quiz\\answer%s.txt' % (quizNum + 1),'w')

    #write out the head of the quizfile
    quizfile.write('Name:\nData:\nPeriod:\n')
    quizfile.write((' ' * 20) + 'State Capital Quiz(From %s)' % (quizNum + 1))
    quizfile.write('\n\n')

    #shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    #loop through all 50 states,making a question for each
    for questionNum in range(50):
        #get right and wrong answers:
        correctanswers = capitals[states[questionNum]]
        wronganswers = list(capitals.values())
        del wronganswers[wronganswers.index(correctanswers)]
        wronganswers = random.sample(wronganswers,3)
        answerOptions = wronganswers + [correctanswers]
        random.shuffle(answerOptions)


        # TODO: Create the quiz and answer key files. 
        quizfile.write('%s.What is the capital of %s?\n' % (questionNum + 1,states[questionNum]))
        for i in range(4):
            quizfile.write(' %s.%s\t ' % ('ABCD'[i],answerOptions[i]))
        quizfile.write('\n')
        #write the answer key to a file
        answerfile.write('%s.%s\n' % (questionNum + 1,'ABCD'[answerOptions.index(correctanswers)]))
    quizfile.close()
    answerfile.close()
