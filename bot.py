import telebot
import time
import os
from telebot import types
from telebot import util
import re

import random

bot_token = '1950492866:AAHoMApimzGSG3XOOCaTFfRhj7EUTzcSqpo'
#https://api.telegram.org/bot1950492866:AAHoMApimzGSG3XOOCaTFfRhj7EUTzcSqpo/getMe
#https://api.telegram.org/bot1950492866:AAHoMApimzGSG3XOOCaTFfRhj7EUTzcSqpo/setWebhook

bot = telebot.TeleBot(token=bot_token)


img = 'https://files.fm/thumb_show.php?i=4jahcz2te' 


def find_at(msg):
  for text in msg:
      if '@' in text:
        return text


chat_id_admin = '-1001540881364' #admin 
chat_id_test = '-1001514164491' #test
chatid = '-1001204245522' #"commu"
list_test = [-1001514164491, -1001540881364]  # int here
listofids = [-1001204245522, -1001514164491]  # int here

# GROUP_CHAT_ID = int(os.environ["-1001514164491"])

def is_api_group(chat_id):
    return chat_id == ''

mrten = 'https://i.imgur.com/FsHc8a0.jpg'
hold_ten = 'https://i.imgur.com/2pol3If.jpg'
roadmap = 'https://i.imgur.com/PwIgfG3.jpg'
founders = 'https://i.imgur.com/cesQlYQ.jpg'
intro = 'https://i.imgur.com/zAKBxfK.jpg'
yieldex_img = 'https://i.imgur.com/QI7iyHN.png'

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#   bot.reply_to(message, 'Welcome! Tenizen')

@bot.message_handler(commands=['teninfo'])
def send_welcome(message):
  bot.send_animation(chatid, 'https://media.giphy.com/media/Js7cqIkpxFy0bILFFA/giphy.gif?cid=ecf05e47g885s8iw1nxa6vh56b8d0wa8zbu6rcziqp9hkog7&rid=giphy.gif&ct=g', disable_notification=True,)
  bot.send_message(chatid, 
  'ข้อมูลเบื้องต้นเกี่ยวกับ TEN Finance\n'
  '/intro = แนะนำตัว TEN Finance\n'
  '/address = Contract address\n'
  '/links = รวมลิ้งต่างๆของ TENFI\n'
  '/roadmap = แผนโปรเจคในอนาคต\n'
  '/tokenomics = แผนธุรกิจของเรา\n'
  '/security = ความปลอดภัยของเรา\n'
  '/price = เช็คราคา\n'
  '/chart = กราฟราคา TENFI\n'
  '/yieldex = Yieldex คืออะไร?\n'
  '/tenlots = Tenlots คืออะไร?\n'
  '/mrten = mr.ten คือใคร?\n'
  '/dev = ทีมงานของ TEN\n' 
  '/founders = ผู้ก่อตั้ง TENFI\n'
  '/moon = wen lambo\n'
  '/hold = ถือไปทำไม\n'
  '/skynet = certik skynet\n'
  '/tracker = ติดตามพอร์ทที่มี TENFI ได้ที่นี่\n'
  '/flashloan = ป้องกันการ flashloan อย่างไร\n'
  '/gas , /highgas = วิธีแก้ไขถ้าพบค่าแก๊สผิดปกติ\n'
  '/tenzap = บริการฝาก LP ง่ายๆ\n'
  '/lp = liquidity provider\n'
  '/fee = ค่าบริการ/ค่าธรรมเนียม\n'
  '/autocompound = ระบบการทบต้น\n'
  '/dust = เศษค้างของเงินฝาก\n'
  '/mvb = โปรเจคที่ TENFI แข่งขันใน BSC')
  # '/กาว = เชิญ Dino มาปล่อยกาว\n'

# textDino = 'เชิญ Dino มาปล่อยกาวครับ @MrDinoWolfofDefi'
# @bot.message_handler(commands=['กาว'])
# def send_welcome(message):
#   # bot.reply_to(message, 'เชิญ Dino มาปล่อยกาวครับ @MrDinoWolfofDefi')
#   bot.send_animation(chatid, 'https://media.giphy.com/media/RnzbAaJIoWm755DKJx/giphy.gif?cid=790b7611f29f921e9870bf065bf333dbe686f45d203a4631&rid=giphy.gif&ct=g', caption=textDino,)

# @bot.message_handler(commands=['กาว'])
# def send_welcome(message):
#   bot.reply_to(message, 'เชิญ Dino มาปล่อยกาวครับ @MrDinoWolfofDefi')

@bot.message_handler(commands=['peko'])
def send_welcome(message):
  bot.reply_to(message, ' อัญเชิญ Admin FB ปากดีย์ ปล่อยความจัญไร @PekoPekool')

@bot.message_handler(commands=['address'])
def send_welcome(message):
  bot.reply_to(message, '0xd15C444F1199Ae72795eba15E8C1db44E47abF62')

@bot.message_handler(commands=['ca'])
def send_welcome(message):
  bot.reply_to(message, '0xd15C444F1199Ae72795eba15E8C1db44E47abF62')

@bot.message_handler(commands=['warn'])
def send_welcome(message):
  # bot.reply_to(message, 'กรุณาระวังคำพูด @MrDinoWolfofDefi')
  bot.send_message(chatid,'กรุณาระวังคำพูด @MrDinoWolfofDefi', reply_to_message_id=message.reply_to_message.id)

@bot.message_handler(commands=['ban'])
def send_welcome(message):
  # bot.reply_to(message, 'อีกทีจะโดนแล้วนะ @MrDinoWolfofDefi')
  bot.send_message(chatid,'อีกทีจะโดนแล้วนะ @MrDinoWolfofDefi', reply_to_message_id=message.reply_to_message.id)

@bot.message_handler(commands=['report'])
def send_welcome(message):
  # bot.reply_to(message, 'อย่าหาทำ @MrDinoWolfofDefi')
  bot.send_message(chatid,'อย่าหาทำ @MrDinoWolfofDefi', reply_to_message_id=message.reply_to_message.id)

# @bot.message_handler(commands=['test'])
# def send_welcome(message):
#   bot.send_message(chat_id_test,'อย่าหาทำ @MrDinoWolfofDefi', reply_to_message_id=message.reply_to_message.id)

# @bot.message_handler(commands=['tracker'])
# def send_welcome(message):
#   bot.reply_to(message, 'สามารถดูมูลค่าสินทรัพย์ที่ฝากใน TEN ได้จากหลากหลายช่องทาง ดังนี้\n'
#   '- https://apeboard.finance/\n'
#   '- https://pacoca.io/\n'
#   '- https://scv.finance/\n'
#   '- https://tin.network/\n'
#   '- https://v2.loremboard.finance/general/dashboard\n'
#   '- https://www.jdiyield.com/')

@bot.message_handler(commands=['tracker'])
def send_welcome(message):
  text = 'สามารถดูมูลค่าสินทรัพย์ที่ฝากใน TEN ได้จากหลากหลายช่องทาง ดังนี้\n- https://debank.com/\n- https://apeboard.finance/\n- https://pacoca.io/\n- https://scv.finance/\n- https://tin.network/\n- https://v2.loremboard.finance/general/dashboard\n- https://www.jdiyield.com/'
  bot.send_message(chatid, text=text, disable_web_page_preview=True)

@bot.message_handler(commands=['chart'])
def send_welcome(message):
  bot.reply_to(message, 'สามารถดูกราฟ TENFI ได้จากลิงค์นี้เลยครับ\n'
  'poocoin\n'
  'https://poocoin.app/tokens/0xd15c444f1199ae72795eba15e8c1db44e47abf62\n\n'

  'dexguru\n'
  'https://dex.guru/token/0xd15c444f1199ae72795eba15e8c1db44e47abf62-bsc')

@bot.message_handler(commands=['gas'])
def send_welcome(message):
  bot.reply_to(message, 'ถ้าพบปัญหาแก๊สแพงกว่าปกติ ลองลบทศนิยมของยอดที่จะฝากลงสักหนึ่งหลัก  ตัวอย่างเช่น 99.1234 เหลือ 99.123 แล้วค่อยทำรายการใหม่นะ')

@bot.message_handler(commands=['highgas'])
def send_welcome(message):
  bot.reply_to(message, 'ถ้าพบปัญหาแก๊สแพงกว่าปกติ ลองลบทศนิยมของยอดที่จะฝากลงสักหนึ่งหลัก  ตัวอย่างเช่น 99.1234 เหลือ 99.123 แล้วค่อยทำรายการใหม่นะ')

