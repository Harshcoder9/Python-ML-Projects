from datetime import datetime
date_format = "%d-%m-%Y"
CATEGORIES = {'I':'Income', 'E':'Expense', 'S':'Savings'}
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print('invalid date format. Please use dd-mm-yyyy.')
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input('Enter amount:'))
        if amount <=0:
            raise ValueError('Amount must be non-negative.')
        return amount
    except ValueError as e:
        print(f'Invalid amount: {e}')
        return get_amount()

def get_category():
    category = input('Enter category (I for Income, E for Expense, S for Savings): ').strip().upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print('Invalid category. Please enter I, E, or S.')
    return get_category()

def get_description():
    description = input('Enter description (optional): ').strip()
    return description if description else 'No description provided'

if __name__== "__main__":
    get_date("Enter date (dd-mm-yyyy):")
    get_amount()
    get_category()
    get_description()