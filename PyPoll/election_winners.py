import os
import csv

election_data_csv = os.path.join("Resources","election_data.csv")

#Set vote counter
total_votes=0
candidate1_votes=0
candidate1_results={"Charles Casper Stockham": candidate1_votes}
candidate2_votes=0
candidate2_results={"Diana DeGette": candidate2_votes}
candidate3_votes=0
candidate3_results={"Raymon Anthony Doane": candidate3_votes}

#Open and read csv file:
with open(election_data_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")

    #Read the header row first
    csv_header=next(csv_file)
    print(f"Header:{csv_header}")

    #Print opening lines
    print("Election Results")
    print("------------------")

    #Read each row in csv file
    for row in csv_reader:

        #Count total number of votes
        total_votes+=1

        #Count each candidate's votes
        if row[2]=="Charles Casper Stockham":
            candidate1_votes+=1
            candidate1_results["Charles Casper Stockham"]=candidate1_votes

        if row[2]=="Diana DeGette":
            candidate2_votes+=1
            candidate2_results["Diana DeGette"]=candidate2_votes
        
        if row[2]=="Raymon Anthony Doane":
            candidate3_votes+=1
            candidate3_results["Raymon Anthony Doane"]=candidate3_votes

    #Calculate each candidate's percentage of votes rounded to 3 decimals
    candidate1_percent=round(candidate1_results["Charles Casper Stockham"]/total_votes*100,3)
    candidate2_percent=round(candidate2_results["Diana DeGette"]/total_votes*100,3)
    candidate3_percent=round(candidate3_results["Raymon Anthony Doane"]/total_votes*100,3)

    #Print results to terminal
    print(f"Total Votes: {str(total_votes)}")
    print("------------------")
    print(f"Charles Casper Stocham: {str(candidate1_percent)}%")
    print(candidate1_results["Charles Casper Stockham"])
    print(f"Diana DeGette: {str(candidate2_percent)}%")
    print(candidate2_results["Diana DeGette"])
    print(f"Raymon Anthony Doane: {str(candidate3_percent)}%")
    print(candidate3_results["Raymon Anthony Doane"])
    print("------------------")
    print("Winnner: Diana DeGette")

    #Print results to text file
    with open("election_data_results.txt","w") as file:
        file.write(f"Total Votes: {str(total_votes)}\n")
        file.write("------------------\n")
        file.write(f"Charles Casper Stocham: {str(candidate1_percent)}%\n")
        file.write(str(candidate1_results["Charles Casper Stockham"]))
        file.write(f"Diana DeGette: {str(candidate2_percent)}%\n")
        file.write(str(candidate2_results["Diana DeGette"]))
        file.write(f"Raymon Anthony Doane: {str(candidate3_percent)}%\n")
        file.write(str(candidate3_results["Raymon Anthony Doane"]))
        file.write("------------------\n")
        file.write("Winnner: Diana DeGette\n")