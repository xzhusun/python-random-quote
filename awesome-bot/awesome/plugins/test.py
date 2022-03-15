from nonebot import on_command, CommandSession


@on_command('保存')
async def get(session: CommandSession):
    baocun = await session.aget(prompt='想保存啥')
    session.state['bc'] = baocun
    await session.send(session.state['bc'])


@on_command('取出')
async def qu(session: CommandSession):
    await session.send(session.state['bc'])
