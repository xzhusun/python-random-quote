from nonebot import on_command, CommandSession
import pymysql


@on_command('选择技能', only_to_me=False)
async def jineng(session: CommandSession):
    all = ''
    qqnum = str(session.ctx['user_id'])
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    cursor.execute(f'select 职业 from user where qq={qqnum}')
    zhiye = str(cursor.fetchone()[0])
    cursor.execute(f'select {zhiye} from 技能 where id<=3')
    for i in cursor.fetchall():
        for x in i:
            all = all + '\n' + str(x)
    jn = (await session.aget(prompt=f'你现在可以选择如下技能{all}\n直接发送技能名即可\n若要查看技能介绍需重新使用命令<技能介绍>\nps：温馨提示只有新用户可选择哦')).strip()
    cursor.execute(f'select 技能1 from user where qq={qqnum}')
    jineng1 = cursor.fetchone()[0]
    if str(jineng1) in str(all):
        await session.send('不可重新选择技能')
    elif jn in all:
        cursor.execute(f'update user set 技能1="{jn}" where qq={qqnum}')
        await session.send(f'你成功学习了{jn}')
    else:
        await session.send('选择失败，无此技能')
    db.commit()
    cursor.close()
    db.close()


@on_command('学习技能',only_to_me=False)
async def xx(session: CommandSession):
    ls=''
    qqnum = str(session.ctx['user_id'])
    jineng = (await session.aget(prompt='你想学习什么技能？（必须得有技能书才能学习）')).strip()
    wz = (await session.aget(prompt='你想把此技能放到那个技能位？')).strip()
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    cursor.execute(f'select 职业 from user where qq={qqnum}')
    zhiye = cursor.fetchone()[0]
    cursor.execute(f"select 物品 from {qqnum}背包")
    beibao=cursor.fetchall()
    if zhiye=='战士':
        ls=['冲击','英勇一击']
    elif zhiye=='魔法师':
        ls=['火球术','霜值新星','魔法屏障']
    elif zhiye=='猎人':
        ls=['迅猛攻击','猴之守护','巨蟒之刺']
    if jineng in ls:
        if (f'{jineng}技能书',)in beibao:
            cursor.execute(f'delete from {qqnum}背包 where 物品="{jineng}技能书"')
            cursor.execute(f'update user set {wz}="{jineng}" where qq={qqnum}')
            await session.send(f'你成功学习了{jineng}')
        else:
            await session.send('学习失败，你可能没有此技能书')
    else:
        await session.send('你该职业不可学习此技能')
    db.commit()
    cursor.close()
    db.close()
