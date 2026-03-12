import qrcode

# base url for puzzles; update with your real domain when deploying
# you can set this to your Render URL or any host that will serve index.html
BASE = "https://treasure-hunt-vaag.onrender.com/index.html?p={}"

for i in range(1, 4):
    url = BASE.format(i)
    img = qrcode.make(url)
    filename = f"qr{i}.png"
    img.save(filename)
    print(f"Generated {filename} -> {url}")