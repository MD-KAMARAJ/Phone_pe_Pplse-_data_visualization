# phonepe_pulse_data_visualization
## Project Overview

This project provides interactive data visualizations and insights into PhonePe's business trends using data from the PhonePe Pulse GitHub repository. By using Python libraries like pandas, Streamlit, Plotly, and Pymysql, along with a MySQL database, user can surf with numerics like transaction volume, types, and geographical distribution.

## Key Functionalities

### Data Extraction and Transformation (ETL):
- Extracts data from the PhonePe Pulse GitHub repository (instructions provided below).
- Applies necessary data cleaning and transformation steps.
- For detailed information on specific functions or configurations, refer to the provided Python scripts [phone_pe_data_extraction.ipynb].
- Feel free to modify the project to suit your specific needs and customizations.

### Exploratory Data Analysis (EDA):
- Analyzes data trends and patterns to identify key insights.
- Cleans and prepares data for visualization.

### Interactive Dashboard:
- Built with Streamlit for a user-friendly web interface.
- Gives a overview through animation in bar graph and detailed analysis in geo maps, bar charts, pie charts,using plotly and ploylt express.
- Offers interactive filters and controls to refine visualizations based on user selections.

### Technologies Used

1. Python
2. pandas
3. MySQL Connector/Python
4. pymysql
5. Plotly (for interactive visualizations)
6. Streamlit (for web app development)
7.json
8.base64(for background image)
## Getting Started

### Prerequisites:
- Install Python and the listed libraries.
- Set up a MySQL database server

### Data Acquisition:
- Clone the PhonePe Pulse repository from GitHub (https://github.com/PhonePe/pulse).
- Place the cloned repository in the same directory as this project

### Settingup Instructions
- Clone the repository to your local machine using git clone ()

### Running the Application
- Open a terminal and navigate to the project directory.
- Run the application using the command streamlit run phone_pe_final.py.
- Access the Streamlit app in your web browser by opening the link displayed in the terminal (usually http://localhost:8501).

### Interactive Dashboard

The Streamlit app provides an intuitive interface to explore PhonePe Pulse data. Users can interact with various features:

- **Filters:**
   - Select specific timeframes (e.g., year, quarter, state) for a more focused analysis.
- **Visualizations:**
    - Explore trends using animative and interactive charts and maps.
    - Gain insights into transaction volume, types, and geographical distribution.

### Disclaimer:

This project is for educational purposes only and does not represent an official product of PhonePe. Refer to the PhonePe Pulse repository's terms of use or licensing information for any restrictions on data usage.

### Contributing

We welcome contributions to this project. Feel free to submit pull requests for bug fixes, feature improvements, or new functionalities. Please follow coding style guidelines (if any) and provide clear documentation for your changes

### Contact

For any questions or feedback, feel free to reach out to [email_id: m.d.kamaraj2000@gmail.com]

### License
This project is licensed under the Apache-2.0 license - see the LICENSE.md file for details
