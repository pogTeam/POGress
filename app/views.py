import random
import logging
import datetime
import calendar
from flask_appbuilder.models.datamodel import SQLAModel
from flask_appbuilder.views import ModelView
from flask_appbuilder.charts.views import DirectChartView, DirectByChartView, GroupByChartView
from models import *
from app import appbuilder, db
from flask_appbuilder.models.group import aggregate_count, aggregate_sum, aggregate_avg

log = logging.getLogger(__name__)


def fill_data():
    try:
        p1 = Player(name='valle')
        db.session.add(p1)
        db.session.commit()
    except Exception as e:
        log.error("Update ViewMenu error: {0}".format(str(e)))
        db.session.rollback()

    ctfs = ['AlexCTF', 'Insomni', '3DS']
    for ctf in ctfs:
        c = Ctf(name=ctf)
        try:
            db.session.add(c)
            db.session.commit()
        except Exception as e:
            log.error("Update ViewMenu error: {0}".format(str(e)))
            db.session.rollback()
    try:
        hw = Chall(category='misc', solved_by='valle', points=10, ctf_id=c.id)
        db.session.add(hw)
        db.session.commit()
    except Exception as e:
        log.error("Update ViewMenu error: {0}".format(str(e)))
        db.session.rollback()


class PlayerModelView(ModelView):
    datamodel = SQLAModel(Player)
   
class CtfModelView(ModelView):
    datamodel = SQLAModel(Ctf)

class ChallModelView(ModelView):
    datamodel = SQLAModel(Chall)

def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)

class ChallGroupByChartView(GroupByChartView):
    datamodel = SQLAModel(Chall)
    chart_title = 'Ctfs Data'

    definitions = [
        {
            'group': 'category',
            'series': [(aggregate_sum, 'points')]
        },
        {
            'group': 'solved_by',
            'series': [(aggregate_sum, 'points')]
        },
 
    ]


db.create_all()
#fill_data()
appbuilder.add_view(PlayerModelView, "Manage Players", icon="fa-folder-open-o", category="Statistics")
appbuilder.add_view(CtfModelView, "Manage CTFs", icon="fa-folder-open-o", category="Statistics")
appbuilder.add_view(ChallModelView, "Manage Challs", icon="fa-folder-open-o", category="Statistics")
appbuilder.add_separator("Statistics")
appbuilder.add_view(ChallGroupByChartView, "Challs statistics", icon="fa-dashboard", category="Statistics")
