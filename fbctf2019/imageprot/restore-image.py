import os
import base64
with open("export", "rb") as f:
    export = f.read()
export = base64.b64decode(export)

os.system('curl https://httpbin.org/status/418 > teapot')
with open("teapot", "rb") as f:
    teapot = f.read()

for i in range(len(export)):
    export = export[:i] + bytes([export[i] ^ teapot[i % len(teapot)]]) + export[i+1:]

with open("image-back.png", "wb") as f:
    f.write(export)
