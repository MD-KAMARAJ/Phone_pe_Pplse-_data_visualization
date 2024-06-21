import pandas as pd
import streamlit as st
import pymysql
import pandas as pd
import json
import plotly.express as px
import requests
import base64


def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "jpg"

    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{main_bg});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Load your image
with open(r"C:\Users\HP USER\Desktop\PhonePe-Logo-Vector.jpg", "rb") as image_file:
    image_bytes = image_file.read()
    encoded_image = base64.b64encode(image_bytes).decode()

# Set the background image
set_bg_hack(encoded_image)

st.title(":violet[Phonepe] Pulse Data Visualization and Exploration")

st.session_state.page_select = st.sidebar.radio('Contents', ['Overview', 'Detailed Analysis', 'Queries'])
if st.session_state.page_select == 'Overview':
    tab4, tab5, tab6 = st.tabs(['Aggregate','Map','Top'])

    def agg_trans_animated():
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_agg_trans = """
        SELECT Year, Quarter, State, Transaction_Type, SUM(Transaction_amount) as Transaction_amount from agg_trans
        group by Year, Quarter,State, Transaction_Type """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_agg_trans)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        custom_color_sequence = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)
        # Create the choropleth map
        map_fig = px.bar(
            df,
            x='State',
            y='Transaction_amount',
            hover_name='Quarter',
            color='Transaction_Type',
            animation_frame='Year',
            color_discrete_sequence=custom_color_sequence,     
            title="Transactions amount of each State")
            
        return map_fig

    with tab4:
        Aggregation_type = st.selectbox("Select Aggregate Type", ['Aggregate Transaction','Aggregate User'])
        if Aggregation_type == 'Aggregate Transaction':
            fig = agg_trans_animated()
            tab4.plotly_chart(fig)

    def agg_user_animated():
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_agg_user = """
        SELECT Year, Quarter, State, Brand_name, SUM(Registered_Users) as Registered_Users from agg_user
        group by Year, Quarter,State, Brand_name """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_agg_user)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        custom_color_sequence = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)
        # Create the choropleth map
        map_fig = px.bar(
            df,
            x='State',
            y='Registered_Users',
            hover_name='Quarter',
            color='Brand_name',
            animation_frame='Year',
            color_discrete_sequence=custom_color_sequence,     
            title="Registered Users of each State and for each Brand")
            
        return map_fig

    with tab4:
        if Aggregation_type == 'Aggregate User':
            fig = agg_user_animated()
            tab4.plotly_chart(fig)

    def map_trans_animated():
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_map_trans = """
        SELECT Year, Quarter, State, District, SUM(Transaction_amount) as Transaction_amount from map_trans
        group by Year, Quarter,State, District; """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_map_trans)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        custom_color_sequence = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)
        # Create the choropleth map
        pie_fig = px.pie(
            df,
            values='Transaction_amount',
            names='State',
            color='District',
            hover_data='Year',
            color_discrete_sequence = custom_color_sequence,     
            title="Transaction amount of each State and for each Brand")
            
        return pie_fig

    with tab5:
        Map_type = st.selectbox("Select Map Type", ['Map_Transaction','Map_User'])
        if Map_type == 'Map_Transaction':
            fig = map_trans_animated()
            tab5.plotly_chart(fig)

    
    def map_user_animated():
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_map_user = """
        SELECT Year, Quarter, State, District, SUM(Registered_Users) as Registered_Users from map_user
        group by Year, Quarter,State, District; """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_map_user)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        custom_color_sequence = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)
        # Create the choropleth map
        bar_fig = px.bar(
            df,
            x='District',
            y='Registered_Users',
            hover_name='Quarter',
            color='State',
            animation_frame='Year',
            color_discrete_sequence=custom_color_sequence,     
            title="Registered Users of each State and for each District")
            
        return bar_fig

    with tab5:
        if Map_type == 'Map_User':
            fig = map_user_animated()
            tab5.plotly_chart(fig)

    def top_trans_animated():
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_top_trans = """
        SELECT Year, Quarter, State, Districts, SUM(Pincode_Transaction_amount) as Pincode_Transaction_amount from top_trans
        group by Year, Quarter,State, Districts; """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_top_trans)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        custom_color_sequence = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)
        # Create the choropleth map
        bar_fig = px.bar(
            df,
            x='Districts',
            y='Pincode_Transaction_amount',
            hover_name='Quarter',
            color='State',
            animation_frame='Year',
            color_discrete_sequence=custom_color_sequence,     
            title="Registered Users of each State and for each District")
            
        return bar_fig

    with tab6:
        Top_type = st.selectbox("Select Top Type", ['Top_Transaction','Top_User'])
        if Top_type == 'Top_Transaction':
            fig = top_trans_animated()
            tab6.plotly_chart(fig)

    def top_user_animated():
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_top_user = """
        SELECT Year, Quarter, State, Districts, SUM(Pincode_Registered_user) as Pincode_Registered_user from top_user
        group by Year, Quarter,State, Districts; """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_top_user)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        custom_color_sequence = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)
        # Create the choropleth map
        bar_fig = px.bar(
            df,
            x='Districts',
            y='Pincode_Registered_user',
            hover_name='Quarter',
            color='State',
            animation_frame='Year',
            color_discrete_sequence=custom_color_sequence,     
            title="Registered Users of each State and for each District")
            
        return bar_fig

    with tab6:
        if Top_type == 'Top_User':
            fig = top_user_animated()
            tab6.plotly_chart(fig)

