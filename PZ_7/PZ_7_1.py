#Дан символ С и строки S, So. После каждого вхождения символа С в строку Ѕ вставить строку Ѕо.
try:
 S = "hdf@hjfdhj@fhjd"
 C = "@"
 S0 = "123"
 r = ''
 for i in S:
     r += i
     if i == C:
         r += S0
 print(r)
except:
    print('Ошибка')