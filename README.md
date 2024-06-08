# WoW Data Hub

## Introduction

**WoW Data Hub** is a project designed to collect, store, analyze, and visualize data from World of Warcraft using the Blizzard APIs. The goal is to provide insights into realm statuses, Mythic dungeon performances, achievement lists, and WoW Token prices.

## Project Objectives

1. **Data Collection**: Retrieve game data from the Blizzard APIs, focusing on World of Warcraft.
2. **Data Storage**: Store collected data in structured (SQL) and unstructured (NoSQL) databases.
3. **Data Analysis**: Process and analyze the data using tools like Apache Spark.
4. **API Development**: Create a RESTful API to expose analyzed data.
5. **Data Visualization**: Visualize the data through interactive dashboards.

## Technologies Used

- **Python**: For data processing and API integration.
- **PostgreSQL**: For structured data storage.
- **MongoDB**: For unstructured data storage.
- **Apache Spark**: For data processing and analysis.
- **Flask**: For developing the RESTful API.
- **Plotly/Dash**: For data visualization.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **PostgreSQL** and **MongoDB** installed and running.
- **Git** for version control.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AntoineMLD/WoW-Data-Hub.git
    cd WoW-Data-Hub
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Setting Up Blizzard API Access

1. **Register an application on Blizzard Developer Portal** to obtain your `client_id` and `client_secret`.
2. **Configure OAuth** settings in your local environment (detailed steps in the next sections).

## Using the WoW Data Hub

1. **Collect Data**: Use the provided scripts to fetch data from the Blizzard API.
2. **Store Data**: Insert the fetched data into PostgreSQL and MongoDB databases.
3. **Analyze Data**: Process the data using Spark for insights and trends.
4. **Expose Data**: Serve the analyzed data through the Flask API.
5. **Visualize Data**: Create interactive visualizations using Plotly/Dash.

## Project Structure

- `/scripts`: Contains data collection and processing scripts.
- `/api`: Contains Flask API code.
- `/visualizations`: Contains scripts for data visualization.
- `/data`: Directory for storing raw and processed data files.

## Contributing

Feel free to submit issues and pull requests to improve this project.

## License

This project is licensed under the MIT License.

---


