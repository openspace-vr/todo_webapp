dynamic_path = "requirements.txt"
new_path = "new_requirements.txt"
index = 0

def get_package():
    with open(dynamic_path, 'r') as file:
        apps = file.readlines() #should be a different name that is local
    return apps

def write_package(install):
    with open(new_path, 'w') as file:
        file.writelines(install)  
