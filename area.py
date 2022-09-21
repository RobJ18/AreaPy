import time

print('*This script can only be used to calculate areas of squares an rectangles*\n')

time.sleep(1)

units = input('What units would you like to use?  \nMeters: \nFeet: \nCentimetres: \nInches: \n')

if units == 'Meters':
    onem = int(input('Can I please have the first measurement: '))
    twom = int(input('Can I please have the second measurement: '))
    print('Your answer is, ', onem * twom, 'm³')

elif units == 'Feet':
    onef = int(input('Can I please have the first measurement: '))
    twof = int(input('Can I please have the second measurement: '))
    print('Your answer is, ', onef * twof, 'ft³')

elif units == 'Centimetres':
    onec = int(input('Can I please have the first measurement: '))
    twoc = int(input('Can I please have the second measurement: '))
    print('Your answer is, ', onec * twoc, 'cm³')

elif units == 'Inches':
    onei = int(input('Can I please have the first measurement: '))
    twoi = int(input('Can I please have the second measurement: '))
    print('Your answer is, ', onei * twoi, 'in³')

else:
    exit()
