# United Airlines Call Center Analysis

This project analyzes call center data to optimize performance metrics and identify improvement opportunities.

## Project Structure

![image](https://github.com/user-attachments/assets/e3efddaa-4eae-4db7-b772-7a217bd71e57)

## Installation

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Prepare your data:


 - Place your CSV files in the data/ directory
 - Ensure file names match those in config.py
 - Required files:

   -- calls.csv <br>
   -- sentiment.csv <br>
   -- customer.csv <br>
   -- reasons.csv <br>
   -- timestamps.csv

4. Run the analysis: ```python main.py```
   
5. Check results:

   -Analysis results will be saved in the results/ directory <br>
   -Excel files contain detailed metrics <br>
   -PNG files contain visualizations

# Output Files

## AHT Analysis:

-aht_analysis.xlsx <br>
-aht_distributions.png <br>
-high_volume_patterns.png

## Self-Service Analysis:

 -self_service_analysis.xlsx <br>
 -recurring_issues.png <br>
 -complexity_distribution.png

## Call Patterns Analysis:

 -call_patterns_analysis.xlsx <br>
 -temporal_patterns.png <br>
 -segment_patterns.png   

<b> PS: Create a .gitignore file to exclude files and directories that should not be committed to GitHub, such as virtual environments (venv/), compiled Python files (__pycache__/), environment variable files (.env), and other temporary or system-specific files. I forgot to include this in my SS above. <b>

