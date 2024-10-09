from config import FILE_PATHS, RESULTS_PATH
from src.data_loader import DataLoader
from src.aht_analysis import AHTAnalyzer
from src.self_service_analysis import SelfServiceAnalyzer
from src.call_patterns_analysis import CallPatternAnalyzer
from src.utils import save_results, ensure_directory

def main():
    try:
        # Ensure results directory exists
        ensure_directory(RESULTS_PATH)
        
        # Load data
        print("Loading data...")
        loader = DataLoader()
        merged_df = loader.load_data(FILE_PATHS)
        
        # Perform AHT analysis
        print("Performing AHT analysis...")
        aht_analyzer = AHTAnalyzer(merged_df, RESULTS_PATH)
        aht_results = aht_analyzer.analyze_factors()
        save_results(aht_results, RESULTS_PATH, 'aht_analysis')
        
        # Perform self-service analysis
        print("Performing self-service analysis...")
        self_service_analyzer = SelfServiceAnalyzer(merged_df)
        self_service_results = self_service_analyzer.analyze_opportunities()
        save_results(self_service_results, RESULTS_PATH, 'self_service_analysis')
        
        # Perform call pattern analysis
        print("Performing call pattern analysis...")
        pattern_analyzer = CallPatternAnalyzer(merged_df)
        pattern_results = pattern_analyzer.analyze_patterns()
        save_results(pattern_results, RESULTS_PATH, 'call_patterns_analysis')
        
        print("Analysis completed successfully!")
        
    except Exception as e:
        print(f"Error in main execution: {str(e)}")
        raise

if __name__ == "__main__":
    main()