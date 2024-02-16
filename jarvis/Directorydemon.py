import os


def search_and_open_app(app_name):
    app_directories = ["C:\\Program Files","C:\\Users\\Siddhu\\AppData"]  # Update this path to the directory where your apps are located

    for app_directory in app_directories:
        for root, dirs, files in os.walk(app_directory):
            for file in files:
                if app_name.lower() in file.lower():
                    app_path = os.path.join(root, file)

                    # Check if the file is executable
                    if app_path.lower().endswith(('.exe', '.bat', '.cmd')):
                        os.startfile(app_path)
                        print(f"Found and opened: {app_path}")
                        return

    print(f"App '{app_name}' not found on your system")


if __name__ == "__main__":
    app_name_to_search = input("Enter the name of the app you want to search for: ")
    search_and_open_app(app_name_to_search)
