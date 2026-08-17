import pyclip
import time
import json

blacklist = ["instagram.com", "google.com"]
image_headers = ["<meta", "<img"]
image_extensions = [".jpg", ".jpeg", ".png", ".webp", ".gif"]

TwitterPair = ["https://x.com","https://vxtwitter.com"]
RedditPair = ["reddit.com","vxreddit.com"]

def RTFCL(content):
    try:
        with open('/home/cubxfy/Projects/exulne/RTFCL/database/states.json', "r") as file:
            states = json.load(file)
        print("Loaded Json")
    except Exception as e:
        print(f"Json loading error {e}")

    if "youtube.com" in content and states.get("youtube"):
        try:
            print("detected: youtube.com")
            i = content.find("?v=")
            if i != -1:
                print("detected: youtube video")
                content = "https://youtu.be/" + content[i+3:]
        except Exception as e:
            print(f"Failed YT-RTFCL {e}")
    elif TwitterPair[0] in content and states.get("twitter"):
        try:
            key = TwitterPair[0]
            replacementSite = TwitterPair[1]
            print(f"detected: {key}")
            i = content.find(key)

            content = content[:i] + replacementSite + content[i+len(key):]
            
        except Exception as e:
            print(f"Twitter Error {e}")

    elif RedditPair[0] in content and states.get("reddit"):
        try:
            key = RedditPair[0]
            replacementSite = RedditPair[1]
            print(f"detected: {key}")
            i = content.find(key)

            content = content[:i] + replacementSite + content[i+len(key):]
            
        except Exception as e:
            print(f"Reddit Error {e}")

    elif states.get("remaining"):
        try:
            print("detected: other link")
            if not content.lower().split("?")[0].endswith(image_extensions):
                    return content.split("?")[0]
        except Exception as e:
            print(f"General Error: {e}")
    
    
    return content

def main():
    print("Started Pyclip")
    # open json
    try:
        with open('/home/cubxfy/Projects/exulne/RTFCL/database/states.json', "r") as file:
            ToggleStates = json.load(file)
        print("Loaded Json")
    except Exception as e:
        print(f"Json loading error {e}")


    try:
        last_seen = pyclip.paste(text=True)
    except:
        last_seen = ""


    while True:
        try:
            CurrentClip = pyclip.paste(text=True)
        except:
            pyclip.copy("")
            CurrentClip = ""
        
        StrippedClip = CurrentClip.strip()

        try:
            for entry in image_headers:
                is_img = True if StrippedClip.startswith(entry) else False

            # checking if startswith http works for both http and https since http includes https
            is_website = StrippedClip.startswith("http")
            is_file = StrippedClip.startswith("file://")

        except Exception as e:
            print(f"Error Checking: {e}")

        try:
            if CurrentClip != last_seen and StrippedClip and is_website and ToggleStates.get("all"):              
                print(f"Detected {StrippedClip}")
                cleanedLink = RTFCL(StrippedClip)
                print("stripped" + StrippedClip)
                pyclip.copy(cleanedLink)
                print(f"Updated Link: {cleanedLink}")
                last_seen = cleanedLink
            else:
                last_seen = CurrentClip
        except Exception as e:
            print(f"Error Cleaning or Updating Link {e}")

    time.sleep(1)

if __name__ == "__main__":
    main()