# video_recommendation_algorithm

**Overview**
This project implements a basic **Video Recommendation System** using a Flask-based API backend. The system provides recommendations based on user interactions with videos and can be extended to use advanced recommendation algorithms like content-based filtering, collaborative filtering, or hybrid models.

--------------

**Features**
- **RESTful API**: 
  - `/recommend_videos`: Provides video recommendations based on user and video data.
- **Data Fetching**:
  - Fetches video and user interaction data from multiple APIs.
  - Mock data is used for demonstration purposes.
- **Recommendation Logic**:
  - Implements a basic content-based filtering approach.

--------------

**Project Structure**
```
.
├── app/
│   ├── __init__.py      # Application setup
│   ├── routes.py        # API routes
├── data/
│   ├── fetch_data.py    # Data fetching logic
├── models/
│   ├── recommendation.py # Recommendation algorithm implementation
├── tests/
│   ├── test_routes.py   # Test cases for API routes
├── main.py              # Entry point for the Flask app
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
```

-------------

**Setup Instructions**

**1. Clone the Repository**
```bash
git clone <repository-url>
cd <repository-folder>
```

### **2. Install Dependencies**
Make sure you have Python installed. Then, install the required Python packages:
```bash
pip install -r requirements.txt
```

**3. Run the Application**
Start the Flask application:
```bash
python main.py
```
The app will be accessible at `http://127.0.0.1:5000/`.

---

**Endpoints**

**/recommend_videos**
- **Method**: `GET`
- **Description**: Returns a list of recommended videos.
- **Parameters**: 
  - `user_data`: Information about the user.
  - `video_data`: Metadata of videos.
- **Example Request**:
```bash
curl -X GET http://127.0.0.1:5000/recommend_videos -H "Content-Type: application/json" -d '{"user_data":"SampleUser", "video_data":"SampleVideo"}'
```
- **Example Response**:
```json
{
  "message": "Successfully received the parameters",
  "user_data": "SampleUser",
  "video_data": "SampleVideo"
}
```

--------------

**Development Details**

**1. Data Fetching**
Data is retrieved from the following APIs:
- Viewed videos
- Liked videos
- Inspired videos
- Rated videos
- Posts metadata
- Users data

For testing purposes, mocked data is used.

**2. Recommendation Algorithm**
The system currently uses **content-based filtering** to recommend videos. 
- Recommendations are based on video metadata and user history.

Future enhancements include:
- **Collaborative Filtering**: Use user-item interaction data.
- **Hybrid Models**: Combine content-based and collaborative filtering.

-----------------

**Future Work**
- Implement advanced recommendation algorithms.
- Add support for real-time data fetching.
- Optimize API performance for large datasets.
- Enhance frontend integration for better user experience.

----------------

**Contributors**
- **Nikita Nodal** - Developer and Maintainer
