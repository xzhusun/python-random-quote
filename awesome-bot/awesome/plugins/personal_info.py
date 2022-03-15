from nonebot import on_command, CommandSession
import pymysql


@on_command('状态', only_to_me=False)
async def zt(session: CommandSession):
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    qqnum = str(session.ctx['user_id'])
    cursor.execute(f"select 名称 from user where qq={qqnum}")
    name = cursor.fetchone()[0]
    cursor.execute(f'select 职业 from user where qq={qqnum}')
    zhiye = cursor.fetchone()[0]
    cursor.execute(f'select 技能1 from user where qq={qqnum}')
    skill1 = cursor.fetchone()[0]
    cursor.execute(f'select 技能2 from user where qq={qqnum}')
    skill2 = cursor.fetchone()[0]
    cursor.execute(f'select 技能3 from user where qq={qqnum}')
    skill3 = cursor.fetchone()[0]
    cursor.execute(f'select 技能4 from user where qq={qqnum}')
    skill4 = cursor.fetchone()[0]
    cursor.execute(f'select 武器 from user where qq={qqnum}')
    arms = cursor.fetchone()[0]
    cursor.execute(f'select 等级 from user where qq={qqnum}')
    dengji = cursor.fetchone()[0]
    cursor.execute(f'select 闪避率 from user where qq={qqnum}')
    sb = cursor.fetchone()[0]
    cursor.execute(f"select 目前经验 from user where qq={qqnum}")
    nowjingyan=cursor.fetchone()[0]
    cursor.execute(f"select 上限经验 from user where qq={qqnum}")
    jingyan=cursor.fetchone()[0]
    await session.send(f'To{name}&个人状态\n'
                       f'*职业：{zhiye}\n'
                       f'*等级：{dengji}\n'
                       f'*经验值:{nowjingyan}/{jingyan}\n'
                       f'*闪避率：{sb}%\n'
                       f'*技能1：{skill1}\n'
                       f'*技能2：{skill2}\n'
                       f'*技能3：{skill3}\n'
                       f'*技能4：{skill4}\n'
                       f'*武器：{arms}\n'
                       f'<当前可用指令>\n'
                       f' 背包|钱包|升级')
    db.commit()
    cursor.close()
    db.close()


@on_command("背包", only_to_me=False)
async def bb(session: CommandSession):
    bb = ''
    qqnum = str(session.ctx['user_id'])
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    try:
        cursor.execute(f"select 物品 from {qqnum}背包")
    except:
        await session.send('你还没有背包')
    baba = cursor.fetchall()
    for i in baba:
        for x in i:
            bb = bb + '|' + str(x)
    await session.send(f'你背包有如下物品\n{bb}\n可用命令<装备 武器名><学习技能><打开xxx宝箱>')


@on_command('钱包', aliases='余额', only_to_me=False)
async def money(session: CommandSession):
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    qqnum = str(session.ctx['user_id'])
    cursor.execute(f'select 积分 from user where qq={qqnum}')
    zhi = cursor.fetchone()
    await session.send(f'你现有货币为{zhi[0]}')
    db.commit()
    cursor.close()
    db.close()

@on_command('升级',only_to_me=False)
async def dj(session:CommandSession):
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    qqnum = str(session.ctx['user_id'])
    cursor.execute(f'select 目前经验 from user where qq={qqnum}')
    nowjy=cursor.fetchone()[0]
    cursor.execute(f'select 上限经验 from user where qq={qqnum}')
    jy=cursor.fetchone()[0]
    if int(nowjy)>=int(jy):
        cursor.execute(f'update user set 等级="中级" where qq={qqnum}')
        await session.send('恭喜你成功进阶到中级')
    else:
        await session.send('升级失败经验值不足')
    db.commit()
    cursor.close()
    db.close()