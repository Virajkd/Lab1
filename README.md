Lab 1

1.Write a program to count the number of vowels and consonants present in an input string.
2.Write a program that accepts two matrices A and B as input and returns their product AB. Check if A & B are multipliable; if not, return error message.
3.Write a program to find the number of common elements between two lists. The lists contain integers.
4.Write a program that accepts a matrix as input and returns its transpose.

Lab 2
1. Please refer to the “Purchase Data” worksheet of Lab Session Data.xlsx. Please load the data and segregate them into 2 matrices A & C (following the nomenclature of AX = C).Do the following activities.
  •What is the dimensionality of the vector space for this data?
  •How many vectors exist in this vector space?
  •What is the rank of Matrix A?
  •Using Pseudo-Inverse find the cost of each product available for sale.

2. Use the Pseudo-inverse to calculate the model vector X for predicting the cost of the products available with the vendor.
3. Mark all customers (in “Purchase Data” table) with payments above Rs. 200 as RICH and others as POOR. Develop a classifier model to categorize customers into RICH or POOR class based on purchase behavior.
4. Please refer to the data present in “IRCTC Stock Price” data sheet of the above excel file. Do the following after loading the data to your programming platform.
   •Calculate the mean and variance of the Price data present in column D.
   •Select the price data for all Wednesdays and calculate the sample mean. Compare the mean with the population mean and note your observations.
   •Select the price data for the month of Apr and calculate the sample mean. Compare the mean with the population mean and note your observations.
   •From the Chg% (available in column I) find the probability of making a loss over the stock. (Suggestion: use lambda function to find negative values)
   •Calculate the probability of making a profit on Wednesday.
   •Calculate the conditional probability of making profit, given that today is Wednesday.
   •Make a scatter plot of Chg% data against the day of the week

5. Data Exploration: Load the data available in “thyroid0387_UCI” worksheet. Perform the following tasks:
   •Study each attribute and associated values present. Identify the datatype (nominal etc.) for the attribute.
   •For categorical attributes, identify the encoding scheme to be employed. (Guidance: employ label encoding for ordinal variables while One-Hot encoding may be employed        for nominal variables).
   •Study the data range for numeric variables.
   •Study the presence of missing values in each attribute.
   •Study presence of outliers in data.
   •For numeric variables, calculate the mean and variance (or standard deviation).

6.Data Imputation: employ appropriate central tendencies to fill the missing values in the data variables. Employ following guidance.
  •Mean may be used when the attribute is numeric with no outliers
  •Median may be employed for attributes which are numeric and contain outliers
  •Mode may be employed for categorical attributes

7. Data Normalization / Scaling: from the data study, identify the attributes which may need normalization. Employ appropriate normalization techniques to create normalized set of data.
8. Similarity Measure: Take the first 2 observation vectors from the dataset. Consider only the attributes (direct or derived) with binary values for these vectors (ignore other attributes). Calculate the Jaccard Coefficient (JC) and Simple Matching Coefficient (SMC) between the document vectors. Use first vector for each document for this. Compare the values for JC and SMC and judge the appropriateness of each of them.
9. Cosine Similarity Measure: Now take the complete vectors for these two observations (including all the attributes). Calculate the Cosine similarity between the documents by using the second feature vector for each document.
10. Heatmap Plot: Consider the first 20 observation vectors. Calculate the JC, SMC and COS between the pairs of vectors for these 20 vectors. Employ similar strategies for coefficient calculation as in A4 & A5. Employ a heatmap plot to visualize the similarities.
