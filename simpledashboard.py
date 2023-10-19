# importing libraries 
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
# define function to display main for our website
def main_page():
    st.title('Exploring Cars data')

# a for loop to put 5 empty lines between title and container underneath!    
    for i in range(5):
            st.text('\n')

# reading our data cars
    cars = pd.read_csv('cars_clean.csv')

# a variable num to call numerical description
    num = cars.describe()

# a variable cat to call categorical description
    cat = cars.describe(include = 'O')

# define a variable descriptive to to let us choose between categorical and numerical descriptive statistics!
    descriptive = st.multiselect('Pick the desired descriptive statistics:', ['Numerical descriptive statistics','Categorical descriptive statistics'])
    
# making the main page container followed by the choice of descriptive choices and a subheader   
    with st.container():
        if 'Numerical descriptive statistics' in descriptive:
            st.subheader('Numerical descriptive statistics')
            st.dataframe(num, use_container_width=True)

        if 'Categorical descriptive statistics' in descriptive:
            st.subheader('Categorical descriptive statistics')
            st.dataframe(cat, use_container_width=True)
       
    
# adding another choice to the main page to choose single or multiple columns to display
    options = st.multiselect(
    'Choose one or multiple columns to display',
    cars.columns)

    # adding filter to display each column value
    # iterate over each selected column in options. For each column, we extract its unique values using cars[column].unique()
    filters = {}
    for column in options:
        values = cars[column].unique()
        selected_values = st.multiselect(f" values for {column}", values)
        if selected_values:
            filters[column] = selected_values

    # a list comprehension that creates a new list called columns_to_display.
    # The purpose of this code is to filter out any columns that are not present in the cars dataframe or not selected in the options.
    columns_to_display = [cars[column] for column in options if column in cars.columns]

    # to display columns beside each other( concat )
    if columns_to_display:
        df = pd.concat(columns_to_display, axis=1)
        
    # to display each column values from filter
        if filters:
            filtered_df = df[df.apply(lambda row: all(row[column] in filters[column] for column in filters), axis=1)]
            filtered_df = filtered_df.reset_index(drop=True) # Reset the index
            st.write(filtered_df)
            num_rows = len(filtered_df)
            st.write(f"Number of rows: {num_rows}")
        else:
            st.write(df)
    else:
        st.write("No columns selected.") 






# define function to display second page for our website
def secondPage():
    st.title('Univariate analysis')
# a for loop to put 5 empty lines between title and container underneath!    
    for i in range(5):
            st.text('\n')
# reading our data cars
    cars = pd.read_csv('cars_clean.csv')

#1st chart
# Create a checkbox in the sidebar to filter by brand
    brand_filter = st.sidebar.checkbox('Brand filter')

# Filter the data based on selected brands
    if brand_filter:
        selected_brands = st.sidebar.multiselect(
            'Choose one or multiple brands to display',
            cars['brand'].unique())
        cars = cars[cars['brand'].isin(selected_brands)]

 # Create the chart
    fig = px.histogram(cars, 
                       x='brand',  
                       color='brand', 
                       text_auto=True, 
                       title='Cars brands distribution').update_xaxes(categoryorder="total descending")

# Display the chart
    st.plotly_chart(fig, use_container_width=True)




#2nd chart
# Create a checkbox in the sidebar to filter by color
    color_filter = st.sidebar.checkbox('Color filter')

# Filter the data based on selected brands
    if color_filter:
        selected_color = st.sidebar.multiselect(
            'Choose one or multiple color to display',
            cars['color'].unique())
        cars = cars[cars['color'].isin(selected_color)]

 # Create the chart
    fig = px.histogram(cars, 
                       x='color',  
                       color = 'color',
                       text_auto=True, 
                       title='Cars colors distribution').update_xaxes(categoryorder="total descending")

# Display the chart
    st.plotly_chart(fig, use_container_width=True)



#3rd chart
# Create a checkbox in the sidebar to filter by color
    year_filter = st.sidebar.checkbox('Years filter')