@bot.message_handler(commands=['yieldex'])
def send_message(message):
  for recipient_id in listofids:
    bot.send_photo(recipient_id, yieldex_img, 'Yieldex คืออะไร?\n1.Yieldex คือการผูก LP โดยจำเป็นต้องมี Tenfi อยู่ในนั้น เป็นกุญแจเปิด Pool\n2.ผลตอบแทนดีกว่า Farm ในขณะที่ APY ผันผวนน้อย ไม่แกว่งเหมือนในฟาร์ม\n3.เลือกความเสี่ยงได้เหมือนกองทุน\n -เสี่ยงมาก ผันผวนสูง( ใช้ Tenfi เยอะ)\n -เสี่ยงกลาง ผันผวนปกติ (ใช้ Tenfi กลาง)\n -เสี่ยงต่ำ stable (ใช้ Tenfi น้อย)\n4.ทุก Yieldex Pool จำเป็นใช้ Tenfi ในการฟาร์ม\n5.ได้เงินต่อที่ 2 จากการถือ Tenfi (ถือเฉยๆ, ฝาก stake เดี่ยว และ ฝากคู่ LP ได้ทั้งหมด) ในรูปแบบของ BUSD เกิดจาก Deposit Fee ของ Yieldex เรียกว่ายิ่งมีคนฝากเยอะ ส่วนแบ่งเป็น เงิน BUSD หรือเงินสดก็ได้เยอะตามอัตราส่วนการถือ Tenfi' '\n\n' 'สรุปคือเกิดแรงซื้อ Tenfi เพื่อฟาร์มที่มีประสิทธิภาพสูงใน Yieldex และมีเงินไว้ใช้ในขณะที่ไม่ต้องขาย Tenfi หรือถอนฟาร์ม. ทำให้ไม่เกิด Sell pressure ด้วยการหมุนเวียนของระบบฟาร์ม มั่นใจว่าจะทำให้เหรียญราคาโดดขึ้นแน่นอน')

@bot.message_handler(commands=['dev'])
def send_welcome(message):
  bot.reply_to(message, 'ทีมงานของ TEN FINANCE เป็นทีมที่เรียกว่า "ไร้พรมแดน" เพราะผู้ก่อตั้ง3ท่านอยู่ประเทศนึง ส่วนทีมพัฒนานั้นรวมหัวกระทิจากหลายมุมโลก มี Dev มือฉกาจที่เคยร่วมพัฒนา BANCOR จนเป็นโปรเจคท็อปร้อยมาแล้วหลายท่านถามว่าเปิดหน้าไหม คำตอบคือไม่ และทาง Mr. TEN ผู้ก่อตั้งหลัก จะพูดเสมอว่าอยากให้เชื่อในตัวโค้ด และ Audit ทั้งหมด ไม่ต้องเชื่อในตัวเค้า เค้าไม่เปิดหน้าเพราะต้องการความเป็นส่วนตัวเท่านั้น แต่การทำ Audit กับทุกที่ต้องผ่านกระบวนการ KYC หรือการยืนยันตัวตน เพราะฉนั้นการที่โปรเจค TEN ผ่าน Audit ทั้ง Certik และเร็วๆนี้ Peckshield ก็เป็นบทพิสูจน์แล้วว่าโปรเจ็คเชื่อถือได้ สามารถดูรีพอร์ทของ Certik เพิ่มเติมได้ที่นี่ https://www.certik.org/projects/tenfinance')

@bot.message_handler(commands=['fee'])
def send_welcome(message):
  bot.send_photo(chatid, 'https://i.imgur.com/oayycxH.jpg', 'การหัก Fee ของ TEN มี 2 ประเภท\n\n'

'1) Fee ที่หักจากเงินต้นที่ฝาก [Deposit]\n'
'เมื่อฝากจะโดนหัก Deposit fee จากเงินต้น = 0.1%\n\n'
'2) Fee ที่หักจาก Reward\n\n'
'- Gas Fee = 0.3%\n'
'- Network Fee = 0.5%\n'
'- Burn Fee\n'
'   สำหรับ Pool ที่ไม่มี TENFI = 3.0%\n'
'   สำหรับ Pool ที่มี TENFI = 1.5%\n'
'ดังนั้น Fee ที่ถูกหักจาก Reward เท่ากับ\n'
'- Pool ที่มี TENFI หัก..\n'
'   0.3%+ 0.5%+ 1.5%= 2.3%\n'
'- Pool อื่นๆ ที่ไม่มี TENFI หัก..\n'
'   0.3%+ 0.5%+ 3.0%= 3.8%\n\n'
'(❗️Tips: ตัวเลขผลตอบแทน (APR/APY) ที่ปรากฎในแพลตฟอร์มมีการหักค่าดำเนินการทั้งหมดแล้ว คุณสามารถเคลมได้ครบตามจำนวน APR ที่ปรากฎไว้)\n\n'
'⚠️ ตอนถอนเงินต้น [Withdraw] ไม่เสีย Fee')

tenzap_vdo = 'https://vod-progressive.akamaized.net/exp=1629659867~acl=%2Fvimeo-prod-skyfire-std-us%2F01%2F3131%2F23%2F590657310%2F2784890505.mp4~hmac=c887abeb04a60191135a5bf564c0c72d633ec9ee57049406e51ea492508facf0/vimeo-prod-skyfire-std-us/01/3131/23/590657310/2784890505.mp4'

@bot.message_handler(commands=['tenzap'])
def send_welcome(message):
  bot.send_video(chatid, tenzap_vdo, caption='TenZap เป็นบริการช่วยสร้าง LP ด้วยการใช้ BNB หรือ BUSD โดยระบบ TenZap จะทำการแบ่งครึ่ง แลกเป็น 2 เหรียญหลังจากนั้นจะผูก LP ให้อัตโนมัติ สะดวกมากๆเลยครับ ส่วนถ้าใครมีเหรียญอยู่แล้วอยากผูกเอง สามารถผูกได้ที่ PancakeSwap ได้เลย')

lpText = 'LP พูลทุกคู่ ของ TEN จะสามารถผูก และ แตก LP ได้ที่ PancakeSwap จ้า เข้าไปที่เมนู Trade > Liquidity ได้เลยหรือกดตามลิ้งนี้\n\nADD พูล TENFI+BNB: https://pancakeswap.finance/add/BNB/0xd15C444F1199Ae72795eba15E8C1db44E47abF62\nADD พูล TENFI+BUSD: https://pancakeswap.finance/add/0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56/0xd15C444F1199Ae72795eba15E8C1db44E47abF62\n\nแตก พูล TENFI+BNB: https://pancakeswap.finance/remove/0xd15C444F1199Ae72795eba15E8C1db44E47abF62/BNB\nแตก พูล TENFI+BUSD: https://pancakeswap.finance/remove/0xd15C444F1199Ae72795eba15E8C1db44E47abF62/0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56\n\nTENFI มี function TENZap ให้คุณสามารถผูก LP ได้ง่ายๆ ที่เดียวจบ แต่มันจะเป็นการใช้เหรียญที่คุณเลือกในการแปลง เช่นถ้าเรามี BUSD 100 มันจะเอาไปซื้อ TENFI 50 แล้วผูก BUSD 50 + TENFI 50 ให้เอง แต่ถ้าใครมีเหรียญอยู่แล้ว ก็ทำที่ Pancakeswap ได้เลย อ่านเพิ่มเติมได้ที่ /tenzap'

@bot.message_handler(commands=['lp'])
def send_welcome(message):
  bot.send_message(chatid, text=lpText, disable_web_page_preview=True)

