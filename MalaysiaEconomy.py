import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="Malaysia Economy Dashboard", layout="wide")

    st.title("🇲🇾 Malaysia Economy Dashboard")
    st.markdown("### An overview of key economic indicators and sectors")

    # Key Economic Indicators (Mock Data for Illustration)
    st.header("Key Indicators")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="GDP (Nominal)", value="$430.89 Billion", delta="4.2%")
    with col2:
        st.metric(label="GDP Per Capita", value="$13,380", delta="3.5%")
    with col3:
        st.metric(label="Inflation Rate", value="2.5%", delta="-0.3%", delta_color="inverse")
    with col4:
        st.metric(label="Unemployment Rate", value="3.3%", delta="-0.1%", delta_color="inverse")

    st.divider()

    # GDP Composition by Sector
    st.header("GDP Composition by Sector")
    
    # Data based on general estimates
    sector_data = {
        'Sector': ['Services', 'Manufacturing', 'Agriculture', 'Mining', 'Construction'],
        'Percentage': [58.2, 23.4, 7.1, 6.4, 3.6]
    }
    df_sectors = pd.DataFrame(sector_data)

    col_chart, col_text = st.columns([2, 1])

    with col_chart:
        st.bar_chart(df_sectors.set_index('Sector'))

    with col_text:
        st.write("""
        **Services**: The largest sector, driven by finance, tourism, and retail.
        
        **Manufacturing**: Key exports include electronics (E&E), petroleum products, and chemicals.
        
        **Agriculture**: Dominated by palm oil and rubber production.
        """)

    st.divider()

    # Trade Information
    st.header("Trade Highlights")
    tab1, tab2 = st.tabs(["Major Exports", "Major Imports"])

    with tab1:
        st.write("1. **Electrical & Electronic Products** (Semiconductors, etc.)")
        st.write("2. **Petroleum Products**")
        st.write("3. **Palm Oil**")
        st.write("4. **Liquefied Natural Gas (LNG)**")
    
    with tab2:
        st.write("1. **Electrical & Electronic Products**")
        st.write("2. **Chemicals & Chemical Products**")
        st.write("3. **Machinery, Equipment & Parts**")
        st.write("4. **Petroleum Products**")

if __name__ == "__main__":
    main()
