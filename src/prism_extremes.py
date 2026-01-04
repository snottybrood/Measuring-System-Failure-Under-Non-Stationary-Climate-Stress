"""
prism_extremes.py

Core functions for analyzing extreme rainfall frequency using
observed precipitation data (e.g., PRISM).

This module implements threshold-based exceedance logic and
epoch-based frequency comparisons under non-stationarity.

These functions are intentionally simple and transparent.
"""

from pathlib import Path
import pandas as pd


# -------------------------------------------------------------------
# Data loading
# -------------------------------------------------------------------

def load_prism_timeseries(
    filepath: Path | str,
    date_col: str = "Date",
    precip_col: str = "inchesPpt"
) -> pd.DataFrame:
    """
    Load a PRISM-derived precipitation time series.

    Parameters
    ----------
    filepath : Path or str
        Path to CSV containing daily precipitation.
    date_col : str
        Name of the date column.
    precip_col : str
        Name of the precipitation column (in inches).

    Returns
    -------
    pd.DataFrame
        DataFrame indexed by datetime with a precipitation column.
    """
    df = pd.read_csv(filepath, parse_dates=[date_col])
    df = df.set_index(date_col)
    df = df.sort_index()

    if precip_col not in df.columns:
        raise ValueError(f"Column '{precip_col}' not found in input data.")

    return df[[precip_col]]


# -------------------------------------------------------------------
# Extreme event logic
# -------------------------------------------------------------------

def flag_extreme_events(
    df: pd.DataFrame,
    precip_col: str = "inchesPpt",
    threshold_in: float = 3.0
) -> pd.Series:
    """
    Flag days exceeding a fixed precipitation threshold.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame indexed by datetime.
    precip_col : str
        Column containing daily precipitation totals (inches).
    threshold_in : float
        Extreme rainfall threshold in inches.

    Returns
    -------
    pd.Series
        Boolean series indicating extreme rainfall events.
    """
    return df[precip_col] >= threshold_in


def count_annual_extremes(
    extreme_flags: pd.Series
) -> pd.Series:
    """
    Count extreme rainfall events by calendar year.

    Parameters
    ----------
    extreme_flags : pd.Series
        Boolean series indexed by datetime.

    Returns
    -------
    pd.Series
        Annual count of extreme events.
    """
    return extreme_flags.resample("Y").sum().astype(int)


# -------------------------------------------------------------------
# Epoch comparison
# -------------------------------------------------------------------

def aggregate_epochs(
    annual_counts: pd.Series,
    epoch_1: tuple[int, int],
    epoch_2: tuple[int, int]
) -> pd.DataFrame:
    """
    Aggregate annual extreme counts into two epochs
    and compute absolute and percent change.

    Parameters
    ----------
    annual_counts : pd.Series
        Annual extreme event counts.
    epoch_1 : tuple (start_year, end_year)
        First historical epoch (inclusive).
    epoch_2 : tuple (start_year, end_year)
        Second historical epoch (inclusive).

    Returns
    -------
    pd.DataFrame
        Summary table with counts and percent change.
    """
    def _slice_epoch(series, start, end):
        return series[
            (series.index.year >= start) &
            (series.index.year <= end)
        ].sum()

    count_1 = _slice_epoch(annual_counts, *epoch_1)
    count_2 = _slice_epoch(annual_counts, *epoch_2)

    if count_1 == 0:
        pct_change = None
    else:
        pct_change = (count_2 - count_1) / count_1 * 100.0

    return pd.DataFrame({
        "epoch_1_start": [epoch_1[0]],
        "epoch_1_end": [epoch_1[1]],
        "epoch_2_start": [epoch_2[0]],
        "epoch_2_end": [epoch_2[1]],
        "epoch_1_event_count": [count_1],
        "epoch_2_event_count": [count_2],
        "percent_change": [pct_change]
    })


# -------------------------------------------------------------------
# Convenience wrapper (optional, but useful)
# -------------------------------------------------------------------

def prism_extreme_frequency_pipeline(
    filepath: Path | str,
    threshold_in: float,
    epoch_1: tuple[int, int],
    epoch_2: tuple[int, int],
    date_col: str = "Date",
    precip_col: str = "inchesPpt"
) -> tuple[pd.Series, pd.DataFrame]:
    """
    End-to-end helper for PRISM extreme rainfall analysis.

    Parameters
    ----------
    filepath : Path or str
        Path to PRISM precipitation CSV.
    threshold_in : float
        Extreme rainfall threshold in inches.
    epoch_1 : tuple
        First epoch (start_year, end_year).
    epoch_2 : tuple
        Second epoch (start_year, end_year).

    Returns
    -------
    annual_counts : pd.Series
        Annual extreme event counts.
    epoch_summary : pd.DataFrame
        Epoch comparison summary table.
    """
    df = load_prism_timeseries(
        filepath,
        date_col=date_col,
        precip_col=precip_col
    )

    extreme_flags = flag_extreme_events(
        df,
        precip_col=precip_col,
        threshold_in=threshold_in
    )

    annual_counts = count_annual_extremes(extreme_flags)

    epoch_summary = aggregate_epochs(
        annual_counts,
        epoch_1=epoch_1,
        epoch_2=epoch_2
    )

    return annual_counts, epoch_summary