@bot.message_handler(commands=['skynet'])
def send_welcome(message):
  bot.reply_to(message, 'คำถาม - ทำไมคะแนน Safety Assessment ของ Skynet Certik ได้น้อยจังครับ\n'
  'คำตอบ - ถ้าลองดูในหมวด safety นะครับ จะเห็นว่าคะแนนนั้นถูกคำนวณมาจากหลายๆองค์ประกอบ 4 ใน 5 ข้อที่เห็นว่าเป็นสีแดงนั้น จะเห็นว่าเป็นหัวข้อที่ไม่ได้เกี่ยวกับความปลอดภัยของ source code ของระบบ TENFI ตรงๆ เช่น\n'
  '1.หัวข้อ open source\n'
  'โค้ดของ TENFI เปิดเป็นสาธารณะอยู่แล้ว ซึ่งทุกคนสามารถเข้าไปอ่านได้ใน bscscan.com หรือแม้แต่ถ้าคุณอยาก คัดลอกโค้ดเรา (fork)ไปทำโปรเจคอื่นก็สามารถทำได้\n\n'
  '2.หัวข้อ established reputation\n'
  'หัวข้อนี้เป็นเรื่องเกี่ยวกับ ชื่อเสียง คะแนนจะเพิ่มขึ้นคงต้องใช้เวลา\n\n'
  '3.หัวข้อ major exchange listings\n'
  'หัวข้อนี้ถูกตั้งขึ้นมาตั้งแต่ก่อนที่ defi จะฮิตแบบในปัจจุบัน และผมคิดว่าข้อนี้น่าจะเปลี่ยนเป็น list DEX แทน CEX ในอนาคต\n\n'
  '4.หัวข้อ Accessible identities\n'
  'ในตอนนี้เราก็แค่ไม่ได้เป็นที่รู้จักในวงกว้าง\n\n'
  '5.the source code quality\n'
  'หัวข้อนี้ทางเราไม่มั่นใจว่าทางผู้ตรวจสอบต้องการแบบไหนแต่มั่นใจได้ว่าทางเราได้ทดสอบระบบของเราเรียบร้อยแล้ว บางทีอาจจะต้องมีให้มีการทดสอบให้ผู้ตรวจสอบดูอีกที\n'
  'https://www.certik.org/projects/tenfinance' )

@bot.message_handler(commands=['autocompound'])
def send_welcome(message):
  bot.reply_to(message, 
  'ทุก pool มี Auto-compound ซึ่งจะทบต้นให้วันละครั้ง เวลา 9:30 UTC หรือ 16:30 น. ตามเวลาเมืองไทย \n\n'
  '** ยกเว้นพูลที่มี TENFI ทั้ง 3 pool ได้แก่\n'
  'TENFI\n'
  'TENFI-BUSD\n'
  'TENFI-WBNB\n'
  'จะไม่มี Auto-compound\n\n'
  'Reward จะแบ่งออกเป็น 2 ส่วน\n'
  'โดยรายละเอียดของแต่ละพูล ให้กดดูตรงปุ่ม "Manage"\n\n'
  'Reward จาก APY = Auto-compound จะได้รับ "คู่เหรียญ LP" ที่เราฝากไว้ จะทบต้นให้เราเองทุกๆวัน ไม่ต้องทำอะไรเพิ่มเติม\n'
  'Reward จาก APR = ได้รับ "TENFI" ซึ่งต้องกด Claim เอง')

intro_vdo = 'https://vod-progressive.akamaized.net/exp=1630703338~acl=%2Fvimeo-prod-skyfire-std-us%2F01%2F4482%2F23%2F597410088%2F2810271332.mp4~hmac=5767d91c8f81a218a0f65a9dd7367e5b418685c26ce649fe8dfc097b8f187fa9/vimeo-prod-skyfire-std-us/01/4482/23/597410088/2810271332.mp4'

@bot.message_handler(commands=['intro'])
def send_welcome(message):
  # for recipient_id in listofids:
  # bot.send_video(chat_id_test, intro_vdo, caption='tenst')
  bot.send_photo(chatid, intro, 'TEN ย่อมาจาก Token Enrichment Network เป็น yield optimizer หมายความว่า TEN ไม่ใช่เวปฟาร์ม แต่ TEN  ทำหน้าที่ เอาสินทรัพย์เราไปฟาร์มที่อื่นให้ โดยตอนนี้มี pancake , belt และ ape และอื่นๆในอนาคต หลังจากนั้นระบบจะทำการเก็บผลผลิตที่ได้ มาทบต้นให้ (auto compound) และได้ TENFI เป็นรางวัลเสริม. เป้าหมายระยะยาวของเทนคือการให้นักลงทุนหน้าใหม่ที่ไม่ได้อยู่ในโลกของ DeFi มาลงทุนได้โดยเน้นความปลอดภัย และความง่าย ผ่านทางระบบ TENZap และ YieldEx. สโลแกนของ TEN คือ "TENFI ทำ DeFi ให้เป็นเรื่องง่าย"')

@bot.message_handler(commands=['dust'])
def send_welcome(message):
  bot.reply_to(message, 'ใครที่เคยลง: คู่ แล้วถอนย้ายไปเดี่ยว หรือใครที่ลงเดี่ยวแล้วย้ายไปคู่ หรือย้ายจากพูลนึง stable นึงไปอีกตัวนึง หรือจะถอดLP เพราะเหตุผลอะไรก็ตาม และคิดว่าดึงออกมาหมดแล้วเพราะตอนถอนกด MAX จริงๆแล้วมันจะเหลือเศษ หรือที่เราเรียกกันว่า "dust" อยู่ ทำให้กด claim all ไม่ได้ เพราะมันจะไปเคลม pool ที่เหลือเศษด้วย ทำให้เสียค่าแก๊สฟรีนะครับ อีกอย่างหลายคนคงชอบให้มันขึ้น APR เฉลี่ยที่ถูกต้อง เพราะถ้ามี "dust" อยู่ใน pool ที่เราไม่ใช้แล้ว มันจะเอามาคำนวน "Your Average APY" ให้มันดูแปลกๆไปด้วย วันนี้เลยลองทำตามที่คุณ @MickyToMoon บอกมา คือการใช้ Emergency Withdrawal ใครอ่านอังกฤษได้ตามลิ้งนี้เลยครับ https://tenfinance.gitbook.io/faq/getting-started/emergency-withdrawal ส่วนใครที่อ่านไม่ได้ ทำตามนี้ครับ\n'
  '1. ไปที่ลิ้งนี้ https://bscscan.com/address/0x264A1b3F6db28De4D3dD4eD23Ab31A468B0C1A96#writeContract\n'
  '2. เลื่อนลงมาจะเจอคำว่า Connect to Web3 \n'
  '3. มันจะให้ต่อ metamask\n'
  '4. เลื่อนลงมาข้อที่ 3 Emergency Withdraw\n'
  '5. พิมเลขของพูลที่จะถอน ตามนี้\n'
  'Farm/Pool ID (PID) | TEN Finance\n'
  '0 - ADA/WBNB (Pancakeswap)\n'
  '1 - BTCB/WBNB (Pancakeswap)\n'
  '2 - WBNB/BUSD (Pancakeswap)\n'
  '3 - CAKE/WBNB (Pancakeswap)\n'
  '4 - DAI/BUSD (Pancakeswap)\n'
  '5 - DOT/WBNB (Pancakeswap)\n'
  '6 - ETH/WBNB (Pancakeswap)\n'
  '7 - WBNB/LINK (Pancakeswap)\n'
  '8 - WBNB/UNI (Pancakeswap)\n'
  '9 - USDC/BUSD (Pancakeswap)\n'
  '10 - USDT/BUSD (Pancakeswap)\n'
  '11 - USDT/WBNB (Pancakeswap)\n'
  '12 - VAI/BUSD (Pancakeswap)\n'
  '13 - XRP/WBNB (Pancakeswap)\n'
  '14 - TENFI (Pancakeswap)\n'
  '15 - TENFI/WBNB (Pancakeswap)\n'
  '16 - TENFI/BUSD (Pancakeswap)\n'
  '18 - ALPHA/WBNB (Pancakeswap)\n'
  '19 - BTCB/BUSD (Pancakeswap)\n'
  '20 - TWT/WBNB (Pancakeswap)\n'
  '23 - CAKE (Pancakeswap)\n'
  '24 - ETH/BTCB (Pancakeswap)\n'
  '25 - ETH/USDC (Pancakeswap)\n'
  '26 - TUSD/BUSD (Pancakeswap)\n'
  '27 - beltBTC (Belt)\n'
  '28 - beltBNB (Belt)\n'
  '29 - beltETH (Belt)\n'
  '30 - 4Belt (Belt)\n'
  '31 - TRX/BUSD (Pancakeswap)\n'
  '32 - SKILL/WBNB (Pancakeswap)\n' 
  '33 - AXS/WBNB (Pancakeswap)\n'    
  '34 - UST/BUSD (Pancakeswap)\n'        
  '35 - POTS/BUSD (Pancakeswap)\n'
  '36 - C98/WBNB (Pancakeswap)\n'
  '37 - USDC/USDT (Pancakeswap)\n'
  '38 - BANANA  (Apeswap)\n'
  '39 - DAI/BUSD (Apeswap) \n'
  '40 - USDC/BUSD (Apeswap)\n'
  '41 - USDT/BUSD (Apeswap)\n'
  '42 - WBNB/BUSD (Apeswap)\n'
  '43 - BANANA/BUSD (Apeswap)\n'
  '44 - BANANA/WBNB (Apeswap)\n'
  '45 - WBNB/UNI (Biswap)\n'
  '46 - ADA/WBNB (Biswap)\n'
  '47 - DOT/WBNB (Biswap)\n'
  '48 - WBNB/LINK (Biswap)\n'
  '49 - BSW/WBNB (Biswap)\n'
  '50 - ETH/USDT (Biswap)\n'
  '51 - USDT/BTCB (Biswap)\n'
  '52 - BTCB/WBNB (Biswap)\n'
  '53 - WBNB/BUSD (Biswap)\n'
  '54 - UST/BUSD (Biswap)\n'
  '55 - USDT/WBNB (Biswap)\n'
  '56 - ETH/WBNB (Biswap)\n'
  '57 - USDT/USDC (Biswap)\n'
  '58 - BSW (Biswap)\n'
  '59 - ETH/BTCB (Biswap)\n'
  '60 - USDT/BUSD (Biswap)\n'
  '61 - TENFI/WBNB (Biswap)')

