
from nonebot import on_command, CommandSession
import pymysql
import random


@on_command('装备', only_to_me=False)
async def use(session: CommandSession):
    wuqi=str(session.current_arg_text.strip())
    qqnum = str(session.ctx['user_id'])
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    if wuqi in ['匕首','砍刀','单手剑']:
        try:
            cursor.execute(f'DELETE FROM {qqnum}背包 WHERE 物品="{wuqi}"')
            cursor.execute(f"update user set 武器='{wuqi}' where qq={qqnum}")
            await session.send(f'已成功装备上了{wuqi}')
        except:
            await session.send('装备失败，可能你的背包里没有该物品哦！')
    else:
        await session.send('它不是武器哦！')
    db.commit()
    cursor.close()
    db.close()


@on_command('打开青铜宝箱', aliases='使用青铜宝箱', only_to_me=False)
async def bx(session: CommandSession):
    qqnum = str(session.ctx['user_id'])
    k = random.randint(1, 10)
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    cursor.execute(f'select 物品 from 青铜宝箱 where id={k}')
    wp = cursor.fetchone()[0]
    cursor.execute(f"select 物品 from {qqnum}背包")
    beibao=cursor.fetchall()
    if ('青铜宝箱',) in beibao:
        if wp == '80货币':
            cursor.execute(f'update user set 积分=积分+80 where qq={qqnum}')
            cursor.execute(f'delete from {qqnum}背包 where 物品="青铜宝箱"')
            await session.send('恭喜你，获得80货币')
        elif wp == '250货币':
            cursor.execute(f'update user set 积分=积分+250 where qq={qqnum}')
            cursor.execute(f'delete from {qqnum}背包 where 物品="青铜宝箱"')
            await session.send('恭喜你，获得250货币')
        else:
            cursor.execute(f'insert into {qqnum}背包(物品) values("{wp}")')
            cursor.execute(f'delete from {qqnum}背包 where 物品="青铜宝箱"')
            await session.send(f'恭喜你，你获得了{wp}')
    else:
        await session.send('你还没有背包也可能没有青铜宝箱哦！')
    db.commit()
    cursor.close()
    db.close()
