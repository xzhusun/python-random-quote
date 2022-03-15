from nonebot import on_command,CommandSession
import pymysql
@on_command('选择职业',only_to_me=False)
async def zh(session:CommandSession):
    qqnum = str(session.ctx['user_id'])
    zhiye = str((await session.aget(prompt='请直接发送你选择的职业：\n战士 魔法师 猎人')).strip())
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    cursor.execute(f'select qq from user')
    allqq=cursor.fetchall()
    if qqnum in str(allqq):
        cursor.execute(f'select 职业 from user where qq={qqnum}')
    else:
        await session.send('请先进行注册')
    dican=cursor.fetchone()
    if dican[0]==None:
        cursor.execute(f'update user set 职业="{zhiye}" where qq={qqnum}')
        cursor.execute(f'update user set 等级="初级" where qq={qqnum}')
        await session.send(f'恭喜你成为一名初级{zhiye}，开始<选择技能>吧')
    else:
        await session.send('你已经有职业了，不可重新选择职业')
    db.commit()
    cursor.close()
    db.close()