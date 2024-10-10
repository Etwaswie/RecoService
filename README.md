# Recommendation System for KION Cinema Database

This project involved developing a microservice for generating real-time recommendations. The system integrates multiple recommendation models, ranging from basic approaches such as popularity and random selections to more advanced algorithms, including kNN (both item-based and user-based), LightFM, DSSM, and MultiVAE.

## Model Architecture
The recommendation process utilizes a two-tier model structure. At the first level, the LightFM model is trained, which combines collaborative filtering and content-based approaches. The second tier employs LightGBM combined with a popularity-based model to enhance recommendations further.

Hyperparameter tuning is conducted using Optuna to optimize parameters like vector distance, ensuring that the model performs effectively. For cold-start users, demographic features are utilized, while users without available features receive popular recommendations.

## Libraries Used
The project employs several libraries, including:

- RecTools: For collaborative filtering.
- implicit: To handle implicit feedback data.
- RecBole: For a comprehensive recommendation framework.

## Data
The recommendation system is built using data from the MTS KION app, capturing user interactions with content over a six-month period. The dataset includes anonymous identifiers for users and content, ensuring privacy while providing rich information for the model.

### Dataset Statistics:
840,000 users,
16,000 items (movies/series),
5.5 million interactions.

### Dataset Files:
users.csv: Contains user information:

- user_id: Unique identifier for the user.
- age: Age group of the user (e.g., "M_N").
- sex: Gender of the user.
- income: Income bracket (e.g., "M_N").
- kids_flg: Indicator of whether the user has children.
  
items.csv: Contains details about the content:

- item_id: Unique identifier for the content.
- content_type: Type of content (movie, series).
- title: Title in Russian.
- title_orig: Original title.
- genres: Genres associated with the content.
- countries: Countries of origin.
- for_kids: Indicator if the content is suitable for children.
- age_rating: Age rating.
- studios: Production studios.
- directors: Directors of the content.
- actors: Main actors.
- keywords: Key terms associated with the content.
- description: Brief overview of the content.

interactions.csv: Contains user interaction data:

- user_id: Unique identifier for the user.
- item_id: Unique identifier for the content.
- last_watch_dt: Date of the last viewing.
- total_dur: Total viewing time for the content in seconds.
- content_type: Type of content (movie, series).

## Metrics
The performance of the recommendation system is evaluated using the map@10 (Mean Average Precision at 10) metric. The results from various models are presented in the project documentation, showcasing the effectiveness of different approaches in delivering relevant recommendations.

![image](https://github.com/user-attachments/assets/b62db919-d666-4496-b15b-ea62ba200fdc)
