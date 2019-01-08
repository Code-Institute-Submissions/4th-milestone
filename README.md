# Sweet Poems

For my fourth milestone project, I decided to create a poembook wesbite, where users can view list of poems, and add their own work too. they can do this by adding a genre and then adding a poem to the website
 
## UX
 

- As a user, I want to read poetry.
- As a user, I want to have a site that will give a list of poems
- As a user, I want the option to add a genre and my own poetry if possible.
- As a user, I want the design to be clean and straightforward.
- As a user, I want the font to be large enough so that it can be readable. 


## Technologies Used

- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/default.asp)
- [Python](https://www.python.org/)
- [materializecss](https://materializecss.com//)
- [Jinja2](http://jinja.pocoo.org/docs/2.10/)

## Testing

1) Home pages will show list of poems

2) To add a poem:
- Click on new poem
- Choose genre
- Fill out form
- Click add poem

A new poem should appear on homepage.

3) Click Manage Genres on nav bar to add a new genre

4) Click Manage Poems to edit or delete poems.

5) Got to footer to access links to other poem sites.

## Deployment

How to deploy to Heroku:

First, create a new Heroku account and create new app. Then type the following into terminal:

- $heroku 
- $heroku login
- $heroku apps
- $git remote -v
- $git remote add heroku https://github.com/ainedoyle/4th-milestone
- $git push -u heroku master
- $sudo pip3 freeze --local > requirements.txt
- $echo web: python run.py > Procfile
Deployed at: https://fourth-milestone-project.herokuapp.com/

## Credits


### Content

https://www.poems4free.com/


### Acknowledgements

- I received inspiration for this project from X

Code Institute 

Udemy

Poems4Free