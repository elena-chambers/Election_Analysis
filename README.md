# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections has given me the following tasks to complete the election audit of a recent local congressional election:

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote
6. Identify which counties participated in the election
7. Calcuate voter turnout by county  
8. Identify which county had the largest turnout

## Resouces
- Data Souce: election_results.csv
- Software: Python 3.8.8, Visual Studio Code, 1.60.2

## Election Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes
    - Diana DeGette received 73.8% of the votes and 272,892 number of votes
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the votes and 272,892 number of votes
- Three counties participated in this election: 
    - Jefferson County
    - Dever County
    - Arapahoe Counry
- Voter turnout by county:
    - Denver had the largest percentage of voters, accounting for 82.2% of votes with 306,055 votes
    - Jefferson accounted for 10.5% of voters with 38,855 votes
    - Arapahoe accounted for 6.7% of voters with 24,801 votes

Below are the figures that are produced from this script:
|Terminal Output            |  Text File Output |
|-------------------------|-------------------------|
|<img width="720" alt="Screen Shot 2021-10-17 at 5 35 03 PM" src="https://user-images.githubusercontent.com/91163155/137648069-a9ce4ee8-495c-4a0f-a093-48bf9add8468.png">  |  <img width="420" alt="Screen Shot 2021-10-17 at 5 18 50 PM" src="https://user-images.githubusercontent.com/91163155/137648077-4e9a430d-1a59-49e7-8e0e-90d4145bea78.png"> |







## Election Audit Summary

This script has the ability to perform detailed analysis of data stored in CSV files and produces results in both a straight-forward text file and printed in the command line. While the outputs may need additional modifications to be more appealing and intuitive, the script itself is able to handle large data volumes very quickly. To increase the use and scale of this script such that it could be used for any election, regaurdless of data volumes, it would be necceasy to build in data cleaning mechanisms that can deal with anomalies, and it would be useful to create functions that can be called to identify whether the data is sorted by city, township, county, state, etc. The hard-coded county variables would need to be more flexible, perhaps using user input via message boxes.

