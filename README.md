## usage
1. edit code
2. push to github
3. since github is connected to Heroku, go to Heroku
4. Manual deploy at Heroku
5. it shall work
   

## Note
1. you need to have requirement.txt, Procfile and runtime.exe setting as here
2. go to Heroku to deploy and see log if any debug needed
3. if use negok `ngrok http 5002`

## webhook setting
1. Heroku: 
   https://python-line-bot-20191217.herokuapp.com/callback
2. ngrok
   `ngrok http 5002` and check what thr port forward


## if need to manual deploy to heroku
https://dashboard.heroku.com/apps/python-line-bot-20191217/deploy/github


## Ref