if st.session_state.page_select == 'Detailed Analysis':

    tab1, tab2, tab3 = st.tabs(["Choropleth", "Bar Graph", "Pie Chart"])

    year = st.sidebar.selectbox("Select Year", [2018, 2019, 2020, 2021, 2022, 2023, 2024])
    quarter = st.sidebar.selectbox("Select Quarter", [1, 2, 3, 4])

    def transform_state_name(state_name):
        state_name = state_name.replace('-', ' ')  # Replace '-' with space
        state_name = state_name.replace('&', 'and')  # Replace '&' with 'and'
        return ' '.join(word.capitalize() for word in state_name.split())

    def geo_visual_agg_trans(year, quarter, transaction_type):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_agg_trans = f"""
        SELECT * FROM agg_trans 
        WHERE Year={year} AND Quarter={quarter} AND Transaction_Type='{transaction_type}'
        """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_agg_trans)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        
        # Transform the state names in the DataFrame
        df['State'] = df['State'].apply(transform_state_name)

        state_replacements = {
        'Andaman And Nicobar Islands': 'Andaman & Nicobar',
        'Dadra And Nagar Haveli And Daman And Diu': 'Dadra and Nagar Haveli and Daman and Diu',
        'Jammu And Kashmir': 'Jammu & Kashmir'
    }

        df['State'] = df['State'].replace(state_replacements)
        
        # GeoJSON URL for India's states
        geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(geojson_url)
        india_states_geojson = response.json()

        # Check the GeoJSON file structure
        print("GeoJSON Structure:\n", json.dumps(india_states_geojson, indent=2))

        # Check state names in the GeoJSON file
        geojson_state_names = [feature['properties']['ST_NM'] for feature in india_states_geojson['features']]
        print("GeoJSON State Names:", geojson_state_names)

        # Check state names in your DataFrame
        df_state_names = df['State'].unique()
        print("DataFrame State Names:", df_state_names)

        # Compare the two sets of state names to ensure they match
        missing_states = set(df_state_names) - set(geojson_state_names)
        if missing_states:
            print("These states are missing in GeoJSON:", missing_states)
        
        # Create the choropleth map
        map_fig = px.choropleth(
            df,
            geojson=india_states_geojson,
            featureidkey="properties.ST_NM",  # This should match the property name in your GeoJSON file
            locations='State',  # Column in your DataFrame
            color='Transaction_amount',  # Column in your DataFrame
            hover_name='State',  # Column in your DataFrame
            color_continuous_scale='Viridis',
            title=f"Transactions of {transaction_type} of each State in year {year} for the Quarter {quarter}"
        )
        
        # Update the map to fit the bounds of the locations
        map_fig.update_geos(fitbounds="locations", visible=False)
        
        # Show the figure (in a real scenario, you would likely save or display this plot)
        return map_fig

    with tab1:
        show_selection = st.checkbox("Aggregate Transaction")
        if show_selection:
            transaction_type = st.selectbox("Select Transaction_type", ['Recharge & bill payments', 'Peer-to-peer payments',
                                                                        'Merchant payments', 'Financial Services', 'Others'])
            if st.button("Submit"):
                fig = geo_visual_agg_trans(year, quarter, transaction_type)
                st.plotly_chart(fig)
            
    def geo_visual_map_trans(year, quarter):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_map_trans = f"""
        SELECT State,SUM(Transaction_amount) as State_Transaction_amount
        FROM map_trans 
        WHERE Year={year} AND Quarter={quarter}
        GROUP BY State;"""
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_map_trans)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Transform the state names in the DataFrame
        df['State'] = df['State'].apply(transform_state_name)

        state_replacements = {
            'Andaman And Nicobar Islands': 'Andaman & Nicobar',
            'Dadra And Nagar Haveli And Daman And Diu': 'Dadra and Nagar Haveli and Daman and Diu',
            'Jammu And Kashmir': 'Jammu & Kashmir'
        }

        df['State'] = df['State'].replace(state_replacements)

        df['State_Transaction_amount'] = pd.to_numeric(df['State_Transaction_amount'])
        
        # GeoJSON URL for India's states
        geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(geojson_url)
        india_states_geojson = response.json()

        color_scale_min = df['State_Transaction_amount'].min()
        color_scale_max = df['State_Transaction_amount'].max()

            # Create the choropleth map
        choropleth_fig = px.choropleth(
            df,
            geojson=india_states_geojson,
            featureidkey="properties.ST_NM",  # This should match the property name in your GeoJSON file
            locations='State',  # Column in your DataFrame
            color='State_Transaction_amount',  # Column in your DataFrame
            hover_name='State',  # Column in your DataFrame
            color_continuous_scale='Viridis',
            range_color=(color_scale_min, color_scale_max),
            title=f"Map Transactions of each State in year {year} for the Quarter {quarter}"
        )

        # Update the map to fit the bounds of the locations
        choropleth_fig.update_geos(fitbounds="locations", visible=False)

        # Display the choropleth map in Streamlit
        tab1.plotly_chart(choropleth_fig)  

        # Close the database connection
        connection.close()

        return df['State'].unique()

    if tab1.checkbox("Map Transaction"):
        geo_visual_map_trans(year, quarter)

    def bar_graph_state_map_transactions(year, quarter, state):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')

        # Correct the SQL query syntax to get data for the selected year, quarter, and state
        query_district_map_transactions = f"""
        SELECT District, SUM(Transaction_amount) as Transaction_amount
        FROM map_trans 
        WHERE Year={year} AND Quarter={quarter} AND State='{state}'
        GROUP BY District
        """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_district_map_transactions)
        data = cursor.fetchall()

        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]

        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Debug: Print the fetched data
        tab2.text("Fetched Data for Bar Graph:")
        tab2.table(df)

        # Check if the DataFrame is empty
        if df.empty:
            tab2.warning(f"No data available for {state} in year {year} for quarter {quarter}")
            connection.close()
            return

        # Create the bar graph
        bar_fig = px.bar(
            df,
            x='District',
            y='Transaction_amount',
            color='Transaction_amount',
            title=f"District Transaction Amount in {state} for Year {year} Quarter {quarter}"
        )            
        # Display the bar graph in Streamlit
        tab2.plotly_chart(bar_fig)

        # Close the database connection
        connection.close()

    with tab2:
        show_selection = st.checkbox("Map Transaction in Bar")
        if show_selection:
        # Establish database connection to get states directly from map_trans table
            connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
            query_states = "SELECT DISTINCT State FROM map_trans"
            cursor = connection.cursor()
            cursor.execute(query_states)
            states_bar_map_trans = cursor.fetchall()
            states_bar_list = [state[0] for state in states_bar_map_trans]
            year_bar = year
            quarter_bar= quarter
            selected_state_for_bar = st.selectbox('Select a state for the bar graph:', states_bar_list)
            bar_graph_state_map_transactions(year_bar, quarter_bar,selected_state_for_bar)   

    def geo_visual_top_trans(year, quarter):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_top_trans = f"""
        SELECT Year, Quarter, State, District_Transaction_amount 
        FROM top_trans 
        WHERE Year={year} AND Quarter={quarter};"""
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_top_trans)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Transform the state names in the DataFrame
        df['State'] = df['State'].apply(transform_state_name)

        state_replacements = {
            'Andaman And Nicobar Islands': 'Andaman & Nicobar',
            'Dadra And Nagar Haveli And Daman And Diu': 'Dadra and Nagar Haveli and Daman and Diu',
            'Jammu And Kashmir': 'Jammu & Kashmir'
        }

        df['State'] = df['State'].replace(state_replacements)
        
        # Calculate the State_Transaction_amount
        df_state_sum = df.groupby('State')['District_Transaction_amount'].mean().reset_index()
        df_state_sum.rename(columns={'District_Transaction_amount': 'State_Transaction_amount'}, inplace=True)
        
        # GeoJSON URL for India's states
        geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(geojson_url)
        india_states_geojson = response.json()

        # Create the choropleth map
        choropleth_fig = px.choropleth(
            df_state_sum,
            geojson=india_states_geojson,
            featureidkey="properties.ST_NM",  # This should match the property name in your GeoJSON file
            locations='State',  # Column in your DataFrame
            color='State_Transaction_amount',  # Column in your DataFrame
            hover_name='State',  # Column in your DataFrame
            color_continuous_scale='Viridis',
            title=f"Transactions of each State in year {year} for the Quarter {quarter}"
        )

        # Update the map to fit the bounds of the locations
        choropleth_fig.update_geos(fitbounds="locations", visible=False)

        # Display the choropleth map in Streamlit
        tab1.plotly_chart(choropleth_fig)

        return df['State'].unique()

    if tab1.checkbox("Top Transaction"):
        geo_visual_top_trans(year, quarter)


    def bar_graph_state_top_transactions(year, quarter, state):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')

        # Correct the SQL query syntax to get data for the selected year, quarter, and state
        query_district_transactions = f"""
        SELECT Districts, AVG(District_Transaction_amount) as District_Transaction_amount
        FROM top_trans 
        WHERE Year={year} AND Quarter={quarter} AND State='{state}'
        GROUP BY Districts """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_district_transactions)
        data = cursor.fetchall()

        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]

        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Debug: Print the fetched data
        tab2.text("Fetched Data for Bar Graph:")
        tab2.table(df)

        # Check if the DataFrame is empty
        if df.empty:
            tab2.warning(f"No data available for {state} in year {year} for quarter {quarter}")
            connection.close()
            return

        # Create the bar graph
        bar_fig = px.bar(
            df,
            x='Districts',
            y='District_Transaction_amount',
            color='District_Transaction_amount',
            title=f"District Transaction Amount in {state} for Year {year} Quarter {quarter}"
        )

        # Display the bar graph in Streamlit
        tab2.plotly_chart(bar_fig)

        # Close the database connection
        connection.close()
    with tab2:
        show_selection = st.checkbox("Top Transaction in Bar")
        if show_selection:
            year_bar=year
            quarter_bar=quarter 
            connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
            query_states = "SELECT DISTINCT State FROM top_trans"
            cursor = connection.cursor()
            cursor.execute(query_states)
            states_bar = cursor.fetchall()
            connection.close()
            states_bar_list = [state[0] for state in states_bar]
            selected_state_for_bar = st.selectbox('Select a state for the bar graph_top_trans:', states_bar_list)
            bar_graph_state_top_transactions(year_bar, quarter_bar, selected_state_for_bar)

    def pie_chart_pincode_top_transactions(year, quarter, state, district):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')

        # Correct the SQL query syntax to get data for the selected year, quarter, state, and district
        query_pincode_top_transactions = f"""
        SELECT Pincode, SUM(Pincode_Transaction_amount) as Pincode_Transaction_amount
        FROM top_trans 
        WHERE Year={year} AND Quarter={quarter} AND State='{state}' AND Districts='{district}'
        GROUP BY Pincode """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_pincode_top_transactions)
        data = cursor.fetchall()

        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]

        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        if df.empty:
            tab3.warning(f"No data available for {state} in year {year} for quarter {quarter}")
            connection.close()
            return

        # Create the pie chart
        top_trans_pie_fig = px.pie(
            df,
            names='Pincode',
            values='Pincode_Transaction_amount',
            title=f"Pincode Transaction Distribution in {district} for Year {year} Quarter {quarter}"
        )

        # Display the pie chart in Streamlit
        tab3.plotly_chart(top_trans_pie_fig)

        # Close the database connection
        connection.close()

    with tab3:
        show_selection = st.checkbox("Top Transaction in Pie")
        if show_selection:
        # Establish database connection to get states directly from top_trans table
            connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
            query_states = "SELECT DISTINCT State FROM top_trans"
            cursor = connection.cursor()
            cursor.execute(query_states)
            states_pie = cursor.fetchall()
            connection.close()
            
            states_pie_list = [state[0] for state in states_pie]
            
            selected_state_for_pie = tab3.selectbox('Select a state for the pie chart:', states_pie_list)

            # Establish database connection to get districts directly from top_trans table for the selected state
            connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
            query_districts = f"SELECT DISTINCT Districts FROM top_trans WHERE State='{selected_state_for_pie}'"
            cursor = connection.cursor()
            cursor.execute(query_districts)
            districts_pie = cursor.fetchall()
            connection.close()
            districts_pie_list = [district[0] for district in districts_pie]
            year_pie=year
            quarter_pie=quarter
            selected_district_for_pie = tab3.selectbox('Select a district for the pie chart:', districts_pie_list)
            # Display the pie chart based on user selections
            pie_chart_pincode_top_transactions(year_pie, quarter_pie, selected_state_for_pie, selected_district_for_pie)


    def geo_visual_agg_user_brand(year,quarter,brand):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_agg_user = f"""
        SELECT * FROM agg_user 
        WHERE Year={year} AND Quarter={quarter} AND Brand_name='{brand}';
        """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_agg_user)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        
        # Transform the state names in the DataFrame
        df['State'] = df['State'].apply(transform_state_name)

        state_replacements = {
        'Andaman And Nicobar Islands': 'Andaman & Nicobar',
        'Dadra And Nagar Haveli And Daman And Diu': 'Dadra and Nagar Haveli and Daman and Diu',
        'Jammu And Kashmir': 'Jammu & Kashmir'
    }

        df['State'] = df['State'].replace(state_replacements)
        
        # GeoJSON URL for India's states
        geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(geojson_url)
        india_states_geojson = response.json()

        # Check the GeoJSON file structure
        print("GeoJSON Structure:\n", json.dumps(india_states_geojson, indent=2))

        # Check state names in the GeoJSON file
        geojson_state_names = [feature['properties']['ST_NM'] for feature in india_states_geojson['features']]
        print("GeoJSON State Names:", geojson_state_names)

        # Check state names in your DataFrame
        df_state_names = df['State'].unique()
        print("DataFrame State Names:", df_state_names)

        # Compare the two sets of state names to ensure they match
        missing_states = set(df_state_names) - set(geojson_state_names)
        if missing_states:
            print("These states are missing in GeoJSON:", missing_states)
        
        if df.empty:
            tab1.warning(f"No data available for {brand} in year {year} for quarter {quarter}")
            connection.close()
            return
        # Create the choropleth map

        map_fig = px.choropleth(
            df,
            geojson=india_states_geojson,
            featureidkey="properties.ST_NM",  # This should match the property name in your GeoJSON file
            locations='State',  # Column in your DataFrame
            color='Registered_Users_of_brand',  # Column in your DataFrame
            hover_name='Brand_name',  # Column in your DataFrame
            color_continuous_scale='Viridis',
            title=f"Registered Users of Brand {brand} in each State in year {year} for the Quarter {quarter}"
        )
        
        # Update the map to fit the bounds of the locations
        map_fig.update_geos(fitbounds="locations", visible=False)
        
        # Show the figure (in a real scenario, you would likely save or display this plot)
        tab1.plotly_chart(map_fig)
        # Close the database connection
        connection.close()


    def geo_visual_agg_user_Registered_user(year,quarter):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_agg_user_registered_user = f"""
        SELECT * FROM agg_user 
        WHERE Year={year} AND Quarter={quarter};
        """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_agg_user_registered_user)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        
        # Transform the state names in the DataFrame
        df['State'] = df['State'].apply(transform_state_name)

        state_replacements = {
        'Andaman And Nicobar Islands': 'Andaman & Nicobar',
        'Dadra And Nagar Haveli And Daman And Diu': 'Dadra and Nagar Haveli and Daman and Diu',
        'Jammu And Kashmir': 'Jammu & Kashmir'
    }

        df['State'] = df['State'].replace(state_replacements)
        
        # GeoJSON URL for India's states
        geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(geojson_url)
        india_states_geojson = response.json()

        # Check the GeoJSON file structure
        print("GeoJSON Structure:\n", json.dumps(india_states_geojson, indent=2))

        # Check state names in the GeoJSON file
        geojson_state_names = [feature['properties']['ST_NM'] for feature in india_states_geojson['features']]
        print("GeoJSON State Names:", geojson_state_names)

        # Check state names in your DataFrame
        df_state_names = df['State'].unique()
        print("DataFrame State Names:", df_state_names)

        # Compare the two sets of state names to ensure they match
        missing_states = set(df_state_names) - set(geojson_state_names)
        if missing_states:
            print("These states are missing in GeoJSON:", missing_states)
        
        # Create the choropleth map
        map_fig = px.choropleth(
            df,
            geojson=india_states_geojson,
            featureidkey="properties.ST_NM",  # This should match the property name in your GeoJSON file
            locations='State',  # Column in your DataFrame
            color='Registered_Users',  # Column in your DataFrame
            hover_name='State',  # Column in your DataFrame
            color_continuous_scale='Viridis',
            title=f"Registered Users in each State in year {year} for the Quarter {quarter}"
        )
        
        # Update the map to fit the bounds of the locations
        map_fig.update_geos(fitbounds="locations", visible=False)
        
        # Show the figure (in a real scenario, you would likely save or display this plot)
        tab1.plotly_chart(map_fig)

        # Close the database connection
        connection.close()

    def geo_visual_agg_user_App_opens(year,quarter):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_agg_user_app_opens = f"""
        SELECT * FROM agg_user 
        WHERE Year={year} AND Quarter={quarter};
        """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_agg_user_app_opens)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        
        # Transform the state names in the DataFrame
        df['State'] = df['State'].apply(transform_state_name)

        state_replacements = {
        'Andaman And Nicobar Islands': 'Andaman & Nicobar',
        'Dadra And Nagar Haveli And Daman And Diu': 'Dadra and Nagar Haveli and Daman and Diu',
        'Jammu And Kashmir': 'Jammu & Kashmir'
    }

        df['State'] = df['State'].replace(state_replacements)
        
        # GeoJSON URL for India's states
        geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(geojson_url)
        india_states_geojson = response.json()

        # Check the GeoJSON file structure
        print("GeoJSON Structure:\n", json.dumps(india_states_geojson, indent=2))

        # Check state names in the GeoJSON file
        geojson_state_names = [feature['properties']['ST_NM'] for feature in india_states_geojson['features']]
        print("GeoJSON State Names:", geojson_state_names)

        # Check state names in your DataFrame
        df_state_names = df['State'].unique()
        print("DataFrame State Names:", df_state_names)

        # Compare the two sets of state names to ensure they match
        missing_states = set(df_state_names) - set(geojson_state_names)
        if missing_states:
            print("These states are missing in GeoJSON:", missing_states)
        
        # Create the choropleth map
        map_fig = px.choropleth(
            df,
            geojson=india_states_geojson,
            featureidkey="properties.ST_NM",  # This should match the property name in your GeoJSON file
            locations='State',  # Column in your DataFrame
            color='App_opens',  # Column in your DataFrame
            hover_name='State',  # Column in your DataFrame
            color_continuous_scale='Viridis',
            title=f"App_opens in each State in year {year} for the Quarter {quarter}"
        )
        
        # Update the map to fit the bounds of the locations
        map_fig.update_geos(fitbounds="locations", visible=False)
        
        # Show the figure (in a real scenario, you would likely save or display this plot)
        tab1.plotly_chart(map_fig)

        # Close the database connection
        connection.close()

    if tab1.checkbox('Agg_user'):
        Agg_User_data_list=['Agg_user_brand','Agg_user_Registered_user','Agg_user_App_opens']
        selected_data=tab1.selectbox('Select any one of the data:', Agg_User_data_list)
        if selected_data=='Agg_user_brand':
            # Call the function to generate and display the maps for a specific year, quarter, and transaction type
            brand_name_list=['Xiaomi','Samsung','Vivo','Oppo','OnePlus','Realme','Apple','Motorola','Lenovo','Huawei','Others',
                            'Tecno','Not Available','Gionee','Infinix','Asus','Micromax','HMD Global','Lava','COOLPAD','Lyf']
            selected_brand=tab1.selectbox('Select any brand for Agg_User:', brand_name_list)
            geo_visual_agg_user_brand(year, quarter,selected_brand)
        if selected_data =='Agg_user_Registered_user':
            geo_visual_agg_user_Registered_user(year,quarter)
        if selected_data =='Agg_user_App_opens':
            geo_visual_agg_user_App_opens(year,quarter)

    def geo_visual_map_user_state(year,quarter):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_map_user_state= f"""
        SELECT * FROM map_user 
        WHERE Year={year} AND Quarter={quarter}
        """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_map_user_state)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        
        # Transform the state names in the DataFrame
        df['State'] = df['State'].apply(transform_state_name)

        state_replacements = {
        'Andaman And Nicobar Islands': 'Andaman & Nicobar',
        'Dadra And Nagar Haveli And Daman And Diu': 'Dadra and Nagar Haveli and Daman and Diu',
        'Jammu And Kashmir': 'Jammu & Kashmir'
    }

        df['State'] = df['State'].replace(state_replacements)
        
        # GeoJSON URL for India's states
        geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(geojson_url)
        india_states_geojson = response.json()

        # Check the GeoJSON file structure
        print("GeoJSON Structure:\n", json.dumps(india_states_geojson, indent=2))

        # Check state names in the GeoJSON file
        geojson_state_names = [feature['properties']['ST_NM'] for feature in india_states_geojson['features']]
        print("GeoJSON State Names:", geojson_state_names)

        # Check state names in your DataFrame
        df_state_names = df['State'].unique()
        print("DataFrame State Names:", df_state_names)

        # Compare the two sets of state names to ensure they match
        missing_states = set(df_state_names) - set(geojson_state_names)
        if missing_states:
            print("These states are missing in GeoJSON:", missing_states)

        df_state_sum = df.groupby('State')['Registered_Users'].sum().reset_index()
        df_state_sum.rename(columns={'Registered_Users': 'State_Registered_Users'}, inplace=True)
        
        # Create the choropleth map
        map_fig = px.choropleth(
            df_state_sum,
            geojson=india_states_geojson,
            featureidkey="properties.ST_NM",  # This should match the property name in your GeoJSON file
            locations='State',  # Column in your DataFrame
            color='State_Registered_Users',  # Column in your DataFrame
            hover_name='State',  # Column in your DataFrame
            color_continuous_scale='Viridis',
            title=f"Registered Users in each State in year {year} for the Quarter {quarter}"
        )
        
        # Update the map to fit the bounds of the locations
        map_fig.update_geos(fitbounds="locations", visible=False)
        
        # Show the figure (in a real scenario, you would likely save or display this plot)
        tab1.plotly_chart(map_fig)

        # Close the database connection
        connection.close()

    if tab1.checkbox("Map_User_State"):
        geo_visual_map_user_state(year, quarter)

    def geo_visual_map_user_Registered_state_bar_chart(year,quarter,state):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_map_user_registered_user = f"""
        SELECT State, District, SUM(Registered_Users) as District_Registered_User
        FROM map_user 
        WHERE Year={year} AND Quarter={quarter} AND State='{state}'
        GROUP BY District;
        """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_map_user_registered_user)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)
        
        if df.empty:
            tab2.warning(f"No data available for {state} in year {year} for quarter {quarter}")
            connection.close()
            return

        # Create the bar graph
        bar_fig_map = px.bar(
            df,
            x='District',
            y='District_Registered_User',
            color='District_Registered_User',
            title=f"District Registered User in {state} for Year {year} Quarter {quarter}",
            color_discrete_sequence=px.colors.qualitative.Vivid  )
        
        # Update the map to fit the bounds of the locations
        bar_fig_map.update_geos(fitbounds="locations", visible=False)
        
        # Show the figure (in a real scenario, you would likely save or display this plot)
        tab2.plotly_chart(bar_fig_map)

        # Close the database connection
        connection.close()

    with tab2:
        show_selection = st.checkbox("Map_user_Registered_state")
        if show_selection:
            year_bar=year
            quarter_bar=quarter
            connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
            query_states = "SELECT DISTINCT State FROM map_user"
            cursor = connection.cursor()
            cursor.execute(query_states)
            states_bar = cursor.fetchall()
            connection.close()
            states_bar_list = [state[0] for state in states_bar]
            selected_state_for_bar = tab2.selectbox('Select a state for the bar graph_map_user_Registered:', states_bar_list)
            geo_visual_map_user_Registered_state_bar_chart(year, quarter,selected_state_for_bar)
    # Call the function to generate and display the maps for a specific year, quarter, and transaction type

    def geo_visual_map_user_state_appOpens(year,quarter):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_map_user_state_appOpens= f"""
        SELECT * FROM map_user 
        WHERE Year={year} AND Quarter={quarter}
        """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_map_user_state_appOpens)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        
        # Transform the state names in the DataFrame
        df['State'] = df['State'].apply(transform_state_name)

        state_replacements = {
        'Andaman And Nicobar Islands': 'Andaman & Nicobar',
        'Dadra And Nagar Haveli And Daman And Diu': 'Dadra and Nagar Haveli and Daman and Diu',
        'Jammu And Kashmir': 'Jammu & Kashmir'
    }

        df['State'] = df['State'].replace(state_replacements)
        
        # GeoJSON URL for India's states
        geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(geojson_url)
        india_states_geojson = response.json()

        # Check the GeoJSON file structure
        print("GeoJSON Structure:\n", json.dumps(india_states_geojson, indent=2))

        # Check state names in the GeoJSON file
        geojson_state_names = [feature['properties']['ST_NM'] for feature in india_states_geojson['features']]
        print("GeoJSON State Names:", geojson_state_names)

        # Check state names in your DataFrame
        df_state_names = df['State'].unique()
        print("DataFrame State Names:", df_state_names)

        # Compare the two sets of state names to ensure they match
        missing_states = set(df_state_names) - set(geojson_state_names)
        if missing_states:
            print("These states are missing in GeoJSON:", missing_states)

        df_state_sum = df.groupby('State')['App_opens'].sum().reset_index()
        df_state_sum.rename(columns={'App_opens': 'State_App_opens'}, inplace=True)
        
        # Create the choropleth map
        map_fig = px.choropleth(
            df_state_sum,
            geojson=india_states_geojson,
            featureidkey="properties.ST_NM",  # This should match the property name in your GeoJSON file
            locations='State',  # Column in your DataFrame
            color='State_App_opens',  # Column in your DataFrame
            hover_name='State',  # Column in your DataFrame
            color_continuous_scale='Viridis',
            title=f"State_App_opens in each State in year {year} for the Quarter {quarter}"
        )
        
        # Update the map to fit the bounds of the locations
        map_fig.update_geos(fitbounds="locations", visible=False)
        
        # Show the figure (in a real scenario, you would likely save or display this plot)
        tab1.plotly_chart(map_fig)

        # Close the database connection
        connection.close()

    if tab1.checkbox("Map_user_State_appOpens"):
        geo_visual_map_user_state_appOpens(year,quarter)


    def geo_visual_map_user_district_App_opens_bar_chart(year,quarter,state):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_map_user_registered_user_app_opens = f"""
        SELECT State, District, SUM(App_opens) as District_App_opens
        FROM map_user 
        WHERE Year={year} AND Quarter={quarter} AND State='{state}'
        GROUP BY District;
        """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_map_user_registered_user_app_opens)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)
        
        if df.empty:
            tab2.warning(f"No data available for {state} in year {year} for quarter {quarter}")
            connection.close()
            return

        # Create the bar graph
        bar_fig_map = px.bar(
            df,
            x='District',
            y='District_App_opens',
            color='District_App_opens',
            title=f"District_App_opens in {state} for Year {year} Quarter {quarter}",
            color_discrete_sequence=px.colors.qualitative.Vivid  )
        
        # Update the map to fit the bounds of the locations
        bar_fig_map.update_geos(fitbounds="locations", visible=False)
        
        # Show the figure (in a real scenario, you would likely save or display this plot)
        tab2.plotly_chart(bar_fig_map)

        # Close the database connection
        connection.close()

    with tab2:
        show_selection = tab2.checkbox("Map_user_Registered_app_opens")
        if show_selection:
            year_bar=year
            quarter_bar=quarter
            connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
            query_states = "SELECT DISTINCT State FROM map_user"
            cursor = connection.cursor()
            cursor.execute(query_states)
            states_bar = cursor.fetchall()
            connection.close()
            states_bar_list = [state[0] for state in states_bar]
            selected_state_for_bar = tab2.selectbox('Select a state for the bar graph_map_user_appOpens:', states_bar_list)
            geo_visual_map_user_district_App_opens_bar_chart(year,quarter,selected_state_for_bar)


    def geo_visual_top_user(year, quarter):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        
        # Correct the SQL query syntax
        query_top_user = f"""
        SELECT Year, Quarter, State, District_Registered_user
        FROM top_user 
        WHERE Year={year} AND Quarter={quarter};"""
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_top_user)
        data = cursor.fetchall()
        
        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        
        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Transform the state names in the DataFrame
        df['State'] = df['State'].apply(transform_state_name)

        state_replacements = {
            'Andaman And Nicobar Islands': 'Andaman & Nicobar',
            'Dadra And Nagar Haveli And Daman And Diu': 'Dadra and Nagar Haveli and Daman and Diu',
            'Jammu And Kashmir': 'Jammu & Kashmir'
        }

        df['State'] = df['State'].replace(state_replacements)
        
        # Calculate the State_Transaction_amount
        df_state_sum = df.groupby('State')['District_Registered_user'].mean().reset_index()
        df_state_sum.rename(columns={'District_Registered_user': 'State_Registered_user'}, inplace=True)
        
        # GeoJSON URL for India's states
        geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(geojson_url)
        india_states_geojson = response.json()

        # Create the choropleth map
        choropleth_fig = px.choropleth(
            df_state_sum,
            geojson=india_states_geojson,
            featureidkey="properties.ST_NM",  # This should match the property name in your GeoJSON file
            locations='State',  # Column in your DataFrame
            color='State_Registered_user',  # Column in your DataFrame
            hover_name='State',  # Column in your DataFrame
            color_continuous_scale='Viridis',
            title=f"Registered user of each State in year {year} for the Quarter {quarter}"
        )

        # Update the map to fit the bounds of the locations
        choropleth_fig.update_geos(fitbounds="locations", visible=False)

        # Display the choropleth map in Streamlit
        tab1.plotly_chart(choropleth_fig)

        return df['State'].unique()

    def bar_graph_district_top_user(year, quarter, state):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')

        # Correct the SQL query syntax to get data for the selected year, quarter, and state
        query_district_transactions = f"""
        SELECT Districts, AVG(District_Registered_user) as District_Registered_user
        FROM top_user
        WHERE Year={year} AND Quarter={quarter} AND State='{state}'
        GROUP BY Districts """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_district_transactions)
        data = cursor.fetchall()

        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]

        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Debug: Print the fetched data
        tab2.text("Fetched Data for Bar Graph:")
        tab2.table(df)

        # Check if the DataFrame is empty
        if df.empty:
            tab2.warning(f"No data available for {state} in year {year} for quarter {quarter}")
            connection.close()
            return

        # Create the bar graph
        bar_fig = px.bar(
            df,
            x='Districts',
            y='District_Registered_user',
            color='District_Registered_user',
            title=f"District Registered user in {state} for Year {year} Quarter {quarter}"
        )

        # Display the bar graph in Streamlit
        tab2.plotly_chart(bar_fig)

        # Close the database connection
        connection.close()

    def pie_chart_pincode_top_user(year, quarter, state, district):
        # Establish database connection
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')

        # Correct the SQL query syntax to get data for the selected year, quarter, state, and district
        query_pincode_transactions = f"""
        SELECT Pincode, SUM(Pincode_Registered_user) as Pincode_Registered_user
        FROM top_user 
        WHERE Year={year} AND Quarter={quarter} AND State='{state}' AND Districts='{district}'
        GROUP BY Pincode """
        
        # Execute the query and fetch the data
        cursor = connection.cursor()
        cursor.execute(query_pincode_transactions)
        data = cursor.fetchall()

        # Retrieve the column names from the cursor
        columns = [desc[0] for desc in cursor.description]

        # Load the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        if df.empty:
            tab3.warning(f"No pie chart data available for {state} in year {year} for quarter {quarter}")
            connection.close()
            return

        # Create the pie chart
        pie_fig = px.pie(
            df,
            names='Pincode',
            values='Pincode_Registered_user',
            title=f"Pincode Registered user in {district} for Year {year} Quarter {quarter}"
        )

        # Display the pie chart in Streamlit
        tab3.plotly_chart(pie_fig)

        # Close the database connection
        connection.close()
    

    if tab1.checkbox("Top Registered user "):
        geo_visual_top_user(year, quarter)
        

    if tab2.checkbox("District_top_user"):
        year_bar = year
        quarter_bar = quarter
        # Establish database connection to get states directly from top_trans table
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        query_states = "SELECT DISTINCT State FROM top_user"
        cursor = connection.cursor()
        cursor.execute(query_states)
        states_bar_top_user = cursor.fetchall()
        connection.close()
        
        states_bar_list_top_user = [state[0] for state in states_bar_top_user]
        
        selected_state_for_bar_top_user = tab2.selectbox('Select a state for the bar graph of top user:', states_bar_list_top_user)

        # Display the bar graph based on user selections
        bar_graph_district_top_user(year_bar, quarter_bar, selected_state_for_bar_top_user)

    if tab3.checkbox("Top User in Pie"):
        year_pie = year
        quarter_pie = quarter
        # Establish database connection to get states directly from top_trans table
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        query_states = "SELECT DISTINCT State FROM top_user"
        cursor = connection.cursor()
        cursor.execute(query_states)
        states_pie_top_user = cursor.fetchall()
        
        states_pie_list_top_user = [state[0] for state in states_pie_top_user]
        
        selected_state_for_pie_top_user= tab3.selectbox('Select a state for the pie chart of top_user:', states_pie_list_top_user)

        query_districts = f"SELECT DISTINCT Districts FROM top_user WHERE State='{selected_state_for_pie_top_user}'"
        cursor = connection.cursor()
        cursor.execute(query_districts)
        districts_pie_top_user = cursor.fetchall()
        connection.close()

        district_pie_list_top_user = [district[0] for district in districts_pie_top_user]
        
        selected_district_for_pie_top_user= tab3.selectbox('Select a district for the pie chart of the top_user:', district_pie_list_top_user)

        year_pie = year
        quarter_pie = quarter
        state = selected_state_for_pie_top_user
        district= selected_district_for_pie_top_user
        # Display the pie chart based on user selections
        pie_chart_pincode_top_user(year, quarter,state,district)

