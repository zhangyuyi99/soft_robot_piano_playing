import numpy as np
from note import Note

class Piano:
    """position information of keys on piano"""

    def __init__(self, central_C_position, key_width = [0,0.025,0,0,0,0]):
        self.central_C_position = central_C_position
        self.key_width = key_width
        self.keys = self.set_keys(key_width)

    def set_keys(self, key_width):

        # middle octave
        C = Note('C', self.central_C_position, 'white')
        Ch = Note('Ch', 0.0, 'black')
        Db = Note('Db', 0.0, 'black')
        D = Note('D',  np.add(self.central_C_position[:], 1*key_width), 'white')
        Dh = Note('Dh', 0.0, 'black')
        Eb = Note('Eb', 0.0, 'black')
        E = Note('E', np.add(self.central_C_position[:], list(map(lambda x: x * 2, key_width))), 'white')
        F = Note('F', np.add(self.central_C_position[:], list(map(lambda x: x * 3, key_width))), 'white')
        Fh = Note('Fh', 0.0, 'black')
        Gb = Note('Gb', 0.0, 'black')
        G = Note('G', np.add(self.central_C_position[:], list(map(lambda x: x * 4, key_width))), 'white')
        Gh = Note('Gh', 0.0, 'black')
        Ab = Note('Ab', 0.0, 'black')
        A = Note('A', np.add(self.central_C_position[:], list(map(lambda x: x * 5, key_width))), 'white')
        Ah = Note('Ah', 0.0, 'black')
        Bb = Note('Bb', 0.0, 'black')
        B = Note('B', np.add(self.central_C_position[:], list(map(lambda x: x * 6, key_width))), 'white')

        # self.C = Note('C', 0.0, 'white')
        # self.Ch = Note('Ch', 0.0, 'black')
        # self.Db = Note('Db', 0.0, 'black')
        # self.D = Note('D', 1*key_width, 'white')
        # self.Dh = Note('Dh', 0.0, 'black')
        # self.Eb = Note('Eb', 0.0, 'black')
        # self.E = Note('E', 2*key_width, 'white')
        # self.F = Note('F', 3*key_width, 'white')
        # self.Fh = Note('Fh', 0.0, 'black')
        # self.Gb = Note('Gb', 0.0, 'black')
        # self.G = Note('G', 4*key_width, 'white')
        # self.Gh = Note('Gh', 0.0, 'black')
        # self.Ab = Note('Ab', 0.0, 'black')
        # self.A = Note('A', 5*key_width, 'white')
        # self.Ah = Note('Ah', 0.0, 'black')
        # self.Bb = Note('Bb', 0.0, 'black')
        # self.B = Note('B', 6*key_width, 'white')

        # keys = {'C':C, 'Ch':Ch, 'Db':Db, 'D':D, 'Dh':Dh, 'Eb':Eb, 'E':E, 'F':F, 'Fh':Fh, 'Gb':Gb, 'G':G, 'Gh':Gh, 'Ab':Ab, 'A':A, 'Ah':Ah, 'Bb':Bb, 'B':B}
        keys = {'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'A': A, 'B': B}

        return keys
