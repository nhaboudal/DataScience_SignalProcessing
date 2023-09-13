# Signal Processing
In this repository I'll provide several code files dedicated to signal processing tasks.


## File 1 : DetectPeaks& Peak Distances ##
This code provides a workflow for importing, normalizing, and visualizing signals from a CSV file. 
It also detects peaks in the signals and calculates the distances between these peaks.

Workflow:
1. Import Signal
Imports the signal data from a CSV file into a list.

3. Normalize Signal
Normalizes the signal data to bring all values between 0 and 1.

5. Visualize Signals
Uses Plotly to visualize the normalized signals over time.

7. Detect Peaks and Peak Distances
Detects peaks in each signal using the find_peaks method from scipy.signal.
Calculates the distances between consecutive peaks.

9. Visualize Peaks and Peak Distances
Visualizes the signals with the detected peaks using Plotly.
Annotates the plot with the distances between consecutive peaks.

Dependencies:

csv: For reading the CSV file.
numpy: For numerical operations.
plotly.graph_objects: For visualization.
scipy.signal: For peak detection.

Usage:

To use this code, ensure you have the required dependencies installed. Adjust the file_path variable to point to your CSV file and then run the script.
