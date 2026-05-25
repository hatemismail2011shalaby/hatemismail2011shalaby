#!/usr/bin/env python3
"""
FILE: wfm_forecast.py
PURPOSE: Automate Erlang C calculations for WFM scheduling
AUTHOR: Hatem Shalaby
"""

import pandas as pd
import numpy as np

def calculate_erlang_c(traffic_intensity, agents):
    """
    Approximate Erlang C formula for wait probability.
    """
    if agents <= 0:
        return 1.0
    
    utilization = traffic_intensity / agents
    if utilization >= 1.0:
        return 1.0 # System unstable
    
    # Simplified approximation for demonstration
    return np.exp(-agents * (1 - utilization))

def generate_schedule(input_file, output_file, target_service_level=0.80):
    """
    Reads volume data and generates optimal staffing schedule.
    """
    try:
        df = pd.read_excel(input_file)
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
        return

    # Calculate Traffic Intensity (A = Calls * AHT / 3600)
    df['traffic_intensity'] = (df['call_volume'] * df['avg_asec']) / 3600
    
    # Dynamic staffing calculation
    required_staff = []
    for _, row in df.iterrows():
        traffic = row['traffic_intensity']
        agents = 1
        while calculate_erlang_c(traffic, agents) > (1 - target_service_level):
            agents += 1
        required_staff.append(agents)
    
    df['required_fte'] = required_staff
    
    # Save output
    df.to_excel(output_file, index=False)
    print(f"Schedule generated: {output_file}")
    print(f"Total FTEs required: {sum(required_staff)}")

if __name__ == "__main__":
    # Example usage: Uncomment to run locally
    # generate_schedule('raw_volume_data.xlsx', 'optimized_schedule.xlsx')
    pass
