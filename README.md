# PROYECTO-2--IRONHACK

![polucion](https://github.com/Lydia-Arocena/PROYECTO-2-APIS/blob/main/POLUCION.png.jpg)

### 1. Introduction:
This project aims to analyze several factors that affect Life Quality for each city worldwide. 


### 2. Hypothesis:
Once this analysis has been carried out, I have formulated 6 hypothesises in order to verify or decline them:
    1. There is a better quality life in South American countries than in Oceania countries.
    2. Air quality has a positive correlation with Outdoor score.
    3. Highest Average Scores in North America and Asia belong to  Canada and Singapore, respectively.
    4. In average, life quality in the Iberian Peninsula is better than in Italy and France.
    5. Tunisia has the highest score while Tanzania has the lowest.
    6. Japan's life quality based on its Healthcare system is the highest in the world.

### 3. Data:
The csv file about life quality in different cities worldwide was downloaded from https://www.kaggle.com/.
This csv has been enriched by the information given by Waki API (https://api.waqi.info/feed). This API informs about air quality by cities and its clasification.

In order to develop this project, I have used the following files:
    - "1.Limpieza_enriquecimientoAPI": In this Jupyter Notebook file, I have cleaned my dataframe resulting from the csv file. In order to do so, I have deleted some unuseful columns, I have renamed others and I have also created a new column called "Average Score" which is the mean of all the other columns.
    Then, I have enriched my resulted dataframe with my API information and added a new column. Additionally, by using another function, this information has been classified in different categories that have been added to the dataframe in a second new column.
    - "2. Visualizacionfinal_contrastehipotesis": In this second Jupyter Notebook file, I have tried to verify or reject my 6  hypothesises by using graphs from different libraries.
    - "main.py": a python file where the code can be run in one go.
    - "src": it is a directory that conteins the above mentioned Jupyter Notebooks files.
    - ".env": a file to keep my token unseen by others.
    - ".gitignore": a file where each line contains a pattern for files/directories to ignore.

SOURCES:
    -https://www.kaggle.com/ (dataset).
    -https://api.waqi.info/feed (API).
    - Some libraries:
        - Requests (https://docs.python-requests.org/en/latest/)
        - Numpy (https://numpy.org/doc/)
        - Os (https://docs.python.org/3/library/os.html)
        - Pandas (https://pandas.pydata.org/)
        - Load_dotenv (https://pypi.org/project/python-dotenv/)
        - Seaborn (https://seaborn.pydata.org/)
        - Matplotli.pyplot (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)
        - Plotly.express (https://plotly.com/python-api-reference/plotly.express.html)


 
### 4. Results:
    - **Hypothesis 1**: This hypothesis could be rejected as the average score of quality life in Oceania  is higher than in South America.
    - **Hypothesis 2**: There in not any correlation between "Air Quality Level" and "Outdoor score": there are many continents with a good air quality level that have a very low Outdoor Score. Therefore, this hypothesis could be rejected.
    - **Hypothesis 3**: Canada and Singapore have the highest average scores in North America and Asia, respectively. Then, we can conclude that this hypothesis could be accepted.
    - **Hypothesis 4**: Spain and Portugal have a higher score than their neighbours France and Italy. Therefore, this hypothesis could be accepted. 
    - **Hypothesis 5**:  It is indeed true that Tunisia has the highest score while Tanzania has the lowest. Thus, we could state that this hypothesis could be accepted.
    - **Hypothesis 6**: Japan has the highest quality life score based on its Healthcare system in the whole world. Therefore, this hypothesis can be also accepted.