if st.session_state.page_select == 'Queries':
    st.header("Queries you may have")
    
    queries = {
        "What are the top 10 States which has the highest transaction count in aggregate transaction of Recharge and Bill payments in last quarter of year 2020 ?": '''SELECT State, Transaction_count from agg_trans where 
                            Year = 2020 and Quarter= 4 and Transaction_Type= "Recharge & bill payments" order by Transaction_count desc limit 10;''',
        "What are the top 10 States which has the highest transaction amount in aggregate transaction of Financial Services in first quarter of year 2022 ?": '''SELECT State, Transaction_amount from agg_trans where 
                            Year = 2022 and Quarter= 1 and Transaction_Type= "Financial Services" order by Transaction_amount desc limit 10;''',
        "What are the Top 10 States which has the least Transaction count in Map Transactions for the year 2019 and in Quarter 2?": '''SELECT State, Transaction_count from map_trans where Year = 2019 and Quarter= 2 order by 
                                                    Transaction_count asc limit 10;''',
        "How many Districts were there in each State of Map Transaction?": '''SELECT State, count(distinct District) as District_count from map_trans group by State;''',
        "How many Pincodes were there in each District of Top Transaction?": '''SELECT Districts, count(distinct Pincode) as Pincode_count from top_trans group by Districts;''',
        "What are the top 10 Pincodes having highest Pincode_Transaction_count for the year 2018 and quarter 3 for the District Chennai ?": '''SELECT Pincode, AVG(Pincode_Transaction_count) AS Avg_Transaction_Count
                    FROM top_trans WHERE Year = 2018 AND Quarter = 3 AND Districts = 'chennai' GROUP BY Pincode ORDER BY Avg_Transaction_Count DESC LIMIT 10;''',
        "What are the brands in aggregate user?": '''SELECT distinct Brand_name FROM agg_user;''',
        "what are the Top 10 brands having highest Registered users for the year 2020 in quarter 2?": '''SELECT Brand_name, SUM(Registered_Users_of_brand) as Total_Registered_Users FROM agg_user WHERE Year = 2020 AND Quarter = 2
                                                                                                        GROUP BY Brand_name  ''',
        "How many Map Registered Users were there in state Tamilnadu in the year 2022 and in quarter 3?": '''select State,District, sum(Registered_Users)as Registered_Users from map_user where Year = 2022 and Quarter = 3 and State = "tamil-nadu" group by District''',
        "How many Map App opens were there in state Assam in the year 2023 and in quarter 2?": '''select State,District, sum(App_opens) as App_opens from map_user where Year = 2023 and Quarter = 2 and State = "assam" group by District''',
        "What are the Top Registered Users were there in state karnataka in the year 2022 and in quarter 3?": '''select State,Districts, sum(District_Registered_user)as District_Registered_user from top_user where Year = 2022 and Quarter = 3 and State = "karnataka" group by Districts order by District_Registered_user desc limit 10''',
        "What are the Top Pincode Registered there in Jorhat District in the state of  Assam in the year 2021 and in quarter 3?": '''SELECT State,Districts,Pincode,SUM(Pincode_Registered_user) AS Pincode_Registered_user FROM top_user WHERE 
    Year = 2021 AND Quarter = 3 AND State = 'assam' AND Districts = 'jorhat' group BY State, Districts, Pincode order by Pincode_Registered_user desc limit 10 ''' }

    query_option = st.selectbox("Select a query to run", list(queries.keys()))

    if st.button("Run Query"):
        query = queries[query_option] # type: ignore
        myconnection = pymysql.connect(host='127.0.0.1', user='root', passwd='Kamaraj@2000', database='phonepe_project')
        cursor = myconnection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        myconnection.close()
        df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])
        print("DataFrame:")
        print(df)  # Print the DataFrame to inspect its contents
        st.table(df)

    # Store the dataframe in session state for later use
        st.session_state['df'] = df 
        st.session_state['query_option'] = query_option

