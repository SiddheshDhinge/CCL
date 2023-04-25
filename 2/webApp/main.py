import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        self.response.out.write(template.render('www/index.html', template_values))

    def post(self):
        region = self.request.get('region')
        area = self.request.get('area')
        url = "http://worldtimeapi.org/api/timezone/"+ region + "/" + area
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        date = data['datetime'][0:10]
        time = data['datetime'][11:19]
        week = data['day_of_week']
        year = data['day_of_year']
        weeknum = data['week_number']
        template_values = {
            "date": date,
            "time": time,
            "week": week,
            "year": year,
            "weeknum": weeknum,
        }

        self.response.out.write(template.render('www/results.html', template_values))


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
app.run()