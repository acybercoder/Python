"""
Things to Remember
The pickle built-in module is only useful for serializing and deserializing objects between trusted programs.
The pickle module may break down when used for more than trivial use cases.
Use the copyreg built-in module with pickle to add missing attribute values, allow versioning of classes, and provide stable import paths.
"""

class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4
        self.points = 0
        
state = GameState()
state.level += 1 # Player beat a level
state.lives -= 1 # Player had to try again

import pickle
    
state_path = 'game_state.bin'
with open(state_path, 'wb') as f:
    pickle.dump(state, f)
    
with open(state_path, 'rb') as f:
    state_after = pickle.load(f)
print(state_after.__dict__)

state = GameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

#
class GameState(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points
        
def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs, )

def unpickle_game_state(kwargs):
    return GameState(**kwargs)

# Use copyreg
import copyreg
copyreg.pickle(GameState, pickle_game_state)

state = GameState()
state.points += 1000
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

class GameState(object):
    def __init__(self, level=0, lives=4, points=0, magic=5):
        self.level = level
        self.lives = lives
        self.points = points
        self.magic = magic

state_after = pickle.loads(serialized)
print(state_after.__dict__)