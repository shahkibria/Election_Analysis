voting_data = [{"County":"Arapahoe","Registered Voter": 422829},{"County":"Denver","Registered Voter":463353},{"County":"Jefferson","Registered Voter":432438}]
for x in voting_data:
    print(x['County']+ " County has "+ str(x["Registered Voter"])+" Registered Voters.")

