
# Weather App

This project provides a simple weather application with both a Command-Line Interface (CLI) and a Graphical User Interface (GUI). The application fetches the current weather data based on the city name provided by the user.

## Features

- **CLI Mode**: A text-based interface that allows users to enter a city name and get the current weather data.
- **GUI Mode**: A graphical interface built with Tkinter for ease of use.
- **Geolocation**: Uses the Nominatim API to fetch coordinates based on city names.
- **Weather Data**: Fetches current weather data using the Open-Meteo API.

## Installation

Ensure you have Python installed on your system. This project requires Python 3.x.

### Dependencies

This project requires the following Python libraries:
- `requests`
- `geopy`
- `prettytable`
- `tkinter` (included with standard Python installations)

You can install the required packages using `pip`:

```bash
pip install requests geopy prettytable
```

## Usage

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/File_name.git
cd Address_to_project_folder
```

Run the main Python script and choose between CLI and GUI modes:

```bash
python File_name.py
```

### CLI Mode

In CLI mode, follow the prompt to enter the city name. The application will display the current weather data in a tabular format.

### GUI Mode

In GUI mode, use the graphical interface to enter the city name and click the "Get Weather" button. The current weather data will be displayed on the interface.

## CLI Weather App

### `fetch_forecast(latitude, longitude)`

Fetches the current weather forecast for the given latitude and longitude.

### `get_coordinates(city_name)`

Fetches the geographical coordinates (latitude and longitude) for the given city name.

### `main()`

Runs the CLI version of the weather app.


 


## GUI Weather App

### `fetch_forecast(latitude, longitude)`

Fetches the current weather forecast for the given latitude and longitude.

### `get_coordinates(city_name)`

Fetches the geographical coordinates (latitude and longitude) for the given city name.

### `display_weather(current_weather)`

Displays the current weather data on the GUI.

### `get_weather()`

Handles the process of getting weather data when the "Get Weather" button is clicked.

### `gui_main()`

Runs the GUI version of the weather app.


## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## Contact

For any questions or feedback, please contact [Chidanand A] at [chidananda1412@gmail.com].
