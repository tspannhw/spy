# spy
Inspired by TURN and Robin David's awesome python library

I found this awesome Python library:   https://github.com/RobinDavid/LSB-Steganography

It let's you hide text in images, binaries in images and images in images.

I was interesting in hiding text messages in images.    After seeing https://en.wikipedia.org/wiki/Turn:_Washington's_Spies I 
thought this was cool.

So using the library, I take an image and text and hide the text in there.   The library produces a new image (PNG) that has the message in it.

I have a second script that extracts the text.

The images look the same to my eyes.

A future test would be to run a deep learning library or image analysis tool on the images to see if they spot the bits.   They should be able to.   A future NiFi tool would be to spot hidden images.
