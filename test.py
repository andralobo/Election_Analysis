counties = ["Arapahoe","Denver","Jefferson"]


##print jefferson
print(counties[2])

## or 
counties[2]


##f find length
len(counties)

## slice list
counties[0:2]

## ouput last 2
counties[1:3]
    ##or 
counties[1:]

## add to list

counties.append("El Paso")

##inster in 2nd spot
counties.insert(2, "El Paso")




# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")