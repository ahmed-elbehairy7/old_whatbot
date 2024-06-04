"""A program that checks if the phone number a vip by checking it's pattern"""

def is_vip(phone : str, starter : str):
    """THE BIG BOSS THAT HAVE ALL VIP NUMBERS PATTERNS
        Excludes till now 4,168,730 numbers from each starter which means 16,674,920 from all numbers which means 4% of the total numbers"""
    
    if one_and_one(phone) or semi_mirror(phone) or beside_numbers(phone) or three_digits(phone) or counted_numbers(phone) or more_than_five(phone) or same_as_starter(phone, starter) or spec_numbers(phone):
        
        return True
    return False


#removing numbers like 'aaaaaaaa', '4dig4dig', 'abababab' including if two numbers are odd
# Excludes 734,500 numbers from the starter numbers
def one_and_one(phone):
    one_and_one_count = 0
    for i in range(4):
        if phone[i] == phone[i + 4]:
              one_and_one_count += 1
    if one_and_one_count >= 3:
         return True
    one_and_one_count = 0
    for i in range(4):
        if phone[i] == phone[i + 2]:
              one_and_one_count += 1
    if one_and_one_count >= 3:
         return True
    return False

#removing semi mirrors like 'abcftabc', 'fabcabct', 'fabctabc', 'abcabct', 'fabctabc', 'ftabcabc'
#Excludes 569169 numbers from the starter numbers
def semi_mirror(phone): 
        if f'{phone[0]}{phone[1]}{phone[2]}' == f'{phone[5]}{phone[6]}{phone[7]}' or f'{phone[1]}{phone[2]}{phone[3]}' == f'{phone[4]}{phone[5]}{phone[6]}'or f'{phone[1]}{phone[2]}{phone[3]}' == f'{phone[5]}{phone[6]}{phone[7]}' or f'{phone[2]}{phone[3]}{phone[4]}' == f'{phone[5]}{phone[6]}{phone[7]}' or f'{phone[0]}{phone[1]}{phone[2]}' == f'{phone[4]}{phone[5]}{phone[6]}' or f'{phone[0]}{phone[1]}{phone[2]}' == f'{phone[3]}{phone[4]}{phone[5]}':
             return True
        return False

#removing number if it consist of 2 or 3 digits only
#Excludes 706960 numbers from the starter numbers
def three_digits(phone):
    numbers = {phone[0]}
    for i in range(8):
        numbers.add(phone[i])
    if len(numbers) <= 3:
         return True
    return False

#removing numbers containing counted numbers
#Excludes 752196 from the starter numbers
def counted_numbers(phone):

    for i in range(5):
        if phone[i] == str(int(f'{phone[i+1]}') + 1).zfill(1) and phone[i+1] == str(int(f'{phone[i+2]}') + 1).zfill(1) and phone[i+2] == str(int(f'{phone[i+3]}') + 1).zfill(1):
            return True
    
    for i in range(5):
        if phone[i] == str(int(f'{phone[i+1]}') - 1).zfill(1) and phone[i+1] == str(int(f'{phone[i+2]}') - 1).zfill(1) and phone[i+2] == str(int(f'{phone[i+3]}') - 1).zfill(1):
            return True

    for i in range(3):
        if f'{phone[i]}{phone[i+1]}'.zfill(2) == str(int(f'{phone[i+2]}{phone[i+3]}') + 1).zfill(2) and f'{phone[i]}{phone[i+1]}'.zfill(2) == str(int(f'{phone[i+4]}{phone[i+5]}') + 2).zfill(2):
            return True
            
    for i in range(3):
        if f'{phone[i]}{phone[i+1]}'.zfill(2) == str(int(f'{phone[i+2]}{phone[i+3]}') - 1).zfill(2) and f'{phone[i]}{phone[i+1]}'.zfill(2) == str(int(f'{phone[i+4]}{phone[i+5]}') - 2).zfill(2):
            return True
            
    for i in range(3):
        if f'{phone[i]}{phone[i+1]}'.zfill(2) == str(int(f'{phone[i+2]}{phone[i+3]}') + 10).zfill(2) and f'{phone[i]}{phone[i+1]}'.zfill(2) == str(int(f'{phone[i+4]}{phone[i+5]}') + 20).zfill(2):
            return True
            
    for i in range(3): 
        if f'{phone[i]}{phone[i+1]}'.zfill(2) == str(int(f'{phone[i+2]}{phone[i+3]}') - 10).zfill(2) and f'{phone[i]}{phone[i+1]}'.zfill(2) == str(int(f'{phone[i+4]}{phone[i+5]}') - 20).zfill(2):
            return True
            
    return False

#removing number if there is doubling numbers or 4 more beside numbers in it
#Excludes 666,460 numbers from the starter numbers
def beside_numbers(phone):
    beside_numbers_count = 0
    for i in range(0, 6, 2):
        if phone[i] == phone[i+1]:
            beside_numbers_count += 1
            if beside_numbers_count >= 3:
                return True
    beside_numbers_count = beside_numbers_count / 2
    for i in range(1, 7, 2):
        if phone[i] == phone[i+1]:
            beside_numbers_count += 1
            if beside_numbers_count >= 3:
                return True
    beside_numbers_count = 0
    for i in range(6):
        if phone[i] == phone[i+1] and phone[i] == phone[i+2]:
            beside_numbers_count += 1
            if beside_numbers_count >= 2:
                return True
    return False

#Removing numbers that have a specific digit 6 times or more
#Excludes 23410 from the starter numbers
def more_than_five(phone):
    for i in range(10):
        count = 0
        for j in range(8):
            if phone[j] == str(i):
                count += 1
        if count >= 5:
            return True
    return False

#Removing numbers that start with the last digit of the starter repeated
#Excludes 99999 numbers from the starter numbers
def same_as_starter(phone, starter):
    if (phone.startswith('0000') == True and starter == '010') or (phone.startswith('111') == True and starter == '011') or (phone.startswith('2222') == True and starter == '012') or (phone.startswith('5555') == True and starter == '015'):
        return True
    return False

#Removing numbers that have 786 or 108 in it
#Excludes 1,197,600 from every starter
def spec_numbers(phone):
    if '786' in phone or '108' in phone:
        return True
    return False