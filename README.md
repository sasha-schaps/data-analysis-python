# data-analysis-python
This is projects in python related to data analysis
<b>Explanation:</b>
Import Libraries: Imports pandas for data manipulation and matplotlib.pyplot for plotting.
analyze_data() Function:
Takes the CSV file name as input.
Reads CSV: Uses pd.read_csv() to load the data into a DataFrame.
Analysis:
df.describe() provides summary statistics (mean, count, etc.).
df.corr() calculates correlations between numerical columns.
Visualization:
Creates a histogram of a specified column (column_name).
Creates a scatter plot between two columns (column1 and column2).
Saves the plots as PNG images.
Error Handling: Includes try-except blocks to handle potential errors like file not found or other exceptions during analysis.
