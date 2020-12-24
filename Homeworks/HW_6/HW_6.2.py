def rec_sq(rec_wi, rec_he):
    return rec_wi * rec_he

def tri_sq(tri_base, tri_he):
    return tri_base * tri_he / 2

def circ_sq(rad):
    return (3.14 * rad ** 2)

figs = {1: 'rectangle', 2: 'triangle', 3: 'circle'}
user_fig = int(input("Choose a figure square of you want to count:\
1 for rectangle, 2 for triangle and 3 for circle ")) 

if user_fig == 1:
    rec_wi = float(input("Width = "))
    rec_he = float(input("Height = "))
    square = rec_sq(rec_wi, rec_he)
elif user_fig == 2:
    tri_base = float(input("Base = "))
    tri_he =  float(input("Height = "))
    square = tri_sq(tri_base, tri_he)
elif user_fig == 3:
    rad = float(input("Radius = "))
    square = circ_sq(rad)

print(f"Your's {figs[user_fig]} square is ", square)



