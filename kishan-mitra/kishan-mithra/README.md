Project README

Python Libraries:

Ensure the following Python libraries are installed:

tkinter (for custom Tkinter interfaces)
matplotlib (for plotting)
pillow (for image processing)
numpy (for numerical operations)
pandas (for data manipulation)
scikit-learn (for machine learning)
tensorflow (for deep learning)
requests (for HTTP requests)

Make sure you have a valid Mapbox API key. Replace the placeholder in your configuration file.

Required Files

background.png: The background image for the graphical user interface (GUI).
satellite_image.png: This file will be created by the script during execution when downloading the satellite image.

my_model.h5: The pre-trained model file. Ensure this file is located in the same directory as your script.
model.py: Contains the scaler object used for normalizing input features.

Hardware Requirements

ESP32 or ESP8266 Board
DHT22 Temperature and Humidity Sensor
Soil Moisture Sensor
Connecting Wires

Software Requirements

MicroPython installed on the ESP32/ESP8266
Adafruit_DHT library for interfacing with the DHT22 sensor
ADC (Analog-to-Digital Converter) for reading the soil moisture sensor

Connecting the Hardware

DHT22 Sensor
VCC: Connect to 3.3V
GND: Connect to GND
Data: Connect to a digital pin (e.g., GPIO 4)

Soil Moisture Sensor

VCC: Connect to 3.3V
GND: Connect to GND
Analog Output: Connect to an analog pin (e.g., GPIO 34)