# Filter the data based on selected brands
    if year_filter:
        selected_year = st.sidebar.multiselect(
            'Choose one or multiple year to display',
            cars['year'].unique())
        cars = cars[cars['year'].isin(selected_year)]

 # Create the chart
    fig = px.histogram(cars['year'].value_counts().reset_index(), 
                       x='year', 
                       y='count',
                       color= 'year',
                       text_auto=True,
                       nbins=50, 
                       title='Cars years distribution')

# Display the chart
    st.plotly_chart(fig, use_container_width=True)




#4th chart
# Create the chart
    fig = px.violin(cars, x='price_in_euro', title='Price Distribution')

# Display the chart
    st.plotly_chart(fig, use_container_width=True)



#5th chart
# Create the chart
    fig = px.box(cars, x='power_ps', title='power_ps Distribution')

# Display the chart
    st.plotly_chart(fig, use_container_width=True)



#6th chart
# Create the chart
    fig = px.pie(cars, 'transmission_type', title='transmission_type Distribution', hole=0.7)
# Display the chart
    st.plotly_chart(fig, use_container_width=True)


#7th chart
# Create a checkbox in the sidebar to filter by color
    fuel_filter = st.sidebar.checkbox('Fuel filter')

# Filter the data based on selected brands
    if fuel_filter:
        selected_fuel = st.sidebar.multiselect(
            'Choose one or multiple fuel to display',
            cars['fuel_type'].unique())
        cars = cars[cars['fuel_type'].isin(selected_fuel)]



# Create the chart
    fig = px.pie(cars, 'fuel_type', title='fuel_type Distribution').update_traces(pull=[0.1, 0, 0])
# Display the chart
    st.plotly_chart(fig, use_container_width=True)



#8th chart
# Create the chart
    fig = px.box(cars, 'fuel_consumption_l_100km', title='fuel consumption Distribution')
# Display the chart
    st.plotly_chart(fig, use_container_width=True)


#9th chart
# Create the chart
    fig = px.box(cars, 'mileage_in_km', title='mileage_in_km Distribution')
# Display the chart
    st.plotly_chart(fig, use_container_width=True)


#10th chart
# Create a checkbox in the sidebar to filter by color
    car_status_filter = st.sidebar.checkbox('car_status filter')

# Filter the data based on selected brands
    if car_status_filter:
        selected_filter = st.sidebar.multiselect(
            'Choose one or multiple status to display',
            cars['car_status'].unique())
        cars = cars[cars['car_status'].isin(selected_filter)]

 # Create the chart
    fig = px.bar(cars['car_status'].value_counts().reset_index(), 
                       x='car_status', 
                       y='count',
                       color='car_status',
                       text_auto=True, 
                       title='car_status_filter distribution')

# Display the chart
    st.plotly_chart(fig, use_container_width=True)






# define function to display second page for our website
def thirdPage():
    st.title('Bivariate analysis')
# a for loop to put 5 empty lines between title and container underneath!    
    for i in range(5):
            st.text('\n')
# reading our data cars
    cars = pd.read_csv('cars_clean.csv')



# Create a checkbox in the sidebar to filter by brand
    brand_filter = st.sidebar.checkbox('Filter by brand')

    # Group by brand and transmission type and calculate the average price
    transmission = cars.groupby(['brand', 'transmission_type'])[['price_in_euro']].mean().reset_index()

    # Filter the data based on selected brands
    if brand_filter:
        selected_brands = st.sidebar.multiselect(
            'Choose one or multiple brands to display',
            cars['brand'].unique())
        transmission = transmission[transmission['brand'].isin(selected_brands)]

    # Create the chart
    fig = px.histogram(transmission, 
                       x='brand', 
                       y='price_in_euro', 
                       color='transmission_type', 
                       barmode='group', 
                       text_auto=True, 
                       title='Average car brands price by transmission type')

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)






# Create a checkbox in the sidebar to filter by consumption
    consumption_filter = st.sidebar.checkbox('Filter by fuel consumption')

