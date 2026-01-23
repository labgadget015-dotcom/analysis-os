"""Funnel Optimization Module - Analyzes and optimizes conversion funnels.

Provides tools for:
- Funnel stage analysis
- Bottleneck identification
- Drop-off quantification
- Optimization recommendations
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class FunnelStage:
    """Represents a single funnel stage."""
    name: str
    count: int
    value: float = 0.0
    
    @property
    def conversion_rate(self) -> float:
        """Get conversion rate (set by FunnelAnalyzer)."""
        return getattr(self, '_conversion_rate', 0.0)
    
    @conversion_rate.setter
    def conversion_rate(self, value: float):
        self._conversion_rate = value


class FunnelAnalyzer:
    """Analyze conversion funnel performance and identify optimization opportunities."""
    
    def __init__(self, data: pd.DataFrame, user_col: str = 'user_id',
                 stage_col: str = 'stage', timestamp_col: str = 'timestamp'):
        """Initialize FunnelAnalyzer.
        
        Args:
            data: DataFrame with user journey data
            user_col: Column name for user identifier
            stage_col: Column name for funnel stage
            timestamp_col: Column name for timestamp
        """
        self.data = data.copy()
        self.user_col = user_col
        self.stage_col = stage_col
        self.timestamp_col = timestamp_col
        self._analyze_stages()
    
    def _analyze_stages(self):
        """Analyze unique stages in the funnel."""
        self.stages = self.data[self.stage_col].unique().tolist()
        self.stage_order = self._determine_stage_order()
    
    def _determine_stage_order(self) -> Dict[str, int]:
        """Determine the order of stages in the funnel."""
        # Sort by first occurrence timestamp
        stage_times = self.data.groupby(self.stage_col)[self.timestamp_col].min().sort_values()
        return {stage: idx for idx, stage in enumerate(stage_times.index)}
    
    def get_funnel_stats(self) -> List[FunnelStage]:
        """Get conversion statistics for each funnel stage.
        
        Returns:
            List of FunnelStage objects with conversion data
        """
        funnel_stats = []
        total_users = self.data[self.user_col].nunique()
        
        for stage in sorted(self.stages, key=lambda s: self.stage_order.get(s, 999)):
            stage_data = self.data[self.data[self.stage_col] == stage]
            stage_users = stage_data[self.user_col].nunique()
            stage_value = stage_data.get('value', pd.Series()).sum() if 'value' in stage_data else 0.0
            
            fs = FunnelStage(name=stage, count=stage_users, value=stage_value)
            fs.conversion_rate = (stage_users / total_users * 100) if total_users > 0 else 0.0
            funnel_stats.append(fs)
        
        return funnel_stats
    
    def calculate_drop_offs(self) -> pd.DataFrame:
        """Calculate drop-off between consecutive stages.
        
        Returns:
            DataFrame with drop-off analysis
        """
        stats = self.get_funnel_stats()
        drop_offs = []
        
        for i in range(len(stats) - 1):
            current = stats[i]
            next_stage = stats[i + 1]
            drop_off_count = current.count - next_stage.count
            drop_off_rate = (drop_off_count / current.count * 100) if current.count > 0 else 0.0
            
            drop_offs.append({
                'from_stage': current.name,
                'to_stage': next_stage.name,
                'users_lost': drop_off_count,
                'drop_off_rate': drop_off_rate,
                'previous_count': current.count,
                'next_count': next_stage.count
            })
        
        return pd.DataFrame(drop_offs)
    
    def identify_bottlenecks(self, threshold: float = 30.0) -> pd.DataFrame:
        """Identify bottleneck transitions (high drop-off).
        
        Args:
            threshold: Drop-off rate threshold to flag as bottleneck
            
        Returns:
            DataFrame of bottlenecks exceeding threshold
        """
        drop_offs = self.calculate_drop_offs()
        bottlenecks = drop_offs[drop_offs['drop_off_rate'] >= threshold].copy()
        bottlenecks['priority_score'] = bottlenecks['users_lost'] * (bottlenecks['drop_off_rate'] / 100)
        
        return bottlenecks.sort_values('priority_score', ascending=False)
    
    def get_optimization_insights(self) -> Dict:
        """Generate comprehensive funnel optimization insights.
        
        Returns:
            Dictionary with recommendations and metrics
        """
        stats = self.get_funnel_stats()
        drop_offs = self.calculate_drop_offs()
        bottlenecks = self.identify_bottlenecks()
        
        # Calculate overall funnel efficiency
        if stats:
            overall_conversion = (stats[-1].count / stats[0].count * 100) if stats[0].count > 0 else 0.0
        else:
            overall_conversion = 0.0
        
        return {
            'total_users': self.data[self.user_col].nunique(),
            'num_stages': len(stats),
            'overall_conversion_rate': overall_conversion,
            'stages': stats,
            'drop_off_analysis': drop_offs,
            'critical_bottlenecks': bottlenecks,
            'optimization_opportunities': self._generate_recommendations(bottlenecks)
        }
    
    def _generate_recommendations(self, bottlenecks: pd.DataFrame) -> List[str]:
        """Generate optimization recommendations based on bottlenecks.
        
        Args:
            bottlenecks: DataFrame of identified bottlenecks
            
        Returns:
            List of actionable recommendations
        """
        recommendations = []
        
        if bottlenecks.empty:
            recommendations.append("Funnel is performing well - maintain current user experience.")
        else:
            top_bottleneck = bottlenecks.iloc[0]
            recommendations.append(
                f"Focus on {top_bottleneck['from_stage']} → {top_bottleneck['to_stage']}"
                f" transition ({top_bottleneck['drop_off_rate']:.1f}% drop-off)"
            )
            
            if len(bottlenecks) > 1:
                recommendations.append(f"Secondary bottleneck: {bottlenecks.iloc[1]['from_stage']} "
                                     f"→ {bottlenecks.iloc[1]['to_stage']}")
        
        return recommendations
