from nonebot import on_command, CommandSession
import random
import time

@on_command('yx',aliases=('猜拳游戏'))
async def yx(session:CommandSession):
    computer = random.randint(1, 3)
    shuju=(await session.aget(prompt='发送（剪刀，石头，布）'))
    if computer==1:
        if shuju=='剪刀':
            await session.send('平局')
        elif shuju=='石头':
            await session.send('你赢了')
        elif shuju=='布':
            await session.send('你输了')
        time.sleep(1)
        await session.send('电脑出了剪刀')
    elif computer==2:
        if shuju=='剪刀':
            await session.send('你输了')
        elif shuju=='石头':
            await session.send('平局')
        elif shuju == '布':
            await session.send('你赢了')
        time.sleep(1)
        await session.send('电脑出了石头')
    else:
        if shuju=='剪刀':
            await session.send('你赢了')
        elif shuju=='石头':
            await session.send('你输了')
        elif shuju == '布':
            await session.send('平局')
        time.sleep(1)
        await session.send('电脑出了剪刀')
@on_command('猜数字')
async def 猜数字(session:CommandSession):
    computer=random.randint(1,100)
    user=''
    while user != computer:
        user =eval ((await session.aget(prompt='请发送所猜的数值')))
        if type(user)!=int:
            await session.send('必须得是个整数')
        else:
            if user>computer:
                await session.send('猜大了')
            elif user<computer:
                await session.send('猜小了')
        time.sleep(1)
    await session.send('猜对了')