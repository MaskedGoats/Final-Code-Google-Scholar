import scholarly
from scholarly import scholarly, ProxyGenerator
import csv
import time
import os

filter_year = 2020

# Perform a search query for articles related to ophthalmology
search_query = scholarly.search_pubs('ophthalmology', 
                                     year_low=filter_year, 
                                     year_high=filter_year,
                                    start_index=1000)
                                     

# Initialize a list to store information for the first 5 authors
authors_info = []

# Retrieve information for the first 5 authors
for i in range(200):
    print(f"Making next request... ({i})")
    publication = next(search_query, None)
    if publication:
        id = publication['author_id'][0]
        publication_year = publication['bib']['pub_year']
        citations = publication['num_citations']
        
        try:
            author_info = scholarly.search_author_id(id)
            author_name = author_info['name']
        except Exception as e:
            print(f"Error retrieving author info for ID {id}: {e}")
            author_name = 'N/A'

        # Append the extracted information to the list
        authors_info.append({
            "Author Name": author_name, 
            "Author ID": id,
            "Publication Year": publication_year,
            "Citations": citations
        })
        print(authors_info[-1])
    time.sleep(5)

# Define the CSV file name
file_name = f"authors_info_{filter_year}.csv"

# Make sure not to overwrite an existing CSV file
file_name_num = 0
while os.path.exists(file_name):
    file_name_num += 1
    file_name = f"authors_info_{filter_year}_{file_name_num}.csv"

print("Writing to file:", file_name) 

# Open the CSV file in write mode
with open(file_name, mode='w', newline='') as file:
    fieldnames = ["Author Name", "Author ID", "Publication Year", "Citations"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write the data rows for all authors
    for author_info in authors_info:
        writer.writerow({
            "Author Name": author_info['Author Name'],
            "Author ID": author_info['Author ID'],
            "Publication Year": author_info['Publication Year'],
            "Citations": author_info['Citations']
        })

print(f"Data for {len(authors_info)} author(s) has been written to {file_name}")
