import aiocqhttp
import pymysql
from nonebot import message_preprocessor, NoneBot
from nonebot.plugin import PluginManager
import zipfile
import os
import requests

group = [547507321,746339543]
comdand = ['背包', '钱包', '副本系统', '商城系统', '状态', '菜单', '副本']

#打包目录为zip文件（未压缩）
def make_zip(source_dir, output_filename):
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, _, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)     #相对路径
            zipf.write(pathfile, arcname)
    zipf.close()
def ifuserqq(qqnum):
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    cursor.execute('select qq from user')
    all = cursor.fetchall()
    db.commit()
    cursor.close()
    db.close()
    if (str(qqnum),) in all:
        return True
    else:
        return False


@message_preprocessor
async def _(bot: NoneBot, event: aiocqhttp.Event, plugin_manager: PluginManager):
    qq = event['user_id']
    db = pymysql.connect(host='114.132.234.220',
                         user='rpg',
                         password='123456',
                         db='rpg')
    cursor = db.cursor()
    cursor.execute(f'select 姓名 from 21计算机2班 where qq={qq}')
    name = cursor.fetchone()[0]
    if event['sub_type'] == 'friend' or event['group_id'] == 704983319:
        if event["message"][0]['type'] == 'image':
            wenzi = (await bot.ocr_image(image=event.message[0]['data']['file']))["texts"]
            x=''
            for i in wenzi:
                x=x+' '+i['text']
            if name in x:
                cursor.execute(f'update 21计算机2班 set 是否已交="是" where qq={qq}')
                r=requests.get(event.message[0]['data']['url'])
                with open("/home/images/"+name+".png",'wb') as f:
                    f.write(r.content)
                await bot.send(event=event,message='你成功提交截图，为计算机2班完成了给小忙，比心比心')
                cursor.execute('select qq,是否已交 from 21计算机2班')
                roomclass = cursor.fetchall()
                if ("否",) not in roomclass:
                    make_zip("/home/images","/home/images.zip")
            else:
                await bot.send(event=event, message='你的截图里没有打上班级姓名，请打好了再来上传')
    if event['sub_type'] == 'friend' or event['group_id'] in group:
        if ifuserqq(event['user_id']) or '注册' in event['raw_message']:
            pass
        elif event['raw_message'] in comdand:
            await bot.send(event=event, message='你还没有注册哦，请先注册一下')
            plugin_manager.switch_plugin("awesome.plugins.jineng", 'awesome.plugins.menu', "awesome.plugins.modular",
                                         'awesome.plugins.personal_info', 'awesome.plugins.pve',
                                         'awesome.plugins.sign_in',
                                         'awesome.plugins.zhiye', 'awesome.plugins.usewp',
                                         state=False)
    db.commit()
    cursor.close()
    db.close()