staff_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for staff in staff_list:
    name = staff.split()[-1]
    split_name = name.title()
    print(f'Привет, {split_name}!')

