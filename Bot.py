# Carbide Twitch Bot. This code was originally written by CultureCoder.
# Thanks to
# /r/LearnPython subreddit and IRC chat
# python.org documentation
# help.twitch.tv documentation

# Configuration
# Change the Channel to your main stream's channel. (e.g twitch.tv/carbidenetworks would become #carbidenetworks)
# Change the Nick to your bot's username.
# Change the Pass to your Twitch bot's oauth key, get it at twitchapps.com/tmi (remember to sign in as the bot account)
# Change the API Key to your Steam web API key. Get it at http://steamcommunity.com/dev/apikey. Use your Twitch URL as the URL.
# Change the Steam ID to your 64 Steam ID. Get it at http://steamid.co

CHANNEL = "#mychannel"
NICK = "mybotsusername" 
PASS = "oauth:xxxxxxxxxxxxxxx"
APIKEY = "xxxxxxxxxxxxx"
STEAMID = "xxxxxxxxxxxx"

#START
# Import modules we need
import socket, string, time, json, requests
print ("Carbide Twitch Chat Bot. Created by CultureCoder")
time.sleep(1)
print ("Contribute to the development at bitbucket.org/CultureCoder/carbidetwitchbot")
time.sleep(1)
print ("Initialising...")
time.sleep(3)
print ("Connecting to the Twitch IRC network. One moment...")
time.sleep(2)
# Leave these alone.
# Twitch IRC Network config
HOST = "irc.chat.twitch.tv"
PORT = 6667



def send_message(message):
    s.send(bytes("PRIVMSG #" + NICK + " :" + message + "\r\n", "UTF-8"))
# Connect to IRC
s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + NICK + " \r\n", "UTF-8"))


while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        break 

while True:
    for line in str(s.recv(1024)).split('\\r\\n'):
        parts = line.split(':')
        if len(parts) < 3:
            continue

        if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = parts[2][:len(parts[2])]

        usernamesplit = parts[1].split("!")
        username = usernamesplit[0]
        
        r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + APIKEY + "&steamids=" + STEAMID)

        data = r.json()
        currentlyPlaying = (data['response']['players'][0]['gameextrainfo'])
        serverIP = (data['response']['players'][0]['gameserverip'])
        print(username + ": " + message)
        if message == "!ip":
            send_message("The current server's IP is " + serverIP)

