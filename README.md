# BOSS Bidding Analysis

Want to see the app in action? Check it out here: https://bossbidding.streamlit.app

The task is simple: take past year SMU BOSS bidding data and conduct statistical analysis to predict what the minimum and median bids might be for future bidding windows.

The execution is just as simple: Use simple, single-variable linear regression (bid price against time) for the prediction. Now extend it to every course that has ever
been bidded for in SMU in the past four years and create a UI and put it on a web application, so I don't need to keep running the same cells on a Jupyter Notebook every time
I need to check the predicted bid prices for any courses I want to bid for.

### Packages Used
- streamlit
- pandas
- scikit-learn
- gcsfs

### Method
1. `load_data.py` loads the spreadsheets from Google Cloud Storage and cleans the data, removing whitespace and dropping NA and 0.0 values
2. `main.py` features Streamlit methods for rendering the web application, and calls `regression.get_analysis_df()` using the filters specified by the user, such as course name, bidding window and round, and professor.
3. `regression.py` uses a Linear Regression model from `scikit-learn` to predict future minimum and median successful bids given the filters specified. Additional logic included to account for possible negative predictions or invalid inputs. Implementation for visualisation of the regression plot with `matplotlib` and `seaborn` is also included.

### Data storage
Access to BOSS results is restricted to SMU staff and faculty behind a login page on the SMU website. Because I don't want to commit Excel files to the repository, I needed to
move the data elsewhere. I used Google Cloud's free tier, which gives me 5 GB for cloud storage for free so long as I set a specific location for the data to be stored.

In essence, instead of the app accessing the data that lives in a subfolder in the working directory/repo, it retrieves the data from GCS, compiles all of it by appending to
a pandas DataFrame, and then conducting analysis from there.
