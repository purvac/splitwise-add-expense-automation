import os
import logging
from splitwise import Splitwise
from splitwise.expense import Expense
from dotenv import load_dotenv


logging.basicConfig(level=logging.DEBUG)
logging.getLogger("requests_oauthlib").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)
logging.getLogger("oauthlib").setLevel(logging.INFO)

# Configure the following variables
TARGET_GROUP = "YouTube premium "
EXPENSE_AMOUNT = "1.00"  # Set the total amount of the expense
EXPENSE_DESCRIPTION = "Test Expense from API"

load_dotenv()

splitwise = Splitwise(
    consumer_key=os.getenv('consumer_key'),
    consumer_secret=os.getenv('consumer_secret'),
    api_key=os.getenv('api_key')
)

splitwise_groups = splitwise.getGroups()
for group in splitwise_groups:
    #if group.getName() == "YouTube premium":
    if group.getName() == TARGET_GROUP:
        target_group_id = group.getId()
        expense = Expense()
        expense.setGroupId(target_group_id)
        expense.setCost(EXPENSE_AMOUNT) 
        expense.setDescription(EXPENSE_DESCRIPTION) 
        
        expense.setSplitEqually()

        try:
            created_expense, errors = splitwise.createExpense(expense)
            if errors:
                print(f"Errors occurred: {errors}")
            else:
                print(f"Successfully created expense with ID: {created_expense.getId()}")
                print(f"Expense description: {created_expense.getDescription()}")
        except Exception as e:
            print(f"An error occurred: {e}")
        break
    else:
        print(f"Group '{group.getName()}' does not match target group '{TARGET_GROUP}'.")