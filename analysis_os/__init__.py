"""Analysis & AI Consulting OS - Production Framework

A unified operating system for data-driven insights and actionable recommendations.
Provides 5-stage pipeline, reusable prompts, checklists, and production-grade automation.
"""

__version__ = "1.0.0"
__author__ = "Gadget Lab"
__license__ = "MIT"

from .core import (
    AnalysisOS,
    AnalysisStage,
    AnalysisConfig,
)
from .data import DataManager
from .llm import LLMAnalyzer
from .reporting import ReportGenerator

__all__ = [
    "AnalysisOS",
    "AnalysisStage",
    "AnalysisConfig",
    "DataManager",
    "LLMAnalyzer",
    "ReportGenerator",
]
