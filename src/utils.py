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
    with pd.ExcelWriter(os.path.join(output_path, f'{filename}.xlsx')) as writer:
        for sheet_name, data in results_dict.items():
            if isinstance(data, pd.DataFrame):
                data.to_excel(writer, sheet_name=sheet_name)
            elif isinstance(data, dict):
                pd.DataFrame(data, index=[0]).to_excel(writer, sheet_name=sheet_name)

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