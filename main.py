import csv
from operator import itemgetter

# function that inputs information for transactions.csv
# NOTE: this function is not used in the program but is here if you want to populate the csv file through the command line
def write_csv(filename):
    # open file in write mode
    with open(filename, 'w') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow(["payer", "points", "timestamp"])

        # write multiple rows given user input
        while True:
            payer = input("Enter payer: ")
            points = input("Enter points: ")
            timestamp = input("Enter timestamp: ")
            writer.writerow([payer, points, timestamp])
            if input("Continue? (y/n): ") == 'n':
                break
        
# Read transactions from CSV file skipping the first row
def read_csv(filename):
    transactions = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        # skips the header row
        next(reader)
        for row in reader:
            transactions.append(row)
    return transactions

# Print transactions in CSV format
# NOTE: this function is not used in the program but is here if you want to print the csv file
def print_csv(transactions):
    for row in transactions:
        print(','.join(row))

# function to spend points and adjust balances using the given contraints
def spend_points(amount, transactions):
    # Sort transactions by timestamp
    transactions = sorted(transactions, key=itemgetter(2))

    # copy transaction to a 2d list 
    transactions_copy = transactions.copy()

    # spend points based on timestamp spending the oldest points first
    for i in range(len(transactions_copy)):
        transactions_copy[i][1] = int(transactions_copy[i][1])
        if transactions_copy[i][1] > 0 and amount > 0:
            if amount <= transactions_copy[i][1]:
                transactions_copy[i][1] -= amount
                amount = 0
                break
            else:
                amount -= transactions_copy[i][1]
                transactions_copy[i][1] = 0

    # if there are any negative balances, adjust them to positive balances
    for i in range(len(transactions_copy)):
        transactions_copy[i][1] = int(transactions_copy[i][1])
        if (transactions_copy[i][1] < 0):
            j = 0
            flag = True
            while j < len(transactions_copy) and flag:
                if (transactions_copy[j][1] > 0):
                    if (transactions_copy[j][1] > abs(transactions_copy[i][1])):
                        transactions_copy[j][1] += transactions_copy[i][1]
                        transactions_copy[i][1] = 0
                        flag = False
                    else:
                        transactions_copy[i][1] += transactions_copy[j][1]
                        transactions_copy[j][1] = 0
                j+=1

    # convert 2d list to dictionary with payer as key and points as value
    res = {}
    for i in range(len(transactions_copy)):
        toadd = {transactions_copy[i][0]: int(transactions_copy[i][1])}
        res.update(toadd)

    # display the final balances
    print(res)
    
# main function to run the program
if __name__ == '__main__':
    transactions = read_csv('transactions.csv')
    # NOTE: if you want to populate the csv file through the command line, uncomment the following lines
    # input amount of points to spend
    # populate = input("Populate transactions.csv? (y/n): ")
    # if populate == 'y':
    #     write_csv('transactions.csv')
    amount = int(input("Enter amount of points to spend: "))
    spend_points(amount, transactions)
