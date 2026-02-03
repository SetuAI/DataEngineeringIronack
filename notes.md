#### Steps to create virtual env

python3 -m venv venv
-m venv : runs the virtual env module
venv : name of the virtual env

python3 -m venv ironhackenv

--- ironhack env has been created
the env exist , but our terminal isnt inside the virtual env

-- we need to source the activation script

source ironhackenv/bin/activate

-- to install all the requirements from txt file

pip install -r requirements.txt

-- to deactivate the virtual env

deactivate

-- to reactivate the virtual env

    