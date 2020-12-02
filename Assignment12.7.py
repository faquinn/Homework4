#Flammond Quinn
#PSID: 1659392



def get_age():
    adult_age = int(input())
    if adult_age < 18 or adult_age > 75:
        raise ValueError('Invalid age.')
    return adult_age

def fat_burning_heart_rate(adult_age):
    heartrate = 220 - adult_age
    heartrate = heartrate * 0.7
    return heartrate

if __name__ == '__main__':
    try:
        adultage=get_age()
        rate=fat_burning_heart_rate(adultage)
        print('Fat burning heart rate for a',adultage,'year-old:', end=' ')
        print(rate,'bpm')
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.\n')
