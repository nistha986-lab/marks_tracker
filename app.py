from flask import Flask, render_template, request
import matplotlib

# Prevent GUI errors
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Create static folder if it doesn't exist
os.makedirs("static", exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():

    graph = False

    if request.method == "POST":

        try:
            year1 = int(request.form["year1"])
            year2 = int(request.form["year2"])
            year3 = int(request.form["year3"])
            year4 = int(request.form["year4"])

            marks = [year1, year2, year3, year4]

            years = [
                "Year 1",
                "Year 2",
                "Year 3",
                "Year 4"
            ]

            plt.figure(figsize=(10, 6))

            plt.plot(
                years,
                marks,
                marker="o",
                linewidth=4,
                color="purple",
                markersize=10
            )

            plt.fill_between(
                years,
                marks,
                color="violet",
                alpha=0.3
            )

            # Add mark values on graph
            for x, y in zip(years, marks):
                plt.text(
                    x,
                    y + 1,
                    str(y),
                    fontsize=11,
                    fontweight="bold"
                )

            plt.title(
                "Student Performance Analysis",
                fontsize=18,
                color="darkblue",
                fontweight="bold"
            )

            plt.xlabel(
                "Academic Years",
                fontsize=12
            )

            plt.ylabel(
                "Marks",
                fontsize=12
            )

            plt.grid(
                linestyle="--",
                alpha=0.5
            )

            plt.tight_layout()

            graph_path = os.path.join(
                "static",
                "marks_graph.png"
            )

            plt.savefig(graph_path)
            plt.close()

            graph = True

        except ValueError:
            graph = False

    return render_template(
        "index.html",
        graph=graph
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )