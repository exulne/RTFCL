# forDiscord = {
#     "x.com":"fxtwitter.com",
#     "reddit.com":"vxreddit.com"
# }
# forDiscordkeys = list(forDiscord.keys())



# s = ["learn", "python", "with", "gfg"]  
# subs = ["le", "py"]  # List of substrings to check for in the strings

# pfxs = ["foo","bar"]
# words = ["food","bart","deece"]

# res = list(filter(lambda string: any([pfx in string for pfx in pfxs]), words))
# print(res)

# pfxs = ["foo","bar"]
# words = ["food","bart","deece"]

# res = [word for word in words if any(pfx in word for pfx in pfxs)]

forDiscord = {
    "x.com":"fxtwitter.com",
    "reddit.com":"vxreddit.com"
}
keys = list(forDiscord.keys())

content = "x.com/asldkfjaksldfl"

if any(key in content for key in keys):
            for key in keys:
                if key in content:
                    replacementSite = forDiscord[key]
                    print(f"detected: {key}")
                    i = content.find(key)

                    content = content[:i] + replacementSite + content[i+len(key):]
                    break

print(content)