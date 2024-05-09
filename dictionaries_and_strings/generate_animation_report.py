import numpy as np
import matplotlib.pyplot as plt
def temperature(depth, time, parameters):
    # parameters = (initial_temperature, temperature_amplitude, angular_wavenumber, angular_frequency)
    return parameters[0] + parameters[1] * np.exp(-parameters[2]*depth) * np.cos(parameters[3]*time - parameters[2]*depth)
def update_figure(frame):
    global plot_curve, temperatures
    plot_curve.set_ydata(temperatures[frame])
    return plot_curve
def parse_animation_code(code_filename):
    with open(code_filename, 'r') as file:
        code_string = file.read()
    return code_string
def format_section_header(header_string):
    return f'<h1>{header_string}</h1>'
def write_html_report(report_string, report_filename):
    with open(report_filename, 'w') as file:
        file.write(report_string)
# Step 1: Parse the animation code from file
animation_code = parse_animation_code('animate_diurnal_heat_wave.py')
# Step 2: Extract code snippets and format them inside <pre> tags
code_snippets = animation_code.split('\n\n')
preformatted_code_snippets = [f'<pre>{snippet.strip()}</pre>' for snippet in code_snippets]
# Step 3: Create three plots of the function at different time values
plt.figure(figsize=(10, 6))
times = [0, 6, 12]  # Time values for the plots
for idx, time_val in enumerate(times):
    temperatures = temperature(np.linspace(0, 10, 100), time_val, (0, 10, 1, 1))  # Sample parameters for plotting
    plt.plot(np.linspace(0, 10, 100), temperatures, label=f'Time: {time_val}h')
plt.legend()
plt.xlabel('Depth')
plt.ylabel('Temperature')
plt.title('Temperature vs Depth at Different Time Values')
plt.grid(True)
plt.savefig('plot1.png')  # Save the plot to a file for inclusion in the HTML report
# Step 4: Insert the plots into the HTML report
plot1_path = 'plot1.png'  # Replace with the actual path to plot 1
plot1_html = f'<img src="{plot1_path}" alt="Plot 1">'
# Step 5: Add the animated GIF file
animated_gif_path = 'animation.gif'  # Replace with the actual path to the animated GIF
animated_gif_html = f'<img src="{animated_gif_path}" alt="Animation GIF">'
# Step 6: Construct the HTML report
header_one_tag = format_section_header('Animation Code Snippets')
code_snippets_html = '\n'.join(preformatted_code_snippets)
plots_header = format_section_header('Plots')
plots_section_html = plot1_html
animated_gif_header = format_section_header('Animated GIF')
animated_gif_section_html = animated_gif_html
full_report_html = f'''
<!DOCTYPE html>
<html>
<head>
<title>Animation Report</title>
</head>
<body>
{header_one_tag}
{code_snippets_html}
{plots_header}
{plots_section_html}
{animated_gif_header}
{animated_gif_section_html}
</body>
</html>
'''
# Step 7: Write the HTML report to file
write_html_report(full_report_html, 'animation_report.html')