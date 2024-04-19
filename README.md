# TE-Dashboard-EasyClone
by Marion Kazazi - Thousandeyes Adoption Engineer 

# Welcome to ThousandEyes Dashboard Easy-Clone 

On this Python Script We are trying to ease the process of Duplicating dashboard within and from different ThousandEyes Organizations 

# What this script can do:

Clone Dashboard from one account group to:
- another account group within the same organization 
- same account group 
- many account groups in the same time 
- one account group of different organization
- many account groups of a different organization 

# What this script cannot do
- If you are cloning to the Account Groups or Organizations that don't share the same TE Test, the dashboard will be cloned as Skeleton. 
- If you are Sharing the TE tests, the Dashboard will be fully cloned with all the tests added

# Along the main purpose this script can: 
- Find the OrgID of the account groups 
- Get Dashboard ID and details of the Specific Dashboard 

# What we need to have before running this script:
- Bearer token of the account who would like to get information of the dashboard (needed Admin account to avoid any problem getting Dashboard Details)
- Bearer token from the account who is Cloning the Dashboard (needed Admin Account to avoid any problem on pushing the Deploy)
- bearer Token can be found in TE platform --> User and Roles --> OAuth Bearer Token

# Steps to perform the script 

# Get Dashboard ID 
-  We run the script to get the AccountID which contain the dashboard 
-  Also to find the AccountID of the Users that we will push the Clone 
-  Bearer token is needed from those accounts or any admin account 

# Run get DashboardID
- We use this script to get the Dashboard ID that we need to clone 
- We would need the bearer token from the organization which contain the Dashboard
- If admin bearer is used no need to fill the Account Group ID (leave it empty and press enter on the script)

# Dashboard Easy Clone 
- We run this script to clone the dashboard once we have information from previous scripts 
- Input the token from the dashboard we would like to clone the dashboard 
- Input the dashboard ID 
- Add the bearer token of the new Org that we would like to clone the dashboard 
-  a- if within the same organization, use the same Token 
- Add the ORG ID that you would like to clone the Dashboard (if many please use comma ',')
- Successful Push will show you the results on the console but also on a file stored on the file 
- If you are ushing the script to many OrgID only the result of the last ORGID added will be shown 

# Things to be aware
Some Widgets that are not updated, not anymore available on TE dashboard can fail the cloning. However the error will direct you to the object/widget that need to be updated or removed in order to make a successful clone.
After pushing this command on the Project folder will be created some files containing data about all the processes where you can get more valuable information!

Enjoy :) 


