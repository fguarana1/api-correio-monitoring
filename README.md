# api-correio-monitoring
This repo monitors correio API and send e-mail to users if the correio-API has any downtime. 

It will e-mail Felipe, Marcelo, Sergio and Guilherme. 

It will break the process at 22 p.m 

It will only trigger if API request code <> 200

It will sleep for 1 hour if it triggers, otherwise it will monitor in each 5 minutes interval 
