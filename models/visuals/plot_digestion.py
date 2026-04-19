import matplotlib.pyplot as plt
from models.digestion_curve import digestion_curve
from data.beverages import beverages

def plot_curve(name):
    curve = digestion_curve(beverages[name])

    time = [c["time"] for c in curve]
    iron = [c["iron"] for c in curve]

    plt.plot(time, iron)
    plt.title(f"Iron Absorption Over Time: {name}")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Absorbed Iron")
    plt.show()


plot_curve("milk_drink")
plot_curve("oat_pomegranate_drink")
