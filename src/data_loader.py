import pandas as pd
from datetime import datetime

class DataLoader:
    def __init__(self):
        self.merged_df = None
        
    def load_data(self, file_paths):
        """
        Load and merge all CSV files
        Args:
            file_paths (dict): Dictionary containing paths to all CSV files
        Returns:
            pd.DataFrame: Merged dataframe with all necessary calculations
        """
        try:
            # Load individual datasets
            df_calls = pd.read_csv(file_paths['calls'])
            df_sentiment = pd.read_csv(file_paths['sentiment'])
            df_customer = pd.read_csv(file_paths['customer'])
            df_reasons = pd.read_csv(file_paths['reasons'])
            df_timestamps = pd.read_csv(file_paths['timestamps'])
            
            # Merge datasets
            print("Merging datasets...")
            merged_df = df_timestamps.merge(df_sentiment, on='call_id', suffixes=('', '_y'))
            merged_df = merged_df.merge(df_customer, on='customer_id', suffixes=('', '_y'))
            merged_df = merged_df.merge(df_reasons, on='call_id', suffixes=('', '_y'))
            
            # Convert datetime columns
            datetime_cols = ['call_start_datetime', 'agent_assigned_datetime', 'call_end_datetime']
            for col in datetime_cols:
                merged_df[col] = pd.to_datetime(merged_df[col])
                
            # Calculate time metrics
            print("Calculating time metrics...")
            merged_df['handle_time'] = (merged_df['call_end_datetime'] - 
                                      merged_df['agent_assigned_datetime']).dt.total_seconds()
            merged_df['wait_time'] = (merged_df['agent_assigned_datetime'] - 
                                    merged_df['call_start_datetime']).dt.total_seconds()
            
            # Add basic temporal features
            merged_df['hour'] = merged_df['call_start_datetime'].dt.hour
            merged_df['dow'] = merged_df['call_start_datetime'].dt.dayofweek
            merged_df['month'] = merged_df['call_start_datetime'].dt.month
            
            self.merged_df = merged_df
            print("Data loading completed successfully")
            return merged_df
            
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise