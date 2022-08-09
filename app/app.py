from flask import Flask, render_template, request
from app.api_client import get_astronomy_pic_of_day, get_mars_pic
from datetime import date

app = Flask(__name__)


@app.route('/')
def index():
    # image_json = get_astronomy_pic_of_day()
    # return render_template('index.html', landing_image=image_json["url"], title=image_json["title"], description=image_json["explanation"])
    url = "https://www.youtube.com/embed/rFDjAfwmWKM?rel=0"
    description = "What it would look like to leave planet Earth? Such an event was recorded visually in great detail by the MESSENGER spacecraft as it swung back past the Earth in 2005 on its way in toward the planet Mercury. Earth can be seen rotating in this time-lapse video, as it recedes into the distance. The sunlit half of Earth is so bright that background stars are not visible. The robotic MESSENGER spacecraft is now in orbit around Mercury and has recently concluded the first complete map of the surface. On occasion, MESSENGER has continued to peer back at its home world. MESSENGER is one of the few things created on the Earth that will never return. At the end of its mission MESSENGER crashed into Mercury's surface."
    return render_template('index.html', landing_image=url, title="Leaving Earth", description=description)


@app.route('/mars')
def mars():
    date_today = date.today()
    date_selected = request.args.get(
        'date-selected', date_today)
    data = get_mars_pic(date_selected)["photos"]
    print(data)
    return render_template('mars.html', date_selected=date_selected, date_today=date_today, data=data)
