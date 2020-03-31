define l = Character('Людмила Самиуллина', color="#ff4cff")
define ky = Character('Курсант', color="#ff0000")
define k = Character('Кристина Царёва', color="#ffbfef")
define le = Character('Алексей Самойов', color="#ffbfef")
define ry = Character('Руслан Муслумов', color="#ffbfef")
define xa = Character('Хатира Сулкейманова', color="#ffbfef")
define al = Character('Алексей Лебедев', color="#ffbfef")
define e = Character('Эльджан Гаджиев', color="#ffbfef")
define bo = Character('Анастасия Болдырева', color="#ffbfef")
define i = Character('Илья Сучков', color="#ffbfef")
define ma = Character('Матюнина Рита', color="#ffbfef")
define t = Character('Таня Визир', color="#ffbfef")
define va = Character('Валерия Кислухина', color="#ffbfef")
define an = Character('Андрей Иванилов', color="#ffbfef")
define ai = Character('Айхан Гурбаналиев', color="#ffbfef")
define dm = Character('Дмитрий Шкитенков', color="#ffbfef")
define m = Character('Марина Шаркунова', color="#ffbfef")
define s = Character('Сараев Кирилл', color="#ffbfef")
define au = Character('Аулова Юлия', color="#ffbfef")
define d = Character('Давыдкина полина', color="#ffbfef")
define ka = Character('Камалова Алена', color="#ffbfef")
define r = Character('Радивил Кристина', color="#ffbfef")
define u = Character('Суслова Юлия', color="#ffbfef")
define x = Character('Хлюстова Елена', color="#ffbfef")
define a = Character('Алили Зохраб (Зёма)', color="#ffbfef")
define dr = Character('Алексеева Дарья', color="#ffbfef")
#тут должен быть сюжет о курсанте (безымянном) и его истории длинною в день.
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:

label start:
    $ star = False
    play music "sunflower-slow-drag.ogg"

    scene bg start

    show  doki

    "Это история об одном безымянном курсанте, который прошёл длинный путь в обучении в юридическим колледже."

    "Сегодня вы увидите один из его последних дней обучения в Юридическом колледже!"

    menu:
         "Тебе интересен такой сюжет?"
         "Да":
             "Отлично , погнали!"
             $ star = True
             jump kolledge

         "Нет":
             "Это твой выбор"
             return

label kolledge :
    #тут должна быть вводная фотография

    "Прошло 4 года стех пор как один курсант проучился в Юридическом колледже"

    "Он многому научился обучаясь там , завел новых друзей и знакомых, возмужал и теперь готов к настоящей взрослой жизни"

    #тут должна быть фотка взвода или несколько фоток

    "Сегодня рассказ пойдет о небезысвестном 413м взводе. Не все куранты этого взвода смогут попасть в историю , но об основных лицах вы узнаете"

    #тут должна быть фотка колледжа.

    ky "{i}(А вот и колледж! Даже не вернится , что я скоро в него не вернусь.)"

    ky "{i}(Ещё недавно я трясся от страха проходя скринниг,  а теперь я выпускник этого заведения)"

    ky "{i}(Сегодня очень важный день - день экзамена! Хорошо что я подготовился(нет))"

    ky "{i}(Я встречаюсь с моим одногрупником по имени Людмила)"

    ky "Примерно так мыглядит продолжение текста"

    k "тебе ещё многое предстоит познать , удачи"

    ky "спасибо"

    if star:
     "это текст для переменной игры"
    else:
     "а вот хер тебе"
return
