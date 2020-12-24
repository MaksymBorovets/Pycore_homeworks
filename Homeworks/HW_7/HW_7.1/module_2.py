import module_1 as m

figs = {1: 'rectangle', 2: 'triangle', 3: 'circle'}
user_fig = int(input("Choose a figure square of you want to count:\
1 for rectangle, 2 for triangle and 3 for circle ")) 

if user_fig == 1:
    m.rec_wi = float(input("Width = "))
    m.rec_he = float(input("Height = "))
    square = m.rec_sq(m.rec_wi, m.rec_he)
elif user_fig == 2:
    m.tri_base = float(input("Base = "))
    m.tri_he =  float(input("Height = "))
    square = m.tri_sq(m.tri_base, m.tri_he)
elif user_fig == 3:
    m.rad = float(input("Radius = "))
    square = m.circ_sq(m.rad)

print(f"Your's {figs[user_fig]} square is ", square)