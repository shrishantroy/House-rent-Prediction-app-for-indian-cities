# House-rent-prediction-app-for-indian-cities
India is a country with huge population, resulting into massive house renting requirements and a well established real estate system. This project is all about developing an application that predicts the rent of a house based on some parameters. The ML model that drives it is trained using Random Forest Regression. Python's Streamlit library was used to develop the interface and the frontend. <br>
<br>
**The Dataset and Preprocessing**<br>
I used a dataset from kaggle for this project(https://www.kaggle.com/datasets/juhibhojani/house-price). It comprises 81 different cities in India. In the preprocessing stage I dropped some columns that were mostly null, **please note Price (in rupees) is the target variable**. However, columns like 'Carpet Area' and 'Super Area' were over 50% null, yet not dropped as they are very important for the rent prediction. Instead, I filled the nulls with medians and attached a seperate feature(carpet area missing and super area missing) each which takes value 1 when the area value is missing(null) and 0 when it is not. I used hot encoding to on categorical data, while I used target encoding to convert the location strings to float type value. Before that, I replaced all the nulls in float type columns with means and with 'unknown' in string type column. The encoding map for hot encoding and the location list are attached.The columns like amount, bathroom, balcony were converted to floats from strings, while the Floor column was used to introduce two new features, the floor number and total floors.<br>
<br>
**Model Training and Performance**<br>
The model was trained using Random Forest Algorithm, with 80% of the dataset while rest of it was used to evaluate its performance.The R2 score is satisfactory(around 0.8037). But the distribution of price rent data is heavily scewed ranging from 0 to 6.7e6. As the histogram shows the test data mostly is within 0 to 4e5 but a small number of values range in 10^6 order<br>
<p align="center">
<img width="632" height="444" alt="image" src="https://github.com/user-attachments/assets/55eb44e5-98a1-4b69-a943-449181f3ef4b" />
</p><br>
The edge high values introduce large errors for some cases, increasing the RMSE.As we can see most of the prediction error is within the range0~12000. Where previously seen most of the test values are 0~4e5. So, the degree of error is acceptable. But It is visible that a tiny portion of error also exists in 10^6 order. This high error for some cases is the main reason for the huge RMSE. Not a big issue since this occurs for a very small number of cases<br>
<p align="center">
<img width="700" height="469" alt="image" src="https://github.com/user-attachments/assets/74b4dc7c-c612-48b4-a4ce-6e9457a82702" />
</p><br>
The mean absolute error is around 563, and the average value of test data is found to be around 7500 and the average value of predicted data is around 7600. Which indicates, the prediction is good for most of the cases with reasonable error.<br>
<p align="center">
<img width="685" height="457" alt="image" src="https://github.com/user-attachments/assets/cd7cbb03-b21e-4d5c-9c73-58ce458417aa" />
</p><br>
<p align="center">
<img width="767" height="472" alt="image" src="https://github.com/user-attachments/assets/505df14b-38ee-4922-b399-0456364be2ff" />
</p>
as we can see there is reasonable prediction for most of the data, with a reasonably linear relationship. But for edge case data, which is around 4e6, it predicts 3e6, that means 1e6 error in the edge case. Proving our assumption that the error in edge case data is increasing the RMSE, the prediction is good for most of the data.<br>
<br>
I used the model to build a web application using streamlit. Access the app through this link. It may take a few minutes to open as the app is large.
https://house-rent-prediction-app-for-indian-cities-kke5kgarw6qzrihdjw.streamlit.app/

