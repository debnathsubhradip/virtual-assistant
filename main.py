# importing speech recognition package from google api
import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import wolframalpha  # to calculate strings into formula
from selenium import webdriver  # to control browser operations
import selenium
from selenium.webdriver.common.keys import Keys

num = 1
counter = 1

def assistant_speaks(output):
    global num

    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1
    print("PerSon : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    # saving the audio file given by google text to speech
    file = str(num) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)


def get_audio():

    global counter

    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")

        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=5)
    print("Stop.")  # limit 5 secs

    try:

        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text

    except:
        if(counter == 0) :
            assistant_speaks("Sorry, Could not understand you, will you please repeat !")








def search_web(input):
   # try :
   #     driver = webdriver.firefox()
   # try :


    driver = webdriver.Chrome("C:\\Users\\Subhradip 1\\Documents\\Virtual Assistant\\drivers\\chromedriver.exe")


    assistant_speaks("Opening Results !")
   # except :
    #    driver = webdriver.edge()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in input.lower():

        assistant_speaks("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower():

        assistant_speaks("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:

        if 'google' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        elif 'search' in input:

            driver.get("https://www.google.com/search?q =")
            driver.find_element_by_name("q").send_keys(input)
            driver.find_element_by_name("q").send_keys(Keys.ENTER)

        else:

            driver.get("https://www.google.com/search?q =")
            driver.find_element_by_name("q").send_keys(input)
            driver.find_element_by_name("q").send_keys(Keys.ENTER)

        return


# function used to open application
# present inside the system.
def open_application(input):
    if "chrome" in input:
        assistant_speaks("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return

    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return

    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return

    elif "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return

    else:


        assistant_speaks("Application not available")
        return

def process_text(input):
    #try:
        keyword_list = ['search', 'play']
        all_text=input
        text=""
        if any(word in all_text for word in keyword_list):
            # a basic web crawler using selenium
            str2=all_text.split(" ")
            a_set = set(keyword_list)
            b_set = set(str2)
            print(str2)
            if (a_set & b_set):
                text=(a_set & b_set)
                str2=' '.join(str2)
                print(str2)
                print("'"+text+"'")
                #str2.remove(text)
                # using join function join the list s by
                # separating words by str1
                search_web(str2)
                return

        elif "who are you" in input or "define yourself" in input or "what are you" in input or "alex who are you" in input :
            speak = '''Hello, I am Alex. Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            any task and here, it's done !'''
            assistant_speaks(speak)
            return

        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Subhradip Debnath."
            assistant_speaks(speak)
            return

        elif "where do you come from" in input or "where do you live" in input or "where do you go" in input:  # just
            speak = """Right at my creator's Home !"""
            assistant_speaks(speak)
            return

        elif "calculate" in input.lower():

            # write your wolframalpha app_id here
            app_id = "WOLFRAMALPHA_APP_ID"
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
            return

        elif 'open' in input:

            # another function to open
            # different application availaible
            open_application(input.lower())
            return

        else:

            assistant_speaks("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
'''''
    except:

        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)
'''


# Driver Code
if __name__ == "__main__":
    #assistant_speaks("Hi my name is Alex.")
    assistant_speaks("Hello Sir.")

    while (1):

        counter = 1
        while (1):
            text = get_audio()
            if "Alex" in str(text) or "Hey Alex" in str(text) or "Hey" in str(text) or "wake" in str(text) or "come on alex" in str(text) or "come on" in str(text) or "hi Alex" in str(text) or "helix" in str(text):
                counter=0
                break
        assistant_speaks("What can i do for you?")
        text = get_audio()

        if text == -1:
            continue

        if "exit" in str(text) or "bye" in str(text) :
            assistant_speaks("Ok Sir. Have a good day ahead !")
            break
        if "sleep" in str(text) :
            counter=1
            assistant_speaks("Ok, Going to Sleep. When you need me just call Alex !")
            while(1):
                text = get_audio()
                if "wake" in str(text) or "hey" in str(text) or "come on" in str(text) or "Alex" in str(text) or "helix" in str(text) or "hi Alex" in str(text) :
                    counter=0
                    break


        # calling process text to process the query
        else:
            process_text(text)