# data-analysis-python
<p>This is projects in python related to data analysis</p>
<p><b>Explanation:</b></p>
<ol>
  <li><b>Import Libraries:</b> Imports pandas for data manipulation and matplotlib.pyplot for plotting.</li>
<li><b>analyze_data() Function:</b>Takes the CSV file name as input.</li>
<li><b>Reads CSV:</b> Uses pd.read_csv() to load the data into a DataFrame.</li>
<li><b>Analysis:</b>
  df.describe() provides summary statistics (mean, count, etc.).
df.corr() calculates correlations between numerical columns.</li>
<li><b>Visualization:</b>
  Creates a histogram of a specified column (column_name).
Creates a scatter plot between two columns (column1 and column2).
Saves the plots as PNG images.</li>
<li><b>Error Handling:</b> Includes try-except blocks to handle potential errors like file not found or other exceptions during analysis.</li></ol>
