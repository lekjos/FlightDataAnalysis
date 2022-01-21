# FlightDataAnalysis
Flight Data Analysis Practice Project

## Dependencies
- python 3.9 or greater
- postgres 11 or greater
- python packages listed in `.\requirements.txt`

## Setting up Postgres
1. Install Postgres
2. Create a database, noting the following values:
    - Database Name
    - User
    - Password
    - Port
    - Host
3. Add a new file named `.env` to the root of this repository with the following values:
```
DB_NAME=<your_db_name_here>
DB_USER=<your_username_here>
DB_PASS=<your_password_here>
DB_HOST=<your_host_here>
DB_PORT=<your_port_here>
```
(do not include the "<>", just a string with the values. Using a .env file prevents your credentials from being stored in the git repo)
    

## Getting Started
1. Clone repo to your local machine
2. Navigate to the root of the repository in terminal or command line
3. run `git pull` and verify that you have the `main` branch checked out
4. Create and activate a [python virtual environment](https://docs.python.org/3/library/venv.html). I recommend naming your virtual environment `env` so it's picked up by the `.gitignore`
5. run `pip install -r requirements.txt` to load dependencies in your virtual environment
6. Open 