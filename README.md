# ZCRUDWebsite
# The website starts by adding in names, IDs, and points to the database and has 4 ways to edit it / utilize it
# Create User: 
# All inputs must be filled (no blanks) and then it adds the user to the database with their ID and points for a change to occur. The ID and points must also be integers.
# Duplicate names, IDs and points are allowed in the database
# Find User:
# The input is some name that might be in the database. If the user is not in the database, the website returns a prompt saying that, and if they exist, the website gives their ID and points as well
# Update User:
# The input is some name that might be in the database, an ID, and points. The ID and points must also be integers. All inputs must be filled or else no changes will happen. After the criteria is complete, by pressing the button the database updates all users with that name to have a newly set ID and points value.
# Remove User
# The input is some name that might be in the database. All users with that name are removed from the database
# The database: 
# When I created CRUDDatabase, it didn't create a .db file in the folder but instead a .file . But the database still updates when I run INSERT, UPDATE and DELETE commands
