# splitwise-add-expense-automation
Python script to automate adding fixed monthly expenses to a Splitwise group and split that expense equally between all members of the group. 

## Project Setup Instructions: 

### Prerequisites

Before you begin, ensure the following are installed on your system:

- **Python 3.x or higher**

You will also need register a **Splitwise App** to obtain credentials to run this script. Instructions for authentication can be found [here](https://splitwise.readthedocs.io/en/latest/user/authenticate.html)

---

### 1. Clone the Repository

```
git clone https://github.com/purvac/splitwise-add-expense-automation.git
cd splitwise-add-expense-automation
```
### 2. Install Python Dependencies (If you are running this script locally)
```
pip install -r requirements.txt
```
### 3. Configure Environment Variables Locally

Create a .env file in the same directory as docker_compose.yaml file and fill in the required variable values. These variable values would be found when you register your Splitwise Application, as given in [Prerequisite Step](https://github.com/purvac/splitwise-add-expense-automation?tab=readme-ov-file#prerequisites). 
```
CONSUMER_KEY=<consumer-key-value>
CONSUMER_SECRET=<consumer-secret-value>
API_KEY=<api-key-value>
```
### 4. Configure Environment Variables for GitHub Actions run

If you are running this script in a GitHub Actions job, save the environment variables given above as secrets to your repository. 
