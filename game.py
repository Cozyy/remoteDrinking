#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests
import random

import json 
from PIL import Image
import tkinter as tk
import tkinter.font as tkFont
import winsound
import sys
import os 
import subprocess
import webbrowser


# import wolframalpha

#---------------------- COZY -------------------------------
# CLIENT_ID = '19bd4855fecf4bd9958c1e34300a9740'
# CLIENT_SECRET = 'f01f5dad82e742959894a833c8f8c480'
#accessToken = 'BQC_vRkmSQOA_B3vCIR90dCaGMqHI0QGQsjW7_cI-Dfj4jj6wokBf8TszelUrCKySyKBuM4HnqDYmpp7SU6yGT7pYoO_icxJh2Fn1bEANTGp0hMST963IYuI0EF8-CKgfqjtMTnTuASHC_sKZxoC2gAi1eiU3mpKR0hDSA'
# refreshToken = 'AQCmlhGmfdiR1qEkHArga8rIALJheBwzA0lR_WG8CK6eydPxNJuXG0gIHj4mZRSsfd25SgL4daCszGiGpTTrW3HjLw8xA25MANYXrAOWCo3YdRLWq_G7AGDHWDGdnqtWYQ4'
# device = '9f0d204b2dd784cef0895f8b929e25e2f9a9f7fe'

# --------------------- PLINFA -----------------------------
#CLIENT_ID = '50704b2e6893445bbd6c72b5638940b5'# marc
CLIENT_ID = '19bd4855fecf4bd9958c1e34300a9740' #ludger
#CLIENT_SECRET = 'dc289d3676bc4baab1d997eb52678b34' #marc
CLIENT_SECRET = 'f01f5dad82e742959894a833c8f8c480'#ludger
#accessToken = 'BQCr-U6_rlTvqS2KKW02SbSTkgR98QQlG7CCknxi1qUdHxdsplHEAjnTXs3FTjBl19Uzgj67_YcawUJlJD0DtEik8C_u-vNGhQslXGxrqsLPHLxJd8tRmKSILmVPRFLXCDxbM6Fa9TvsjkfUQW5CPEQxdDk2L1by8x4E45K7Cz702A'
# refreshToken = 'AQAHng9BI73Q0vGrvYMcua8MwlppEbJMd1n1KwY8CSIAv_ART5WkakH3rLjjTZaXWxjMx7B9eo9CC80llKu1pDum9PuWybISrs_jzSZPAzB_GD2Zle72FNIxjrWXF1a-ARI' #marc 
refreshToken = 'AQCmlhGmfdiR1qEkHArga8rIALJheBwzA0lR_WG8CK6eydPxNJuXG0gIHj4mZRSsfd25SgL4daCszGiGpTTrW3HjLw8xA25MANYXrAOWCo3YdRLWq_G7AGDHWDGdnqtWYQ4' #ludger
# device = '9a6710ea3df552326233d390109540bd95b090e2' #marc
device = '9f0d204b2dd784cef0895f8b929e25e2f9a9f7fe'

#names
names = ["firstoverlord","Model","Rewe Roland","18cm","Pilsenberger","penny auf wish", "djstyler"]
acc_names = ["firstoverlord","Model","Rewe Roland","18cm","Pilsenberger","penny auf wish" ,"djstyler"]


actions = ["saufen","wasserfall","bombe","fingern"]

 
#signature songs
saufi = ('spotify:track:3IsASNnv8A9dS7GoZy1LY9', 78000)
verkaufen = ('spotify:track:3NXZKCnMY9I4neCpaHF906', 56000)
turbo = ('spotify:track:4k1OADTXVmuABulPYY9IIu', 30600) # turbo für Rewe Roland oder lieber für alle? :D
zuschuetten = ('spotify:track:3ZmMS1rktap3UuDqQdbaA6', 7500)
cozy = ('spotify:track:1H5VQuShs4qfwBXyHF0PeH',129000)
allewollenmichficken = ('spotify:track:7M4zWJmzuf8aZ2aEQUnzU3',64000)
shots = ('spotify:track:1V4jC0vJ5525lEF1bFgPX2',92000)
waterfall = ('spotify:track:4EqeYEXkNDwCmVAaSDp8Pp',0)
joana = ('spotify:track:5Tcyb48NB2vhQqh35oInkf', 55500)
kenning = ('spotify:track:75n8FqbBeBLW2jUzvjdjXV',7000)

