Welcome! This app is a work in progress server that will allow you to interact with all of your music and Sonos devices. You are able to use http requests to adjust your music and even integrate with ifttt.

To run the server just navigate to the folder containing the python files and run

python HTTP.py [Desired port number]

How to use http push's
In the headers of your push request add a header "Data"

For the actual data in "Data" you can type any of the following to do its respective task:
Play
Pause
Volume+
Volume-
Next
Prev
IsPlaying (returns 200 if paused and 201 if playing, this is for debugging)

My current setup is the server running on a pc that is on the same subnet as my sonos devices, I then put it on a ngrok server (https://ngrok.com/) and I am currently using the http push app for the pebble time.

Thanks to the Soco team for their sonos integration library!
