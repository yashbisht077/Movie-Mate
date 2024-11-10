# Movie-Mate 🎥
![preview](https://github.com/yashbisht077/Movie-Mate/blob/main/utils/image.jpeg?raw=true)
#

This project is for movie enthusiasts looking to explore films based on personalized recommendations. It’s ideal for anyone who wants to discover new movies without the hassle of scrolling through endless options. Whether you’re a casual viewer or a cinephile, the Movie-Recommender provides a fast, easy way to find movies you might enjoy.

## About Me
Hi! I’m Shankar Singh, a second-year B.Tech student pursuing Computer Science and Engineering (CSE). During my second year, I developed MovieMate, a movie recommendation app, which allowed me to explore my interests in data science, machine learning, and web development.

The MovieMate app uses a content-based recommendation system to provide personalized movie suggestions based on user preferences. The app fetches movie data from The Movie Database API and leverages algorithms to recommend similar movies, making it a practical application of machine learning in real-world scenarios.

I am passionate about expanding my knowledge of technology, and I enjoy working on projects that integrate data structures, algorithms, and machine learning. Feel free to explore my repository, and reach out if you want to collaborate or discuss ideas!

Let me know if you’d like to add anything else!
## Acknowledgements

 - [Streamlit](https://streamlit.io/):
    For providing an easy-to-use framework to build the web interface and interact with users.
 - [pandas](https://pandas.pydata.org/):
    For data manipulation and analysis, particularly for handling the movie datasets.
 - [scikit-learn](https://scikit-learn.org/stable/):
    For the machine learning tools, especially the cosine_similarity function used to calculate movie similarity.
 - [numpy](https://numpy.org/):
    For numerical operations and array manipulations.
 - [OpenAI](https://openai.com/):
    For the assistance and guidance on developing the project.

    Additionally, special thanks to the open-source contributors and the broader developer community for their resources, tutorials, and support, which made building this project possible.

## Work-Flow
For a comprehensive overview of the project’s structure, please see the [Directory Structure](https://github.com/yashbisht077/Movie-Mate/blob/main/utils/Work-Flow.md) document.

## API Reference

#### Fetch movies (using TMDb’s movie database):


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required** Your API key to authenticate the request. |
| `id` | `string` | **Required** The unique identifier of the movie (e.g., 530 for A Grand Day Out). |





## Features

- Movie Selection
- Custom Number of Recommendations
- Rating Filter
- Movie Details
- Streamlit Interface
- Content-Based Recommendation Algorithm
- External API Integration
- Pickle Files for Data Storage
- Dynamic UI Elements
- Recommendations Display
- Error Handling
- Interactive Elements


## Installation

**Installation Guide**

1. **Prerequisites**
Before installing the app, make sure you have the following installed on your system:

    •	Python (Version 3.7 or higher)

    •	pip (Python package manager)


2. **Clone the Repository**
```bash
git clone https://github.com/yashbisht077/Movie-Mate.git
cd Movie-Mate
```
3. **Set Up a Virtual Environment (Optional but Recommended)**

It’s recommended to use a virtual environment to manage dependencies and avoid conflicts with system-wide packages.

•	Create a virtual environment:
```bash
python -m venv venv
```
•	Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```

4. **Install Dependencies**

Use pip to install the required dependencies listed in the requirements.txt file. If the requirements.txt file is not yet created, you can manually list dependencies, such as:
```bash
pip install -r requirements.txt
```
5. **Set Up API Key for Movie Database**

To fetch movie details (posters, ratings, etc.), you need to register for an API key from The Movie Database (TMDb).

    1.	Visit TMDb API and create an account if you don’t have one.
    2.	Obtain your API Key from the TMDb settings.
    3.	Store the API key in your code by replacing the placeholder values in the api_keys list in the app.py file.
```bash
api_keys = [
    "your_tmdb_api_key_here"
]
```
6. **Run the Streamlit App**

Once the dependencies are installed and the API key is configured, you can start the app using Streamlit. Run the following command from your project directory:
```bash
streamlit run app.py
```
7. **Access the App**

After running the command, Streamlit will start the app and provide a local URL like http://localhost:8501/ where you can access the app.

Troubleshooting

•	Issue: Missing Dependencies :
If you run into issues with missing packages, ensure you’ve activated your virtual environment (if you’re using one) and installed all necessary dependencies with pip install -r requirements.txt.

•	Issue: API Key Invalid :
If you receive errors related to fetching movie details, verify that your TMDb API key is correct and placed properly in the code.

This guide should help you get your Movie-Mate app up and running. Let me know if you encounter any issues during installation!
## License

This project is licensed under the [MIT](https://github.com/yashbisht077/Movie-Mate/blob/main/LICENSE) License. See the LICENSE file for more details.



## Screenshots

![SS](https://github.com/yashbisht077/Movie-Mate/blob/main/utils/SS.png?raw=true)
<br/>
___
