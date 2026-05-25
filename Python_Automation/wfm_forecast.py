
import pandas as pd
import numpy as np

def generate_wfm_schedule(volume_data, target_shr=0.8):
    """
    Calculates required FTEs based on Erlang C logic approximation.
    """
    df = pd.read_excel(volume_data)
    df['traffic_intensity'] = df['call_volume'] * df['avg_asec'] / 3600
    df['required_agents'] = np.ceil(df['traffic_intensity'] / target_shr)
    
    # Output to Excel
    with pd.ExcelWriter('optimized_schedule.xlsx') as writer:
        df[['interval', 'required_agents']].to_excel(writer, index=False)
    return "Schedule generated."
