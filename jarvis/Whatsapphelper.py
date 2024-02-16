import pandas as pd
import pywhatkit as kit

# Load the CSV file into a DataFrame
csv_file = "jarvis/contacts.csv"  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)


# Get the name of the person from the user
# name = input("Enter the name of the person: ")

# Search for the person's phone number based on their name
def sendwhatmsg_instantly(name, message):
    global phone_number
    try:
        phone_number = df.loc[df['Name'] == name, 'Number'].values[0]
    except IndexError:
        print(f"No contact found for {name}. Make sure the name is in the CSV file.")

    # Send the WhatsApp message instantaneously
    try:
        kit.sendwhatmsg_instantly(f"+91{phone_number}", message)
        print(f"Message sent to {name} at {phone_number} instantaneously.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