@bot.message_handler(commands=['security'])
def send_welcome(message):
  bot.reply_to(message, 'ความปลอดภัย หลายท่านถามถึงความปลอดภัย ทางทีม TEN เรียกได้ว่าเอาความปลอดภัยเป็นรากฐานของโปรเจ็คเลยก็เป็นได้ เพราะทางทีมผู้ก่อตั้งรู้ดีว่า การจะดึงนักลงทุนใหม่ๆ ที่อาจยังไม่เคยเข้าถึงโลกของ DeFi มาก่อนเลย จะให้เค้ามาลงทุนในโปรเจ็ค DeFi ว่ายากแล้ว จะให้ลงทุนใน TEN ที่เป็นโปรเจ็คหน้าใหม่นั้นมีความจำเป็นต้องให้ผู้คนเชื่อมั่นในระบบได้อย่างไร้ข้อกังขา เพราะฉะนั้นทางโปรเจ็คจึง\n'
  '1. ลงทุนควักเนื้อทำ Audit เสร็จก่อนเปิดตัวโปรเจ็ค ถือได้ว่าเป็นโปรเจ็คแรกๆที่มีการ Audit จาก CertiK ตั้งแต่วันแรกที่เปิด ไม่ใช่เปิดแล้วหาตังไปออดิทแบบที่โปรเจคอื่นๆนิยมทำ\n'
  '2. TEN เป็น1ในไม่กี่โปรเจ็คที่ลงทุนจ่ายค่าบริการ Skynet กับ CertiK เพื่อคอยตรวจสอบ 24 ชั่วโมงถึงความน่าเชื่อถือและความเสี่ยงต่างๆของโปรเจ็ค อ่านเพิ่มได้ที่ /skynet\n'
  '3. นอกจากนั้น TEN ยังซื้อประกัน "CertiK Shield" ที่จะช่วยในกรณีที่ถูกแฮค ทางทีมบริหารจะมีเงินประกันคืนมาให้เพื่อเอามาชดเชยความเสียหายได้ อ่านเพิ่มเติมได้ที่ https://shield.certik.org/shield-pool-stats\n'
  '4. CertiK จัดอันดับให้เท็นติดท็อป 10 ของโปรเจ็คที่ปลอดภัยที่สุดบน Binance Smart Chain ทั้งๆที่เป็นโปรเจ็คเล็กๆ ลองดูโปรเจ็คที่อยู่สูงกว่าเท็น ส่วนใหญ่เป็นโปรเจ็คยักษ์ใหญ่ตัวท็อปเท่านั้น https://www.certik.org/boards/bsc\n'
  '5. ตัวโค้ดของ YieldEx ได้รับการตรวจสอบจาก Peckshield ที่ถือว่าเป็นทีม audit อันดับ 1 ของโลก DeFi\n'
  '6. หลายคนเอาความปลอดภัยไปผูกกับคำว่าเปิดหน้าไหม ตอบตรงนี้เลยว่าไม่เปิดหน้า และทาง Mr. TEN ผู้ก่อตั้งหลัก จะพูดเสมอว่าอยากให้เชื่อในตัวโค้ด และ Audit ทั้งหมด ไม่ต้องเชื่อในตัวเค้า ไม่ต้องสนใจว่าเค้าเป็นใคร เค้าไม่เปิดหน้าเพราะต้องการความเป็นส่วนตัวเท่านั้น แต่การทำ Audit กับทุกที่ต้องผ่านกระบวนการ KYC หรือการยืนยันตัวตน เพราะฉนั้นการที่โปรเจค TEN ผ่าน Audit ทั้ง Certik และ Peckshield ก็เป็นบทพิสูจน์แล้วว่าโปรเจ็คเชื่อถือได้ 100%\n'
  '7. ตัวโปรเจ็คมี timelock 72 ชั่วโมง')


@bot.message_handler(commands=['flashloan'])
def send_welcome(message):
  bot.reply_to(message, 'ทำไม TENFI ถึงแทบไม่มีโอกาสโดน Flash Loan?\n'
  '1. การ mint เหรียญ TEN ไม่ได้มีความเกี่ยวข้องอะไรเลยกับราคาบนกระดาน ทำให้ปริมาณเหรียญไม่กระทบกับราคา\n'
  '2. Deposit fee คือสิ่งที่เป็นนิรภัยชั้นที่ 2 ของ TENFI ซึ่งมีหน้าที่ในการป้องกันคนที่จะพยายามจะมากู้ยืมเงินไปทำ flash loan ผ่านระบบเบื้องหลังใน smart contract ทำให้เมื่อเกิด transaction ผิดปกติขึ้น ระบบจะไม่อนุญาตแม้จะตั้ง slippage และ gas fee ไว้สูงสุด (แฮกเกอร์จะชอบตั้งให้สูงเพื่อให้ transaction ผ่านเร็วๆ) ดังนั้นหาก hacker ผ่านด่านแรกมาได้ ก็จะมาเจอด่านที่สองซึ่งปัดตก transaction ได้ทันที\n'
  '3. เงินทุนไม่ได้มีการเก็บไว้ในตัว contract แต่ LP ก็ยังมีการรันต่างๆ ได้ตามปกติ ดังนั้นจึงเป็นไม่ได้ที่จะเกิดการ flash loan เหมือนกรณี pancakebunny')

@bot.message_handler(commands=['tokenomics'])
def send_welcome(message):
   bot.reply_to(message, '💎 ระบบเศรษฐศาสตร์โทเคนของ TEN (TEN Tokenomics)💎\n\n'

  'ชื่อโทเคน : TENFI\n'
  'ปริมาณทั้งหมดในระบบ : 256,000,000\n'
  'ปริมาณที่ปล่อยก่อนเริ่มระบบ : ไม่มี\n'
  'ปริมาณเหรียญที่ปล่อย ณ เริ่มระบบ : 5,120,000 (2% ของทั้งหมด)\n'
  'TENFI ซื้อได้ในช่องทาง TEN Website และ Pancakeswap\n'
  'อัตราการปล่อยโทเคน : 4.44 ต่อ block หรือ 128,000 TENFI ต่อวัน\n\n'

  '🔥  รายละเอียดค่าธรรมเนียม :\n\n'

  'Fee: จะถูกจัดเก็บเฉพาะส่วนของกำไรเท่านั้น :\n'
  'ส่วนที่ถูกนำไปเบิร์น: 1.50% (TENFI pools) และ 3.00% (Non-TENFI pools)\n'
  'ค่าบริการเครือข่าย: 0.5%\n'
  'ค่าแก๊ส: 0.3% \n\n'

  'ส่วนของภาษี ที่จัดเก็บในทุกๆยอดการฝาก  :\n'
  'ค่าธรรมเนียมการฝาก : 0.10%\n\n'

  '🔥 สรุปค่าธรรมเนียมทั้งหมด : 2.3% - 3.8% บนผลกำไร + 0.10% ของทุกๆยอดฝาก\n'
  '📔 สำหรับรายละเอียดเพิ่มเติม โปรดอ่านเอกสารทางการของเราบน https://tenfinance.gitbook.io/faq'),
    


