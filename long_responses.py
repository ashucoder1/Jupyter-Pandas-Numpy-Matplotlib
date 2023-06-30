import random

R_EATING="I dont like eating,I am a bot obviously!"

def unknown():
    response=['Could you rephrase that!',
              'sounds about right',
              '......',
              'what?'][random.randrange(4)]
    
    return response