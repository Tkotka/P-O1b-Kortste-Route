import csv
import matplotlib.pyplot as plt
import os

def process_and_visualize_csv(file_path, columns_to_plot):
    # Initialize lists to store data
    x_values = []
    y_values = []

    # Define a color map for consistent colors
    color_map = {
        1: 'blue',
        2: 'green',
        3: 'red',
        4: 'purple',
        5: 'orange'
    }

    # Read the CSV file
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # First value is the x coordinate
            x = float(row[0])
            # Remaining values are y coordinates
            y = [float(row[i]) for i in columns_to_plot]  # Adjust index for 1-based to 0-based

            x_values.append(x)
            y_values.append(y)

    # Transpose y_values to get separate lists for each function
    y_values_transposed = list(map(list, zip(*y_values)))

    # Plot the data
    plt.figure(figsize=(18, 6), dpi=600)  # Increase figure size and resolution
    for i, y in enumerate(y_values_transposed):
        plt.plot(x_values[:], y[:], color=color_map[columns_to_plot[i]])

    plt.xlabel('Metingnummer')
    plt.ylabel('LDR-waarde')
    # plt.title('CSV Data Visualization')

    # Set the legend with correct labels
    labels = ["linksvoor", "rechtsvoor", "achter", "delta", "average"]
    plt.legend([labels[i-1] for i in columns_to_plot])

    # Save the figure as an EPS file with the same name as the input file
    eps_file_path = os.path.splitext(file_path)[0] + '.eps'
    plt.savefig(eps_file_path, format='eps')

    # Save the figure as an PNG file with the same name as the input file
    png_file_path = os.path.splitext(file_path)[0] + '.png'
    plt.savefig(png_file_path, format='png',dpi=600)

# Example usage
file_path = '20250121-160454_voorbeeld.csv'
columns_to_plot = [1,2,3,4,5]  # Specify the column numbers to plot (1-based index)
process_and_visualize_csv(file_path, columns_to_plot)
