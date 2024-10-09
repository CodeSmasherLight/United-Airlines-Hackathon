import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.utils import plot_save_figure

class AHTAnalyzer:
    def __init__(self, df, results_path):
        self.df = df
        self.results_path = results_path
        
    def analyze_factors(self):
        """Main analysis method for AHT factors"""
        try:
            # Convert results to DataFrames explicitly
            agent_perf = self.analyze_agent_performance()
            call_types = self.analyze_call_types()
            volume_patterns = self.analyze_high_volume_periods()
            freq_diff = self.calculate_frequency_difference()
            
            results = {
                'agent_performance': agent_perf,
                'call_type_impact': call_types,
                'volume_patterns_hourly': volume_patterns['hourly'],
                'volume_patterns_daily': volume_patterns['daily'],
                'frequency_difference': pd.DataFrame([freq_diff])
            }
            
            # Generate visualizations
            self.plot_aht_distributions()
            self.plot_high_volume_patterns()
            
            return results
            
        except Exception as e:
            print(f"Error in AHT analysis: {str(e)}")
            raise
    
    def analyze_agent_performance(self):
        """Analyze agent-level performance metrics"""
        metrics = self.df.groupby('agent_id').agg({
            'handle_time': ['mean', 'std', 'count'],
            'average_sentiment': 'mean',
            'wait_time': 'mean'
        })
        # Flatten column names
        metrics.columns = ['_'.join(col).strip() for col in metrics.columns.values]
        return metrics.round(2)
    
    def analyze_call_types(self):
        """Analyze impact of different call types on AHT"""
        metrics = self.df.groupby('primary_call_reason').agg({
            'handle_time': ['mean', 'std', 'count'],
            'wait_time': 'mean',
            'average_sentiment': 'mean'
        })
        # Flatten column names
        metrics.columns = ['_'.join(col).strip() for col in metrics.columns.values]
        return metrics.sort_values('handle_time_mean', ascending=False)
    
    def analyze_high_volume_periods(self):
        """Analyze patterns during high volume periods"""
        hourly_metrics = self.df.groupby('hour').agg({
            'handle_time': 'mean',
            'wait_time': 'mean',
            'call_id': 'count'
        }).sort_values('call_id', ascending=False)
        
        daily_metrics = self.df.groupby('dow').agg({
            'handle_time': 'mean',
            'wait_time': 'mean',
            'call_id': 'count'
        })
        
        return {
            'hourly': hourly_metrics,
            'daily': daily_metrics
        }
    
    def calculate_frequency_difference(self):
        """Calculate percentage difference between most and least frequent call reasons"""
        call_volumes = self.df['primary_call_reason'].value_counts()
        most_freq = call_volumes.index[0]
        least_freq = call_volumes.index[-1]
        
        most_freq_aht = self.df[self.df['primary_call_reason'] == most_freq]['handle_time'].mean()
        least_freq_aht = self.df[self.df['primary_call_reason'] == least_freq]['handle_time'].mean()
        
        pct_difference = ((most_freq_aht - least_freq_aht) / least_freq_aht) * 100
        
        return {
            'most_frequent_reason': most_freq,
            'least_frequent_reason': least_freq,
            'percentage_difference': round(pct_difference, 2)
        }
    
    def plot_aht_distributions(self):
        """Create AHT distribution visualizations"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Overall AHT distribution
        sns.histplot(data=self.df, x='handle_time', ax=ax1)
        ax1.set_title('Distribution of Handle Times')
        
        # AHT by call reason
        sns.boxplot(data=self.df, x='primary_call_reason', y='handle_time', ax=ax2)
        ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
        ax2.set_title('Handle Time Distribution by Call Reason')
        
        plt.tight_layout()
        plot_save_figure(fig, self.results_path, 'aht_distributions')
    
    def plot_high_volume_patterns(self):
        """Create visualizations for high volume patterns"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Hourly patterns
        hourly_data = self.df.groupby('hour')['handle_time'].mean()
        hourly_data.plot(kind='bar', ax=ax1)
        ax1.set_title('Average Handle Time by Hour')
        
        # Daily patterns
        daily_data = self.df.groupby('dow')['handle_time'].mean()
        daily_data.plot(kind='bar', ax=ax2)
        ax2.set_title('Average Handle Time by Day of Week')
        
        plt.tight_layout()
        plot_save_figure(fig, self.results_path, 'high_volume_patterns')