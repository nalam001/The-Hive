# The-Hive
Software Engineering Project - Active Teaming System

Contributors - Team C: Alexandria Guo, Linda Wong, Michael Mayaguari, Niharika Alam

A collaborative project for CSC 32200, taught by Professor Jie Wei. This system, named *The Hive*, is built using Python, tkinter, and MySQL.

## Running the Project
#### Requirements
[Python](https://www.python.org/downloads/)

You must have pip from python3 installed and the *Pretty Table Library:* using the following snippet:
```bash
$ pip install PrettyTable
```
[MySQL](https://dev.mysql.com/downloads/)

#### Database Setup
On MySQL Workbench run TheHive.sql and TheHive_POPULATE.sql files. This will create and populate the database so that the project can be tested.

In db.py, change the information to connect to the database to your local server (host, user, and passwd).
![image](https://user-images.githubusercontent.com/44476083/81892560-67023200-9579-11ea-8763-2f9c209dc3ea.png)

#### To Run:
Clone the repository:

```bash
$ git clone https://github.com/mgmayagu/The-Hive.git
```

cd into the respository:
```bash
$ cd The-Hive
```

run the program by:
```bash
$ python visitor.py
```
#### Notes:
* Sample users and projects have been populated into the database if the instructions above have been followed. 
* To run through and navigate the system, login through one of the three types of users (each type has there only page and features listed below).
* To test out registration, input your own email to recieve email (registration will still go through but the status email it will bounce)

## Useful Documents:
Project Specifications: [System features](http://www-cs.engr.ccny.cuny.edu/~csjie/322/s20/spec_s20.docx)

Phase 1: [Spec Report](https://github.com/mgmayagu/The-Hive/blob/master/Reports/Spec%20Report%20-%20Team%20C.pdf)

Phase 2: [Design Report](https://github.com/mgmayagu/The-Hive/blob/master/Reports/Spec%20Report%20-%20Team%20C.pdf)

Phase 3: [Final Report](https://github.com/mgmayagu/The-Hive/blob/master/Reports/Final%20Report%20-%20Team%20C.pdf)

## Screenshots
Landing Page (Visitor)
![image](https://user-images.githubusercontent.com/44476083/81894818-c1ea5800-957e-11ea-95bf-fb85222d505e.png)

OU Page
![image](https://user-images.githubusercontent.com/44476083/81895236-cb27f480-957f-11ea-9d75-9c090cd07417.png)

VIP Page
![image](https://user-images.githubusercontent.com/44476083/81895408-1c37e880-9580-11ea-8f6c-9e863acd46e0.png)

SU Page
![image](https://user-images.githubusercontent.com/44476083/81895477-412c5b80-9580-11ea-9374-110a167ef333.png)

Group Page
![image](https://user-images.githubusercontent.com/44476083/81895745-fe1eb800-9580-11ea-8d9d-3f3b3f2c4cf2.png)

## Project Specifications
### Purpose

This system will facilitate active teaming of people with similar interest and skill-set to forge groups for a certain do-good project.

### Type of users:
*	visitor: no need to login, just surf around
*	ordinary user (OU): all self registered users who are approved by SU, need login
*	VIP: OUs whose reputation scores exceed a threshold set by SU
*	super-user (SU): one founding SU who initializes the system; one democratic SU who is voted by VIPs

### System features:
*	For a random visitor, the system provide a GUI showcasing the top 3 rated projects and top rating OU profiles and SU profiles to showcase the power of the system. A visitor can surf around to find more OUs/VIPs and projects 
*	Give visitor an option to register to be OU: the visitor has to fill in basic personal information such as name, email address, interest, credential and reference who are already an OU or VIP of the system. One SU will check these info to either approve or reject. If approved, the SU will send an email with account id and password, when the new OU first login, s/he is required to change the password. If rejected, the applicant has one chance to appeal and the SU will make a final decision to reverse the rejection: if still reject, then this visitor will be put in blacklist forever. The approved OU will receive an initial reputation score by the reference: an OU can give a score 0-10; a VIP can give score 0-20.
*	OUs can form groups by inviting other OU(s) for a certain purpose: the other OUs can accept or reject the invite. If reject, the OU should respond by the reason. An OU can put some OUs to his/her white-box: accept all invites or black-box: reject all invites with automatic message. For instance, the group could be some students taking 32200 as a study group. 
*	Once a group is formed, a group web-page should be made available that is accessible to all group members: some information is public to be browsed by visitors and other OUs, some could be set as private to the group members only such as evaluations and warnings. All group members can moderate and post to the group page. This page will be used for posting updates and scheduling meet-ups.
*	Any group member can ask for a meet-up polling to find common time for all members to meet. Once all members responded, the time slot with the most votes will be chosen. If a member has missed scheduled meeting twice, s/he will receive a warning. The voted out member can appeal to the SU to possibly change the reputation scores. Each group member should have a track record for the number of assigned tasks that have been done, which is the foundation for the group warnings and the appeals of the affected group member(s).
*	The group members can vote to issue a warning or a praise to a group member, the vote must be unanimous. A member receiving 3 warnings will be automatically removed from the group and get a 5 point reputation score deduction. The group can also vote to kick out a member directly, the member will be removed from the group and receives 10 point reputation score deduction. An OU with negative reputation score will be removed from the system and put into black-list automatically.
*	The group members can vote to close the group, and conduct an exit evaluation to other members. Each member will receive the median reputation score given by all other members. And every member can decide if s/he is willing to put the other member to her/his white-box or black-box afterwards and why. After group closure, the SU will assign a VIP to evaluate the group and determine a reputation score for the entire group to be added/deducted for all members involved. The system will keep a ranking list of finished groups to be showcased.
*	An OU whose reputation score is higher than 30 will be promoted to VIP; and a VIP whose score is lower than 25 will be demoted. All VIPs can vote one VIP as the democratic SU. 
*	Visitors and OUs can complain to SU about a group or other OUs, the SU will decide if the complaint merit action. The SU can decide to shut down the group or OU and punish all involved by a certain score deduction or even kick them out from the entire system.
*	OUs who are kicked out will have the final chance to login and do some final processing and will be unable to login ever after.
*	The entire system keep a list of taboo word list, any message by any OU with these taboo word will be converted to *** automatically and the OU’s reputation score will be decreased by 1: if s/he uses the same word again later, his/her reputation score will be decreased by 5.
*	OUs can send compliment about other OUs to SU, and SU will increase the reputation score of the complimented OU, any OU receiving 3 compliments, regardless of the reputation score.

### Other system requirements:
*	A consistent system GUI is required: don’t keep popping up new windows to cause a mess
*	Besides the foregoing items, each team can have a creative feature for this system, which is worth 10% of the project. A feature deemed extremely creative will receive an up to 10% bonus by discretion.
*	No need to make this system web based or mobile based, the latter two can be viewed as a creative feature if your team choose to do so.
*	For details not listed in the foregoing items your team is free to use your own judgment to proceed in your system design and development.
