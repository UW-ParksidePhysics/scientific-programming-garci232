import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def temperature(depth, time, parameters):
    # parameters = (initial_temperature, temperature_amplitude, angular_wavenumber, angular_frequency)
    return parameters[0] + \
        parameters[1] * np.exp(-parameters[2]*depth) * \
        np.cos(parameters[3]*time - parameters[2]*depth)

def create_plots(times, depths, temperatures):
    fig, axs = plt.subplots(3, figsize=(8, 12))

    for i, t in enumerate([0, len(times)//2, len(times)-1]):
        axs[i].plot(depths, temperatures[t])
        axs[i].set_title(f'Temperature at t = {times[t]:.0f} seconds')
        axs[i].set_xlabel('Depth [m]')
        axs[i].set_ylabel('Temperature [°C]')
        axs[i].grid(True)

    plt.tight_layout()
    plt.savefig('plots.png')

def generate_animation(times, depths, temperatures):
    def update_figure(frame):
        plot_curve.set_ydata(temperatures[frame])
        return plot_curve

    fig, ax = plt.subplots()
    plot_curve, = ax.plot(depths, temperatures[0])

    def init():
        return plot_curve,

    animation_result = animation.FuncAnimation(fig=fig, func=update_figure, 
                                               frames=len(times), init_func=init, 
                                               interval=200, blit=True)

    animation_result.save('animation.gif', writer='pillow')

def parse_animation_code(code_filename):
    with open(code_filename, 'r') as file:
        code = file.read()
    return code

def format_section_header(header_string):
    return f"<h1>{header_string}</h1>\n\n"

def write_html_report(report_string, report_filename):
    with open(report_filename, 'w') as file:
        file.write(report_string)

if __name__ == '__main__':
    code_snippets = parse_animation_code("animate_diurnal_heat_wave.py").split('\n\n')

    report_string = ""
    for snippet in code_snippets:
        report_string += f"{format_section_header('Code Snippet')}\n<pre>\n{snippet}\n</pre>\n"

    report_string += format_section_header('Plots')
    mean_surface_temperature = 10
    temperature_amplitude = 10
    depth_sample_number = 501
    times = np.linspace(0, 24 * 60 * 60 * 50, depth_sample_number)
    depths = np.linspace(0, -np.log(0.002)/np.sqrt(2*np.pi/(24*60*60))/(2*np.pi/(24*60*60)), depth_sample_number)
    temperatures = []
    temperature_parameters = (mean_surface_temperature, temperature_amplitude, 
                              np.sqrt(2*np.pi/(24*60*60)), 2*np.pi/(24*60*60))
    for time in times:
        temperatures.append(temperature(depths, time, temperature_parameters))
    temperatures = np.array(temperatures)

    create_plots(times, depths, temperatures)

    report_string += '<img src="plots.png">\n\n'

    report_string += format_section_header('Animation')
    generate_animation(times, depths, temperatures)
    report_string += '<img src="animation.gif">\n\n'

    write_html_report(report_string, 'animation_report.html')