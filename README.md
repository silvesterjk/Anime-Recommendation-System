#Building a Content-Based Anime Recommendation System

In this project, I developed a content-based recommendation system for anime using an ETL (Extract, Transform, Load) pipeline and a collaborative filtering approach. The content-based anime recommendation system has several potential business use cases and benefits. Here are some key business cases for implementing such a system:
1. Personalized Recommendations: The system provides tailored recommendations based on users' preferences, enhancing their overall viewing experience.
2. Increased User Engagement: By offering relevant anime suggestions, the system keeps users engaged and encourages longer viewing sessions.
3. Improved User Satisfaction: Users are more likely to be satisfied when they discover anime shows that align with their interests, leading to higher retention rates.

And many more.

#1 Data Extraction and Cleaning:
The first step involves extracting the anime data from a CSV file named "myanimelist_data.csv." I used the pandas library to read the CSV file into a DataFrame. 

<img width="1084" alt="image" src="https://github.com/silvesterjk/DEProject/assets/108580657/9aa78fd4-9eb3-4dff-a67e-4991a4c489c0">
<img width="897" alt="image" src="https://github.com/silvesterjk/DEProject/assets/108580657/c7151149-8d58-4f26-80f1-ff861da79c27">

The data contained information such as anime IDs, titles, scores, genres, types, episodes, members, and premiering details. To ensure data consistency, I performed cleaning operations on the anime titles using regular expressions. This involved removing unwanted characters and standardizing the text format. Additionally, I selected relevant columns from the DataFrame for further analysis and recommendation.

<img width="897" alt="image" src="https://github.com/silvesterjk/DEProject/assets/108580657/9ac83ab2-0a45-4a4c-a1a8-884abffae3d4">

The first step involves extracting the anime data from a CSV file named "myanimelist_data.csv." I used the pandas library to read the CSV file into a DataFrame. The data contained information such as anime IDs, titles, scores, genres, types, episodes, members, and premiering details. To ensure data consistency, I performed cleaning operations on the anime titles using regular expressions. This involved removing unwanted characters and standardizing the text format. Additionally, I selected relevant columns from the DataFrame for further analysis and recommendation.

#2 Data Storage in PostgreSQL:
To facilitate efficient data retrieval and scalability, I stored the cleaned anime data in a PostgreSQL database. Using the SQLAlchemy library, I established a connection to the database and created an engine for data insertion. The pandas DataFrame was then written to a table named "anime_table2" within the database.

<img width="1286" alt="image" src="https://github.com/silvesterjk/DEProject/assets/108580657/bcc151de-1dbb-4f9e-a4b5-502753b7717d">

To facilitate efficient data retrieval and scalability, I stored the cleaned anime data in a PostgreSQL database. Using the SQLAlchemy library, I established a connection to the database and created an engine for data insertion. The pandas DataFrame was then written to a table named "anime_table2" within the database.

#3 Anime Recommendation using Content-Based Filtering:
For the recommendation system, I implemented a content-based filtering approach. The main idea is to recommend anime based on the similarity of their content, specifically the genres. I used the TfidfVectorizer from scikit-learn to transform the genres into a sparse matrix, capturing the importance of each genre in each anime.

<img width="689" alt="image" src="https://github.com/silvesterjk/DEProject/assets/108580657/b35c605d-d5ac-4f5d-9e39-866549961f4a">


Next, I computed the sigmoid kernel, which measures the similarity between anime based on their genre profiles. This resulted in a similarity matrix that represents the pairwise similarities between all anime in the dataset.

To make recommendations, I created a function that takes an input anime title and retrieves the top 10 most similar anime based on the sigmoid kernel scores. The function returns a DataFrame with the recommended anime titles and their respective ratings.

#4 Integration and Automation with Apache Airflow:
To automate the ETL pipeline and recommendation system, I leveraged Apache Airflow. I created a DAG (Directed Acyclic Graph) named "anime_etl_pipeline" that schedules the execution of the ETL process and the recommendation task. The ETL process is triggered daily, ensuring up-to-date data in the database.

<img width="1434" alt="image" src="https://github.com/silvesterjk/DEProject/assets/108580657/d69775e1-0a3d-4755-9e17-f9d7b7d80aa2">


