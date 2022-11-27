import pandas as pd
import numpy as np
from numpy.random import choice


class Die():
    ''' 
    This class represents a die with N sides and W weights.
    
    ...
    
    Attributes
    ----------
    _die : dataframe
        private dataframe that includes the sides and weights of the die
        as the columns
    
    Methods
    -------
    
    changeWeight(faceValue, newWeight)
        Changes the weight of the given face to the new given weight
    
    rollDie(rolls = 1)
        Rolls the die rolls times and returns a list of outcomes
    
    showDie()
        Shows the current set of faces and weights by returning the _die
        dataframe
        
    '''
    
    def __init__(self, faces):
        '''
        After checking initial conditions, a private dataframe die
        object is created based on an array of faces and and an array of 
        weights. The weights array is default to 1.0.
        
        Parameters
        ----------
            faces: numpy nd array 
                Can be either an int, float, or String.
                Specifically, can only be int32, float64, or |S1
        
        '''
        
        #Checking criteria of the argument
        
            #If faces dtype is not int32, float64, or |S1, then an error
            #is raised
        
        if not faces.dtype == 'int32' and not faces.dtype == '|S1' and not faces.dtype == 'float64':
            raise TypeError('Incorrect dtype')
       
            #Checking if the elements of the face are unique
        
        if not len(set(faces)) == len(faces):
            raise TypeError('The elements of the faces array must be unique')
        
        
        #Fillings weights np array with 1s
        
        weights = np.full(len(faces), 1, dtype = float)
        
        #Creating _die dataframe by combining faces and weights arrays
        
        self._die = pd.DataFrame({'Faces': faces, 'Weights' : weights})
    
    def changeWeight (self, faceValue, newWeight):
        '''
        After checking intial conditions, changes the weight of
        the given face to the new given weight
        
        Parameters
        ----------
            faceValue: |S1, int32, or float64
                The face value whoose weight wants to be changed
            newWeight: float, or a number that can be converted to a float
                New weight value
        Returns
        -------
        None
        '''
        #Checking criteria of arguments
        
            #Checking to see if the face passed is in the array of faces. If not, an error is raised.
        
        if not faceValue in set(self._die.Faces):
            raise TypeError('This face does not exist')
            
            #If float, makes method work.
            #If the new weight is not a float, but can be converted to a float, then it is converted to a float
            #If the new weight is neither a float, and it can't be converted to a float, then an error is raised.

        if not newWeight == float:
            try:
                newWeight = float(newWeight)
                
            except:
                
                raise TypeError('This value is neither a float nor can it be converted to one')
            
            #Changing weight of the given face to the new weight
            
        #Index of the face value that wants to be changed
        index = self._die.index[self._die['Faces'] == faceValue][0]

        #Change weight of the given face to the new weight

        self._die.iat[index, 1] = newWeight
    
    def rollDie(self, rolls = 1):
        '''
        Parameters
        ----------
        rolls: int
            How many times the die is to be rolled
        
        Returns
        -------
        outcomes: list
            The list of outcomes after the roll
        '''
        facesList = self._die.Faces

        weightsList = self._die.Weights
        
        weightsList = weightsList/sum(weightsList)

        outcomes = list(choice(facesList, rolls, p = weightsList))

        return outcomes
    
    def showDie(self):
        '''
        Returns the die dataframe
        
        Parameters
        ----------
        None
        
        Returns
        -------
        _die: dataframe
        '''
        return self._die
    
'Tested'    
class Game():
    '''
    This class represents a game with one or more die of equivalent list of faces but possibly different weights.
    This class has the ability to roll all the dice a certain number of times.
    ...
    
    Attributes
    ----------
    
    dice: list
        Private list that contains the Die objects that are part of the game
    
    _results: dataframe
        Stores the results of the game
    
    Methods
    -------
        play(n)
            Plays the game n times and saves the results to a private dataframe
    
    '''
    
    
    def __init__(self, dieObjects):
        '''
        Takes a list of dieObjects and instantiates a new Game object with similar dice.
        
        Parameters
        ----------
            dieObjects: list
                List with Die objects as elements
        
        '''
        
        self.dice = dieObjects
        
    
    def play(self, n):
        '''
        Rolls all the Die in the _dice list n times. The result is saved in _results, the private dataframe.
        
        Parameters
        ----------
            n: int
                The amount of times the dies in the dieObjects list will be rolled
        '''
        
        #Creating a dataframe with the results of the first die in the dieObjects list
        
        rollResult = self.dice[0].rollDie(n)
        
        self._results = pd.DataFrame(rollResult)
        
        #Adding the results of all the die after the first die to the _results dataframe
        
        for x in range(1, len(self.dice)):
             
            dieResult = self.dice[x].rollDie(n)
        
            self._results[x] = dieResult
        
        self._results.index.name = 'Roll Number'
    'Unfinished'     
    def show(self, tabFormat = 'w'):
        '''
        Shows the user the results of the most recent play
        
        Parameters
        ----------
        tabFormat: String
            Indicates whether to return the value in wide format or narrow format
            'w' for wide format
            'n' for narrow format
        
        Returns
        -------
            _results: pandas dataframe
                private dataframe that has the results of the most recent game
        '''
        
        try:
            not tabFormat == 'w' or not tabFormat == 'n'
                
        except:
            raise TypeError('The given table format does not exist. Table format must be either narrow or wide')
        
        if tabFormat == 'w':
            return self._results
        ''' 
        if tabFormat == 'n':
            narrow_results = pd.DataFrame({
                'Roll': self._results.index
                'Die' : self._results.names
        '''         
        