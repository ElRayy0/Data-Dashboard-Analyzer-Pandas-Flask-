# Data Dashboard Analyzer

A Flask-based web application for analyzing and visualizing sales data using Pandas.

## Features

- **Sales Dashboard**: View key statistics and metrics from CSV data
- **Data Analysis**: Automatic data summary using pandas describe functionality
- **Web Interface**: Clean HTML display of analytics

## Requirements

- Python 3.7+
- Flask
- Pandas
- SQLite3

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install flask pandas
   ```

## Usage

1. Ensure you have a `sales.csv` file in the project directory
2. Run the application:
   ```bash
   python dashboard.py
   ```
3. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
.
├── dashboard.py      # Main Flask application
├── sales.csv         # Sample sales data
└── README.md         # Project documentation
```

## License

This project is open source and available under the MIT License.
