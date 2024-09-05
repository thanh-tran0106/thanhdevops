# Cat Shelter Website

## Project Introduction

This personal project is designed to enhance my DevOps skills by creating a comprehensive cat shelter website. Inspired by my passion for cats, the website serves as a centralized platform for managing and displaying information about cats in the shelter. Users can access details such as name, breed, age, coloration, and medical records of cats. 

Users can create accounts to become members of the shelter, log in, and utilize various features. The website also includes a section called “I've Found a Pet” for users to report cats in need of assistance.

### Future Enhancements

In future versions, the website will integrate advanced AI capabilities to:
- Analyze data on cats and users for more effective matching between potential adopters and cats.
- Notify users via email about cats that may be well-suited for adoption based on their preferences and the cats’ profiles.

## Author

- **Thanh Tran**

## Technology Used

- **Frontend:** Nginx, HTML, CSS, JavaScript
- **Backend:** Django
- **Database:** PostgreSQL
- **Virtualization:** UTM, AWS

## System Architecture
![System Architecture](https://github.com/thanh-tran0106/thanhdevops/blob/master/system_architecture.drawio.png?raw=true))

1. **Frontend**
    - **Nginx**
        - Handles and serves static assets
        - Acts as a reverse proxy to forward user requests to the backend server (Django)
        - Manages SSL/TLS encryption for HTTPS connections

2. **Backend**
    - **Django**
        - Processes user requests, handles data processing and application workflows
        - Manages database interactions
        - Handles user accounts, registration, login, and permissions
        - Renders HTML templates for various parts of the site, including cat details and user profiles

3. **Database**
    - **PostgreSQL**
        - Stores structured data related to the cat shelter, including cat information, user accounts, and found pet records
        - Handles queries and transactions for efficient data access and updates
        - Maintains database schema to support various data types and relationships

## Installation

### Local Setup (VMs)

**Created 2 virtual machines:**

- **VM 1:** Nginx and PostgreSQL
- **VM 2:** Django Server and Django Storage


### AWS Deployment (EC2 Instances)

Deployment involves the following EC2 instances:

- **EC2 Instance 1:** Nginx and PostgreSQL and Django storage
- **EC2 Instance 2:** Django Server
![Environment Setup](https://github.com/thanh-tran0106/thanhdevops/blob/master/environment_setup.drawio.png?raw=true)

## Application Structure

- **Application Architecture Diagram**
- **User Flow Diagram**
![User_Flow](https://github.com/thanh-tran0106/thanhdevops/blob/master/user_flow.drawio.png?raw=true)
- **Entity-Relationship Diagram (ERD)**







![Database_Diagram](https://github.com/thanh-tran0106/thanhdevops/blob/master/database_diagram.drawio-2.png?raw=true))

 To learn more about the process of how I created the database, you can read my LinkedIn article at the link below.
https://www.linkedin.com/pulse/postgresql-learning-diary-thanh-tran-qvwgf/?trackingId=sGVfI20nQ%2FuYyuIXnFkQHw%3D%3D


### Code Explanation

## Project Status 🚧

**This project is currently under active development and editing.** We are continually working on updates and improvements. Please check back regularly for the latest changes and updates.







