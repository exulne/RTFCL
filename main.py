import pyclip
import time

blacklist = ["instagram.com", "google.com"]
image_extensions = (".jpg", ".jpeg", ".png", ".webp", ".gif")

forDiscord = {
    "x.com":"fxtwitter.com",
    "reddit.com":"vxreddit.com"
}
keys = list(forDiscord.keys())

enabled_list = ["yt", "replace"]

def RTFCL(content):
    if content.startswith("http"):
        print("detected: website")

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
    else:
        print("not a website, nothing to clear")
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
            is_html_image = current_data.strip().startswith(("<meta", "<img"))

            if current_data != last_seen and current_data.strip() and not is_html_image:
                print(f"Detected: {current_data[:30]}...")

                new_data = RTFCL(current_data.strip())

                pyclip.copy(new_data)

                last_seen = new_data
                print("Clipboard updated!")
            
            elif is_html_image:
                last_seen = raw_data

        except Exception as e:
            print(f"Error reading clipboard: {e}")

        time.sleep(0.2)


if __name__ == "__main__":
    main()