import os
import logging
from splitwise import Splitwise
from splitwise.expense import Expense
from dotenv import load_dotenv
from datetime import datetime


logging.basicConfig(level=logging.DEBUG)
logging.getLogger("requests_oauthlib").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)
logging.getLogger("oauthlib").setLevel(logging.INFO)

load_dotenv()

current_month = datetime.today().strftime("%B %Y")
# Configure the following variables
TARGET_GROUP = "YouTube premium "  # Set the target group name
EXPENSE_AMOUNT = "22.99"  # Set the total amount of the expense
EXPENSE_DESCRIPTION = f"{current_month} YouTube Premium"  # Set the description of the expense   

splitwise = Splitwise(
    consumer_key=os.getenv('CONSUMER_KEY'),
    consumer_secret=os.getenv('CONSUMER_SECRET'),
    api_key=os.getenv('API_KEY')
)

target_group_found = False

splitwise_groups = splitwise.getGroups()
for group in splitwise_groups:
    #if group.getName() == "YouTube premium":
    if group.getName() == TARGET_GROUP:
        target_group_found = True
        logging.info(f"Target group '{TARGET_GROUP}' found with ID: {group.getId()}")
        target_group_id = group.getId()
        expense = Expense()
        expense.setGroupId(target_group_id)
        expense.setCost(EXPENSE_AMOUNT) 
        expense.setDescription(EXPENSE_DESCRIPTION) 
        
        expense.setSplitEqually()

        try:
            created_expense, errors = splitwise.createExpense(expense)
            logging.info(f"Successfully created expense with ID: {created_expense.getId()}")
            logging.info(f"Expense description: {created_expense.getDescription()}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
        break
   
if not target_group_found:
    logging.warning(f"Group '{group.getName()}' does not match target group '{TARGET_GROUP}'.")