@bot.message_handler(commands=['roadmap'])
def send_welcome(message):
   bot.reply_to(message, 'TEN มีอะไรมาใหม่บ้างในช่วงนี้? 🗺\n'
  'จากที่ทุกๆได้อ่านแผนการพัฒนาโครงการใน medium (https://medium.com/tenfinance/ten-x-future-f0d44048f1a). มีหลากหลายสิ่งที่ได้พัฒนาและเกิดขึ้นแล้ว และเรามาอัพเดตว่ามีอะไรที่เกิดขึ้นและกำลังจะมาในเร็วๆนี้กันบ้างครับ :\n\n'

  '📅 Q3 2021 - เร็วๆนี้\n'
  'ยิลด์เด็กซ์อยู่ในช่วงเตรียมการขั้นสุดท้าย ตรวจทานด้วยทีมภายในและทดสอบระบบให้ดำเนินการอย่างราบรื่น และหาจุดบกพร่องต่างๆ\n'
  'ส่งตรวจความเรียบร้อยและความปลอดภัยของโค้ดยิลเด็กซ์กับบริษัทตรวจโค้ดระดับต้นๆของโลกอย่าง Peckshield\n'
  'เปิดให้บริการยิลด์เด็กซ์บน binance smart chain\n'
  'เปิดตัว LP4LP ซึ่งให้บริการฝาก LP หนึ่ง ให้ผลตอบแทนอีก LP หนึ่ง\n'
  'วิจัยการฟาร์มข้าม chain\n'
  'ติดต่อค้นหาพันธมิตรใน CEX อันดับต้นๆของโลก 10 อันดับ\n'
  'เพิ่ม vaults ใหม่ๆ ที่ได้รับความนิยม\n\n'

  '📆 Q4 2021 - ในอนาคต\n'
  'ต่อยอดการวิจัยการฟาร์มข้าม chain และสร้างระบบขึ้นมาด้วยการฟาร์มโดย TENFI\n'
  'TENSwap และ AMM DEX ของเราเอง\n'
  'เริ่มสร้างแนวคิดและแผนการทำ TENSure ประกันบนโลก DeFi ของเราเอง\n'
  'เริ่มสร้างแนวคิดและแผนการทำ TENLend แพลทฟอร์มให้บริการกู้ยืม\n'
  'แผนการลิสต์บน CEX อันดับต้นๆของโลก เช่น binance เป็นต้น\n'
  'ชาร์ทให้ข้อมูลประสิทธิภาพของผลตอบแทนในการลงทุน\n'
  'โปรแกรมทางเลือกในการปรับสมดุลของเงินฝาก (rebalance stake option)\n'
  'เพิ่ม LP ใหม่ๆสำหรับคู่ TENFI'),

  
    
@bot.message_handler(commands=['mvb'])
def send_welcome(message):
   bot.reply_to(message, 'MVB จะแบ่งออกเป็นสองขั้นตอนที่ออกแบบมาเพื่อค้นหาโครงการที่ดีที่สุด 10 โครงการจากหมวดหมู่ต่างๆ ซึ่งมีผู้สมัคร/โครงการมากกว่า 500 รายทั่วโลก โดยหลังจากผ่านระยะที่หนึ่ง ก็มีโครงการ 20 อันดับแรก ที่ได้ผ่านไปสู่ระยะที่สอง\n'
  'และหลังจากผ่านไป 3 เดือนก็ได้มาสู่โครงการที่ชนะ 10 โครงการสุดท้าย  ซึ่งนอกจากจะต้องเป็นไปตามเกณฑ์ของ Binance แล้ว โครงการต่างๆ ยังได้รับการทดสอบโดยตลาดที่มีความผันผวนสูง ซึ่งเพิ่มความซับซ้อนให้กับการแข่งขันนี้\n'
  'ทุกโครงการที่ชนะจะได้รับ : \n'
  '1. เงินช่วยเหลือ10,000 ดอลลาร์\n'
  '2.ได้ตรวจสอบความปลอดภัย QuickScan จาก Certik\n'
  '3.สนับสนุนการตรวจสอบความปลอดภัยเต็มรูปแบบ\n'
  '4.การประชุมเชิงปฏิบัติการพิเศษกับผู้เชี่ยวชาญในอุตสาหกรรม\n'
  '5.รวมถึงทุกโครงการมีโอกาสในการลงทุนโดยตรงที่อาจเกิดขึ้นจาก Binance.com รวมถึงได้ลิสต์ใน Binance'),

@bot.message_handler(commands=['mrten'])
def send_message(message):
  for recipient_id in listofids:
    bot.send_photo(recipient_id, mrten, 'Mr.TEN เคยเป็นผู้บริหารกองทุนเฮดจ์ฟันในบริษัทที่เขาก่อตั้งขึ้นมาปี ค.ศ. 2009 โดยจุดเริ่มต้นอาชีพนี้ เริ่มเมื่อ ค.ศ. 2001 จากการทำงานเป็นนักวิเคราะห์ในบริษัทของครอบครัว\n' 'ตลอดในช่วงระยะเวลาการทำงานของเขาในบริษัท เขาได้รับรางวัลจากหลายๆอุตสาหกรรม ซึ่งเขาได้มีส่วนร่วมในการอภิปรายทั้งในการประชุมในสมาคมต่างๆ รวมถึงงานเขียนและยังตีพิมพ์วารสารออกมามากมายอีกด้วย\n' 'ผลงานการบริหารกองทุนให้กับลูกค้าสถาบันนั้น ได้รับชื่อเสียงในมิติของการการควบคุมความเสี่ยงอย่างเชี่ยวชาญและมีผลตอบแทนจากการลงทุนที่โดดเด่น')



@bot.message_handler(commands=['founders'])
def send_welcome(message):
  for recipient_id in listofids:
    bot.send_photo(recipient_id, founders, '')
    bot.send_message(recipient_id, 
  '👔 Mr. TEN\n'
  'ผู้บริหารกองทุนเฮดจ์ฟันที่ได้รางวัลมามากมาย\n'
  'สร้างความสำเร็จโดยพาบริษัทของเขา ได้รางวัลในหลายอุตสาหกรรม\n'
  'ผู้อภิปรายในงานประชุมในหลายอุตสาหกรรม\n'
  'ประสบการณ์บริหารกองทุนมากกว่า 15 ปีในกลุ่มนักลงทุนสถาบัน\n'
  'บริการกองทุนให้กับลูกค้ายักษ์ใหญ่มาหลายสถาบัน\n\n'

  '👔 Mr. A\n'
  'ผู้เรียนรู้ด้านเทคโนโลยี ที่มีวิสัยทัศน์กว้างไกล\n'
  'ผู้ร่วมก่อตั้ง โปกเกอร์ออนไลน์ อันดับแรกๆของโลก\n'
  'ได้กรุยทางเข้าไปในโลกของเทคโนโลยีการยืนยันอายุตั้งแต่สมัยแรกๆ\n'
  'ทำงานเกี่ยวกับซอฟท์แวร์ตรวจการขนส่งสินค้าและโปรแกรมบริหารโลจิสติก\n'
  'สุดท้าย เขาเป็นตำนานนักดนตรีในถิ่นของเขา ซึ่งเป็นที่รักของทุกๆคน\n\n'

  '👔 Mr. D\n'
  'นักเทรดรุ่นเก๋าที่มีผลงานที่พิสูจน์แล้วว่าสามารถพิชิตตลาดได้ทุกรูปแบบ\n'
  'ก่อตั้งบริษัทโบร๊กเก้อเป็นของตัวเอง บริษัทเขาเป็นที่ปรึกษาการเทรด Forex, หุ้น และ คอมโมดิตี้อื่นๆ (เช่น ทอง) ออนไลน์\n'
  'เป็นแฟนตัวยงของ Fintech และคอยลงทุนให้บริษัท Fintech ใหม่ๆอยู่เสมอ\n'
  'ประสบการณ์ที่ยาวนานของเขาในบริษัทการเงินช่วยกำหนดทิศทางและความเชื่อของเขาในโลกของ DeFi ว่ามันคืออนาคตของการเงิน\n'
  )

sticker_alert = 'CAACAgUAAxkBAAJDZ2ErjjG6RL7w57RL45oYdwxZ8l6PAAI2BAACsNOZVmdETVBQekPKIAQ'

