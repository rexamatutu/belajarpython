# untuk mendapat nilai A nilai rata rata mulai 90 ~ 100
# untuk mendapat nilai B nilai rata rata mulai 80 ~ 89
# untuk mendapat nilai C nilai rata rata mulai 70 ~ 79
# untuk mendapat nilai D nilai rata rata mulai 60 ~ 69
# untuk mendapat nilai E nilai rata rata kurang dari 60

# matematika
# english
# b indo
# pkn
# biologi
# fisika



m = int(input('Nilai Matematika:'))
e = int(input('Nilai English:'))
i = int(input('Nilai B indo:'))
p = int(input('Nilai Pkn:'))
b = int(input('Nilai Biologi:'))
f = int(input('Nilai Fisika:'))
rata_rata = (m+e+i+p+b+f)/6

if (rata_rata >= 90 and rata_rata <= 100):
    print(f'rata rata {rata_rata} mendapatkan nilai A')
elif (rata_rata >= 80 and rata_rata < 90):
    print(f'rata rata {rata_rata} mendapatkan nilai B')
elif (rata_rata >= 70 and rata_rata < 80):
    print(f'rata rata {rata_rata} mendapatkan nilai C')
elif (rata_rata >= 60 and rata_rata < 70):
    print(f'rata rata {rata_rata} mendapatkan nilai D')
elif (rata_rata < 60):
    print(f'rata rata {rata_rata} mendapatkan nilai F')
else:
    print(f'rata rata {rata_rata} Error')