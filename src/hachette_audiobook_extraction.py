import os
import xml.etree.ElementTree as ET
import pandas as pd

# Directory containing the XML files
xml_directory = 'xml-files/hachette'

# Initialize an empty list to store the book data
books = []

# Iterate over each XML file in the directory
for filename in os.listdir(xml_directory):
    if filename.endswith('.xml'):
        # Parse the XML file
        tree = ET.parse(os.path.join(xml_directory, filename))
        root = tree.getroot()

        # Iterate over each Product in the file
        for product in root.findall('Product'):
            # Initialize an empty dictionary to store this book's data
            book = {}

            # Extract the fields
            for product_id in product.findall('.//ProductIdentifier'):
                if product_id.find('ProductIDType').text == '15':
                    book['ISBN13'] = product_id.find('IDValue').text
                    break

            book['Title'] = product.find('.//TitleText').text

            subtitle_elem = product.find('.//Subtitle')
            book['Subtitle'] = subtitle_elem.text if subtitle_elem is not None else ''

            authors_elem = product.findall('Contributor')
            book['Authors/Narrators'] = ', '.join([contributor.find('PersonName').text for contributor in authors_elem]) if authors_elem else ''

            imprint_elem = product.find('.//ImprintName')
            book['Imprint'] = imprint_elem.text if imprint_elem is not None else ''

            pub_date_elem = product.find('.//PublicationDate')
            book['Pub Month Year'] = pub_date_elem.text if pub_date_elem is not None else ''

            us_price_elem = product.find('.//Price[CurrencyCode="USD"]')
            book['US Price'] = us_price_elem.find('PriceAmount').text if us_price_elem is not None else ''

            ca_price_elem = product.find('.//Price[CurrencyCode="CAD"]')
            book['CA Price'] = ca_price_elem.find('PriceAmount').text if ca_price_elem is not None else ''

            on_sale_date_elem = product.find('.//OnSaleDate')
            book['On Sale Date'] = on_sale_date_elem.text if on_sale_date_elem is not None else ''

            audio_run_time_elem = product.find('.//ExtentValue')
            book['Audio Run Time'] = audio_run_time_elem.text if audio_run_time_elem is not None else ''

            bisac_elem = product.find('.//BASICMainSubject')
            book['BISAC'] = bisac_elem.text if bisac_elem is not None else ''

            language_elem = product.find('.//LanguageCode')
            book['Language'] = language_elem.text if language_elem is not None else ''

            # Add the book to the list
            books.append(book)

# Convert the list of books into a pandas DataFrame
df = pd.DataFrame(books)

# Load BISAC code mapping from CSV
bisac_df = pd.read_csv('bisac.csv', header=None, names=['BISAC', 'Subject'])

# Add two new columns for primary and secondary categories
bisac_df['Primary Category'] = None
bisac_df['Secondary Category'] = None

# Iterate over the DataFrame rows
for i, row in bisac_df.iterrows():
    # Split the 'Subject' into parts
    parts = row['Subject'].split(' / ')

    # Assign the parts to the appropriate columns
    bisac_df.at[i, 'Primary Category'] = parts[0]
    if len(parts) > 1:
        bisac_df.at[i, 'Secondary Category'] = parts[1]

# Drop the now redundant Subject column
bisac_df.drop('Subject', axis=1, inplace=True)

# Merge the two dataframes on the BISAC code column
df = pd.merge(df, bisac_df, on='BISAC', how='left')

# Write the DataFrame to an Excel file
df.to_excel('audiobook_metadata.xlsx', index=False)
