import pyclip
import time

def RTFCL(content):
    if "x.com" in content:
        i = content.find("x.com")
        content = content[:i] + "fxtwitter" + content[i+1:]

    if "youtube.com" in content:
        i = content.find("?v=")
        content = "https://youtu.be/" + content[i+3:]

    if content[0:4] == "http":
        i = content.find("?")
        content = content[0:i]

    return content

def main():
    print("Monitoring clipboard with pyclip...")
    
    try:
        last_seen = pyclip.paste(text=True)
    except:
        last_seen = ""

    while True:
        try:
            current_data = pyclip.paste(text=True)

            if current_data != last_seen and current_data.strip():
                print(f"Detected: {current_data[:30]}...")

                new_data = RTFCL(current_data.strip())

                pyclip.copy(new_data)

                last_seen = new_data
                print("Clipboard updated!")

        except Exception as e:
            print(f"Error reading clipboard: {e}")

        time.sleep(0.2)

if __name__ == "__main__":
    main()