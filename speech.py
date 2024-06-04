import os

import pyttsx3
def speech(string):
    engine = pyttsx3.init()
        # Speak the detection results
    engine.say(string)
    engine.runAndWait()

# def append(directory,string):
#     # Ensure directory exists
#     if not os.path.exists(directory):
#         os.makedirs(directory)
    
#     file_path = os.path.join(directory, "string.txt")
    
#     # Check if file exists, if not, create it
#     if not os.path.exists(file_path):
#         with open(file_path, 'w') as file:
#             file.write(string + '\n')
#             speech(string)
#     else:
#         # Check for duplicacy
#         with open(file_path, 'r') as file:
#             lines = file.readlines()
#             if string + '\n' not in lines:
#                 # Append string to file if not already present
#                 with open(file_path, 'a') as file:
#                     file.write(string + '\n')
#                     speech(string)


def append(directory, string):
    # Ensure directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, "string.txt")
    
    # Check if file exists, if not, create it
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(string + '\n')
            speech(string)
    else:
        # Read existing lines
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_entries = len(lines)
            
            if num_entries == 0:
                # Just append if there are no entries
                with open(file_path, 'a') as file:
                    file.write(string + '\n')
                    speech(string)
            elif num_entries <= 10:
                # Check for duplicacy against last i entries
                if string + '\n' not in lines[-num_entries:]:
                    # Append string to file if not already present
                    with open(file_path, 'a') as file:
                        file.write(string + '\n')
                        speech(string)
            else:
                # Check for duplicacy against last 10 entries
                if string + '\n' not in lines[-10:]:
                    # Append string to file if not already present
                    with open(file_path, 'a') as file:
                        file.write(string + '\n')
                        speech(string)

