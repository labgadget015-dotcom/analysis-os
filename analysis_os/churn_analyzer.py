"""Churn Analysis Module - Identifies and predicts customer churn risk.

Provides tools for:
- Historical churn analysis
- Predictive modeling
- Segmentation by risk level
- Retention action recommendations
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from datetime import datetime, timedelta


class ChurnAnalyzer:
    """Analyze and predict customer churn patterns."""
    
    def __init__(self, data: pd.DataFrame, customer_col: str = 'customer_id',
                 date_col: str = 'date', revenue_col: str = 'revenue'):
        """Initialize ChurnAnalyzer with transaction data.
        
        Args:
            data: DataFrame with transaction history
            customer_col: Column name for customer identifier
            date_col: Column name for transaction date
            revenue_col: Column name for revenue/value
        """
        self.data = data.copy()
        self.customer_col = customer_col
        self.date_col = date_col
        self.revenue_col = revenue_col
        self._prepare_data()
    
    def _prepare_data(self):
        """Prepare and validate data."""
        self.data[self.date_col] = pd.to_datetime(self.data[self.date_col])
        self.latest_date = self.data[self.date_col].max()
    
    def calculate_churn_rate(self, lookback_days: int = 90,
                             churned_days: int = 60) -> float:
        """Calculate churn rate over period.
        
        Args:
            lookback_days: Period to analyze
            churned_days: Days inactive to be considered churned
            
        Returns:
            Churn rate as percentage
        """
        cutoff_date = self.latest_date - timedelta(days=lookback_days)
        active_customers = self.data[self.data[self.date_col] >= cutoff_date][self.customer_col].unique()
        
        inactive_cutoff = self.latest_date - timedelta(days=churned_days)
        churned = self.data[(self.data[self.date_col] < inactive_cutoff) &
                            (self.data[self.customer_col].isin(active_customers))][self.customer_col].unique()
        
        if len(active_customers) == 0:
            return 0.0
        return (len(churned) / len(active_customers)) * 100
    
    def identify_at_risk_customers(self, inactivity_days: int = 45,
                                   min_historical_revenue: float = 100) -> pd.DataFrame:
        """Identify customers at risk of churn.
        
        Args:
            inactivity_days: Days without activity triggers at-risk flag
            min_historical_revenue: Minimum historical value to consider
            
        Returns:
            DataFrame of at-risk customers with risk metrics
        """
        risk_date = self.latest_date - timedelta(days=inactivity_days)
        
        # Get customer summary
        customer_summary = self.data.groupby(self.customer_col).agg({
            self.date_col: ['max', 'count'],
            self.revenue_col: ['sum', 'mean']
        }).reset_index()
        
        customer_summary.columns = ['customer_id', 'last_activity', 'transaction_count',
                                    'total_revenue', 'avg_transaction']
        
        # Filter for at-risk
        at_risk = customer_summary[
            (customer_summary['last_activity'] < risk_date) &
            (customer_summary['total_revenue'] >= min_historical_revenue)
        ].copy()
        
        at_risk['days_inactive'] = (self.latest_date - at_risk['last_activity']).dt.days
        at_risk['risk_score'] = (at_risk['days_inactive'] / inactivity_days * 50 +
                                 at_risk['total_revenue'] / at_risk['total_revenue'].max() * 50)
        
        return at_risk.sort_values('risk_score', ascending=False)
    
    def segment_by_risk(self, at_risk_df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        """Segment customers into risk tiers.
        
        Args:
            at_risk_df: DataFrame from identify_at_risk_customers
            
        Returns:
            Dictionary with 'high', 'medium', 'low' risk segments
        """
        high_threshold = at_risk_df['risk_score'].quantile(0.66)
        med_threshold = at_risk_df['risk_score'].quantile(0.33)
        
        return {
            'high': at_risk_df[at_risk_df['risk_score'] >= high_threshold],
            'medium': at_risk_df[(at_risk_df['risk_score'] >= med_threshold) &
                                 (at_risk_df['risk_score'] < high_threshold)],
            'low': at_risk_df[at_risk_df['risk_score'] < med_threshold]
        }
    
    def generate_summary(self) -> Dict:
        """Generate comprehensive churn analysis summary.
        
        Returns:
            Dictionary with key metrics and insights
        """
        at_risk = self.identify_at_risk_customers()
        segments = self.segment_by_risk(at_risk)
        
        return {
            'total_customers': self.data[self.customer_col].nunique(),
            'churn_rate_90d': self.calculate_churn_rate(),
            'at_risk_count': len(at_risk),
            'high_risk_count': len(segments['high']),
            'high_risk_revenue': segments['high']['total_revenue'].sum(),
            'medium_risk_count': len(segments['medium']),
            'medium_risk_revenue': segments['medium']['total_revenue'].sum(),
            'risk_segmentation': segments
        }
