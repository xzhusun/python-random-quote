import nonebot
import pymysql


@nonebot.scheduler.scheduled_job(
    'cron',
    # year=None,
    # month=None,
    # day=None,
    # week=None,
    # day_of_week="mon,tue,wed,thu,fri",
    hour=0,
    # minute=46,
    # second=None,
    # start_date=None,
    # end_date=None,
    # timezone=None,
)
async def _():
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    cursor.execute('update user set 是否签到="否" ')
    db.commit()
    db.close()
