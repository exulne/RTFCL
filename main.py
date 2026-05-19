import pyclip
import time

blacklist = ["instagram.com", "google.com"]
image_extensions = (".jpg", ".jpeg", ".png", ".webp", ".gif")

forDiscord = {
    "https://x.com":"https://fxtwitter.com",
    "reddit.com":"vxreddit.com"
}
keys = list(forDiscord.keys())

enabled_list = ["yt", "replace"]

def RTFCL(content):
    # specific youtube check
    if "youtube.com" in content:
        print("detected: youtube.com")
        i = content.find("?v=")
        if i != -1:
            print("detected: youtube video")
            content = "https://youtu.be/" + content[i+3:]
    
    # general discord replacements
    elif any(key in content for key in keys):
        for key in keys:
            if key in content:
                replacementSite = forDiscord[key]
                print(f"detected: {key}")
                i = content.find(key)

                content = content[:i] + replacementSite + content[i+len(key):]
                break

    print("detected: other link")
    if not content.lower().split("?")[0].endswith(image_extensions):
            return content.split("?")[0]

    return content

def main():
    print("Monitoring clipboard with pyclip...")
    try:
        last_seen = pyclip.paste(text=True)
    except:
        last_seen = ""

    while True:
        try:
            raw_data = pyclip.paste()
            current_data = pyclip.paste(text=True)

            #checks
            is_img = current_data.strip().startswith(("<meta", "<img"))
            is_website = current_data.strip().startswith("http")
            is_file = current_data.strip().startswith("file://")

            if current_data != last_seen and current_data.strip() and is_website:
                print(f"Detected Something")
                new_data = RTFCL(current_data.strip())
                pyclip.copy(new_data)

                last_seen = new_data
                print("updated")
            else:
                last_seen = current_data
        except Exception as e:
            print(f"Error reading clipboard: {e}")

        time.sleep(0.2)

if __name__ == "__main__":
    main()