@bot.message_handler(commands=['ดึงสติ'])
def send_welcome(message):
  bot.send_sticker(chatid, sticker_alert)
  bot.send_message(chatid, 'สวัสดีงับ ชาว TENizens ..จาร์วิสเอง\n\n'
  'ตอนนี้ TENFI กำลังมาแรง\n'
  'จะมีทั้งคนที่เข้ามาลงทุนระยะยาว\n'
  'คนที่เข้ามาฟาร์ม stable\n'
  'วาฬที่มาเล่นรอบ\n'
  'และคนที่เข้ามาเพราะตามกระแสหรือ FOMO \n'
  'อยากเตือนให้เพื่อนๆทำความเข้าใจกับตัวโปรเจคก่อนลงทุน การลงทุนมีความเสี่ยง โปรดศึกษาโปรเจคก่อนการลุงทุน\n\n'
  'หากใครมีข้อสงสัยเรื่องโปรเจค โปรดพิมพ์ /teninfo แล้วศึกษาได้เลย\n\n'
  'ด้วยความห่วงใยจากจาวิส')

@bot.message_handler(commands=['hold'])
def send_welcome(message):
  for recipient_id in listofids:
    bot.send_photo(recipient_id, hold_ten, '')
    bot.send_message(recipient_id, 
  'TENFI เคยคิดกันไหมว่ามีเหตุผลอะไรในการถือเหรียญ Gov ตัวนี้? \n\n'
  'เหตุผลดีๆว่าทำไม การถือ TENFI จะได้ประโยชน์มหาศาลในระยะยาว มีดังนี้:\n\n'
  '1. TEN มุ่งมั่นที่จะสร้าง usecase / utility ให้กับเหรียญ ไม่เหมือนเหรียญอื่นๆ ที่ถือไว้เพื่อขายเพียงอย่างเดียว โดยทางทีมงานเตรียมสร้างผลตอบแทนให้กับนักลงทุน โดยอาศัยการใช้งานจริงๆของเหรียญ TENFI ผ่าน YIELDEX อ่านเพิ่มได้ที่ /yieldex\n'
  '2. ผู้นำร่องแพลตฟอร์ม ที่ผลักดันความปลอดภัยเป็นอันดับหนึ่งใน BSC เพราะ TEN มีทั้งการตรวจโค้ดทั้งในและบริษัทนอกอย่างcertik รวมถึงเปิดระบบตรวจตรา 24 ชั่วโมง Skynet และซื้อประกัน CertiK Shield สำหรับชดเชยความเสียหายอีกด้วย\n'
  '3. ผู้ร่วมก่อตั้งทั้งสามท่านที่ประสบการณ์ทางการเงินอย่างมากมายและเข้มข้น รวมถึงเชี่ยวชาญด้านเทคโนโลยีทางการเงิน และการพัฒนาระบบซอฟท์แวร์ ทำให้ TEN ถูกควบคุมโดยมืออาชีพอย่างแน่นอน อ่านเพิ่มได้ใน /founders\n'
  '4. TEN ยังมี market cap ที่ยังเล็กอยู่ และมีศักยภาพในการเติบโตมหาศาลจนคาดไม่ถึง ตามศักยภาพของทีมพัฟฒนาที่พร้อมจะผลักดันออกมา\n'
  '5. Mr.TEN ผู้ร่วมก่อตั้งที่ แอคทีฟ ขั้นสุด ไม่ว่านักลงทุนจะมีปัญหา คำถาม ข้อเสนอแนะ ข้อติ คำชม รวมถึงเรื่องพูดคุยต่างๆ ก็พร้อมที่จะมาตอบและพูดคุยกับนักลงทุนตลอด เกือบจะ 24 ชั่วโมงเลยทีเดียว แพลตฟอร์มอื่นคุณเคยคุยกับผู้ก่อตั้งเขาไหม?\n'
  '6. TEN ถูกจัดลำดับความปลอดภัยใน CertiK ให้ติด top 10 ของ BSC \n'
  '7. TENFI เป็นหนึ่งในเงินฝากลงทุน ที่มีค่าธรรมเนียมการฝากต่ำที่สุดใน BSC (ค่าธรรมเนียมฝากไม่เกิน 0.1% เมื่อฝาก และไม่มีค่าธรรมเนียมถอน)\n'
  '8. TENFI ลงสมัคร MVBIII ลองคิดเอาเองนะครับว่าถ้าชนะจะเกิดอะไรขึ้น\n'
  )


sticker_moon = 'CAACAgUAAxkBAAJDXWEg-lqPP9ywhbw6oxmIExjx70wAA-cCAAJNOulUQQABqlPay9ucIAQ'
@bot.message_handler(commands=['moon'])
def send_welcome(message):
  # for recipient_id in listofids:
  #   bot.send_sticker(recipient_id, sticker_moon)
  #   bot.send_message(recipient_id, 'พระจันทร์ก็แค่ทางผ่าน')
  bot.send_animation(chatid, 'https://media.giphy.com/media/VeEdSh0sSEC2y7DD4a/giphy.gif')
  time.sleep(1)
  bot.send_message(chatid, '5')
  time.sleep(1)
  bot.send_message(chatid, '4')
  time.sleep(1)
  bot.send_message(chatid, '3')
  time.sleep(1)
  bot.send_message(chatid, '2')
  time.sleep(1)
  bot.send_message(chatid, '1')
  time.sleep(1)
  bot.send_animation(chatid, 'https://media.giphy.com/media/91A470o8aV55EdvHGl/giphy.gif')


sticker_saturn = 'CAACAgUAAxkBAAJDXmEhWgYxNn1kT3O4l9NGCnfp2TCZAAKPAgACB93pVN9Z0DVv3d5dIAQ'
@bot.message_handler(commands=['saturn'])
def send_welcome(message):
  for recipient_id in listofids:
    bot.send_sticker(recipient_id, sticker_saturn)
    bot.send_message(recipient_id, 'จะไปทำไมพระจันทร์ถ้าปลายทางเราคือดาวเสาร์')

wellcome_gif = ['https://media.giphy.com/media/FQyQEYd0KlYQ/giphy.gif',
  'https://media.giphy.com/media/l4JyOCNEfXvVYEqB2/giphy.gif?cid=790b761160ebca57830d633ac703d01604d28286d56419bb&rid=giphy.gif&ct=g',
  'https://media.giphy.com/media/7dWhY1FK7CFTDdpSMB/giphy.gif?cid=ecf05e47wucbceq7h23hwj8cldsrfhrq90ymz88oh33ckzqi&rid=giphy.gif&ct=g',
  'https://media.giphy.com/media/fVP2MhefOGXhf82V8V/giphy.gif?cid=ecf05e47r4lc10gyt25vzbdrurt2qvhsh0xf3rc2clf5rfmv&rid=giphy.gif&ct=g',
  'https://media.giphy.com/media/26xBxLkLj3sHcwdNe/giphy.gif?cid=ecf05e47ahp21z76bh5221z3edkttx8nwbvkjapxepaof02x&rid=giphy.gif&ct=g',]

# @bot.message_handler(commands=['links'])
# def send_welcome(message):
#   bot.send_animation(chat_id_test, (random.choice(wellcome_gif)))

@bot.message_handler(commands=['links'])
def test_send_message_with_inlinemarkup(self):
  text = 'ยินดีต้อนรับเข้าสู่ TEN FINANCE! 💎\nTENFI ทำให้ Defi เป็นเรื่องง่าย 🔥\nศึกษาข้อมูลของ TEN FINANCE ได้จากการพิมพ์ 👉 /teninfo'
  keyboard = [[types.InlineKeyboardButton("🌐 Website", url='https://ten.finance/'),
            types.InlineKeyboardButton("🥞 PancakeSwap", url='https://exchange.pancakeswap.finance/#/swap?outputCurrency=0xd15c444f1199ae72795eba15e8c1db44e47abf62')],
          [types.InlineKeyboardButton("📖 Medium", url='https://tenfinance.medium.com/'),
            types.InlineKeyboardButton("📚 Documents", url='https://tenfinance.gitbook.io/faq/')],
          [types.InlineKeyboardButton("📢 Ann.Chn.", url='https://t.me/tenfinance_ann'),
            types.InlineKeyboardButton("💰 Price.Chn.", url='https://t.me/BinanceRocketTENFI')],
          [types.InlineKeyboardButton("🌳 Linktr.ee", url='https://linktr.ee/tenfi'),
            types.InlineKeyboardButton("🗺 Roadmap", url='https://medium.com/tenfinance/ten-x-future-f0d44048f1a')],
            [types.InlineKeyboardButton("💬 TENFI Official", url='https://t.me/tenfinance')],
          [types.InlineKeyboardButton("🛡 CERTIK (Audits + Skynet + Shield)", url='https://www.certik.org/projects/tenfinance')]]
  markup = types.InlineKeyboardMarkup(keyboard)
  ret_msg = bot.send_animation(chatid, 'https://media.giphy.com/media/Js7cqIkpxFy0bILFFA/giphy.gif?cid=ecf05e47g885s8iw1nxa6vh56b8d0wa8zbu6rcziqp9hkog7&rid=giphy.gif&ct=g', disable_notification=True, reply_markup=markup)
  assert ret_msg.message_id 


  # '/กาว = เชิญ Dino มาปล่อยกาว\n'
  # ret_msg = bot.send_animation(chatid, 'https://media.giphy.com/media/Js7cqIkpxFy0bILFFA/giphy.gif?cid=ecf05e47g885s8iw1nxa6vh56b8d0wa8zbu6rcziqp9hkog7&rid=giphy.gif&ct=g', caption=text, disable_notification=True, reply_markup=markup)
 
  # ret_msg = bot.send_animation(chatid, 'https://media.giphy.com/media/Ta4mvw2BRONmQHNFOf/giphy.gif', caption=text, disable_notification=True, reply_markup=markup)
  # wellcome_media = bot.send_animation(chatid, (random.choice(wellcome_gif)))


