
# Project 9: Azure SQL Database
Due: _________ at 11:59 PM <br>
Points: __________


## Introduction:
Now we are going to be connecting our webserver and Python scripts to a cloud database! Specifically, we are going to be using Microsoft Azure SQL Database. Our goal for this module is to create a Microsoft Azure server, create an SQL database, and connect our app to this database to store our sensor readings. Once we have completed this module you will be able to view all of our readings and query the database to perform an analysis of the readings.

<br><br>


## Microsoft Azure:

Microsoft Azure is a cloud computing service created by Microsoft for building, testing, deploying, and managing applications and services through Microsoft-managed data centers. It provides a range of cloud services, including those for computing, analytics, storage, and networking. Users can pick and choose from these services to develop and scale new applications, or run existing applications, in the public cloud. Azure offers solutions for all industries through a comprehensive set of compliant offerings, integrated tools, DevOps, and a marketplace for building any application.

### Azure SQL Database:
On Microsoft Azure, we will be specifically using the SQL database. Microsoft Azure SQL Database is a fully managed relational cloud database service that provides SQL Server engine compatibility with built-in intelligence. It offers a scalable service that can handle large amounts of data and a wide range of transactional processing workloads. Azure SQL Database is designed to make managing and scaling applications easier with features like high availability, security, and recovery built into the service. It's suitable for a variety of applications, from small projects to large-scale enterprise use and will be perfect for our project.

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
- **Step 11**: Under your servers network settings you can either allow public access or set up a private endpoint to connect to the server. We chose to allow public access.
- **Step 12**: To accomplish this under the networking settings -> public access, select 'selected networks' for the public access option.
- **Step 13**: Now you must add a firewall rule with your network's ip address as the start and end ip to allow access.
- **Step 14**: Save these settings and go back to the home of the Azure Portal

Now we should have created a server to host our SQL database with the proper networking settings to allow access from our machine. If you accomplished this successfully, it is time to create the table and start to connect our python app to the database!


[docs]: https://learn.microsoft.com/en-us/azure/?product=popular
[tut]:https://learn.microsoft.com/en-us/azure/azure-sql/database/single-database-create-quickstart?view=azuresql&tabs=azure-portal
[portal]:https://portal.azure.com/#home






















