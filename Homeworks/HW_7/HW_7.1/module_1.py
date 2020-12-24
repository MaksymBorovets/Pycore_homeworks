from math import pi as p, sqrt as s, pow

def rec_sq(rec_wi, rec_he):
    return rec_wi * rec_he

def tri_sq(tri_base, tri_he):
    return tri_base * tri_he / 2

def circ_sq(rad):
    return p * pow(rad, 2)