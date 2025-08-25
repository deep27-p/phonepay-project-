                PhonePe Transaction Insights

 📄 Problem Statement: PhonePe Transaction Insights Dashboard
This project is a **data visualization dashboard** built using **Streamlit, Plotly, and Pandas.It analyzes and visualizes **PhonePe transaction data** across Indian states with interactive charts and maps.The main objective of the project is to provide insights into **transaction trends, distributions, and regional comparisons** through an easy-to-use web application.`
1. Introduction

Digital payments in India have seen exponential growth, driven by platforms like **PhonePe**, which enable seamless financial transactions. Analyzing these transaction patterns can provide valuable insights into **user behavior, transaction distribution, and market penetration across different states**. However, there is a lack of interactive, visual, and real-time dashboards that allow stakeholders to explore this data effectively.

 2. Problem Definition

Currently, transaction data is available in raw form but is difficult to interpret due to the following challenges:

* **Lack of Visualization:** Raw CSV and JSON data do not provide clear insights without proper visualization.
* **Geographical Complexity:** Understanding state-wise distribution requires geospatial mapping.
* **Decision-Making Gap:** Businesses, policymakers, and researchers struggle to derive actionable insights without an intuitive interface.

Thus, there is a need to build a **Streamlit-based interactive dashboard** that visualizes PhonePe transaction insights across Indian states using **maps, charts, and filters**.



 3. Objectives

* To build a **data visualization dashboard** using Streamlit.
* To integrate **India GeoJSON maps** for state-level transaction analysis.
* To provide **interactive filters** (Year, State) for customized insights.
* To represent insights through **metrics, choropleth maps, bar charts, and pie charts**.
* To enable **decision-making support** for stakeholders like businesses and analysts.

 4. Scope of the Project

* **In-scope**:

  * Visualization of state-wise transaction distribution.
  * Representation of total, average, and comparative transaction amounts.
  * User-friendly interface with Streamlit.

* **Out-of-scope**:

  * Real-time live API integration from PhonePe (due to restrictions).
  * User authentication and payment gateway functionality.
 5. Expected Outcomes

* An **interactive dashboard** where users can explore PhonePe transaction patterns.
* **Geospatial representation** of transactions on India’s map.
* **Comparative insights** via bar charts and pie charts.
* A structured way to analyze **digital payment trends across states**.

---

⚡ This document can serve as the **Problem Statement section** in your final year project report.

👉 Do you want me to also prepare a **separate "Project Objectives & Deliverables" section** that you can attach right after this in your report?


Additionally added the features:
1. Decoding Transaction Dynamics on PhonePe
The leadership team seeks a deeper understanding of these patterns to drive targeted business strategies.
2. Device Dominance and User Engagement Analysis
PhonePe aims to enhance user engagement and improve app performance by understanding user preferences across different device brands. 


3. Insurance Penetration and Growth Potential Analysis

PhonePe has ventured into the insurance domain, providing users with options to secure various policies..
4. Transaction Analysis for Market Expansion
PhonePe operates in a highly competitive market, and understanding transaction dynamics at the state level is crucial for strategic decision-making. 
5. User Engagement and Growth Strategy
PhonePe seeks to enhance its market position by analyzing user engagement across different states and districts. 
Objective for phonepe
**“PhonePe Transaction Insights Dashboard”** (using Streamlit, Pandas, Plotly, and GeoJSON for India maps), here’s a clear **objective** you can include in your report:
 🎯 Project Objective
The main objective of this project is to **analyze and visualize PhonePe transaction data** across different states of India, enabling better understanding of digital payment trends. The project aims to:
1. **Provide interactive dashboards** for exploring transaction patterns across Indian states.
2. **Visualize transaction amounts geographically** using choropleth maps for state-level comparisons.
3. **Offer statistical insights** such as total transactions, average transaction per state, and number of states involved.
4. **Enable state-wise and year-wise filtering** of data for customized analysis.
5. **Compare states through charts** (bar chart, pie chart) to highlight distribution and growth trends.
6. **Present raw data tables** for detailed examination of underlying records.
🎯 Advantages of phonepe Project
1.Interactive Dashboard
 * Built using **Streamlit**, so it’s easy to use and doesn’t require advanced coding to interact with.
 * Sidebar filters let users explore by state and year dynamically.
2. Clear Visualizations
* Choropleth Map: Shows transaction amounts across India with geographical context.
* Bar Chart**: Compares state-wise totals for quick ranking.
 * Pie Chart**: Displays distribution of transactions, highlighting major contributors.

3. Data Insights at a Glance
 * Displays total transactions, average per state, and number of active states** using `st.metric`.
 * Helps stakeholders quickly understand transaction trends without digging into raw data.

4. Real-time & Scalable
 * Fetches data dynamically from an online CSV and GeoJSON — so it can easily be updated with live PhonePe datasets.
 * Works well for larger datasets if needed.


5.Educational Value
 * Demonstrates integration of multiple Python libraries:
 * Streamlit** (dashboard/UI)
 * Pandas** (data manipulation)
 *Plotly** (interactive visualizations)
 * Requests/JSON** (handling GeoJSON data)

6. Practical Use Case
  * Can be used by financial analysts, businesses, or policymakers to understand digital payment adoption** across regions.
 * Useful for market expansion strategies (which states have low/high adoption).

7. User-Friendly & Lightweight
 * Runs in a browser, no complex setup needed.
 * Provides both **visual + raw table preview**, making it useful for both analysts and general users.

Technologies Used
* **Python 3.9+**
* **Streamlit** – for building the dashboard interface
* **Pandas** – for data manipulation
* **Plotly Express** – for creating interactive charts and maps
* **Requests & JSON** – for fetching and processing geojson/state boundary data
* **PyArrow** (used internally by Streamlit for dataframes)
 Features Implemented
 🔹 Data Handling
1. Fetches transaction data from an online **CSV dataset**.
2. Preprocesses the data (renaming columns, filtering states, etc.).
3. Loads **GeoJSON** data to enable Indian state-level mapping.
 🔹 Interactive Filters
    1. Sidebar with **multi-select filters** for:
    2. State(s) * Year(s) (if available in dataset)
   🔹 Key Metrics
1.Total Transaction Amount**
2.Average Transaction Amount per State**
3.Number of States Selected**

🔹 Visualizations
1. **Choropleth Map** – Transaction amount by state (color-coded on India map).
2. **Bar Chart** – State-wise transaction totals, sorted in descending order.
3. **Pie Chart** – Distribution of transaction amounts by state.
4. **Data Table** – Interactive preview of the filtered dataset.

System Workflow
1. Data Loading:
    *CSV dataset is fetched using Pandas.
   * State boundaries are fetched using GeoJSON.

2. Filtering & Processing
  * User-selected states and years are applied.
   * Data is aggregated for metrics and plots.
 3. Visualization
  * Plotly Express generates interactive charts.
   * Streamlit displays them in a clean, interactive UI.
4. Limitations
* Currently uses a **sample dataset** (COVID active cases mapped as transactions).
* Yearly breakdown only works if dataset has `Year` column.
* Requires **internet connectivity** to fetch GeoJSON and CSV.

 5. Future Enhancements
* Replace demo dataset with **actual PhonePe Pulse data**.
* Add **district-level analysis**.
* Implement **trend line charts** (monthly/quarterly).
* Export insights as **PDF/Excel reports**.

Conclusion
This project successfully demonstrates how **Streamlit + Plotly** can be used to create an **interactive dashboard for financial/transaction insights**.
It can easily be extended to real-world PhonePe data, providing businesses and analysts with powerful tools for **decision-making and regional analysis**.
▶️ How to Run the PhonePe Transaction Insight Dashboard
Launch the Streamlit Dashboard
Run the app using: bash streamlit run phonepa.py 🌐 Open your browser and go to:  http://localhost:8501/
