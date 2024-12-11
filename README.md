# Medicaldecisionsupportsystem
**Problem Statement**
The objective of this project is to develop an intelligent medical decision support system that analyzes patient data to assist doctors in making informed decisions about the best treatment options for individual patients. By leveraging machine learning and data analysis, the system will provide personalized treatment recommendations based on the patient’s medical history, symptoms, lab results, and other relevant factors.

**Objective**
As a significant application of artificial intelligence in the medical field, medical decision support systems demonstrate enormous potential in improving diagnostic accuracy and optimizing treatment plans. Against this backdrop, constructing efficient and reliable intelligent medical decision support systems has become a current research hotspot and challenge. This system needs to address key technical issues such as data processing, model construction, and system integration to achieve an end-to-end process from knowledge acquisition to decision support.

The development of an intelligent medication recommendation system can greatly benefit the healthcare industry by providing personalized and targeted treatment plans using artificial intelligence. This system analyzes patient data. The goal is to improve patient outcomes and reduce healthcare costs. The system utilizes machine learning algorithms to analyze large amounts of patient data, identifying patterns and relationships that may not be visible to human clinicians.

The proposed system takes into account meta-data about the problem, which can vary greatly, depending on the problem. The system gives possible recommendations that might be relevant to the user.

****Modules:**
**1. Data Collection**
Utilized the excel file and imported it to the jupyter notebook and imported all the necessary libraries like pandas, seaborn, matplotlib.

![000](https://github.com/user-attachments/assets/0fab91af-ba82-4a75-86be-ea9809674ec7)


**2. Data Exploration/ Data Pre-Processing**
Performed Exploratory Data Analysis by checking for null values, information of int or object or float values, descriptive statistics and dropping the null values.

![001](https://github.com/user-attachments/assets/4e057fe1-86a8-44e4-952e-15b735e9fedd)

![002](https://github.com/user-attachments/assets/825fac77-5359-42b4-abd1-7ed22e52e003)


**3. Feature Engineering**
From the entire set of columns, we could see that only the 'Sex' column has values in object format. For the machine learning model to understand, we will be converting 'Sex' column into a numerical column using Label Encoder technique. The output of 'Sex' column would now be in 0s and 1s where 0 denotes Male and 1 denotes Female.

![004](https://github.com/user-attachments/assets/b97b4a77-c048-4c32-9d6a-8cda3d834ef5)


Using correlation function, we could identify which of the parameter is contributing more to the medical evaluation process.

![005](https://github.com/user-attachments/assets/c582f211-2adf-4869-a409-5f529260bec7)

Using pie-chart, we could analyse how much percentage of data requires medical decision support system and how many doesn't require with '0' meaning ' does not requires medical decision support system' and with '1' meaning 'requires medical decision support system'. 

![006](https://github.com/user-attachments/assets/5ccc2358-54c1-4b9e-84a1-223f488e943b)

Using boxplot, we tried to find out the optimal value for the medical parameters which can then be used for training and testing omitting the outliers.

![011](https://github.com/user-attachments/assets/59e4aa9a-e20e-4c8a-bca6-efe1d18f6984)

![012](https://github.com/user-attachments/assets/87152da2-c73d-4aea-a44b-0ca0f15b2a86)

**4. Model Training**
Assigning input values to variable x and output values to variable y

![013](https://github.com/user-attachments/assets/5e4b915d-3599-46b1-be4a-83ce5d4fdd71)

Using sklearn library, we split the training and testing data with a training size of 0.70 and random state value as 42.
Using different machine learning models, we tried to predict the accuracy of the model. Amongst all the trail and errors, decision tree regressor showed high accuracy compared to other models like logistic regression, random forest classfier.

![014](https://github.com/user-attachments/assets/c6d4344e-a12f-40a2-8f87-c7c0632a7c3e)

Using bar chart, we have visualized the accuracy score amongst the machine learning models.

![015](https://github.com/user-attachments/assets/0c39b774-56f9-4355-8888-e8147bad90cc)

**5. Model Deployment**
Using streamlit, we have delployed a machine learning model,where we could predict whether a person needsthe medical decision support system or not.

![016](https://github.com/user-attachments/assets/8f16d7ba-bba6-4530-a0e4-49c0b8b607b0)

![017](https://github.com/user-attachments/assets/a6d4bd7c-891d-4fff-891f-8f314b18f2c8)

![018](https://github.com/user-attachments/assets/021d17ab-9023-4c43-9cdf-6ac466468c0f)

![019](https://github.com/user-attachments/assets/ea32c126-ad78-4536-9708-43c8133ea624)

![020](https://github.com/user-attachments/assets/269f5682-05ac-43c4-bd10-ce1beef9b343)


