import vip
class number():
    
    def __init__(self, phone_number : str):
        
        self.phone_num = phone_number
        self.phone = phone_number[3:]
        self.starter = phone_number[:3]
        self.vip = vip.is_vip(self.phone, self.starter)

    def nextPhone(self, phone):
        self.phone = str(int(phone) + 1).zfill(8)
        return self.phone
    
    def nextStarter(self):
        if self.phone != '99999999':
            pass
        elif self.starter == '015':
            self.starter = '010'
        elif self.starter == '012':
            self.starter = '015'
        else:
            self.starter = str(int(self.starter) + 1).zfill(3)
        return self.starter
    
    def __str__(self):
        return f"phone('{phone.phone_num}')"
    
    
phone = number('01000000000')

count = 0
vip_count = {}

while phone.phone <= '99999999':

    #Gaurdian
    if not phone.vip:
        continue
    
    count += 1
    print(phone.phone_num)

    if vip.beside_numbers(phone.phone):
        vip_count['beside numbers'] = vip_count.get('beside numbers', 0) + 1
    
    if vip.counted_numbers(phone.phone):
        vip_count['counted numbers'] = vip_count.get('counted numbers', 0) + 1
    
    if vip.more_than_five(phone.phone):
        vip_count['more than five'] = vip_count.get('more than five', 0) + 1
    
    if vip.one_and_one(phone.phone):
        vip_count['one and one'] = vip_count.get('one and one', 0) + 1
    
    if vip.same_as_starter(phone.phone, phone.starter):
        vip_count['same as starter'] = vip_count.get('same as starter', 0) + 1
    
    if vip.semi_mirror(phone.phone):
        vip_count['Semi mirror'] = vip_count.get('Semi mirror', 0) + 1
    
    if vip.spec_numbers(phone.phone):
        vip_count['Spec numbers'] = vip_count.get('Spec numbers', 0) + 1
    
    if vip.three_digits(phone.phone):
        vip_count['Three digits'] = vip_count.get('Three digits', 0) + 1

    phone.nextStarter()
    phone.phone = phone.nextPhone(phone.phone)
    

print(vip_count)