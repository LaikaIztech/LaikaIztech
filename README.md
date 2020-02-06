## What are we?

Project: Laika is a proposal to place a number of probes to certain locations within IZTECH to gather data on the dog
population of the school.

IZTECH does not have a dog problem, but it is the belief of our team that we have a dog overpopulation problem that
is getting worse with each passing day, which is creating a strain
on the wellbeing of the animals and the students alike.

In order to help alleviate this problem, Project: Laika aims to gather data necessary to develop strategies combat
dog overpopulation.

We do not wish euthanasia of animals, and we strongly believe for any creature this should be
a matter of last resort. We believe numerous technological and logistical methods can help combat this problem both in short term
and much more long term, we will propose a paper detailing our  recommendations after we gather the necessary data, make the
necessary research and contact the necessary experts.

## Why are we?

Project Laika will attempt to detect dog populations across the school, to do this, each Laika Beacon is equipped with a
videocamera and a wifi-chip, within certain intervals, camera sends its data to a central server and the frame is analysed
by a Python script which detects the number of dogs in it. This data is published periodically.

## How Are We?

Laika Beacons are small devices that transmit photos from their cameras. To be specific, these devices ran on the ESP8266 platform
and is either coded in C or MicroPython. This data is then transfered to the central server, central server is very simple web server
powered by Flask, it gets the data and feeds it into a Haar Cascade algorith, powered by OpenCV 3. Its model was developed by using
multiple resources among which Stanford's Dog Dataset, and was trained in house.

## Privacy

Data collected by Laika is very delicate given its nature. Frames captures by the cameras are deleted as soon as they are processed by the central server. Connection between the server and the Laikas
are performed by encrypted HTTPS requests. Moreover, majority of our code is open source, and therefore is open to critization as you see fit.
## Where are we?

<iframe style="width: 100%; height: 400px;" 
src="src/website/map.html">
</iframe>