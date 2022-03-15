import pymysql
from nonebot import on_command, CommandSession

@on_command('签到',only_to_me=False)
async def sgin_in(session:CommandSession):
    qqnum = str(session.ctx['user_id'])
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    cursor.execute('select qq from user')
    all = cursor.fetchall()
    if (str(qqnum),) not in all:
        await session.send('你还未注册，请先进行注册！')
    else:
        cursor.execute(f'select 是否签到 from user where qq={qqnum}')
        sgin=cursor.fetchall()
        if ('是',) in sgin:
            await session.send('你今日已经签到了！')
        else:
            cursor.execute(f'update user set 积分=积分+100 where qq={qqnum}')
            cursor.execute(f'update user set 是否签到="是" where qq={qqnum}')
            await session.send('恭喜你！\n签到成功获得100货币')
    db.commit()
    cursor.close()
    db.close()