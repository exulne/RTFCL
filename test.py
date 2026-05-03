"https://youtu.be/qtyy95Vevrk"
"https://www.youtube.com/watch?v=qtyy95Vevrk"

content = "https://www.youtube.com/watch?v=qtyy95Vevrk"
i = content.find("?v=")
print(i)
content = "https://youtu.be/" + content[i+3:]

print(content)