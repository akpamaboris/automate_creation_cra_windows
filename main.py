import os

# Create the name of the file you want and edit the location of where you want to put your projects
path_of_project ='C:/Users/Utilisateur/Documents/projects'
name_to_check ='react-app_'

# Check if the name of the file is what the user wants
def check_name_of_file(name_of_file):
    new_name=""
    for i in name_of_file:
        if i == '_':
            new_name += '_'
            break
        else:
            new_name += i
    if new_name == name_to_check:
        return True
    else:
        return False

# Check if the location exists
if not os.path.exists(path_of_project):
    os.makedirs(path_of_project)
# I go in the location where i need to execute my command
os.chdir(path_of_project)

# I list all the files and folders in the location
files = os.listdir('C:/Users/Utilisateur/Documents/projects')

# I use this variable to know what is the name of the last file
last_number = 0

for index, item in enumerate(files):
    is_it_the_folder_i_want = check_name_of_file(item)
    last_char = item[-1]
    if is_it_the_folder_i_want and int(last_char) >= last_number:
        last_number = int(last_char) + 1



os.system("npx create-react-app " + "react-app" +"_"+str(last_number ))