# Group by brand and price_in_euro and calculate the fuel_consumption_l_100km
    cons_price =cars.groupby(['brand','fuel_consumption_l_100km'])[['price_in_euro']]\
            .mean().reset_index().sort_values(by='fuel_consumption_l_100km')

    # Filter the data based on selected consumption
    if consumption_filter:
        selected_consumption = st.sidebar.multiselect(
            'Choose one or multiple consumption to display',
            sorted(cars['fuel_consumption_l_100km'].unique()))
        cons_price = cons_price[cons_price['fuel_consumption_l_100km'].isin(selected_consumption)]

    # Create the chart
    fig = px.histogram(cons_price, 
                       x='fuel_consumption_l_100km', 
                       y='price_in_euro', 
                       color='brand', 
                       barmode='group', 
                       text_auto=True, 
                       title='Car\'s prices by fuel consumption ')

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)






# Create a checkbox in the sidebar to filter by year
    year_filter = st.sidebar.checkbox('Filter by year')

# Group by year , price_in_euro and sum price in euro.
    pr_year = cars.groupby(['year'])[['price_in_euro']].sum().reset_index()

# Filter the data based on selected year
    if year_filter:
        selected_year = st.sidebar.multiselect(
            'Choose one or multiple year to display',
            sorted(pr_year['year'].unique()))
        pr_year = pr_year[pr_year['year'].isin(selected_year)]

    # Create the chart
    fig = px.histogram(pr_year,
                       x='year',
                       y='price_in_euro',
                       color='year',
                       nbins=50,
                       text_auto=True,
                       title='Sum of price per year').update_xaxes(tickvals=pr_year['year'].unique())
                       

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)








# Create a checkbox in the sidebar to filter by cars status
    status_filter = st.sidebar.checkbox('Filter by status')

# Group by car status, price_in_euro and sum price in euro.
    pr_mileage = cars.groupby(['car_status'])[['price_in_euro']].sum().reset_index()

# Filter the data based on selected status
    if status_filter:
        selected_status = st.sidebar.multiselect(
            'Choose one or multiple status to display',
            sorted(pr_mileage['car_status'].unique()))
        pr_mileage = pr_mileage[pr_mileage['car_status'].isin(selected_status)]

    # Create the chart
    fig = px.histogram(pr_mileage,
                       x='price_in_euro',
                       y='car_status',
                       color='car_status',
                       nbins=50,
                       text_auto=True,
                       title='Sum of price per cars mileage status')
                       

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)





# Create a checkbox in the sidebar to filter by fuel type
    fuel_filter = st.sidebar.checkbox('Filter by fuel type')

# Group by fuel type, price_in_euro and sum price in euro.
    pr_fuel = cars.groupby(['fuel_type'])[['price_in_euro']].sum().reset_index()

# Filter the data based on selected fuel type
    if fuel_filter:
        selected_filter = st.sidebar.multiselect(
            'Choose one or multiple fuel to display',
            sorted(pr_fuel['fuel_type'].unique()))
        pr_fuel = pr_fuel[pr_fuel['fuel_type'].isin(selected_filter)]

    # Create the chart
    fig = px.histogram(pr_fuel,
                       x='price_in_euro',
                       y='fuel_type',
                       color='fuel_type',
                       nbins=50,
                       text_auto=True,
                       title='Sum of price per cars fuel type')
                       
# Display the chart
    st.plotly_chart(fig, use_container_width=True)






# Create a checkbox in the sidebar to filter by model 
    model_filter = st.sidebar.checkbox('Filter by model')

# Group by model, brand and sum price in euro.
    pr_brand = cars.groupby(['model','brand'])[['price_in_euro']].sum().reset_index()

# Filter the data based on selected fuel type
    if model_filter:
        selected_model = st.sidebar.multiselect(
            'Choose one or multiple model to display',
            sorted(pr_brand['model'].unique()))
        pr_brand = pr_brand[pr_brand['model'].isin(selected_model)]

    # Create the chart
    fig = px.histogram(pr_brand,
                       x='price_in_euro',
                       y='model',
                       color='brand',
                       nbins=50,
                       text_auto=True,
                       title='Sum of price per cars model')
                       

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)








