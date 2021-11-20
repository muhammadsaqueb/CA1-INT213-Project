import pyttsx3 #pip install pyttsx3 (for output voice)
import speech_recognition as sr #pip install speechRecognition (for input and voice recognition)
import datetime #for date and time
import wikipedia #pip install wikipedia
import webbrowser #for opening webbrowser
import os #for accessing the functions of operating system anf for system compatibility
import smtplib #Simple Mail Transfer Protocol (SMPT) it allows us to send mail
import platform #used to retrieve as much possible information about the platform 
import requests
import json
from datetime import date
import calendar
from time import time
from selenium import webdriver

engine = pyttsx3.init('sapi5') #SAPI5 is a microsoft speech API (Speech Application Programming Interface)
voices = engine.getProperty('voices')
#print(voices[1].id) #for printing the voices id which is in-built in Windows Operating System 
engine.setProperty('voice', voices[1].id) #voice[1] means femail voice(Hazel)


def speak(audio):
    #funtion for output voice or for speak convert our text ro speech
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    #function for wishing me whenever i run program according to time.
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")
        
    print("I'm FRIAS, Female Represented Artificial Inteligence System, How Can I Help You ")     
    speak("I'm FRIAS, Female Represented Artificial Inteligence System, How Can I Help You ")       

def news():
    speak("News for today.. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=59b14aeab1dc4fc5af8525a5e7a54b40"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving on to the next news..Listen Carefully")

    speak("Thanks for listening...")

def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer() #for recogning input voice
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # seconds of non-speaking audio before a phrase is considered complete

        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('muhammadsaqueb07@gmail.com', 'Marvel@2251824')
    server.sendmail('muhammadsaqueb07@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takecommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "google" in query:
           # query = query.split(" ")
            print("Sir, What You Have To Search :")
            speak("Sir, What You Have To Search :")
            search = takecommand()
            print("Hold on Sir, I will show you result regarding " + search + " .")
            speak("Hold on Sir, I will show you result regarding " + search + " .")
            webbrowser.open("https://www.google.com/search?q=" + search + "&amp;")

        elif "youtube" in query:
            #query = query.split(" ")
            print("Sir, Which video You want To Search :")
            speak("Sir, Which video You want To Search :")
            search = takecommand()
            print("Hold on Sir, I will show you result regarding " + search + " .")
            speak("Hold on Sir, I will show you result regarding " + search + " .")
            webbrowser.open("https://www.youtube.com/results?search_query=" + search + "/")

        elif "weather" in query:
           # query = query.split(" ")
            print(" Sir, Can You Please Tell me the Location ")
            speak(" Sir, Can You Please Tell me the Location ")
            location = takecommand()
            print("Hold on Sir, I will show you weather condition of " + location + " .")
            speak("Hold on Sir, I will show you weather condition of " + location + " .")
            webbrowser.open("https://www.wunderground.com/weather/in/"+location+"/" )

        elif 'music' in query:
            music_dir = "C:\\Users\\mdsaq\\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\mdsaq\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # sale yh to ek hi h hn whi h idea whi se uthaya h
            os.startfile(codePath)

        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "mdsaquibe9357309084@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    

        elif "news" in query:
            news()

        elif "about you" in query: 
            speak("here is some information about me.")
            pyth_ver=platform.python_version()
            print(f"Python version:{pyth_ver}")
            speak(f"Python version:{pyth_ver}")
            pyth_imple = platform.python_implementation()
            print(f"Python implementation: {pyth_imple}")
            speak(f"Python implementation: {pyth_imple}")
            pyth_build = platform.python_build()
            print(f"Python build no. and date: {pyth_build}")
            speak(f"Python build no. and date: {pyth_build}")
            pyth_compiler = platform.python_compiler()
            print(f"Python compiler: {pyth_compiler}")
            speak(f"Python compiler: {pyth_compiler}")
            machine_info = platform.machine()
            print(f"Machine type: {machine_info}")
            speak(f"Machine type: {machine_info}")
            syst = platform.system()
            print(f"Operating system: {syst}")
            speak(f"Operating system: {syst}")
            node = platform.node()
            print(f"System's network name: {node}")
            speak(f"System's network name: {node}")
            processor = platform.processor()
            print(f"Platform processor: {processor}")
            speak(f"Platform processor: {processor}")
            plat = platform.platform()
            print(f"Platform information: {plat}")
            speak(f"Platform information: {plat}")
            arch = platform.architecture()
            print(f"Platform architecture: {arch}")
            speak(f"Platform architecture: {arch}")

        elif "reboot" in query:
            check=speak("""Want to Reboot your computer ?
            1. Shutdown
            2. Restart            
            """ );
            if takecommand() ==  'shutdown' :
                print("Are You Sure to Shutdown You Computer?")
                speak("Are You Sure to Shutdown You Computer?")
                if takecommand() == "yes":
                    os.system("shutdown /s /t 1");


            if takecommand() ==  'restart' :
                print("Are You Sure to Restart You Computer?")
                speak("Are You Sure to Restart You Computer?")
                if takecommand() == "yes":
                    os.system("restart /r /t 1");

        elif "exit" in query:
            print("Thank You Sir, Have A Nice Day")
            speak(exit())

        elif 'attend my class' in query:
            curr_date = date.today()
            curr_day = calendar.day_name[curr_date.weekday()]
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            print(time_now)
            speak(time_now)
            print(curr_date)
            speak(curr_date)
            print(curr_day)
            speak(curr_day)
            
            if curr_day == 'Monday': #class routine of Monday 
                hour_class = int(datetime.datetime.now().hour)
                if hour_class >=9 and hour_class < 11: #Monday INT306 Class

                    speak("Your INT306 DBMS Class is gonna start please be ready to Attend")

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    int306 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[2]/td[3]')
                    int306.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=12 and hour_class < 14:   #Monday INT213 Class

                    speak("Your INT213 Python Programming Class is gonna start please be ready to Attend") 

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    int213 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[3]/td[3]')
                    int213.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=15 and hour_class < 16:  #Monday CSE320 Class

                    speak("Your CSE320 Software Engineering is gonna start please be ready to Attend")        

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    cse320 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[4]/td[3]')
                    cse320.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=16 and hour_class < 17:  #Monday CSE211 Class

                    speak("Your CSE211 Computer Organization and Design Class is gonna start please be ready to Attend") 

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    cse211 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[5]/td[3]')
                    cse211.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()


            elif curr_day == 'Wednesday': #class routine of Wednesday 
                hour_class = int(datetime.datetime.now().hour)
                if hour_class >=9 and hour_class < 10: #Wednesday PEL131 Class

                    speak("Your PEL131 Commnucation Skills Class is gonna start please be ready to Attend") 

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    pel131 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[2]/td[2]')
                    pel131.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=10 and hour_class < 11:   #Wednesday CSE211 Class

                    speak("Your CSE211 Computer Organization and Design Class is gonna start please be ready to Attend") 

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    cse211 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[3]/td[3]')
                    cse211.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=12 and hour_class < 14:  #Wednesday INT306 Class

                    speak("Your INT306 DBMS Class is gonna start please be ready to Attend")

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    int306 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[4]/td[3]')
                    int306.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=15 and hour_class < 16:  #Wednesday CSE205 Class

                    speak("Your CSE205 Data Structure Class is gonna start please be ready to Attend")

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    cse205 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[5]/td[3]')
                    cse205.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=16 and hour_class < 17:  #Wednesday CSE320 Class

                    speak("Your CSE320 Class is gonna start please be ready to Attend") 

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    cse320 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[6]/td[3]')
                    cse320.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()   

            elif curr_day == 'Thursday': #class routine of Thursday 
                hour_class = int(datetime.datetime.now().hour)
                if hour_class >=9 and hour_class < 10: #Thursday MTH401 Class

                    speak("Your MTH401 Discrete Mathematics Class is gonna start please be ready to Attend")

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    mth401 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[2]/td[3]')
                    mth401.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=10 and hour_class < 11:   #Thursday PEL131 Class

                    speak("Your PEL131 Commnucation Skills Class is gonna start please be ready to Attend") 

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    pel131 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[3]/td[3]')
                    pel131.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=12 and hour_class < 13:  #Thursday CSE211 Class

                    speak("Your CSE211 Computer Organization and Design Class is gonna start please be ready to Attend")        

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    cse211 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[4]/td[3]')
                    cse211.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=13 and hour_class < 14:  #Thursday INT306 Class

                    speak("Your INT306 DBMS Class is gonna start please be ready to Attend") 

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    int306 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[5]/td[3]')
                    int306.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=15 and hour_class < 17:  #Thursday INT213 Class

                    speak("Your INT213 Python Programming Class is gonna start please be ready to Attend") 

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    int213 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[6]/td[3]')
                    int213.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

            elif curr_day == 'Friday': #class routine of Friday 
                hour_class = int(datetime.datetime.now().hour)
                if hour_class >=20 and hour_class < 21: #Friday CSE205 Class

                    speak("Your CSE205 Data Structure Class is gonna start please be ready to Attend")

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    cse205 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[2]/td[3]')
                    cse205.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=12 and hour_class < 13:   #Friday MTH401 Class

                    speak("Your MTH401 Discrete Mathematics Class is gonna start please be ready to Attend") 

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    mth401 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[3]/td[3]')
                    mth401.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

            elif curr_day == 'Saturday': #class routine of Saturday 
                hour_class = int(datetime.datetime.now().hour)
                if hour_class >=9 and hour_class < 10: #Saturday MTH401 Class

                    speak("Your MTH401 Discrete Mathematics Class is gonna start please be ready to Attend")

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    mth401 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[2]/td[3]')
                    mth401.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=10 and hour_class < 11:  #Saturday PEL131 Class

                    speak("Your PEL131 Commnucation Skills Class is gonna start please be ready to Attend") 

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    pel131 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[3]/td[3]')
                    pel131.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=12 and hour_class < 14:  #Saturday CSE205 Class

                    speak("Your CSE205 Data Structure Class is gonna start please be ready to Attend")        

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    cse205 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[4]/td[3]')
                    cse205.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=15 and hour_class < 16:  #Saturday CSE320 Class

                    speak("Your CSE320 Software Engineering Class is gonna start please be ready to Attend") 

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    CSE320 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[5]/td[3]')
                    CSE320.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()

                elif hour_class >=16 and hour_class < 17:  #Saturday CSE211 Class

                    speak("Your CSE211 Computer Organization and Design Class is gonna start please be ready to Attend") 

                    driver = webdriver.Chrome(executable_path="D:\PYTHON\chromedriver_win32\chromedriver.exe")
                    driver.get("https://myclass.lpu.in/")

                    Username =  driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
                    Username.send_keys('12020603')

                    Password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
                    Password.send_keys('Veronica@2251824')

                    login = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
                    login.click() 

                    Classes = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
                    Classes.click()

                    compact_view = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[3]/div[1]/button[2]')
                    compact_view.click()

                    cse211 = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[6]/td[3]')
                    cse211.click()

                    join_class = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
                    join_class.click()
