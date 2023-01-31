from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Run this app with `python app.py` and visit http://127.0.0.1:8050/ in your web browser.
app = Dash(__name__)


# Reading in the data sets downloaded from https://data.louisvilleky.gov
expenditures_2019 = pd.read_csv('Lou_Data/eExpenditures_2019.csv', low_memory=False)
expenditures_2020 = pd.read_csv('Lou_Data/eExpenditures_2020.csv', low_memory=False)
expenditures_2021 = pd.read_csv('Lou_Data/eExpenditures_2021.csv', low_memory=False)
expenditures_2022 = pd.read_csv('Lou_Data/eExpenditures_2022.csv', low_memory=False)

stops_2019 = pd.read_csv('Lou_Data/LMPD_STOP_DATA_2019.csv', low_memory=False)
stops_2020 = pd.read_csv('Lou_Data/LMPD_STOP_DATA_2020.csv', low_memory=False)
stops_2021 = pd.read_csv('Lou_Data/LMPD_STOP_DATA_2021.csv', low_memory=False)
stops_2022 = pd.read_csv('Lou_Data/LMPD_STOP_DATA_2022.csv', low_memory=False)

crime_data_2018 = pd.read_csv('Lou_Data/Louisville_Metro_KY_-_Crime_Data_2018.csv', low_memory=False)
crime_data_2019 = pd.read_csv('Lou_Data/Louisville_Metro_KY_-_Crime_Data_2019.csv', low_memory=False)
crime_data_2020 = pd.read_csv('Lou_Data/Louisville_Metro_KY_-_Crime_Data_2020.csv', low_memory=False)
crime_data_2021 = pd.read_csv('Lou_Data/Louisville_Metro_KY_-_Crime_Data_2021.csv', low_memory=False)
crime_data_2022 = pd.read_csv('Lou_Data/Louisville_Metro_KY_-_Crime_Data_2022.csv', low_memory=False)

employee_characteristics = pd.read_csv('Lou_Data/Louisville_Metro_KY_-_LMPD_Employee_Characteristics.csv', low_memory=False)


expenditures_All = pd.concat([expenditures_2019, expenditures_2020, expenditures_2021, expenditures_2022])
stops_All = pd.concat([stops_2019, stops_2020, stops_2021, stops_2022])
craime_data_All = pd.concat([crime_data_2018, crime_data_2019, crime_data_2020, crime_data_2021, crime_data_2022])


expenditure_bar = px.bar(expenditures_All, x="DepartmentName", y="Budget_Type", color="Fiscal_Year", barmode ="group")


app.layout = html.Div(children=[
    html.H1(children='Louisville Metro Expenditure Data, 2019- 2022'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        # id='Test',
        figure=expenditure_bar
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)