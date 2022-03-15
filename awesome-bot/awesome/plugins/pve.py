from http import server
from nonebot import on_command, CommandSession
import pymysql
import random
from .hurt import h


@on_command('副本系统', aliases='副本', only_to_me=False)
async def _(session: CommandSession):
    userzt = {'生命值': 100, '护甲值': 0, '是否冻结': False, '闪避值': 0, '本回合伤害': 0, '使用技能': '', '是否闪避': False, '逃跑是否成功': False}
    guiwuzt = {'生命值': 100, '护甲值': 0, '是否冻结': False, '闪避值': 15, '本回合伤害': 0, '使用技能': '', '是否闪避': False, '怪物名': ''}
    monster = ['新手村', '逃跑']
    alllist = ''
    qqnum = str(session.ctx['user_id'])
    name = (await session.aget(prompt=f'目前副本有\n'
                                      f'新手村（铲平小怪建议初级进入）\n'
                                      f'直接回复即可')).strip()
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    if str(name) in monster:
        cursor.execute(f'select {name} from 怪物')
        guiwuzt["怪物名"] = random.choice(cursor.fetchall())[0]
        cursor.execute(f'select 闪避率 from user where qq={qqnum}')
        userzt['闪避值'] = int(cursor.fetchone()[0])
        cursor.execute(f'select 技能1,技能2,技能3,技能4 from user where qq={qqnum}')
        for i in cursor.fetchall():
            for x in i:
                alllist = alllist + '\n&' + str(x)
        while True:
            cursor.execute(f'select 1技能1,1技能2,1技能3,1技能3 from 怪物 where {name}="{guiwuzt["怪物名"]}"')
            guiwuzt['使用技能'] = random.choice(cursor.fetchall()[0])
            if userzt['逃跑是否成功']:
                userzt['逃跑是否成功'] = False
                userzt['使用技能'] = (await session.aget(prompt=f'怪物名：{guiwuzt["怪物名"]}\n'
                                                            f'向目标发出技能攻击可使用的技能命令有{alllist}\n'
                                                            f'你刚刚逃跑时被{guiwuzt["怪物名"]}抓住了\n'
                                                            f'怪物施展{guiwuzt["使用技能"]}对你造成了{guiwuzt["本回合伤害"]}点伤害\n'
                                                            f'<怪物护甲值：{guiwuzt["护甲值"]}>\n'
                                                            f'<你的护甲值：{userzt["护甲值"]}>\n'
                                                            f'<怪物血量：{guiwuzt["生命值"]}>\n'
                                                            f'<我的血量：{userzt["生命值"]}>\n'
                                                            f'可用指令<逃跑>')).strip()
            elif userzt['是否闪避']:
                userzt['使用技能'] = (await session.aget(prompt=f'怪物名：{guiwuzt["怪物名"]}\n'
                                                            f'向目标发出技能攻击可使用的技能命令有{alllist}\n'
                                                            f'你刚刚靠灵活的身手闪避了{guiwuzt["怪物名"]}的攻击\n'
                                                            f'并使用了{userzt["使用技能"]}对怪物造成了{userzt["本回合伤害"]}点伤害\n'
                                                            f'<怪物护甲值：{guiwuzt["护甲值"]}>\n'
                                                            f'<你的护甲值：{userzt["护甲值"]}>\n'
                                                            f'<怪物血量：{guiwuzt["生命值"]}>\n'
                                                            f'<我的血量：{userzt["生命值"]}>\n'
                                                            f'可用指令<逃跑>')).strip()
            elif guiwuzt['是否闪避']:
                userzt['使用技能'] = (await session.aget(prompt=f'怪物名：{guiwuzt["怪物名"]}\n'
                                                            f'向目标发出技能攻击可使用的技能命令有{alllist}\n'
                                                            f'{guiwuzt["怪物名"]}闪避了你的攻击\n'
                                                            f'并且对你使出了{guiwuzt["使用技能"]}造成{guiwuzt["本回合伤害"]}点伤害\n'
                                                            f'<怪物护甲值：{guiwuzt["护甲值"]}>\n'
                                                            f'<你的护甲值：{userzt["护甲值"]}>\n'
                                                            f'<怪物血量：{guiwuzt["生命值"]}>\n'
                                                            f'<我的血量：{userzt["生命值"]}>\n'
                                                            f'可用指令<逃跑>')).strip()
            elif guiwuzt['是否冻结']:
                userzt['使用技能'] = (await session.aget(prompt=f'怪物名：{guiwuzt["怪物名"]}\n'
                                                            f'向目标发出技能攻击可使用的技能命令有{alllist}\n'
                                                            f'因使用了霜值新星造成{userzt["本回合伤害"]}点伤害,{guiwuzt["怪物名"]}本回合被冻结\n'
                                                            f'<怪物护甲值：{guiwuzt["护甲值"]}>\n'
                                                            f'<你的护甲值：{userzt["护甲值"]}>\n'
                                                            f'<怪物血量：{guiwuzt["生命值"]}>\n'
                                                            f'<我的血量：{userzt["生命值"]}>\n'
                                                            f'可用指令<逃跑>')).strip()
            elif userzt['是否冻结']:
                userzt['使用技能'] = (await session.aget(prompt=f'怪物名：{guiwuzt["怪物名"]}\n'
                                                            f'向目标发出技能攻击可使用的技能命令有{alllist}\n'
                                                            f'{guiwuzt["怪物名"]}施展霜值新星造成{guiwuzt["本回合伤害"]}点伤害'
                                                            f'你因为被冻结下次回合无法造成有效伤害\n '
                                                            f'<怪物护甲值：{guiwuzt["护甲值"]}>\n'
                                                            f'<你的护甲值：{userzt["护甲值"]}>\n'
                                                            f'<怪物血量：{guiwuzt["生命值"]}>\n'
                                                            f'<我的血量：{userzt["生命值"]}>\n'
                                                            f'可用指令<逃跑>')).strip()
            elif userzt['使用技能'] == '':
                userzt['使用技能'] = (await session.aget(prompt=f'出现了一只{guiwuzt["怪物名"]}\n'
                                                            f'向目标发出技能攻击可使用的技能命令有{alllist}\n'
                                                            f'<怪物护甲值：0>\n'
                                                            f'<你的护甲值：0>\n'
                                                            f'<怪物血量：{guiwuzt["生命值"]}>\n'
                                                            f'<我的血量：{userzt["生命值"]}>\n'
                                                            f'可用指令<逃跑>')).strip()
            else:
                userzt['使用技能'] = (await session.aget(prompt=f'怪物名：{guiwuzt["怪物名"]}\n'
                                                            f'向目标发出技能攻击可使用的技能命令有{alllist}\n'
                                                            f'你使用了{userzt["使用技能"]}对怪物造成了{userzt["本回合伤害"]}点伤害\n'
                                                            f'怪物施展{guiwuzt["使用技能"]}对你造成了{guiwuzt["本回合伤害"]}点伤害\n'
                                                            f'<怪物护甲值：{guiwuzt["护甲值"]}>\n'
                                                            f'<你的护甲值：{userzt["护甲值"]}>\n'
                                                            f'<怪物血量：{guiwuzt["生命值"]}>\n'
                                                            f'<我的血量：{userzt["生命值"]}>\n'
                                                            f'可用指令<逃跑>')).strip()
            if str(userzt['使用技能']) not in alllist and userzt['使用技能'] != '逃跑':
                await session.send('无此技能')
                continue
            elif userzt['使用技能'] == '逃跑':
                taopao = random.randint(0, 2)
                if taopao == 0:
                    await session.send('逃跑成功')
                    break
                else:
                    userzt['逃跑是否成功'] = True
            try:
                h(userzt, guiwuzt, qqnum)
                h(guiwuzt, userzt, 2301865114)
            except:
                await session.send("你还没又武器哦无法造成有效伤害，此回合浪费")
            if guiwuzt["生命值"] <= 0:
                cursor.execute(f'update user set 积分=积分+50 where qq={qqnum}')
                cursor.execute(f'update user set 目前经验=目前经验+50 where qq={qqnum}')
                await session.send(f'成功击败了{guiwuzt["怪物名"]},获得50货币50经验值')
                break
            elif userzt["生命值"] <= 0:
                cursor.execute(f'update user set 积分=积分-20 where qq={qqnum}')
                await session.send('你已阵亡，花费20货币疗伤')
                break
    else:
        await session.send('无此副本')
    db.commit()
    cursor.close()
    db.close()
