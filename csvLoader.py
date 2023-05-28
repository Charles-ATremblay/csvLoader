#we want to extract the data from a csv file and put it into a dictionary.
#The dictionary will have the following format:
#key: the first element of the row
#value: the rest of the row
import csv
import json

def csvLoader(csvFilePath):
    #create a dictionary
    csvDict = {}
    #open the csv file
    with open(csvFilePath) as csvFile:
        #create a csv reader
        csvReader = csv.reader(csvFile, delimiter=',')
        #loop through the csv file
        for row in csvReader:
            #add the key and value to the dictionary
            csvDict[row[0]] = row[1:]
        
    #remove the first key-value pair of the dictionary
    firstKey = list(csvDict.keys())[0]
    del csvDict[firstKey]
    #return the dictionary
    return csvDict

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        config_dict = json.load(config_file)
    return config_dict


# Load the configuration from the JSON file
config_path = "config.json"
config = load_config(config_path)

# Get the CSV file path from the configuration
csv_file_path = config["csv_file_path"]

# Run the function using the CSV file path
csvDict = csvLoader(csv_file_path)

