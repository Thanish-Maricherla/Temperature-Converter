temp=float(input("Enter the Tempreature in Celsius : "))
fahrenheit=(temp*1.8)+32

print('%0.1f celsius = %0.1f fahrenheit'%(temp,fahrenheit))

if fahrenheit>104:
    print("IT IS TOO HOT!!")
elif fahrenheit<50:
    print("IT IS TOO COLD!!")
else:
    print("TEMPERATURE IS NICE!!")