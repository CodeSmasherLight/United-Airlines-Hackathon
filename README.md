# United Airlines Call Center Analysis

This project analyzes call center data to optimize performance metrics and identify improvement opportunities.

## Project Structure

united_airlines_analysis/
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── aht_analysis.py
│   ├── self_service_analysis.py
│   ├── call_patterns_analysis.py
│   └── utils.py
│
├── data/
│   ├── calls.csv
│   ├── sentiment.csv
│   ├── customer.csv
│   ├── reasons.csv
│   └── timestamps.csv
│
├── results/
│   └── .gitkeep
│
├── requirements.txt
├── config.py
├── main.py
└── README.md


## Installation

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  On Windows: venv\Scripts\activate
```

2. Install requirements: ```pip install -r requirements.txt```

3. Prepare your data:


- Place your CSV files in the data/ directory
- Ensure file names match those in config.py
- Required files:

   calls.csv
   sentiment.csv
   customer.csv
   reasons.csv
   timestamps.csv

4. Run the analysis: ```python main.py```
   
5. Check results:

   -Analysis results will be saved in the results/ directory
   -Excel files contain detailed metrics
   -PNG files contain visualizations

# Output Files

## AHT Analysis:

-aht_analysis.xlsx
-aht_distributions.png
-high_volume_patterns.png

## Self-Service Analysis:

-self_service_analysis.xlsx
-recurring_issues.png
-complexity_distribution.png

## Call Patterns Analysis:

=call_patterns_analysis.xlsx
-temporal_patterns.png
-segment_patterns.png   
   

