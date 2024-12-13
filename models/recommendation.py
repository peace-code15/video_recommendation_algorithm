from sklearn.preprocessing import StandardScaler
import pandas as pd

class RecommendationEngine:

    def __init__(self, user_data, video_data):
        self.user_data = user_data
        self.video_data = video_data

    def preprocess_data(self):
        try:
            # Convert columns to numeric, coercing errors into NaN
            self.video_data.iloc[:, 1:] = self.video_data.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")
            self.video_data.dropna(inplace=True)  # Drop rows with NaN after conversion
            
            # Apply StandardScaler to the data
            scaler = StandardScaler()
            self.video_data.iloc[:, 1:] = scaler.fit_transform(self.video_data.iloc[:, 1:])
            
            print("Data preprocessing completed successfully.")

        except Exception as e:
            print(f"Error during data preprocessing: {str(e)}")

    def recommend_videos(self):
        self.preprocess_data()

        # Placeholder for your video recommendation logic
        print("Recommendation logic is implemented here.")