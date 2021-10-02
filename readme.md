# Welcome to Stream Game Over New World Bot (SGO-NW)

## Legal and Disclaimer:

**THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.**

This bot will only store the following **public** user data: 

- User's discord public nickname.

## How to set up: 

- Clone the repository.
- install the dependencies: 
  - python3 (3.8 or higher)
  - dotenv
  - colorama
  - discord
- Add environment_variable *DISCORD_TOKEN* with the bot token
- exceute **SGO_DiscordBot_NW.py**
- Happy botting.

### Tips for setting the server: 

Under linux machines as a host you can use *screen* to have your application running 24/7. 

### usage

```
$ screen
$ python3 yourApp.py
```

Then use:

- `ctrl+A + D` to detach the screen and let the application running. (you can safely close any ssh connection)
- `screen -r` to attach again the bot terminal
- `ctrl+A + K` To kill the screen process and end the bot.

## Bot commands: 

**Disclaimer** : Names with spaces will be concatenated using   *_*   . Example: *Red hat* --> *Red_hat* 

### Request 

.request (.r) [amount] [item]: adds a new request entry, if the user already had requested one, the amount gets overriden

#### usage 

```
.r 150 Shrimps
```

```
.r 19 Blue Mushrooms
```



### Deliver Request

.deliverRequest (.dr) [ammount] [item] [requester] : delivers the amount of items to the person who requested it. It will update the remaning value or will remove the request if it has been fullfilled.

#### usage 

```
.dr 75 Shrimps UserName
```

```
.dr 4 Blue_Mushrooms UserName
```

**Note the underscore concatenating Blue and Mushrooms**

### Clear Request

.closeRequest (.cr) [item] : fully removes a request from the user for a given item

#### usage

```
.cr Shrimps
```

### Close All Requests

.closeAllRequest (.car) : Removes all the request by made the requester.

#### usage

```
.cr_all
```

### List Requests

.listRequests (.lr) [OPTIONAL item/username] List either all the requests or the request for a given item or username if specified.

#### usage

```
.lr
```

```
.lr Shrimps
```



### Help

.man (.h) list all the commands that can be perform  by this bot.

#### usage

```
.man
```



### backup

..backup (.bu): gets a .csv file with the current data stored in the bot.

#### usage

```
.bu
```



### recover

.recover (.rc) [Optional : last]: Either recovers the status from the previous session or recovers from the last command given.

#### usage

```
.recover
```

```
.recover last
```





