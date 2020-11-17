print('Determination of the type of demand elasticity according to the arc elasticity formula:')
Pa = int(input('Enter the starting price: '))
Qa = int(input('Enter initial demand: '))
Pb = int(input('Enter the final price: '))
Qb = int(input('Enter the final demand: '))
if (Pb - Pa) != 0 and (Qa + Qb) != 0:
    E = ((Qb - Qa)/(Pb - Pa)) * ((Pa + Pb)/(Qa + Qb))
    if abs(E) > 1:
        print('Demand is elastic')
    elif 0 < abs(E) < 1:
        print('Demand is inelastic')
    elif abs(E) == 1:
        print('Demand has unit elasticity')
    elif abs(E) == 0:
        print('Demand is completely inelastic')
    else:
        print('Demand is perfectly elastic')
else:
    print('Demand is perfectly elastic')