# Check if a DataFrame exists in the session state
    if 'df' in st.session_state and not st.session_state['df'].empty:
        if st.button("Pictorial representation"):
            df = st.session_state['df']
            query_option = st.session_state['query_option']
            
            # Create the appropriate plot based on the query option
            if query_option == "What are the top 10 States which has the highest transaction count in aggregate transaction of Recharge and Bill payments in last quarter of year 2020 ?":
                fig = px.bar(df, x="State", y="Transaction_count", color="State",hover_data= "Transaction_count", title="Top 10 States having the highest transaction count in aggregate transaction of Recharge and Bill payments in last quarter of year 2020")
                st.plotly_chart(fig)
            elif query_option == "What are the top 10 States which has the highest transaction amount in aggregate transaction of Financial Services in first quarter of year 2022 ?":
                fig = px.bar(df, x="State", y="Transaction_amount", color="State", title="Top 10 States having the highest transaction amount in aggregate transaction of Financial Services in first quarter of year 2022")
                st.plotly_chart(fig)
            elif query_option == "What are the top 10 States which has the least Transaction count in Map Transactions for the year 2019 and in Quarter 2?":
                fig = px.bar(df, x="State", y="Transaction_count", color="State", title="Top 5 States having the least Transaction count in Map Transactions for the year 2019 and in Quarter 2")
                st.plotly_chart(fig)
            elif query_option == "How many Districts were there in each State of Map Transaction?":
                fig = px.bar(df, x="State", y="District_count",color= "State", title="Districts in each State of Map Transaction")
                st.plotly_chart(fig)
            elif query_option == "How many Pincodes were there in each District of Top Transaction?":
                fig = px.bar(df, x="Districts", y="Pincode_count",color="Districts",title="Pincodes in each District of Top Transaction")
                st.plotly_chart(fig)
            elif query_option == "What are the top 10 Pincodes having highest Pincode_Transaction_count for the year 2018 and quarter 3 for the District Chennai ?":
                fig = px.pie(df, values="Avg_Transaction_Count", names ="Pincode",title="Top 10 Pincodes having highest Pincode_Transaction_count for the year 2018 and quarter 3 for the District Chennai")
                st.plotly_chart(fig)
            elif query_option == "what are the Top 10 brands having highest Registered users for the year 2020 in quarter 2?":
                fig = px.pie(df, values="Total_Registered_Users", names="Brand_name",title="Top 10 Brands with highest Registered users")
                st.plotly_chart(fig)
            elif query_option == "How many Map Registered Users were there in state Tamilnadu in the year 2022 and in quarter 3?":
                fig = px.bar(df, x="District", y="Registered_Users",hover_name="State", title="Map Registered Users in Tamilnadu for the year 2022 in quarter 3")
                st.plotly_chart(fig)
            elif query_option == "How many Map App opens were there in state Assam in the year 2023 and in quarter 2?":
                fig = px.bar(df, x="District", y="App_opens",hover_name="State", title="Map App openers in Assam for the year 2023 in quarter 2")
                st.plotly_chart(fig)
            elif query_option == "What are the Top Registered Users were there in state karnataka in the year 2022 and in quarter 3?":
                fig = px.bar(df, x="Districts", y="District_Registered_user",hover_name="State", title="Top Registered Users in Karnataka for the year 2022 in quarter 3")
                st.plotly_chart(fig)
            elif query_option == "What are the Top Pincode Registered there in Jorhat District in the state of  Assam in the year 2021 and in quarter 3?":
                fig = px.pie(df, values="Pincode_Registered_user",names="Pincode", title="Top Pincode Registered Users in Jorhat District of Assam for the year 2022 in quarter 3")
                st.plotly_chart(fig)
            else:
                st.warning("Graph for this query option is not configured yet.")
