# Audiobook XML Parser

This readme provides an overview of an Audiobook XML Parser, a script that extracts relevant data from an XML file representing audiobook metadata and exports it to an Excel spreadsheet. Additionally, it provides instructions on how to upload the generated Excel file to Google Drive.

### Features

- Parses XML files containing audiobook metadata.
- Extracts relevant data such as book title, author, duration, and description.
- Outputs the extracted data to an Excel spreadsheet for easy viewing and manipulation.
- Supports uploading the generated Excel file to Google Drive for convenient storage and sharing.

### Prerequisites

To run the Audiobook XML Parser, ensure that you have the following:

1. Python: The script is written in Python, so you need to have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Required Libraries: Install the necessary Python libraries by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This command will install the required libraries specified in the `requirements.txt` file.

3. Google Drive API Setup:
   - Enable the Google Drive API and create credentials for your project. Follow the instructions in the Google Drive API documentation to set up the API: [https://developers.google.com/drive](https://developers.google.com/drive)
   - Download the credentials file in JSON format.

### Usage

1. Place the Audiobook XML Parser script in the same directory as your XML file.

2. Rename your XML file to `audiobook.xml` or modify the script to reflect your XML file's name.

3. Replace `credentials.json` in the script with the path to your downloaded Google Drive API credentials JSON file.

4. Run the script using the following command:

   ```
   python audiobook_xml_parser.py
   ```

5. The script will process the XML file, extract the relevant data, and generate an Excel file named `audiobook_metadata.xlsx` in the same directory.

6. Optionally, if you want to upload the generated Excel file to Google Drive, provide a Google Drive folder ID or modify the script to specify the destination folder. Then uncomment the relevant lines in the script.

7. Re-run the script to upload the Excel file to Google Drive.

### Customization

You can modify the script according to your specific requirements. Some potential customizations include:

- Changing the XML file name or location.
- Modifying the extracted data fields.
- Adjusting the Excel output format.
- Adding error handling or logging.

### License

This Audiobook XML Parser is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute it according to the terms of the license.

### Disclaimer

The Audiobook XML Parser is provided as-is without any warranty. Use it at your own risk. The author is not responsible for any damages or losses arising from its use.

### Credits

This script was created by Sean Wang. If you have any questions or suggestions, please contact Sean Wang at seanshaochenwang@gmail.com.
