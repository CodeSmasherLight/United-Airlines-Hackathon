import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def ensure_directory(directory):
    """Create directory if it doesn't exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_results(results_dict, output_path, filename):
    """Save analysis results to Excel file"""
    ensure_directory(output_path)
    
    # Ensure the results_dict is not empty
    if not results_dict:
        print(f"Warning: No data available to save in {filename}.xlsx")
        return
    
    with pd.ExcelWriter(os.path.join(output_path, f'{filename}.xlsx'), engine='openpyxl') as writer:
        for sheet_name, data in results_dict.items():
            # Handle DataFrame case
            if isinstance(data, pd.DataFrame):
                if not data.empty:
                    data.to_excel(writer, sheet_name=sheet_name)
                else:
                    print(f"Warning: Empty DataFrame for sheet {sheet_name}, skipping.")
            
            # Handle dictionary case
            elif isinstance(data, dict):
                # Check if dictionary is not empty and has valid structure
                if data and all(isinstance(k, str) and isinstance(v, (list, int, float, str)) for k, v in data.items()):
                    pd.DataFrame([data]).to_excel(writer, sheet_name=sheet_name)
                else:
                    print(f"Warning: Invalid or empty dictionary for sheet {sheet_name}, skipping.")
            
            # Handle unexpected data type
            else:
                print(f"Warning: Unsupported data type for sheet {sheet_name}, skipping.")

def plot_save_figure(fig, output_path, filename):
    """Save matplotlib figure to file"""
    ensure_directory(output_path)
    fig.savefig(os.path.join(output_path, f'{filename}.png'))
    plt.close(fig)

def setup_plotting_style():
    """Set up consistent plotting style"""
    plt.style.use('seaborn')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = [12, 8]
    plt.rcParams['figure.dpi'] = 100