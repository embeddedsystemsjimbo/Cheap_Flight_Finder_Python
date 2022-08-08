# Cheap_Flight_Finder_Python


This Python app finds the cheapest available flights online using the Tequila API. The API searches a predetermined list of destinations stored as a Google Sheets document and accessed using the Sheety API (See Figure 1). 

If the API finds a flight that is cheaper than the historic lowest price for a certain destination, the app sends an email or an SMS message to the user via the Twillio API (See Figure 2).

For more info see the links below:

https://www.kiwi.com/en/
https://www.twilio.com
https://sheety.co

***

![image](https://user-images.githubusercontent.com/76194492/183331367-d112e853-7d4d-4e4f-a4b0-7c25d462a84d.png)
Figure 1: Google Sheet sample.

***

![IMG_5387FB04EB44-1](https://user-images.githubusercontent.com/76194492/183343141-3dae83f3-4762-4a49-81de-0b4c36176d0a.jpeg)
Figure 2: Sample Text Message.
