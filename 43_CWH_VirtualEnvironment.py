""" A virtual environment is a tool used to isolate specific Python environments on a single machine, 
allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful 
when working on projects that have conflicting package versions or packages that are not compatible with each other. """

""" # Create a virtual environment
python -m venv myenv

# Activate the virtual environment (Linux/macOS)
source myenv/bin/activate

# Activate the virtual environment (Windows)
myenv\Scripts\activate.bat """


""" Once the virtual environment is activated, any packages that you install using pip will be installed 
in the virtual environment, rather than in the global Python environment. This allows you to have a separate 
set of packages for each project, without affecting the packages installed in the global environment.
# Deactivate the virtual environment
deactivate """

# check this out open terminal and create a virtual environment and then do this create a any python file then download any random pip packets and modules
# then first run that  on your virtual Environment and then run in gloable environment you'll see the version difference 
""" In addition to creating and activating a virtual environment, it can be useful to create a requirements.txt file that lists the packages and their 
versions that your project depends on. This file can be used to easily install all the required packages in a new environment.
# Output the list of installed packages and their versions to a file
pip freeze > requirements.txt
# Install the packages listed in the requirements.txt file
pip install -r requirements.txt """

""" Using a virtual environment and a requirements.txt file can help you manage the dependencies for 
your Python projects and ensure that your projects are portable and can be easily set up on a new machine. """