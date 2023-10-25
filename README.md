# ids706_python_template
Mini project8 for ids706: 
- Rust version of Project 5: Python Script interacting with SQL Database


## Requirements
- Rust 1.73
- Virtual environment (optional but recommended, already set up as env in Makefile)
- Packages listed in `.\.devcontainer\setup.sh`


## Set Up
1. Run `make install` to install all packages listed in setup.sh

2. Run `make refactor` to check up the style and format of the Rust Code

3. Run `make test` to test the ./src/database.py

4. Run `make run` to check the functionality of the database query in ./src/database.py

(You can also Run `make all` to finish all the set up operations at the same time)

## Database Interaction
After set up, you can run `make deploy` to get the output of database query in ./src/database.py


## Structure
1. `.devcontainer` includes a Dockerfile, devcontainer.json and setup.sh. The files in this container specify how the project can be set up.

2. `.github` includes the CI/CD settings

3. `Cargo.toml` includes all configuration, dependencies and metadata of Rust Project

3. `.src` includes all the Rust source file

4. `Makefile` includes all the make settings for this project

5. `book.db` is the database we will operate on

6. `.gitignore` includes all the files that do not want to be tracked by github

7. `.pythonVersion` includes the python version of the Rust source file

## CI/CD
GitHub Actions are configured for Continuous Integration and Continuous Deployment. See `.github/workflows/ci_cd.yml` for details.