@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def test_send_message_with_inlinemarkup(self):
  text = 'ยินดีต้อนรับเข้าสู่ TEN FINANCE! 💎\nTENFI ทำให้ Defi เป็นเรื่องง่าย 🔥\nศึกษาข้อมูลของ TEN FINANCE ได้จากการพิมพ์คำสั่งต่างๆตามนี้ 👉'
  bot.send_video(chatid, intro_vdo, caption=text,disable_notification=True)
  bot.send_message(chatid, 
  'ข้อมูลเบื้องต้นเกี่ยวกับ TEN Finance\n'
  '/intro = แนะนำตัว TEN Finance\n'
  '/address = Contract address\n'
  '/links = รวมลิ้งต่างๆของ TENFI\n'
  '/roadmap = แผนโปรเจคในอนาคต\n'
  '/tokenomics = แผนธุรกิจของเรา\n'
  '/security = ความปลอดภัยของเรา\n'
  '/price = เช็คราคา\n'
  '/chart = กราฟราคา TENFI\n'
  '/yieldex = Yieldex คืออะไร?\n'
  '/tenlots = Tenlots คืออะไร?\n'
  '/mrten = mr.ten คือใคร?\n'
  '/dev = ทีมงานของ TEN\n' 
  '/founders = ผู้ก่อตั้ง TENFI\n'
  '/moon = wen lambo\n'
  '/hold = ถือไปทำไม\n'
  '/skynet = certik skynet\n'
  '/tracker = ติดตามพอร์ทที่มี TENFI ได้ที่นี่\n'
  '/flashloan = ป้องกันการ flashloan อย่างไร\n'
  '/gas , /highgas = วิธีแก้ไขถ้าพบค่าแก๊สผิดปกติ\n'
  '/tenzap = บริการฝาก LP ง่ายๆ\n'
  '/lp = liquidity provider\n'
  '/fee = ค่าบริการ/ค่าธรรมเนียม\n'
  '/autocompound = ระบบการทบต้น\n'
  '/dust = เศษค้างของเงินฝาก\n'
  '/mvb = โปรเจคที่ TENFI แข่งขันใน BSC\n'
  )


# @bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
# def test_send_message_with_inlinemarkup(self):
#   text = 'ยินดีต้อนรับเข้าสู่ TEN FINANCE! 💎\nTENFI ทำให้ Defi เป็นเรื่องง่าย 🔥\nศึกษาข้อมูลของ TEN FINANCE ได้จากการพิมพ์ 👉 /teninfo'
#   keyboard = [[types.InlineKeyboardButton("🌐 Website", url='https://ten.finance/'),
#             types.InlineKeyboardButton("🥞 PancakeSwap", url='https://exchange.pancakeswap.finance/#/swap?outputCurrency=0xd15c444f1199ae72795eba15e8c1db44e47abf62')],
#           [types.InlineKeyboardButton("📖 Medium", url='https://tenfinance.medium.com/'),
#             types.InlineKeyboardButton("📚 Documents", url='https://tenfinance.gitbook.io/faq/')],
#           [types.InlineKeyboardButton("📢 Ann.Chn.", url='https://t.me/tenfinance_ann'),
#             types.InlineKeyboardButton("💰 Price.Chn.", url='https://t.me/BinanceRocketTENFI')],
#           [types.InlineKeyboardButton("🌳 Linktr.ee", url='https://linktr.ee/tenfi'),
#             types.InlineKeyboardButton("🗺 Roadmap", url='https://medium.com/tenfinance/ten-x-future-f0d44048f1a')],
#             [types.InlineKeyboardButton("💬 TENFI Official", url='https://t.me/tenfinance')],
#           [types.InlineKeyboardButton("🛡 CERTIK (Audits + Skynet + Shield)", url='https://www.certik.org/projects/tenfinance')]]
#   markup = types.InlineKeyboardMarkup(keyboard)
#   ret_msg = bot.send_video(chatid, intro_vdo, caption=text,disable_notification=True, reply_markup=markup)
#   # wellcome_media = bot.send_animation(chatid, (random.choice(wellcome_gif)))
#   assert ret_msg.message_id 
  # bot.send_video(chat_id_test, intro_vdo, caption='tenst')

# def on_user_joins(message):
#   if not is_api_group(message.chat.id):
#       return

#   name = message.new_chat_participant.first_name
#   if hasattr(message.new_chat_participant, 'last_name') and message.new_chat_participant.last_name is not None:
#       name += u" {}".format(message.new_chat_participant.last_name)

#   if hasattr(message.new_chat_participant, 'username') and message.new_chat_participant.username is not None:
#       name += u" (@{})".format(message.new_chat_participant.username)

#   bot.reply_to(message, text_messages['welcome'].format(name=name))




# file_data = open('../examples/detailed_example/kitten.jpg', 'rb')

# @bot.message_handler(commands=['test'])
# def send_welcome(message):
#   bot.send_photo(message, open(img1, 'rb'))

# @bot.message_handler(regexp=r'lambo LAMBO')
# def send_welcome(message):
#   bot.send_message(chat_id_test, 
#   'Lambo : คือแปลว่าการที่ราคาเหรียญพุ่งขึ้นไปสูงมาก ๆ เปรียบเทียบกับราคาของเหรียญที่เพิ่มขึ้น จนสามารถซื้อรถ Lamborghini ได้หนึ่งคัน หากอยู่ในกลุ่ม Telegram ของต่างชาติมักเจอคำว่า When Lambo ?'
#   )
# sticker_dop = 'CAACAgUAAxkBAAJDYWEiLv7lYqpOH3Oy6vP2u-a7hpc3AAL1AgACQfqYVu8UjzD2YsBQIAQ'


randomText= ['ของเค้าก็ดีนะ','ทำไมต้องพูดถึงเหรียญอื่นด้วย TENFI ดีกว่าตั้งเยอะ','เตือน*','หนีไป','ก็พอได้นะ']
randomTen= ['ตัวนี้คือดีย์ Jarvis รู้ Jarvis เรียนมา','ไม่ซื้อตอนนี้ระวังตกรถ Jarvis เตือนแล้วนะ','ตัวนี้ดี เชื่อ Jarvis', 'หลุมเพื่อน หลุม']
randomJarvis= ['มีอะไรให้รับใช้ครับ','ว่าไงครับ','ไม่สนิทอย่าเรียกบ่อย','เพื่อนเล่นหรอ','ครับนาย','YES BOSS','Sir, yes sir!', 'ได้ครับพี่ ดีครับผม เหมาะสมครับท่าน']
randomGoodnight= ['Good night and sleep tight.' ,'Goodnight','ฝันดีครับ','sweetheart.','Have a good sleep.','Time to hit the pillow.','ZzZzZZz','Sleep well.','Have a good sleep.', 'Night Night.','Nighty night.','See you tomorrow morning.','See you in my dreams.','Sleep well.']
randomBought= ['To da Moon','คือลือ','สวยพี่สวย','ขอแบบนี้อีก','ขอแบบเบิ้มๆ','จัดมาดิ เอาแบบเบิ้ม ๆ น่ะมะคือลือน่ะ']
randomSold= ['ขายหมู','อ้าวๆ เป็นจังได๋ ไหวบ่หนิ','แล้วจะเสียใจ']


