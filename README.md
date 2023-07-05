# RaspberryPie-AutoAdzan-Python
Create auto adzan on raspberry pie, by using respective API 


## Components:

1. Raspberry Pi Zero: This is the main computer board.
2. USB Sound Card: To connect audio output devices to the Raspberry Pi Zero.
3. Speakers or Headphones: For playing the Adzan voice.
4. Internet Connection: To access Adzan voice data and prayer time information.

## Setup Steps:

1. Set up the Raspberry Pi Zero:

* Install the operating system (e.g., Raspbian) on an SD card and insert it into the Raspberry Pi Zero.
* Connect the necessary peripherals such as a keyboard, mouse, and monitor to the Raspberry Pi Zero.
* Power on the Raspberry Pi Zero and follow the setup instructions to configure the operating system.

2. Connect the USB Sound Card:
* Plug the USB sound card into one of the USB ports on the Raspberry Pi Zero.
Ensure the sound card is properly detected by the operating system.

3. Install Required Software:
* Open a terminal on the Raspberry Pi Zero.
* Update the system's package lists by running the following command:
```
sudo apt update
```
* Install the necessary audio playback software, such as mpg321, by running the following command:
```
sudo apt install mpg321
```
* Install Python (if not already installed) using the following command:
```
sudo apt install python3
```


4. Obtain the Adzan Voice:
* Search for Adzan voice files online or record them yourself.
* Save the Adzan voice file in a directory on your Raspberry Pi Zero.

5. Play the Adzan Voice:
* Open a terminal on the Raspberry Pi Zero.
* Navigate to the directory where the Adzan voice file is stored using the `cd` command.
* Use the `mpg321` command to play the Adzan voice file. For example:
```
mpg321 adzan.mp3
```
Replace "adzan.mp3" with the actual filename of your Adzan voice file.

6. Obtain Prayer Time Data:
* Find a reliable API or online service that provides accurate prayer time data.
* Sign up for an account and obtain an API key, if required.
* Familiarize yourself with the API documentation and learn how to retrieve prayer time data.

7. Write a Python Script:
* In the terminal, navigate to the directory where you want to store the Python script using the `cd` command.
* Use a text editor (e.g., Nano) to create a new Python script file. For example:
```
nano update_prayer_times.py
```

* In the text editor, write the Python script to fetch the prayer time data from the API and update the Adzan playback schedule accordingly.
* Import necessary modules (e.g., `requests` for making HTTP requests and `crontab` for modifying the crontab file).
* Write code to make an HTTP request to the API and retrieve the prayer time data using your API key.
* Parse the response and extract the prayer times.
* Update the crontab file with the new prayer times using the crontab module.
* Save the script file.

8. Schedule the Script:
* Open the crontab file for editing using the `crontab -e` command in the terminal.




* Add a new line to schedule the execution of your Python script at a specific time. For example, to run the script every day at midnight, add the following line:
```
0 0 * * * python3 /path/to/update_prayer_times.py
```

______________________________________________________________
Reference
* https://www.smartazan.com/how-azan-for-google-home-raspberry-pi
* https://youtu.be/4Xgf3jIRqKo
