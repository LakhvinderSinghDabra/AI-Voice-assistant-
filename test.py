import musicLibrary
import webbrowser
#joining words after "play":
def splitJoin(call):
    if call.lower().startswith("play"):
        index1array=call.split(" ") #spliting commadn into array
        joinfunc=splitJoin(index1array)[1:]
        sound=joinfunc
        link=musicLibrary.music(sound)
        webbrowser.open(link)
        
        print("command:",call)
    pass
def example2(call):
    if call.lower().startswith("play "):
        sound=call.lower()[5:]
        link= musicLibrary.music[sound]
        webbrowser.open(link)
    pass