import unittest
from monetecarlo import Die

class DieTest(unittest.TestCase):
    
    'Tested'
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
            
if __name__ == '__main__':
    unittest.main()
    
    