# Create a checkbox in the sidebar to filter by power 
    power_filter = st.sidebar.checkbox('Filter by power')

# Group by brand, model and power_ps.
    power = cars.groupby(['model','brand'])[['power_ps']].value_counts().reset_index()

# Filter the data based on selected power
    if power_filter:
        selected_power = st.sidebar.multiselect(
            'Choose one or multiple power to display',
            sorted(power['power_ps'].unique()))
        power = power[power['power_ps'].isin(selected_power)]

# Create the chart
    fig = px.histogram(power, 
                       x='model', 
                       y='power_ps', 
                       color='brand', 
                       nbins=50, 
                       text_auto=True, 
                       title='power per cars model') 
                       

# Display the chart
    st.plotly_chart(fig, use_container_width=True)





# Create a checkbox in the sidebar to filter year by fuel type 
    fyear_filter = st.sidebar.checkbox('Filter by year of fuel')

# Group by year, fuel type.
    f_count = cars.groupby(['year'])[['fuel_type']].value_counts().reset_index()

# Filter the data based on selected year
    if fyear_filter:
        selected_fyear = st.sidebar.multiselect(
            'Choose one or multiple year to display',
            sorted(f_count['year'].unique()))
        f_count = f_count[f_count['year'].isin(selected_fyear)]

# Create the chart
    fig = px.histogram(f_count, 
                       x='year', 
                       y='count', 
                       color='fuel_type', 
                       barmode='group', 
                       text_auto=True, 
                       title='fuel type per year').update_xaxes(tickvals=f_count['year'].unique())
                       

# Display the chart
    st.plotly_chart(fig,use_container_width=True)







# Create a checkbox in the sidebar to filter fuel consumption by transmission type 
    ftrans_filter = st.sidebar.checkbox('Filter by transmission')

# Group by transmission, fuel consumption type.
    tr_fuel = cars.groupby(['transmission_type'])[['fuel_consumption_l_100km']].sum().reset_index()

# Filter the data based on selected year
    if ftrans_filter:
        selected_ftrans = st.sidebar.multiselect(
            'Choose one or multiple transmission to display',
            sorted(tr_fuel['transmission_type'].unique()))
        tr_fuel = tr_fuel[tr_fuel['transmission_type'].isin(selected_ftrans)]

# Create the chart
    fig = px.histogram(tr_fuel, 
                       x='fuel_consumption_l_100km', 
                       y='transmission_type', 
                       color='transmission_type',
                       nbins=50, 
                       text_auto=True, 
                       title='fuel consumption per transmission type')
                       

# Display the chart
    st.plotly_chart(fig,use_container_width=True)







# Create a checkbox in the sidebar to filter fuel consumption by fuel type 
    ftype_filter = st.sidebar.checkbox('Filter by fuel_type')

# Group by fuel type, fuel consumption .
    cons_fuel = cars.groupby(['fuel_type'])[['fuel_consumption_l_100km']].sum().reset_index()

# Filter the data based on selected year
    if ftype_filter:
        selected_ftype = st.sidebar.multiselect(
            'Choose one or multiple fuel type to display',
            sorted(cons_fuel['fuel_type'].unique()))
        cons_fuel = cons_fuel[cons_fuel['fuel_type'].isin(selected_ftype)]

# Create the chart
    fig = px.histogram(cons_fuel, 
                       x='fuel_consumption_l_100km', 
                       y='fuel_type', 
                       color='fuel_type',
                       nbins=50, 
                       text_auto=True, 
                       title='fuel consumption by fuel type')
                       

# Display the chart
    st.plotly_chart(fig,use_container_width=True)






# Create a checkbox in the sidebar to filter cars status by brand 
    st_filter = st.sidebar.checkbox('Filter by cars status')

# Group by stats , brand .
    stats_brand = cars.groupby(['car_status'])[['brand']].value_counts().reset_index()

# Filter the data based on cars status
    if st_filter:
        selected_st = st.sidebar.multiselect(
            'Choose one or multiple status to display',
            sorted(stats_brand['car_status'].unique()))
        stats_brand = stats_brand[stats_brand['car_status'].isin(selected_st)]

