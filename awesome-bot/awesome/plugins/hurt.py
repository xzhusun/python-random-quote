from http.cookiejar import FileCookieJar
import random
from matplotlib.pyplot import ginput
import pymysql


def h(gjzt, beigjzt, qqunm):
    if gjzt['是否冻结']:
        pass
    else:
        gjzt['本回合伤害'] = 0
        beigjzt['是否冻结'] = False
        db = pymysql.connect(host='114.132.234.220',
                             user='rpg',
                             password='123456',
                             db='rpg')
        cursor = db.cursor()
        cursor.execute(f'select 武器 from user where qq={qqunm}')
        wuqi = cursor.fetchone()[0]
        if gjzt['使用技能'] == '冲击':
            shanghai = random.randint(8, 25)
            gjzt['本回合伤害'] = shanghai
            if beigjzt['护甲值'] > shanghai:
                beigjzt['护甲值'] = beigjzt['护甲值'] - shanghai
            else:
                shanghai = shanghai - beigjzt['护甲值']
                beigjzt['生命值'] = beigjzt['生命值'] - shanghai
                beigjzt['护甲值'] = 0
            return gjzt, beigjzt
        elif gjzt['使用技能'] == '英勇一击':
            shanghai = random.randint(1, 50)
            gjzt['本回合伤害'] = shanghai
            if beigjzt['护甲值'] > shanghai:
                beigjzt['护甲值'] = beigjzt['护甲值'] - shanghai
            else:
                shanghai = shanghai - beigjzt['护甲值']
                beigjzt['生命值'] = beigjzt['生命值'] - shanghai
                beigjzt['护甲值'] = 0
            return gjzt, beigjzt
        elif gjzt['使用技能'] == '火球术':
            shanghai = random.randint(19, 22)
            gjzt['本回合伤害'] = shanghai
            if beigjzt['护甲值'] > shanghai:
                beigjzt['护甲值'] = beigjzt['护甲值'] - shanghai
            else:
                shanghai = shanghai - beigjzt['护甲值']
                beigjzt['生命值'] = beigjzt['生命值'] - shanghai
                beigjzt['护甲值'] = 0
            return gjzt, beigjzt
        elif gjzt['使用技能'] == '霜值新星':
            shanghai = random.randint(10, 19)
            gjzt['本回合伤害'] = shanghai
            if beigjzt['护甲值'] > shanghai:
                beigjzt['护甲值'] = beigjzt['护甲值'] - shanghai
            else:
                shanghai = shanghai - beigjzt['护甲值']
                beigjzt['生命值'] = beigjzt['生命值'] - shanghai
                beigjzt['护甲值'] = 0
            if random.randint(0, 1):
                beigjzt['是否冻结'] = True
            else:
                beigjzt['是否冻结'] = False
            return gjzt, beigjzt
        elif gjzt['使用技能'] == '魔法屏障':
            gjzt['护甲值'] = gjzt['护甲值'] + 40
            return gjzt, beigjzt
        elif gjzt['使用技能'] == '迅猛攻击':
            if wuqi is None:
                return
            else:
                shanghai = random.randint(10, 30)
                gjzt['本回合伤害'] = shanghai
                if beigjzt['护甲值'] > shanghai:
                    beigjzt['护甲值'] = beigjzt['护甲值'] - shanghai
                else:
                    shanghai = shanghai - beigjzt['护甲值']
                    beigjzt['生命值'] = beigjzt['生命值'] - shanghai
                    beigjzt['护甲值'] = 0
            return gjzt, beigjzt
        elif gjzt['使用技能'] == '猴之守护':
            gjzt['闪避值'] = gjzt['闪避值'] + 8
            return gjzt, beigjzt
        elif gjzt['使用技能'] == '巨蟒之刺':
            gjzt['本回合伤害'] = 15
            beigjzt['护甲值'] = beigjzt['护甲值'] * 0.5
            if beigjzt['护甲值'] > 15:
                beigjzt['护甲值'] = beigjzt['护甲值'] - 15
            else:
                shanghai = 15 - beigjzt['护甲值']
                beigjzt['生命值'] = beigjzt['生命值'] - shanghai
                beigjzt['护甲值'] = 0
            return gjzt, beigjzt
        cursor.close()
        db.close()