# saufi = ["2m713Kjk2GYOeBxr7rnbr7", 0, 78000]
# verkaufen = ["5MaSmwBPafFh88zscUMRRx", 0, 56000]
ticking = ('spotify:track:7lNsWRIxEuFmQzxmmABP4C',0)
explosion = ('spotify:track:5QseJL10xWSeqv36RSFf1f',0)
gangnam = ('spotify:track:03UrZgTINDqvnUMbbIMhql',0)

name_songs = {"firstoverlord" : saufi, 
              "penny auf wish" : verkaufen, 
              "Rewe Roland" : turbo, 
              "18cm" : joana, 
              "Pilsenberger" : kenning, 
              "djstyler" : zuschuetten, 
              "Model" : allewollenmichficken,
              "alle" : shots}

name_pics = {"firstoverlord" : "nils.jpg", 
             "Rewe Roland" : "steven3.jpg", 
             "18cm" : "sandra.jpg", 
             "Pilsenberger" :"ludger.jpg", 
             "penny auf wish" : "tabea.jpg", 
             "djstyler" : "marc.jpg", 
             "Model" : "sara.jpg",
             "alle" : "alle.jpg",
             "wasserfall" :"wasserfall.jpg",
             "bombe" : "bombe.jpg"}

#curl -X "PUT" "https://api.spotify.com/v1/me/player/play" --data "{\"context_uri\":\"spotify:album:5ht7ItJgpBH7W6vJ5BqpPr\",\"offset\":{\"position\":5},\"position_ms\":0}" 
#-H "Accept: application/json" -H "Content-Type: application/json" 
#-H "Authorization: Bearer BQDP6m0nK7pUK9bNs69ZJPhz13Jw3uJnfO1SP_sv4_0C7_hCpl9oIsE0-w4y0znjIQMMCDFEAyxF4NwBOMv5VTvYzGZ7_DW8bX6MynWEGaRdIwYHbi9Hxo8AQOhw2hpGmWwFuq-9OwJj-O_pj2ey5IUu3EYru_cKIwkW0l5CWVJGxVBPUcR_dn-MbwEw9YK0ZqxhBPQ_2bC1kxzERABuzLBzz8HKc2HS8sTlTuXyP_yEHajeQ1rqyvxTelPAZyxgkdy2TdvTUSnjogLmpjY"


api = 'https://api.spotify.com/v1/me/'
pause = api + 'pause'
info_current_song = api + 'player'
#r=requests.put(url="https://api.spotify.com/v1/me/player/play",headers = headers)
#print(r.text)

#use get req in browser and update code then use this function to get desired pair of refresh token
# after this update refresh token on top of this document (cancer solution)
def get_acc_ref():
# Code Cozy:
  # get_req_for_code = 'https://accounts.spotify.com/de/authorize?client_id=19bd4855fecf4bd9958c1e34300a9740&redirect_uri=https:%2F%2Fwww.spotify.com%2Fde%2Fhome%2F&response_type=code&scope=user-read-private%20user-read-email%20user-read-recently-played%20user-read-playback-position%20user-modify-playback-state%20user-read-currently-playing%20user-read-playback-state'
   # now get refresh and authcode token via post request 
  # code = 'AQDAP-3QhmqxZE4JPGUHcv6iXcqSmoUuBIsQL-kl2WlGsQdnPtP0t1GxQ7Dq1I3ymdwNywt9E6BImJOgpxqeHbbSSxmylILnVJBEq7GqWR7KIlL0mvVucBE112UMDazUBe0LTNQ9TNWwNcjjKL4vsYz68Hzxx36JP5rqfqDfQnt92rUbVmVBNK1rUp8eT77Esu4VBn8VkQ-MEtKIaIWtpyiw_nc5mguxkrvAeQtWwJMlmBig7OgG1_PXliXcbuNE7Gpir-9x6qWIFDMXtSmHMwXyFJsmiobSeya6Gb7odXopNhyvrNTrvtI8VLzmrUXyI2IFOvAsIt7OkGM9qmeQlyLiYg7l2aEPQpvE_LEbCwjOzreG2Wv2xgRlmPJARcxBKiE9iyXb9q8CFSXFz_79GtYNUw'

