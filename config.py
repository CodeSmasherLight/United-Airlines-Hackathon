import os

# Project paths
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(PROJECT_ROOT, 'data')
RESULTS_PATH = os.path.join(PROJECT_ROOT, 'results')

# File paths
FILE_PATHS = {
    'calls': os.path.join(DATA_PATH, 'calls.csv'),
    'sentiment': os.path.join(DATA_PATH, 'sentiment.csv'),
    'customer': os.path.join(DATA_PATH, 'customer.csv'),
    'reasons': os.path.join(DATA_PATH, 'reasons.csv'),
    'timestamps': os.path.join(DATA_PATH, 'timestamps.csv')
}

# Analysis parameters
SENTIMENT_THRESHOLD = 0.5
HANDLE_TIME_PERCENTILE = 0.25
COMPLEXITY_BINS = 4