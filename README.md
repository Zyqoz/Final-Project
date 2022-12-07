# Final-Project

Metadata:

My name is Mir Muhammad Abdur Rahman and the project name is Montecarlo

Synopsis:

This is how the class is used:

        array = np.array([1])

        Die1 = Die(array)
        Die2 = Die(array)
        Die3 = Die(array)

        dice = [Die1, Die2, Die2]

        game1 = Game(dice)
        game1.play(5)
        
        analyzer = Analyzer(game1)
        analyzer.jackpot_count()

## API Description        

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
    
    class Game():
    '''
    This class represents a game with one or more die of equivalent list of faces but possibly different weights.
    This class has the ability to roll all the dice a certain number of times.
    ...
    
    Attributes
    ----------
    
    dice: list
        List that contains the Die objects that are part of the game
    
    _results: dataframe
        Stores the results of the game
    
    Methods
    -------
        play(n)
            Plays the game n times and saves the results to a private dataframe
    
    '''
    
    class Analyzer():
    '''
    Takes the result of a single game and computes statistical values of that game. These properties are available as attribute objects
    
    Attributes
    ----------
    game: Game object
        The Game object on which analysis is done
        
    type: String
        Shows the dtype of the faces used
        
    face_counts_per_roll: dataframe
        Has the face and the amount of times this was rolled
    
    jackpot_count: int
        Count of how many times there was a jackpot in the game
    
    jackpot_results: dataframe
        Shows which rolls resulted in a jackpot and their corresponding faces
        
    combo_count: dataframe
        Distinct combination of faces rolled along with their counts
    
    
    Methods
    -------
    
    face_counts_per_roll()
        Computes how many times a given face is ruled in every event
        
    jackpot()
        Returns how many times there was a roll where all faces were equivalent
    
    combo()
        Computes the distinct amount of faces rolled along with their counts
    
    '''
