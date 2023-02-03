# Abhinav Chinta - Fetch Coding Exercise

This repository contains code for the Fetch Coding Exercise - Software Engineering Internship

## Pre-requisites

- Python 3.6
- Git

## Installation
To clone this repository to your local system, follow these steps:

1. Open a terminal window.
2. Navigate to the directory where you want to store the repository.
3. Run the following command:

```
$ git clone https://github.com/abhinav-chinta/Abhinav-FetchOA.git
```

Once the repository has been cloned, navigate to the repository directory using the following command:

```
$ cd Abhinav-FetchOA
```

Once you are in the repository directory, you can run the following command to run the program:

```
$ python3 main.py
```

Once you run this command, you will be prompted to enter the amount of points you want to spend. Enter the amount and press enter. The program will then output the desired dictionary of payers and points based on the given constraints.

## Populating the CSV File
To populate the CSV file with data, follow these steps:

1. Open transactions.csv in a text editor.
2. Enter the data in the format specified in the instruction document.
3. Save the file.
4. For usability purposes, the CSV file has been populated with the default data provided in the instructions.

If you want to use the CSV file as input, follow the steps in the "Optional CSV Input Functionality" section.


## Optional CSV Input Functionality
There are 2 "NOTES" within the code that allow you to use a CSV file as input. If you want to use this functionality, follow these steps:

1. Open the main.py file in a text editor.
2. Uncomment the first "NOTE" by removing the "#" at the beginning of the line.
3. Comment out the second "NOTE" by adding a "#" at the beginning of the line.
4. Save the file.
5. Run the following command:

```
$ python3 main.py
```
You will then be prompted to enter the fields of the CSV file in the following order:

1. Payer
2. Points
3. Timestamp

Once you have entered all the fields, press enter. Following this the program will prompt you to either continue or enter another set of fields. If you want to enter another set of fields, enter "y" and press enter. If you want to stop entering fields, enter "n" and press enter. Once you have entered all the fields, the program will output the desired dictionary of payers and points based on the given constraints.

## Authors

- Abhinav Chinta

## License

This project is licensed under the MIT License - see the LICENSE.md file for details



