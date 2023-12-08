
# Project 9: Azure SQL Database
Due: _________ at 11:59 PM <br>
Points: __________


## Introduction:
Now we are going to be connecting our webserver and Python scripts to a cloud database! Specifically, we are going to be using Microsoft Azure SQL Database. Our goal for this module is to create a Microsoft Azure server, create an SQL database, and connect our app to this database to store our sensor readings. Once we have completed this module you will be able to view all of our readings and query the database to perform an analysis of the readings.

<br><br>


## Microsoft Azure:

Microsoft Azure is a cloud computing service created by Microsoft for building, testing, deploying, and managing applications and services through Microsoft-managed data centers. It provides a range of cloud services, including those for computing, analytics, storage, and networking. Users can pick and choose from these services to develop and scale new applications, or run existing applications, in the public cloud. Azure offers solutions for all industries through a comprehensive set of compliant offerings, integrated tools, DevOps, and a marketplace for building any application.

### Azure SQL Database:
On Microsoft Azure, we will be specifically using the SQL database. Microsoft Azure SQL Database is a fully managed relational cloud database service that provides SQL Server engine compatibility with built-in intelligence. It offers a scalable service that can handle large amounts of data and a wide range of transactional processing workloads. Azure SQL Database is designed to make managing and scaling applications easier with features like high availability, security, and recovery built into the service. It's suitable for a variety of applications, from small projects to large-scale enterprise use, and will be perfect for our project.

### Creating the Azure Server and Database:

When creating your database there are many different options you can choose from in terms of pricing, connectivity, storage, usage, etc. So be sure to check the latest [documentation][docs] to achieve your desired results. But, we will provide a loose guide for how we accomplished this. Here is also a [tutorial][tut] from Microsoft.

- **Step 1**: Navigate to the Azure [Portal][portal] and make an account.
- **Step 2**: Sign up for a subscription based on your specific needs (free trial, basic, developer, etc.)
- **Step 3**: After you have created your account and have the appropriate subscription you need to create a resource group for your server and database. Make sure this has a unique name for your needs
- **Step 4**: Create an SQL server. This option will be under the 'Create a resource' option. 
- **Step 5**: Assign an authentication method: You will use this server to host your database so when assigning an authentication method make sure you make a note of the SQL admin name and password or the Microsoft Entra information. You can choose to allow access via SQL authentication, Microsoft entra, or both. NOTE: For implementation, we used the SQL Admin login information
- **Step 6**: Assign your server to the resource group you made, give it a name, and create it.
- **Step 7**: Create an SQL Database under the create a resource option
- **Step 8**: For this database assign it a unique name and assign it to your current subscription plan, the server we just created, and the resource group we created.
- **Step 9**: When creating the database you can choose the storage setting and workload environment you need for your specific needs. We chose developer workload and general storage.
- **Step 10**: Now that we have created our database and server we need to edit the networking settings of our server to allow connectivity.
- **Step 11**: Under your server's network settings you can either allow public access or set up a private endpoint to connect to the server. We chose to allow public access.
- **Step 12**: To accomplish this under the networking settings -> public access, select 'selected networks' for the public access option.
- **Step 13**: Now you must add a firewall rule with your network's IP address as the start and end IP to allow access.
- **Step 14**: Save these settings and go back to the home of the Azure Portal

Now we should have created a server to host our SQL database with the proper networking settings to allow access from our machine. If you accomplished this successfully, it is time to create the table and start to connect our Python app to the database!

- **Step 15**: Navigate to your SQL Database
- **Step 16**: Navigate to 'Query Editor'
- **Step 17**: Run the following query to create the table (you can change the table name if you want) NOTE: If you ran into trouble while editing the networking/connectivity settings of the server or database you may not have access to create the table. Refer to documentation [here][connect] 
   <br><br>CREATE TABLE SensorReadings (
      ReadingID INT IDENTITY(1,1) PRIMARY KEY,
      AirTemperature FLOAT, WaterTemperature FLOAT,
      Humidity FLOAT,
      Timestamp DATETIME DEFAULT GETDATE()
  );<br><br>

Now it is time to go back to our Python app and connect it to the database.
<br>

## Connecting the Python Application to SQL Database
At this point, we should have a fully function Azure server and Azure SQL database. We must now adjust our app.py file to insert the readings into the database. This process involves three main tasks: software configuration, establishing a connection to the database, and querying the database.
<br>

### Software Configuration
We will be using Python's 'pyodbc' package to communicate with our database. To ensure our system has the necessary drivers to access this package and communicate with our SQL database you will need to run the following commands. NOTE: depending on your system and the versions of different package's on your system the commands may vary slightly be sure to refer to the official Microsoft documentation to run the correct commands. These commands are to act as a guide for you rather than the exact commands one may need to run. The following are the Ubuntu commands we used:

```
sudo apt-get update
pip install pyodbc
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc
curl https://packages.microsoft.com/config/debian/11/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
```
<br>
[documentation][installdocs]
<br>

### Connecting to the database
You must follow these steps to connect your Python app to the SQL database

- **Step 1**: Add 'import pyodbc' to your imports
- **Step 2**: Create a connection string  example:
conn_str = (
    "DRIVER={driver name};"
    "SERVER={server name}"
    "DATABASE={database name};"
    "UID={admin id}"
    "PWD={your password}"
  <br><br>
NOTE: You can find template connection strings for your database under the overview tab of your SQL database in the Azure portal
<br><br>
-**Step 3**:
  




[docs]: https://learn.microsoft.com/en-us/azure/?product=popular
[tut]:https://learn.microsoft.com/en-us/azure/azure-sql/database/single-database-create-quickstart?view=azuresql&tabs=azure-portal
[portal]:https://portal.azure.com/#home
[connect]:https://learn.microsoft.com/en-us/azure/azure-sql/database/connectivity-settings?view=azuresql&tabs=azure-portal
[installdocs]:https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=debian18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline#18























