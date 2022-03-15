import pymysql
from nonebot import on_command, CommandSession


@on_command('注册', only_to_me=False)
async def useradd(session: CommandSession):
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    qqnum = str(session.ctx['user_id'])
    cursor.execute('select qq from user')
    all = cursor.fetchall()
    if (str(qqnum),) in all:
        await session.send('你已经注册过了，不能重新注册')
    else:
        name = session.current_arg_text.strip()
        if not name:
            await session.send('用户名不能为空\n'
                               '注册格式<注册 名称>')
        else:
            cursor.execute(f'insert into user(qq,名称) values({qqnum},"{name}")')
            db.commit()
            cursor.close()
            db.close()
            await session.send('注册成功\n'
                            '开始进行选择职业吧\n'
                            '可用指令<选择职业>')