# Code Plinfa:
  get_req_for_code = 'https://accounts.spotify.com/de/authorize?client_id=50704b2e6893445bbd6c72b5638940b5&redirect_uri=https:%2F%2Fwww.spotify.com%2Fde%2Fhome%2F&response_type=code&scope=user-read-private%20user-read-email%20user-read-recently-played%20user-read-playback-position%20user-modify-playback-state%20user-read-currently-playing%20user-read-playback-state'
  code = 'AQDKyjYI91fe34YZDUM7RkeENtvmKgHpnn7JyOBB_BCvbcq9FvuvftUkqj8075GcZYfUugRT2nAARtymXnR0QesN1Wb6HtKGCq6Fj58PgjuwxxwHGjQlEREgXH9OvT_cOTv9wBZ0K-kO78d7F6S1tl90-YaOe_qfPMZ688Bl_JC2g7CdRSTIraPZnWy5OTbp9pvZklruHsOJlAiFDfpMMYv06rmjRDBnSQ-K3H6eIUH8sC_cBUQ_G26lOv-ZibeIzJQNEr7SkFL18a6oIvEB8OhvwNglZFeOh5ucagTuxVQcL1HTTgIEajdh5ZTbMccsX-CjBD7XReb4Uxge1CaCiStR2qTeE_s2-TD6u8syntuGlGGHOCwKW5bgmehCEjLMxMMLBZKgyUY1iQcSKpBRqj380w'
  data = {'grant_type' : 'authorization_code', 'code' : code, 'redirect_uri' : 'https://www.spotify.com/de/home/', 'client_id' : CLIENT_ID, 'client_secret' : CLIENT_SECRET }
  r = requests.post(url = 'https://accounts.spotify.com/api/token', data = data)
  print(r.text)
  return 


def refresh_token():
# https://accounts.spotify.com/authorize?client_id=5fe01282e44241328a84e7c5cc169165&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&
# scope=user-read-private%20user-read-email&state=34fFs29kd09
    
    #needs to be refreshed after every post request
    #params = {'client_id' : '19bd4855fecf4bd9958c1e34300a9740', 'redirect_uri' : 'https://www.spotify.com/de/home/','response_type' : 'code', 'show_dialog' : 'false'}
    #r = requests.get(url = 'https://accounts.spotify.com/authorize', params = params)
    
    # now get refresh and authcode token via post request 
    #data = {'grant_type' : 'authorization_code', 'code' : code, 'redirect_uri' : 'https://www.spotify.com/de/home/', 'client_id' : CLIENT_ID, 'client_secret' : CLIENT_SECRET }
    #r = requests.post(url = 'https://accounts.spotify.com/api/token', data = data)

    # actually refresh the access token
    r = requests.post(url = 'https://accounts.spotify.com/api/token', data = {'grant_type' : 'refresh_token', 'refresh_token' : refreshToken, 'client_id' : CLIENT_ID, 'client_secret' : CLIENT_SECRET})
    jsonStr = r.text
    token = json.loads(jsonStr)['access_token']
    print("access_token :",token)
     
    return token 




def fingern():
    msg = "Macht die Augen zu.\n Zählt von 3 runter\n und zeigt auf denjenigen,\n der trinken soll.\n Der mit den meisten Votes\n muss 3 Schlücke trinken"
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    show_alert(msg,20)
    return 

def bombe():
    bombemThemen = ["Synonyme für den Penis", "Charaktere in Harry Potter", "Biermarken", "Wörter, die Bär \n beinhalten", "Fitnessübungen","Tänze",  "Synonyme für \n sich betrinken"]
    play_song(ticking[0],0)
    thema = random.sample(bombemThemen, 1)
    n = getName()
    msg = str(thema[0]) + "\n" + n + " fängt an"
    show_pic("bombe")
    time.sleep(2)
    time_till_explosion =  random.randint(20, 60)
    show_alert(msg,time_till_explosion)
    #time.sleep(time_till_explosion)
    play_song(explosion[0],0)
    time.sleep(5)
    os.system("taskkill /im Microsoft.Photos.exe /f")
    return 

