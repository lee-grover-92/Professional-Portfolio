# 📊 Data Analytics Portfolio — Lee Grover

Hi, I'm **Lee Grover** — a data analyst who specialises in transforming raw, messy data into clear insights and practical solutions.  
My work spans data cleaning, exploratory analysis, feature engineering, visualisation, and end‑to‑end analytical modelling using **Python, SQL, Excel, and Power BI**.

This portfolio showcases real analytical workflows, from raw data ingestion all the way through to dashboards and stakeholder‑ready insights.

---

## 📫 Contact

- **LinkedIn:** https://www.linkedin.com/in/lee-grover-a33938118/
- **Email:** groverlee1992@gmail.com

---

## 🛠 Skills & Tools

### Programming & Analysis
- Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit‑learn)  
- SQL (MySQL, PostgreSQL, Azure SQL)  
- Exploratory Data Analysis (EDA)  
- Data cleaning & wrangling  
- Statistical analysis  

### Visualisation
- Power BI  
- Tableau  
- Python visualisation libraries  

### Other Tools
- Excel (Pivot Tables, VLOOKUP, Power Query)  
- Git & GitHub  
- Jupyter Notebook  

---

## 📂 Featured Projects

---

# 🐾 Pet Insurance Analytics Project  
*A full end‑to‑end SQL + Python + BI project simulating a real‑world pet insurance business.*

This project models the operations of a UK‑based pet insurance provider using a fully relational MySQL database and synthetically generated data. It mirrors the expectations of a junior data analyst role by covering the entire analytics lifecycle.

### 🔍 Highlights
- Fully normalised relational schema (customers, pets, policies, claims, vet visits, payments)  
- Python‑generated synthetic data with realistic business logic  
- Bulk loading, validation, and integrity checks in MySQL  
- Analytical SQL queries for KPIs such as loss ratio, claim frequency, CLV, and breed risk  
- Processed datasets for BI tools  
- Power BI/Tableau dashboards  

### 📁 Repository Structure
```
pet_data_project/
│
├── README.md
│
├── data/
│   ├── raw/                            # Synthetic CSVs for each table
│   └── processed/                      # Final exports for analysis or BI
│
├── sql/
│   ├── create_db.sql                   # Schema creation
│   ├── batch_load_csv.sql              # Bulk CSV import
│   ├── data_overview_queries.sql       # Initial exploration
│   ├── integrity_checks.sql            # FK and data validation
│   └── analysis_queries.sql            # Business-focused SQL analysis
│
├── scripts/
│   ├── fake_insurance_data_creator.py  # Python data generator
│   ├── export_views_to_csv.py          # Exports SQL views to CSV
│   └── sql_server_settings.bat         # Local MySQL config
│
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   ├── claims_risk_modelling.ipynb
│   └── customer_lifetime_value.ipynb
│
├── dashboards/
│   ├── powerbi/
│   └── tableau/
│
├── docs/
│   ├── schema_diagram.png
│   ├── data_dictionary.md
│   └── project_overview.pdf
│
└── images/
    └── dashboard_screenshots/
```

---

# 🏎️ F1 Podium Probability Analysis  
*A predictive modelling project estimating the probability of a Formula 1 driver achieving a podium finish.*

This project uses historical F1 data (1950–2020) to build an interpretable classification model and uncover the factors that most influence podium outcomes.

### 🔍 Highlights
- Multi‑dataset ingestion and cleaning (drivers, constructors, circuits, races, results)  
- Feature engineering (driver experience, constructor form, qualifying deltas, circuit characteristics)  
- Exploratory analysis of driver, team, and circuit trends  
- Predictive modelling using logistic regression / decision trees  
- Feature importance analysis for stakeholder insights  
- Interactive dashboard for exploring podium probabilities  

### 📁 Repository Structure
```
F1_Podium_Probability_Analysis/
│
├── dashboards/
│   └── powerbi_dashboard.pbix          # Interactive dashboard
│
├── data/
│   ├── raw/                            # Original Kaggle datasets
│   └── processed/                      # Cleaned & merged analytical datasets
│
├── notebooks/
│   ├── 01_data_preparation.ipynb       # Cleaning & standardisation
│   ├── 02_eda.ipynb                    # Exploratory analysis
│   ├── 03_modelling.ipynb              # Predictive modelling workflow
│   └── 04_insights.ipynb               # Findings & interpretation
│
├── src/
│   ├── data_cleaning.py                # Cleaning utilities
│   ├── feature_engineering.py          # Derived variables & transformations
│   ├── modelling.py                     # Model training & evaluation
│   └── utils.py                         # Shared helper functions
│
├── README.md                            # Project documentation
└── requirements.txt                     # Python dependencies
```

---

## 🎯 What This Portfolio Demonstrates

- Ability to design and implement relational databases  
- Strong SQL for analysis, validation, and data engineering  
- Python for data generation, cleaning, modelling, and automation  
- Clear analytical storytelling and visualisation  
