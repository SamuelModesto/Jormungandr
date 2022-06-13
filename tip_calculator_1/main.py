print('Wellcome to the tip calculator')
bill = float(input('What was the total bill? $'))
percent = int(input('What percentage tip would you like to give? 10, 12, or 15?'))
num_people = int(input('How many people to split the bill?'))
resultBill = bill + bill * percent / 100
result = resultBill / num_people
total_per_person = round(result, 2)
print(f'Each person should pay: ${total_per_person} ')

