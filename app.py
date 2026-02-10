# Flask application entry point

from flask import Flask, render_template, request
import logging
from datetime import datetime

# --------------------------------------------------
# App Factory
# --------------------------------------------------
app = Flask(__name__)

# --------------------------------------------------
# Configuration
# --------------------------------------------------
app.config["DEBUG"] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "dev-secret-key"  # replace in production

# --------------------------------------------------
# Logging
# --------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# --------------------------------------------------
# Global Template Variables
# --------------------------------------------------
@app.context_processor
def inject_globals():
    return {
        "site_name": "My Organization",
        "current_year": datetime.now().year
    }

# --------------------------------------------------
# Request Hooks
# --------------------------------------------------
@app.before_request
def log_request_info():
    logging.info(
        f"{request.method} request to {request.path} from {request.remote_addr}"
    )

# --------------------------------------------------
# Routes
# --------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About Us")


@app.route("/events")
def events():
    return render_template("events.html", title="Events")


@app.route("/past-events")
def past_events():
    return render_template("past-events.html", title="Past Events")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html", title="Gallery")


@app.route("/merchandise")
def merchandise():
    return render_template("merchandise.html", title="Merchandise")


@app.route("/donate")
def donate():
    return render_template("donate.html", title="Donate")


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Us")


@app.route("/our-team")
def our_team():
    return render_template("our-team.html", title="Our Team")


@app.route("/our-story")
def our_story():
    return render_template("our-story.html", title="Our Story")


@app.route("/mission-vision")
def mission_vision():
    return render_template("mission-vision.html", title="Mission & Vision")


@app.route("/youth-programs")
def youth_programs():
    return render_template("youth-programs.html", title="Youth Programs")


@app.route("/partnerships")
def partnerships():
    return render_template("partnerships.html", title="Partnerships")

# --------------------------------------------------
# Error Handlers
# --------------------------------------------------
@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        "404.html",
        title="Page Not Found"
    ), 404


@app.errorhandler(500)
def internal_server_error(error):
    logging.error(f"Server Error: {error}")
    return render_template(
        "500.html",
        title="Server Error"
    ), 500

# --------------------------------------------------
# Run App
# --------------------------------------------------
if __name__ == "__main__":
    app.run()
