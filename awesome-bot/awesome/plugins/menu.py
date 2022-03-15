from nonebot import on_command, CommandSession
import pymysql


@on_command('菜单', aliases='帮助', only_to_me=False)
async def get_menulist(session: CommandSession):
    qqnum = str(session.ctx['user_id'])
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    cursor.execute(f'select 名称 from user where qq={qqnum}')
    name = cursor.fetchone()[0]
    await session.send(f'To-{name}\n'
                       f'——注册|签到——\n'
                       f'技能系统|个人信息\n'
                       f'副本系统|商城系统\n'
                       f'猜拳游戏|猜数字')
    cursor.close()
    db.close()


@on_command('个人信息', only_to_me=False)
async def xx(session: CommandSession):
    qqnum = str(session.ctx['user_id'])
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    cursor.execute(f'select 名称 from user where qq={qqnum}')
    name = cursor.fetchone()[0]
    await session.send(f'-^{name}^-\n&.钱包\n&.背包\n&.状态')
    cursor.close()
    db.close()


@on_command('技能系统', only_to_me=False)
async def jn_(session: CommandSession):
    await session.send('选择技能\n技能介绍\n学习技能')


@on_command('技能介绍', only_to_me=False)
async def js_(session: CommandSession):
    all = ''
    zyjn = (await session.aget(prompt='你想查看那个职业技能?\n战士\n魔法师\n猎人\n直接发送上述名词即可')).strip()
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    cursor.execute(f'select {zyjn} from 技能')
    for i in cursor.fetchall():
        for x in i:
            all = all + '\n' + str(x)
    jnname = (await session.aget(prompt=f'你想查看那个什么技能?{all}\n直接发送技能名即可')).strip()
    cursor.execute(f'select {zyjn}技能介绍 from 技能 where {zyjn}="{jnname}"')
    js = str(cursor.fetchone()[0])
    await session.send(js)
    db.commit()
    cursor.close()
    db.close()


@on_command('商城系统', only_to_me=False)
async def sd(session: CommandSession):
    qqnum = str(session.ctx['user_id'])
    bb = ''
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    cursor.execute('select 商品 from 商店')
    for i in cursor.fetchall():
        for x in i:
            cursor.execute(f'select 价格 from 商店 where 商品="{str(x)}"')
            d = str(cursor.fetchone()[0])
            bb = bb + '\n' + str(x) + ' ' + d
    wp = (await session.aget(prompt=f'商品 价格{bb}\n发送商品名查商品介绍\n购买商品命令<购买商品名>')).strip()
    if str(wp) in str(bb):
        cursor.execute(f'select 介绍 from 商店 where 商品="{wp}"')
        js = cursor.fetchone()[0]
        await session.send(str(js))
    else:
        wp = str(wp)[2:]
        cursor.execute(f'select 积分 from user where qq={qqnum}')
        mongy = cursor.fetchone()[0]
        cursor.execute(f'select 价格 from 商店 where 商品="{wp}"')
        jg = cursor.fetchone()[0]
        if int(mongy) >= int(jg):
            try:
                cursor.execute(f'update user set 积分=积分-{jg} where qq={qqnum}')
                if wp == '背包':
                    cursor.execute(f'create table {qqnum}背包 (物品 varchar(255))')
                    await session.send('购买成功,已经自动帮你开启了背包功能')
                else:
                    try:
                        cursor.execute(f'insert into {qqnum}背包(物品) values("{wp}")')
                        await session.send('购买成功，已经帮你放入仓库了')
                    except:
                        await session.send('你还没有背包存入物品无法购买，货币不退还')
            except:
                await session.send('购买失败，命令有误')
        else:
            await session.send('你的余额不足，无法购买')
    db.commit()
    cursor.close()
    db.close()