def get_current_song_info():
    accessToken = refresh_token() #~~~
    
    bearer = 'Bearer ' + accessToken    
    headers = {'Authorization': bearer,
              'Accept' : 'application/json',
              'Content-Type' : 'application/json' }
    r = requests.get(url = 'https://api.spotify.com/v1/me/player', headers = headers )
    jsonStr = r.text
    print(jsonStr)

#    albumURI = json.loads(jsonStr)['item']['album']['uri']
#    trackNR = json.loads(jsonStr)['item']['track_number']
#    print(albumURI,trackNR,song_ms)

    trackURI = json.loads(jsonStr)['item']['uri']
    song_ms = json.loads(jsonStr)['progress_ms']

    print(trackURI, song_ms)
    return trackURI, song_ms        

def pause_song():
    accessToken = refresh_token()

    bearer = 'Bearer ' + accessToken    
    headers = {'Authorization': bearer,
              'Accept' : 'application/json',
              'Content-Type' : 'application/json' }
    url = "https://api.spotify.com/v1/me/player/pause"
    requests.put(url = url, headers = headers)
    return 


def resume_song():
    accessToken = refresh_token()
    bearer = 'Bearer ' + accessToken    
    headers = {'Authorization': bearer,
              'Accept' : 'application/json',
              'Content-Type' : 'application/json' }
    url = "https://api.spotify.com/v1/me/player/play"
    requests.put(url = url, headers = headers)
    return 

def play_song(songURI, ms):

   accessToken = refresh_token() #~~~
#    l = name_songs[name]
   play = api + 'player/play'
   bearer = 'Bearer ' + accessToken    
   headers = {'Authorization': bearer,
              'Accept' : 'application/json',
              'Content-Type' : 'application/json' }
#    data = "{\"context_uri\": \"spotify:album:%s\", \
#            \"offset\":{\"position\":%d},           \
#            \"position_ms\":%d}" % (l[0], l[1], l[2])

   # Habe hier mal probiert einfach ne URI zu geben, funktioniert super (solange es ein context ist, also album, artist, playlist etc., für einzelne tracks s.u)^^
   test_data = "{\"context_uri\": \"spotify:artist:4FDj6mh458K7m9Txwyj2rt\",  \
               \"position_ms\":0}"
   # Hier dann mal wie ich mir das gerade vorstelle getestet
   test_data2 = "{\"context_uri\": \"%s\",  \
                \"position_ms\":%d}" % (songURI, ms)
   # trackURI haben keinen context, also gibt man hier keine "context_uri" mehr an sondern einfach "uris" (man kann mehrere angebene noch nicht probiert)
   test_data3 = "{\"uris\": [\"%s\"],  \
                \"position_ms\":%d}" % (songURI, ms)
   r = requests.put(url = play,  headers = headers, data = test_data3)

   #print(r.url)
   #print(r.content)
    #msg = "Mach

def show_pic(name):
    pic = name_pics[name]
    img = Image.open(pic)
    img.show()
    
    #img.close() # Schließt nicht das gezeigte Bild (Wird von nem Unterprozess gehandhabt auf den wir nicht zugreifen können, ist wohl zum debuggen gedacht) 
    return

def getName():
    return random.choice(names)

def saufen():
    name = getName()
    show_pic(name)

    uri, ms = name_songs[name]
    play_song(uri, ms)

    time.sleep(15)
     # TODO sleep anpassen, ggf. an Individuelle Zeiten der Songs
    return
   

