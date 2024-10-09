import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

class CallPatternAnalyzer:
    def __init__(self, df):
        self.df = df
        self.le = LabelEncoder()
        
    def analyze_patterns(self):
        """Main analysis method for call patterns"""
        # Add temporal features
        self.add_temporal_features()
        
        # Perform analyses
        temporal_patterns = self.analyze_temporal_patterns()
        segment_patterns = self.analyze_customer_segments()
        sentiment_patterns = self.analyze_sentiment_patterns()
        
        # Generate visualizations
        self.plot_temporal_patterns()
        self.plot_segment_patterns()
        
        return {
            'temporal_patterns': temporal_patterns,
            'segment_patterns': segment_patterns,
            'sentiment_patterns': sentiment_patterns
        }
    
    def add_temporal_features(self):
        """Add time-based features to the dataset"""
        self.df['hour'] = self.df['call_start_datetime'].dt.hour
        self.df['dow'] = self.df['call_start_datetime'].dt.dayofweek
        self.df['month'] = self.df['call_start_datetime'].dt.month
    
    def analyze_temporal_patterns(self):
        """Analyze patterns across different time periods"""
        return {
            'hourly': self.df.groupby(['hour', 'primary_call_reason']).size().unstack(),
            'daily': self.df.groupby(['dow', 'primary_call_reason']).size().unstack(),
            'monthly': self.df.groupby(['month', 'primary_call_reason']).size().unstack()
        }
    
    def analyze_customer_segments(self):
        """Analyze patterns across customer segments"""
        return self.df.groupby(['elite_level_code', 'primary_call_reason']).agg({
            'call_id': 'count',
            'handle_time': 'mean',
            'average_sentiment': 'mean'
        })
    
    def analyze_sentiment_patterns(self):
        """Analyze sentiment patterns by call reason"""
        return self.df.groupby('primary_call_reason').agg({
            'average_sentiment': ['mean', 'std'],
            'customer_tone': lambda x: x.mode().iloc[0] if not x.empty else None,
            'silence_percent_average': 'mean'
        })
    
    def plot_temporal_patterns(self):
        """Create visualization for temporal patterns"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Hourly patterns
        hourly_calls = self.df.groupby('hour')['call_id'].count()
        hourly_calls.plot(ax=ax1, kind='bar')
        ax1.set_title('Call Volume by Hour')
        ax1.set_xlabel('Hour of Day')
        
        # Daily patterns
        daily_calls = self.df.groupby('dow')['call_id'].count()
        daily_calls.plot(ax=ax2, kind='bar')
        ax2.set_title('Call Volume by Day of Week')
        ax2.set_xlabel('Day of Week')
        
        plt.tight_layout()
        plt.savefig('results/temporal_patterns.png')
        plt.close()
    
    def plot_segment_patterns(self):
        """Create visualization for customer segment patterns"""
        plt.figure(figsize=(10, 6))
        segment_data = self.df.groupby('elite_level_code')['handle_time'].mean()
        sns.barplot(x=segment_data.index, y=segment_data.values)
        plt.title('Average Handle Time by Customer Segment')
        plt.tight_layout()
        plt.savefig('results/segment_patterns.png')
        plt.close()
    
    def predict_call_reasons(self, test_df):
        """Optional: Predict call reasons for test data"""
        # Prepare features
        features = [
            'hour', 'dow', 'elite_level_code', 'average_sentiment',
            'silence_percent_average'
        ]
        
        # Prepare training data
        X = self.df[features]
        y = self.le.fit_transform(self.df['primary_call_reason'])
        
        # Train model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X, y)
        
        # Make predictions
        test_features = test_df[features]
        predictions = self.le.inverse_transform(model.predict(test_features))
        
        return predictions