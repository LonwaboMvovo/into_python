# test calutils.py
# Stephan Jamieson
# 4/8/2015

def print_welcome():
    print('Test harness for calutils')
    
def get_selection():
    print('\nChoose from the following options:')
    print('0. quit')
    print('1. Test is_leap_year().')
    print('2. Test month_name().')
    print('3. Test days_in_month().')
    print('4. Test first_day_of_year().')
    print('5. Test first_day_of_month().')
    return int(input())

def test_leap_year():
    from calutils import is_leap_year

    year = int(input('Enter the year (4 digits):\n'))
    if is_leap_year(year):
        print('The year '+str(year)+' is a leap year.')
    else:
        print('The year '+str(year)+' is not leap year.')

def test_month_name():
    from calutils import month_name
    
    for month_number in range(1, 13):
        print('Month number '+str(month_number)+ ' is '+month_name(month_number)+'.')
        

def test_days_in_month():
    from calutils import days_in_month

    year = int(input('Enter the year (4 digits):\n'))
    for month_number in range(1, 13):
        print('The days in the month with number '+str(month_number)+ ' in year '+str(year)+' is '+str(days_in_month(month_number, year))+'.')
        
def test_first_day_year():
    from calutils import first_day_of_year
    
    year = int(input('Enter the year (4 digits):\n'))
    print('The first day of '+str(year)+' is '+str(first_day_of_year(year))+'.')
    
def test_first_day_month():
    from calutils import first_day_of_month
    
    month = int(input('Enter the month (1 for January, ..., 12 for December):\n'))
    year = int(input('Enter the year (4 digits):\n'))
    print('The first day of month '+str(month)+' in '+str(year)+' is '+str(first_day_of_month(month, year))+'.')
    
def main():
    print_welcome()
    
    selection = get_selection()
    while not selection==0:

        if selection==1:
            test_leap_year()
        elif selection==2:
            test_month_name()
        elif selection==3:
            
            test_days_in_month()
        elif selection==4:
            test_first_day_year()
        elif selection==5:
            test_first_day_month()
        else:
            print('That selection was not recognised.')

        selection = get_selection()
        
        
main()