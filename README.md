# NBA 2024 Data Extraction and Analysis

This project provides an interactive web application for exploring and analyzing NBA 2024 player statistics.  
It extracts raw NBA data, processes it into clean datasets, and visualizes insights such as top-performing players, comparisons, and trends.

---

## 🚀 Features
- Extract and clean NBA 2024 season data
- Interactive dashboard built with [Plotly Dash](https://dash.plotly.com/)
- Visualizations of player statistics and rankings
- CSV exports of raw, cleaned, and top players datasets
- Custom styling for a user-friendly interface

---

## 📂 Project Structure
```
NBA_2024_Data_Extraction_and_Analysis-main/
├── app.py                  # Main application entry point
├── callbacks.py            # Interactive callbacks for dashboard functionality
├── creation_csv.py         # Script to generate and clean CSV data
├── data.py                 # Data loading and processing logic
├── layout.py               # Layout and UI components of the dashboard
├── nba_stats_2024.csv      # Raw dataset
├── nba_stats_2024_cleaned.csv  # Cleaned dataset
├── top_10_best_players.csv # Derived dataset with top players
└── assets/
    └── style.css           # Custom CSS for styling
```

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HoussemLangar/NBA_2024_Data_Extraction_and_Analysis.git
   cd NBA_2024_Data_Extraction_and_Analysis-main
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate    # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run the application locally:
```bash
python app.py
```

Then open your browser and navigate to:
```
http://127.0.0.1:8050/
```

---

## 📊 Data Sources
The datasets in this project (`nba_stats_2024.csv`) were collected and processed from publicly available NBA statistics.  

---

## 📄 License

This project is licensed under the MIT License – feel free to modify and use it.  

---

## 👤 Author

Developed by **Houssem LANGAR**  
📧 Email: houssemlangar3@gmail.com  