# Create the chart
    fig = px.histogram(stats_brand, 
                       x='count', 
                       y='car_status', 
                       color='brand',
                       nbins=50, 
                       text_auto=True, 
                       title='status per brand')
                       

# Display the chart
    st.plotly_chart(fig,use_container_width=True)






def perform_univariate_analysis(cars):
    # Get the list of available columns
    columns = cars.columns.tolist()

    # Select the column for the analysis
    column = st.selectbox('Select column', columns)

    # Perform univariate analysis
    chart_types = ['bar', 'box', 'violin', 'line', 'scatter', 'histogram', 'pie', 'donut', 'area']
    selected_chart = st.selectbox('Select chart type', chart_types)

    if selected_chart == 'bar':
        color = st.selectbox('Select color', columns)
        chart = px.bar(cars.groupby(column).size().reset_index(name='count'), x=column, y='count', color=color)
    elif selected_chart == 'box':
        chart = px.box(cars, x=column)
    elif selected_chart == 'violin':
        chart = px.violin(cars, x=column)
    elif selected_chart == 'line':
        y_column = st.selectbox('Select Y-axis column', columns)
        chart = px.line(cars, x=column, y=y_column)
    elif selected_chart == 'scatter':
        y_column = st.selectbox('Select Y-axis column', columns)
        chart = px.scatter(cars, x=column, y=y_column)
    elif selected_chart == 'histogram':
        color = st.selectbox('Select color', columns)
        chart = px.histogram(cars, x=column, color=color)
    elif selected_chart == 'pie':
        chart = px.pie(cars, names=column)
    elif selected_chart == 'donut':
        chart = px.pie(cars, names=column, hole=0.5)
    elif selected_chart == 'area':
        chart = px.area(cars, x=column)

    # Display the chart
    st.plotly_chart(chart, use_container_width=True)

def perform_bivariate_analysis(cars):
    # Get the available columns
    columns = cars.columns.tolist()

    # Select the X-axis and Y-axis columns
    x_column = st.selectbox('Select X-axis column', columns)
    y_column = st.selectbox('Select Y-axis column', columns)

    # Perform bivariate analysis
    chart_types = ['scatter', 'line', 'bar', 'box', 'violin', 'histogram', 'pie', 'donut', 'area']
    selected_chart = st.selectbox('Select chart type', chart_types)

    if selected_chart == 'scatter':
        chart = px.scatter(cars, x=x_column, y=y_column)
    elif selected_chart == 'line':
        chart = px.line(cars, x=x_column, y=y_column)
    elif selected_chart == 'bar':
        color = st.selectbox('Select color', columns)
        chart = px.bar(cars, x=x_column, y=y_column, color=color)
    elif selected_chart == 'box':
        chart = px.box(cars, x=x_column, y=y_column)
    elif selected_chart == 'violin':
        chart = px.violin(cars, x=x_column, y=y_column)
    elif selected_chart == 'histogram':
        color = st.selectbox('Select color', columns)
        chart = px.histogram(cars, x=x_column, y=y_column, color=color)
    elif selected_chart == 'pie':
        chart = px.pie(cars, names=x_column, values=y_column)
    elif selected_chart == 'donut':
        chart = px.pie(cars, names=x_column, values=y_column, hole=0.5)

    # Display the chart
    st.plotly_chart(chart, use_container_width=True)

def fourthPage():
    st.title('Do it yourself')

    # Read the data file
    cars = pd.read_csv('cars_clean.csv')

    # Sidebar options
    analysis_type = st.sidebar.radio('Select analysis type', ['Univariate', 'Bivariate'])

    if analysis_type == 'Univariate':
        perform_univariate_analysis(cars)
    elif analysis_type == 'Bivariate':
        perform_bivariate_analysis(cars)




pages = {'Exploratory Data Analysis':main_page,
          'Univariate analysis': secondPage,
          'Bivariate analysis' : thirdPage,
          'DIY'          : fourthPage
}    
select_page = st.sidebar.selectbox('Select overview',pages.keys())
pages[select_page]()



