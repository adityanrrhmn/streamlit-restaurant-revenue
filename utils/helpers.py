"""
Helper functions for the Streamlit Dashboard
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def load_data(file_path: str = None, uploaded_file=None) -> pd.DataFrame:
    """
    Load data from file path or uploaded file
    
    Args:
        file_path: Path to CSV file
        uploaded_file: Streamlit uploaded file object
    
    Returns:
        pandas DataFrame
    """
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    elif file_path is not None:
        df = pd.read_csv(file_path)
    else:
        raise ValueError("Either file_path or uploaded_file must be provided")
    
    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the dataframe
    
    Args:
        df: Input DataFrame
    
    Returns:
        Preprocessed DataFrame
    """
    df = df.copy()
    
    # Convert Date column if exists
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.month_name()
        df['Day'] = df['Date'].dt.day
        df['DayOfWeek'] = df['Date'].dt.day_name()
    
    return df


def create_line_chart(df: pd.DataFrame, x_col: str, y_col: str, 
                      color_col: str = None, title: str = "Line Chart") -> go.Figure:
    """
    Create an interactive line chart
    """
    fig = px.line(
        df, x=x_col, y=y_col, color=color_col,
        title=title,
        template="plotly_dark",
        markers=True
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        hovermode='x unified'
    )
    return fig


def create_bar_chart(df: pd.DataFrame, x_col: str, y_col: str,
                     color_col: str = None, title: str = "Bar Chart",
                     orientation: str = 'v') -> go.Figure:
    """
    Create an interactive bar chart
    """
    fig = px.bar(
        df, x=x_col, y=y_col, color=color_col,
        title=title,
        template="plotly_dark",
        orientation=orientation,
        barmode='group'
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    return fig


def create_pie_chart(df: pd.DataFrame, values_col: str, names_col: str,
                     title: str = "Pie Chart") -> go.Figure:
    """
    Create an interactive pie chart
    """
    fig = px.pie(
        df, values=values_col, names=names_col,
        title=title,
        template="plotly_dark",
        hole=0.4  # Donut chart style
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig


def create_scatter_plot(df: pd.DataFrame, x_col: str, y_col: str,
                        color_col: str = None, size_col: str = None,
                        title: str = "Scatter Plot") -> go.Figure:
    """
    Create an interactive scatter plot
    """
    fig = px.scatter(
        df, x=x_col, y=y_col, color=color_col, size=size_col,
        title=title,
        template="plotly_dark",
        hover_data=df.columns
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    return fig


def create_heatmap(df: pd.DataFrame, title: str = "Correlation Heatmap") -> go.Figure:
    """
    Create a correlation heatmap for numeric columns
    """
    numeric_cols = df.select_dtypes(include=['number']).columns
    corr_matrix = df[numeric_cols].corr()
    
    fig = px.imshow(
        corr_matrix,
        text_auto='.2f',
        title=title,
        template="plotly_dark",
        color_continuous_scale='RdBu_r',
        aspect='auto'
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    return fig


def calculate_metrics(df: pd.DataFrame, sales_col: str = 'Sales', 
                      quantity_col: str = 'Quantity') -> dict:
    """
    Calculate key metrics from the dataframe
    """
    metrics = {
        'total_sales': df[sales_col].sum() if sales_col in df.columns else 0,
        'avg_sales': df[sales_col].mean() if sales_col in df.columns else 0,
        'total_quantity': df[quantity_col].sum() if quantity_col in df.columns else 0,
        'total_transactions': len(df),
        'unique_products': df['Product'].nunique() if 'Product' in df.columns else 0,
        'unique_regions': df['Region'].nunique() if 'Region' in df.columns else 0
    }
    return metrics


def filter_dataframe(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    """
    Apply filters to dataframe
    
    Args:
        df: Input DataFrame
        filters: Dictionary of column: value(s) to filter
    
    Returns:
        Filtered DataFrame
    """
    filtered_df = df.copy()
    
    for column, values in filters.items():
        if column in filtered_df.columns and values:
            if isinstance(values, list):
                filtered_df = filtered_df[filtered_df[column].isin(values)]
            else:
                filtered_df = filtered_df[filtered_df[column] == values]
    
    return filtered_df


def format_currency(value: float, prefix: str = "Rp") -> str:
    """
    Format number as Indonesian Rupiah currency
    """
    return f"{prefix} {value:,.0f}"


def format_number(value: float) -> str:
    """
    Format number with thousand separators
    """
    return f"{value:,.0f}"
