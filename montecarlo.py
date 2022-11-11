import pandas as pd

class Die():
    """ 
    This class instantiates a die with N sides and W weights, and the die can be rolled to select a face
    """
    
    def __init__(self, faces):
        
        if not faces.dtype == 'i' or not faces.dtype == 'S':
            return 'Incorrect dtype'
        
        if not len(np.unique(faces)) == len(faces):
            return 'The elements of the faces must be unique'
        
        weights = fill(len(faces), 1, dtype = float)
        
        df = pd.DataFrame(faces,weights)
        
        return df