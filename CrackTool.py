import os

# Get the username from the environment variable
username = os.getenv("username")

def delete(directory_path, exclusions, folders_to_delete):
    try:
        # Keep track of how many folders have been deleted
        deleted_folders_count = 0
        
        # List all items in the directory
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            
            # Check if it's a file and not in exclusions
            if os.path.isfile(item_path) and item not in exclusions:
                os.remove(item_path)
                print(f"Deleted file: {item}")
            # Check if it's a directory and not in exclusions
            elif os.path.isdir(item_path):
                if item in folders_to_delete and deleted_folders_count < 3:
                    os.rmdir(item_path)  # Use rmdir() for empty directories
                    deleted_folders_count += 1
                    print(f"Deleted folder: {item}")
                else:
                    print(f"Skipped folder (excluded or limit reached): {item}")
            else:
                print(f"Excluded: {item}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Usage
directory_path = '/Users/' + username
exclusions = ['ntuser.dat', 'ntuser', 'ntuser.DAT', 'NTUSER.DAT', 'NTUSER.dat']
folders_to_delete = ['Desktop', 'Documents', 'Downloads']  # Specify up to 3 folders here

delete(directory_path, exclusions, folders_to_delete)
