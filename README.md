# CSV Loader

The CSV Loader program is designed to load data from a CSV file into a dictionary. It removes the first key-value pair from the dictionary and returns the resulting dictionary.

## Usage

1. Ensure you have Python installed on your system.

2. Clone this repository or download the `csv_loader.py` file.

3. Install the required dependencies by running the following command:
    pip install csv

4. Prepare your CSV file with the data you want to load. The FIRST ROW MUST contain all the attributes and it will not be added to the dictionary. The first column will be used as the key for the dictionary.

5. Create a JSON config file (`config.json`) that contains the path to your CSV file. The JSON file should have the following structure:
```json
{
    "csv_file_path": "C:\\path\\to\\your\\csv\\file.csv"
}
```
Replace "C:\\path\\to\\your\\csv\\file.csv" with the actual path to your CSV file.

6. Run the csv_loader.py script using the following command:
    python csv_loader.py

7. The program will process the CSV file and fill the dictionary with the information contained in the given CSV file.

Dependencies
    - csv