def show_alert(msg,t):
  root = tk.Tk()
  root.title("info")
  windowWidth = root.winfo_reqwidth()
  windowHeight = root.winfo_reqheight()
  # Gets both half the screen width/height and window width/height
  positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
  positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
  # Positions the window in the center of the page.
  root.geometry("+{}+{}".format(positionRight, positionDown))
  fontStyle = tkFont.Font(family="Lucida Grande", size=40)

  labelExample = tk.Label(root, text=msg, font=fontStyle)
  tk.Label(root, text="Aufgabe").pack()
  labelExample.pack(side=tk.TOP)
  root.after(t*1000, lambda: root.destroy())     # time in ms
  
  root.mainloop()

def wasserfall():
    show_pic('wasserfall')
    beginner = getName()
    msg = "Wasserfall!!!11! " + beginner + " fängt an!"
    play_song(waterfall[0],waterfall[1])
    show_alert(msg,20)
    #time.sleep(20)
    
    return 

def gangnam():
    chosen_one = getName()
    msg = chosen_one + "!\n" + "Tanze den \n Gangnam Style! \n Video kommt!"
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    show_alert(msg,8)
    pause_song()
    open_video("https://youtu.be/AV1biKT426I?t=55",43)
    #resume_song()
    return 


def fitness():
    chosen_one = getName()
    msg = chosen_one + "!" + "\n Mache 1 Minute \n Fitness \n Video kommt!"
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    show_alert(msg,8)
    pause_song()
    open_video("https://youtu.be/Auo8veVyRIY?t=1491",70)
    #resume_song()
    return   


def scooter():
    chosen_one = getName()
    msg = chosen_one + "!" + "\n Sing den \n Song! Sei geil!\n Video kommt!"
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    show_alert(msg,8)
    pause_song()
    open_video("https://youtu.be/fMpzMlumAzM?t=89",51)
    #play_song()    
    return 

def open_video(url,t):
    pause_song()
    webbrowser.open_new_tab(url)
    time.sleep(t)
    os.system("taskkill /im firefox.exe /f")
    # webbrowser.
    resume_song()
    return

#scope=user-read-private%20user-read-email%20user-read-recently-played%20user-read-playback-position%20user-modify-playback-state%20user-read-currently-playing
def main():
  actions = ["saufen"]*20 + ["wasserfall"]*3 + ["bombe"]*2 + ["fingern"]*2  
  #actions = ["saufen"]*10 + ["wasserfall"]*3 + ["bombe"]*2 + ["fingern"]*2 + ["gangnam", "fitness", "scooter"]
  print(actions)
  #saufen()
    # get_acc_ref()
  #wasserfall()
  #url = "https://www.youtube.com/watch?v=43aJSsKQA_0?autoplay=1&mute=1"
  #open_video(url, 5)
  #os.startfile(url)
  
  #fingern()
  #bombe()
  #play_song(shots[0],shots[1])
  #show_pic('alle')
# Maybe einfach am Anfang des loops jedes Mal refreshen? Könnte man dann als Parameter mitgeben wenn nötig. Ist vielleicht auch dumm alle Funktionen mit Parametern vollzuklatschen x)
  while True:
    #   accessToken = refresh_token()  
    #   TODO hier noch sleepen zwischen den Iterationen.

    
    #wasserfall()    
    delay = random.randint(100, 150)
    action = random.choice(actions)
    print(action, 'will happen in', delay, 'seconds')
    time.sleep(delay)
    #cur_uri, cur_ms = saufi
    cur_uri, cur_ms = get_current_song_info()
    # Hier alle prompts als if-cases, danach gehts wieder zum alten Song  
    if action == "saufen":
        saufen()
    if action == "wasserfall":
        wasserfall()    
    if action == "bombe":
        bombe()    
    if action == "fingern":
        fingern()

    if action == "fitness":
        # print("fitness plays")
        fitness()
        actions.remove("fitness")
    if action == "gangnam":
        # print("gangnam plays")
        gangnam()
        actions.remove("gangnam")
    if action == "scooter":
        # print("scooter plays")
        scooter()
        actions.remove("scooter")

    # Zum unterbrochenen Song zurück
    os.system("taskkill /im Microsoft.Photos.exe /f")
    play_song(cur_uri, cur_ms)
    
    # ??
    #USER = 'd03ueir6zw7k1dyywjc97fee2?si=GVU-LsDRTg2vL5KPMTbfJg'

if __name__ == "__main__":
    main()
