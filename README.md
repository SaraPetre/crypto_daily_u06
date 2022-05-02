# ![](https://i.imgur.com/vV68Gs6.png)

>## u06 Soloproject DOE21, Chas Academy
Develop an application to get the top10 crypto coins from API downloaded to a Sqlite database, select the data wanted and send a report by MailHog. The project is developed in Python.

A solo project with 4 moment. 
- Planning, 1 week
- sprint 1, 3 weeks
- handover, 1 week. 
- sprint 2, 3 veeks

After working solo with this project "It´s all about crypto now!" I hand over this project to one of my school team member. This person gets a handover by me and then continue this application according to the planning. Find the planning document down below.
## Files & folders in this repository
- README.md
- .gitignore
- .gitlab.yml
- Dockerfile
- docker-compose.yaml
- maildir/
- requirements.txt
- src/
    - aras_all_in_one_.py
    - user_choice_api.py

## To-do on handover
- "Fork" this repository.
- Read this README.md
- Do the installation needed to run the application. Please see "Installation" dow below.
- Continue the work according to the plan for sprint 1 in the down below document:
https://docs.google.com/document/d/16sWO6KkhfXqQ3EMUyhdAViWXFmrrSJecTuYik7u4_lA/edit

## Repository
https://gitlab.com/SaraPetre/crypto_daily_u06

## Planning
https://docs.google.com/document/d/16sWO6KkhfXqQ3EMUyhdAViWXFmrrSJecTuYik7u4_lA/edit

### Technologies Used

<img align="left" alt="Docker" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/docker/docker.png" />

<img align="left" alt="Python" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />

<img class="logo"  src="images/sqlite370_banner.gif" alt="SQLite" width="26px" border="0" />

<img src="images/hog.png" height="20" alt="MailHog"/>
<br />
<br />


## Visuals- This is the report that ends up in MailHog

![](https://i.imgur.com/aEorryb.png)

## Installation
### Install the requirement with the following command in your terminal
>pip install -r requirements.txt
### Install browser for visual image of sqlite-Optional
https://sqlitebrowser.org/dl/
### Install Docker desktop - Needed
https://www.docker.com/products/docker-desktop/
### Start MailHog by Docker. Run in terminal:
>docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog

##### OR

### Run by starting from the Docker image, and Docker compose -file. You need to be in the same folder as the Docker and Docker Compose -files.

### If it is the first time
> docker-compose up -d --build
### Then you can use:
> docker-compose up -d

Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.
## Test by pipeline CI/CD in GitLab
There are code quality tests set up in the file:
> docker-compose.yaml

The tests done is:
> - pycodestyle
> - pylint 
> - flake8


## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
