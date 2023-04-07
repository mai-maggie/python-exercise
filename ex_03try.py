hrs=input('Enter Hours:')
rate=input('Enter rate:')
try:
   fh=float(hrs)
   fr=float(rate)
   print('Pay',fh*fr)
except:
   print('Please enter number for both input!') 
