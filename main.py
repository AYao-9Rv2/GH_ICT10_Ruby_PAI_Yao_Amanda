# students in clubs
from pyscript import display

club1 = {'Ashley','Shane','Moroi'}
club2 = {'Aiise','Micah','Ashley'}
only_1C = club1.difference(club2)
only_2C = club2.difference(club1)

display(club1 ^ club2, target='output') # 2
display(club1 & club2, target='output') # 3
display(only_1C, target='output') # 4
display(only_2C, target='output') # 5
display(club1 - club2, target='output') # 6