@bot.message_handler(regexp=r'/BOUGHT|Bought')
def send_welcome(message):
  bot.reply_to(message, (random.choice(randomBought)))

@bot.message_handler(regexp=r'/SOLD|Sold')
def send_welcome(message):
  bot.reply_to(message, (random.choice(randomSold)))

@bot.message_handler(regexp=r'/Prayuth|ประยุทธ์|ประยุทธ')
def send_welcome(message):
  bot.reply_to(message, 'ออกไป')

@bot.message_handler(regexp=r'/ข้นใส|ข้นใส|คนที่ไหน')
def send_welcome(message):
  bot.reply_to(message, 'Ima Robot')

# @bot.message_handler(regexp=r'/dop|Dop|DOP|wad|wex|definix|six|WAD|WEX|DEFINIX|SIX|WARDEN|warden|tuk|TUK|bunny|BUNNY|Alpaca|ALPACA|พีวียู|พี วี ยู|pvu|p v u|P วี U|พี V ยู|พีvยู|PVU|พีvu')
# # @bot.message_handler()
# def send_welcome(message):
#   bot.reply_to(message, (random.choice(randomText)))


randomPrice= ['$1','$2','$3','$4','$5','$6','$7','$8','$9','$10','$11','$12','$13','$14','$15','$16','$17','$18','$19','$20','$21','$22','$100']
randomEx= ['ก็หรูละ', 'ก็ได้อยู่นะ','แน่ๆ','ก็พอซื้อ LAMBO ขับได้อะนะ','ก็พอแล้วแหละ','ก็พอซื้อสวนมะพร้าว 20 ไร่ได้อะ']


@bot.message_handler(regexp=r'สิ้นปี.*ราคา')
def send_welcome(message):
  bot.reply_to(message, 'จาร์วิสคิดว่า' + ' ' + (random.choice(randomPrice)) + ' ' + (random.choice(randomEx))) 


@bot.message_handler(regexp=r'/จาวิส|jarvis|JARVIS|จาร์วิส|Jarvis|จาวิส')
def send_welcome(message):
  bot.reply_to(message, (random.choice(randomJarvis)))

@bot.message_handler(regexp=r'/ฝันดีครับ|ฝันดีครับ|ฝันดีค่ะ|ฝันดีคับ|ฝันดีค่า|ฝันดีค๊าบ|Goodnight')
def send_welcome(message):
  bot.reply_to(message, (random.choice(randomGoodnight)))


# @bot.message_handler(regexp=r'/ราคา|ราคา|ราคาขึ้น|ราคาลง')
# def send_welcome(message):
#   bot.reply_to(message, 'อยากคุยเรื่องราคาไปคุยทีห้องนี้ได้เลยครับ\nhttps://t.me/tenfipricediscussion')

@bot.message_handler(commands=['TENFI'])
def send_welcome(message):
    bot.reply_to(message, (random.choice(randomTen)))
    
@bot.message_handler(commands=['TEN'])
def send_welcome(message):
  bot.reply_to(message, (random.choice(randomTen)))

@bot.message_handler(commands=['ten'])
def send_welcome(message):
  bot.reply_to(message, (random.choice(randomTen)))

@bot.message_handler(commands=['tenfi'])
def send_welcome(message):
  bot.reply_to(message, (random.choice(randomTen)))

@bot.message_handler(commands=['Tenfi'])
def send_welcome(message):
  bot.reply_to(message, (random.choice(randomTen)))

@bot.message_handler(commands=['หลุม'])
def send_welcome(message):
  bot.reply_to(message, 'หลุมกว่านี้ไม่มีแล้วเพื่อน')

# @bot.message_handler(regexp=r'สวัสดีตอนเช้า|อรุณสวัสดิ์|morning')
# def send_message(message):
#   bot.send_photo(chatid, 'https://www.xn--k3cc7brobq0b3a7a3s.com/wp-content/uploads/2019/05/DSC_1405.jpg', 'สวัสดีวันพุธ มีความสุขโชคดีมีชัย นะครับชาว TENizens')

randomRug= ['โอกาสเป็น 0','ไม่มีวันนั้น','TENFI ไม่มีคำสั่งนี้ครับ']

@bot.message_handler(commands=['rugpull'])
def send_welcome(message):
  bot.reply_to(message,  (random.choice(randomRug)))

@bot.message_handler(commands=['rug'])
def send_welcome(message):
  bot.reply_to(message,  (random.choice(randomRug)))


@bot.message_handler(commands=['tenlots'])
def send_welcome(message):
  bot.reply_to(message,  'Tenlots คืออะไร\n\n'
  'Tenlots คือจำนวน Tenfi ที่คุณมี ไม่ว่าจะฟาร์มเดี่ยว ฟาร์มคู่ LP หรือถือใน wallet ก็นับเป็น tenlots ทั้งหมด\n\n'
  'สมมติ เรามี Tenfi ที่ฟาร์มในระบบทั้งหมด 450000 เหรียญ\n'
  'ใน Tab ของ Tenlots เราก้จะโชว์ 450000 ซึ่งเราสามารถนำไป stake สร้าง passive income ในรูปแบบของ BUSD หรือ BNB สามารถเลือกได้ รายได้มาจาก Yieldex Revenue มีอัตราส่วนดังนี้\n\n'
  '1. บัตรทองแดง ใช้ Tenlots สองพันห้าร้อยเหรียญต่อใบ มีจำกัด หนึ่งหมื่นใบ\n'
  '2. บัตรเงิน ใช้ Tenlots ห้าหมื่นเหรียญต่อใบ มีจำกัด สองพันใบ\n'
  '3. บัตรทอง ใช้ Tenlots สองแสนห้าหมื่นเหรียญต่อใบ มีจำกัด สองร้อยใบ\n\n'
  'การแบ่ง รายได้ จะมาจาก Yieldex Revenue แบ่งออกเป็นสามส่วน \n'
  '33.33% สำหรับแต่ละประเภทของบัตร\n'
  'นั่นหมายความว่า บัตรทองจะมีส่วนแบ่งเยอะกว่าเนื่องจากคนแบ่งน้อยกว่า\n'
  'Tenlots ยังสามารถนำไปใช้ในการเพิ่ม APR ใน Yieldex อีกด้วย\n')

@bot.message_handler()
def send_welcome(message):
  if message.text == 'TEN' or message.text == 'TENFI' or message.text == 'ten' or message.text == 'tenfi' or message.text == 'Tenfi':
    bot.reply_to(message, (random.choice(randomTen)))
  elif message.text == 'BNB' or message.text == 'bnb':
    bot.reply_to(message, '1 BNB = 1 TENFI')

  # bot.send_message(chat_id_test, (random.choice(randomText)))
  # if message.text == 'dop' or message.text == 'Dop' or message.text == 'DOP' or message.text == 'wad' or message.text == 'wex' or message.text == 'cake' or message.text == 'definix' or message.text == 'six' or message.text == 'WAD' or message.text == 'WEX' or message.text == 'CAKE' or message.text == 'DEFINIX' or message.text == 'SIX' or message.text == 'WARDEN' or message.text == 'tuk' or message.text == 'wad' or message.text == 'wad' or message.text == 'wad' or message.text == 'wad':
  # elif message.text == 'Test':
  #   bot.send_message(chat_id_test, 'Test succeeded')
  # else:
  #   bot.send_message(chat_id_test, 'Sorry I don\'t get it!')
  # bot.send_sticker(chatid, sticker_dop)
  # bot.send_message(chatid, 'จะพูดถึงเหรียญอื่นทำไม ในเมื่อ Tenfi ดีกว่าตั้งเยอะ')

# sticker_goodnight = 'CAACAgUAAxkBAAJDY2Eip9KALqT8qhfj7Kn1zzZXZ0WhAAKEAQACdTdYVsbJc07RnY3aIAQ'

# @bot.message_handler(regexp=r'/ฝันดีครับ|Goodnight|goodnight/g')
# def send_welcome(message):
#   bot.send_sticker(chat_id_test, sticker_goodnight)
#   bot.send_message(chat_id_test, 'ฝันดีครับชาว TENizens')

# @bot.message_handler(func=lambda message: message.text == "ฝันดีครับ" or "ฝันดี" or "ฝันดีคะ" or "ฝันดีค่ะ")
# def send_welcome(message):
#   bot.send_sticker(chatid, sticker_goodnight)
#   bot.send_message(chatid, 'ฝันดีครับชาว TENizens')


while True:
  try:
    bot.polling()
  except Exception:
    time.sleep(15)
