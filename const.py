from enum import Enum


class Messages(str, Enum):
    START = """Привет! 👋

Я чат-бот Мастерской живых украшений Натальи Коротковой.

Скажу по секрету 🤫, я бы и сам носил эти украшения, но я виртуальный.

Я очень рад, что Вы присоединились к нам и расскажу всю основную информацию.

Если останутся вопросы, напишите Наталье @Nataliya_Korotkova."""
    ORDER = """Для создания изделия понадобятся актуальные фотографии, если дополнительно добавите видео — еще лучше. 
Фотографии должны быть живыми, не как на паспорт. Где Вы в обычной жизни и видно лицо. Можно селфи.

Украшения, которые представлены в канале, выкуплены заказчиками и служат как ознакомительный материал с подчерком мастера.

Аксессуары индивидуальны и не имеют повторений, создаются по энергии Вашего поля."""
    DELIVERY = """Доставка не входит в стоимость заказа и рассчитывается в соответствии с тарифами перевозчика.

Способы доставки:

• Яндекс.Доставка
• СДЭК
• Почта России
• Самовывоз (м. Улица Скобелевская)

В данный момент самый удобный способ доставки — Яндекс. Привозят на ближайший ПВЗ Яндекс.Маркет."""
    PRICE = """Стоимость индивидуальных украшений:

• Серьги от 2500 ₽
• Браслет от 3000 ₽
• Цепи с кулоном и др. от 4000 ₽

Конечная цена формируется после готовности."""
    CARE = """Рекомендации по уходу за украшениями:

• Избегайте контакта аксессуаров с косметикой и бытовой химией.

• Не распыляйте духи непосредственно на изделие.

• Снимайте при физической нагрузке.


Есть один нюанс. ☝🏻Скорее всего, Вы не захотите их снимать, поэтому поделюсь обратной связью от клиентов:

"Я в восторге и не хочу их снимать!"

"Только утром поняла, что заснула в украшениях."

"Провела неделю на море и даже не снимала."

"Ношу и вообще не снимаю."

"Не носила бижутерию из-за аллергии, а  сейчас вся шкатулка заполнена твоими украшениями!"


Можете ни в чем себе не отказывать. 
Соблюдение рекомендаций лишь продлит срок службы изделий. Помните, что главная опасность — это духи и агрессивная химия. ❌"""
    ABOUT = """У подростков аксессуары ассоциируются с артефактами. 

У детей это любимые украшения. 

Взрослые носят годами и их любовь не гаснет. 

Украшения несут в себе состояния, которые Вам сейчас необходимы. Если Вы чувствуете, что не хотите их снимать, не снимайте. Значит, организму так нужно."""
    VERSION = "Версия бота %s"
    UNKNOWN = "Не разберу... Повтори!"


class Buttons(str, Enum):
    DELIVERY = "📦 Доставка"
    ORDER = "📨 Заказ"
    PRICE = "💳 Стоимость"
    CARE = "❤️ Уход"
    ABOUT = "🪄 О свойствах"


class Commands(str, Enum):
    RESTART = "Перезапуск"
    VERSION = "Версия"
