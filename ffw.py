import pyttsx3
def read_line_and_speak(filename):
    try:
        engine=pyttsx3.init()
        with open (filename,'r')as file:
            content=file.read()
            engine.setProperty('rate',150)
            engine.say(content)
            engine.ruAndWait()
            print("content spoken successfully")
    except FileNotFoundError:
        print(f"file{filename} not found.please provide a valid path")
        if__name__=="__main__";
        file_path=input("Enter the path to the file:")
        read_file_and_speak(file_path)