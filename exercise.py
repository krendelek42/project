#  Определение типа эластичности спроса по цене с использованием формулы эластичности дуги
print('Determining the type of price elasticity of demand using the arc elasticity formula:')
#  константы
Pa = int(input('Enter the starting price: '))
Qa = int(input('Enter initial demand: '))
Pb = int(input('Enter the final price: '))
Qb = int(input('Enter the final demand: '))
if (Pb - Pa) != 0 and (Qa + Qb) != 0:
    E = ((Qb - Qa)/(Pb - Pa)) * ((Pa + Pb)/(Qa + Qb))  #  формула эластичности спроса по цене
    if abs(E) > 1:
        print('Demand is elastic')  #  спрос эластичен
    elif 0 < abs(E) < 1:
        print('Demand is inelastic')  #  спрос неэластичен
    elif abs(E) == 1:
        print('Demand has unit elasticity')  # спрос имеет единичную эластичность
    elif abs(E) == 0:
        print('Demand is completely inelastic')  # спрос абсолютно неэластичен
    else:
        print('Demand is perfectly elastic')  # спрос абсолютно эластичен
else:
    print('Demand is perfectly elastic')  # спрос абсолютно эластичен
