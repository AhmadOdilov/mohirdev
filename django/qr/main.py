import qrcode

img = qrcode.make('hello')
img.save('hello.png')