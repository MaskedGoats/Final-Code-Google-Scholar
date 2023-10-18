import csv

# Function to separate the first and last names or handle "N/A" values
# Function to separate the first and last names or handle "N/A" values
def separate_name(name):
    if name.lower() == 'n/a':
        return 'N/A', 'N/A'
    
    # Split the name by a comma and strip whitespace from both parts
    parts = name.split(',')
    if len(parts) >= 1:
        name_part = parts[0].strip()
        words = name_part.split()
        
    if len(words) >= 2:
        first_name = words[0]
        last_name = words[-1]
    else:
        first_name, last_name = name_part, ''

    return first_name, last_name

# Input and output file paths
input_file_path = 'authors_info_2023_1.csv'
output_file_path = 'authors_info_2023_1.sep.csv'

# Read the input CSV file and write to the output file
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
    # Create CSV reader and writer objects
    csv_reader = csv.DictReader(input_file)
    fieldnames = csv_reader.fieldnames + ['First Name', 'Last Name']
    csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    # Process and write the data
    # Process and write the data
    for row in csv_reader:
        author_name = row['Author Name']
        first_name, last_name = separate_name(author_name)
        row['First Name'] = first_name
        row['Last Name'] = last_name
        csv_writer.writerow(row)


print("CSV processing complete. Output written to", output_file_path)
