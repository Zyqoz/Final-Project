import unittest
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer
import numpy as np
import pandas as pd

class DieTest(unittest.TestCase):
    
    def test_1_changeWeight(self):
        '''
        Creates a Die object and then changes the weight and then checks if the weight was indeed changed 
        '''
        array = np.array([1, 2, 3])
        
        die = Die(array)
        
        die.changeWeight(1, 2.0)
        
        
        value = die._die.iat[0, 1] == 2.0
        message = 'Unable to create die object and change its weight properly'
        self.assertTrue(value, message)
        
    def test_2_rollDie(self):
        '''
        Creates a die object and then rolls it 5 times. Checks to see if the returned object is a list of length 5
        '''

        array = np.array([1, 2, 3])

        die = Die(array)

        outcomes = die.rollDie(5)

        value = isinstance(outcomes, list) and len(outcomes) == 5

        message = "The returned object after a roll is either not a list or is not of proper length"
        self.assertTrue(value, message)
        
    def test_3_showDie(self):
        '''
        Creates a die then checks if the displayed die from showDie is equal to the die itself
        '''

        faces = np.array([1, 2, 3])

        die = Die(faces)

        dieItself = die._die

        displayedDie = die.showDie()

        value = dieItself.equals(displayedDie)

        message = 'The shoeDie method does not display the actual die'

        self.assertTrue(value, message)

class GameTest(unittest.TestCase):

    def test_1_play(self):
        
        '''
        Creates two Die objects and then creates a Game object. The Game object is played and the resulting dataframe is checked if it has 10 elements as it should
        '''
        array1 = np.array([1, 2, 3])
        array2 = np.array([1, 2, 3])

        die1 = Die(array1)
        die2 = Die(array2)

        dieObjects = [die1, die2]

        testGame = Game(dieObjects)

        testGame.play(10)

        value = len(list(testGame._results.index)) == 10

        message = 'The _results dataframe is not being setup properly'

        self.assertTrue(value, message)

    def test_2_show(self):
        '''
        Checks and sees if the _results dataframe is equivalent to the dataframe given by the show() method when comparing the wide formats
        
        '''
        array1 = np.array([1, 2, 3])
        array2 = np.array([1, 2, 3])

        die1 = Die(array1)
        die2 = Die(array2)

        dieObjects = [die1, die2]

        testGame = Game(dieObjects)

        testGame.play(10)

        resultsFromShow = testGame.show()

        value = testGame._results.equals(resultsFromShow)

        message = '_results dataframe is not equivalent to the dataframe given by the show() method when comparing the wide formats'

        self.assertTrue(value, message)

class AnalyzerTest(unittest.TestCase):

    def test_1_face_counts_per_roll(self):
        '''
        Checks to see if the dimension of the face_counts_per_roll dataframe is  what it should be

        '''
        
        array1 = np.array([0, 1, 2, 8, 4])
        array2 = np.array([0, 1, 2, 8, 4])

        Die1 = Die(array1)
        Die2 = Die(array2)

        dice = [Die1, Die2]

        game = Game(dice)
        game.play(3)

        analyzer = Analyzer(game)
        analyzer.compute_face_counts_per_roll()


        value = analyzer.face_counts_per_roll.shape == (3, len(array1))
        message = 'The dimension of the face_counts_per_roll dataframe is not what it should be'

        self.assertTrue(value, message)
        
    def test_2_jackpot_count(self):
        '''
        Creates 3 one sided dies and checks if the jackpot count is equal to 5
        '''
        array = np.array([1])

        Die1 = Die(array)
        Die2 = Die(array)
        Die3 = Die(array)

        dice = [Die1, Die2, Die2]

        game1 = Game(dice)
        game1.play(5)


        analyzer = Analyzer(game1)

        jackpot_count = analyzer.jackpot_count()

        value = jackpot_count == 5
        message = 'Jackpot count is not working properly with a 1 sided die'

        self.assertTrue(value, message)
        
if __name__ == '__main__':
    unittest.main()
    
    