import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SelfServiceAnalyzer:
    def __init__(self, df):
        self.df = df
        
    def analyze_opportunities(self):
        """Main analysis method for self-service opportunities"""
        recurring_issues = self.analyze_recurring_issues()
        complexity_analysis = self.analyze_call_complexity()
        self_service_candidates = self.identify_self_service_candidates()
        
        # Generate visualizations
        self.plot_recurring_issues()
        self.plot_complexity_distribution()
        
        return {
            'recurring_issues': recurring_issues,
            'complexity_analysis': complexity_analysis,
            'self_service_candidates': self_service_candidates
        }
    
    def analyze_recurring_issues(self):
        """Analyze frequently occurring issues"""
        return self.df.groupby('primary_call_reason').agg({
            'call_id': 'count',
            'handle_time': 'mean',
            'average_sentiment': 'mean',
            'wait_time': 'mean'
        }).sort_values('call_id', ascending=False)
    
    def analyze_call_complexity(self):
        """Analyze call complexity based on handle time"""
        # Add complexity categorization
        self.df['call_complexity'] = pd.qcut(
            self.df['handle_time'],
            q=4,
            labels=['Simple', 'Moderate', 'Complex', 'Very Complex']
        )
        
        # Analyze complexity by call reason
        return self.df.groupby(['primary_call_reason', 'call_complexity']).size().unstack()
    
    def identify_self_service_candidates(self):
        """Identify issues that could be handled through self-service"""
        return self.df[
            (self.df['handle_time'] <= self.df['handle_time'].quantile(0.25)) &
            (self.df['average_sentiment'] >= self.df['average_sentiment'].quantile(0.5))
        ].groupby('primary_call_reason').agg({
            'call_id': 'count',
            'handle_time': 'mean',
            'average_sentiment': 'mean'
        }).sort_values('call_id', ascending=False)
    
    def plot_recurring_issues(self):
        """Create visualization for recurring issues"""
        plt.figure(figsize=(12, 6))
        recurring_issues = self.df['primary_call_reason'].value_counts()
        sns.barplot(x=recurring_issues.index, y=recurring_issues.values)
        plt.xticks(rotation=45)
        plt.title('Frequency of Call Reasons')
        plt.tight_layout()
        plt.savefig('results/recurring_issues.png')
        plt.close()
    
    def plot_complexity_distribution(self):
        """Create visualization for call complexity distribution"""
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.df, x='primary_call_reason', y='handle_time', hue='call_complexity')
        plt.xticks(rotation=45)
        plt.title('Call Duration Distribution by Reason and Complexity')
        plt.tight_layout()
        plt.savefig('results/complexity_distribution.png')
        plt.close()