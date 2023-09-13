# 1. Import Signal 
import csv

# Path to the CSV file
file_path = '/Users/nada/Desktop/FullSignal.csv'

# List to store the contents of the CSV file
signal = []

# Open the CSV file and read its contents
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file and append to the signal list
    for signalsample in csv_reader:
        signal.append(signalsample)

# Now, the signal variable contains the contents of the CSV file
#print(signal)




#2. Normalize Signal 
min_value = min(float(val) for signalsample in signal for val in signalsample)
max_value = max(float(val) for signalsample in signal for val in signalsample)

normalized_signal = [[(float(val) - min_value) / (max_value - min_value) for val in signalsample] for signalsample in signal]

#print(normalized_signal)




#3. Visualize Signals
import plotly.graph_objects as go

# Calculate the time array in milliseconds
frequency = 125
sampling_interval_ms = 1000 / frequency
time_ms = [i * sampling_interval_ms for i in range(len(normalized_signal[0]))]

# Create a Plotly figure
fig = go.Figure()

# Iterate over each row in the normalized_signal and add it to the figure
for index, signalsample in enumerate(normalized_signal):
    fig.add_trace(go.Scatter(x=time_ms, y=signalsample, mode='lines', name=f'Signal {index + 1}'))

# Update layout for better visualization
fig.update_layout(title='Plot of Each Signal',
                  xaxis_title='Time (milliseconds)',
                  yaxis_title='Value')

# Show the plot
fig.show()




#4. Detect Peaks and Peak Distances 
import numpy as np
import plotly.graph_objects as go
from scipy.signal import find_peaks

# Calculate the time array in milliseconds
frequency = 125  # Adjust these values as needed based on your signal frequency 
sampling_interval_ms = 1000 / frequency 
time_ms = [i * sampling_interval_ms for i in range(len(normalized_signal[0]))]

PeaktoPeak =[]  # Initialize the HRV list

# Loop for detecting peaks and saving peak distances in HRV
for index, signalsample in enumerate(normalized_signal):
    # Detect peaks with refinements
    peaks, _ = find_peaks(signalsample, height=0.5, distance=10, prominence=0.3)  # Adjust these values as needed
    
    # Calculate distances between peaks in milliseconds
    distances = [(peaks[i+1] - peaks[i]) * sampling_interval_ms for i in range(len(peaks)-1)]
    
    # Append the distances to the Distance List 
    PeaktoPeak.append(distances)


    

#5.Visualzie Peaks and Peak Distances 
import plotly.graph_objects as go
from scipy.signal import find_peaks

# Calculate the time array in milliseconds
frequency = 125
sampling_interval_ms = 1000 / frequency
time_ms = [i * sampling_interval_ms for i in range(len(normalized_signal[0]))]

PeaktoPeak = []

# Loop for plotting each signalsample with peaks using Plotly
for index, signalsample in enumerate(normalized_signal):
    # Detect peaks with refinements
    peaks, _ = find_peaks(signalsample, height=0.5, distance=10, prominence=0.3)  # Adjust these values as needed
    
    # Calculate distances between peaks in milliseconds
    distances = [peak * sampling_interval_ms for peak in np.diff(peaks)]
    PeaktoPeak.append(distances)
    
    # Create a Plotly figure
    fig = go.Figure()

    # Add the signalsample data as a line trace
    fig.add_trace(go.Scatter(x=time_ms, y=signalsample, mode='lines', name=f'Signal {index + 1}'))

    # Add the peaks as markers
    fig.add_trace(go.Scatter(x=[time_ms[p] for p in peaks], y=[signalsample[p] for p in peaks], mode='markers', name='Peaks'))

    # Add annotations to show distances between peaks
    annotations = []
    for i in range(len(peaks) - 1):
        mid_time = (time_ms[peaks[i]] + time_ms[peaks[i+1]]) / 2
        distance = time_ms[peaks[i+1]] - time_ms[peaks[i]]
        annotations.append(
            dict(
                x=mid_time,
                y=signalsample[peaks[i]],
                xref="x",
                yref="y",
                text=f"{distance:.2f} ms",
                showarrow=False,
                arrowhead=4,
                ax=0,
                ay=40
            )
        )
    fig.update_layout(annotations=annotations)

    # Update layout for better visualization
    fig.update_layout(title=f'Plot of Signal {index + 1} with Peaks',
                      xaxis_title='Time (milliseconds)',
                      yaxis_title='Value')
    
    # Show the plot
    fig.show()

