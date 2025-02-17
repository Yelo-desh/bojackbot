import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# 🔹 أدخل توكن البوت الخاص بك هنا
TOKEN = "7482787955:AAGvZqrux0j9_AOFWMHh9WfSt_TwsYzLyhw"
bot = telebot.TeleBot(TOKEN)

# 🔹 قائمة الحلقات مع File IDs
episodes = {
    "الموسم 1": [
        "BAACAgEAAxkBAAMvZ7JvklX132epjcrrvpT_-bOS-k4AAvUEAALt65BFiLsYdA7CRX82BA", "BAACAgEAAxkBAAMxZ7Jv-VGa1Na6PXvXvbCqOPVqBM8AAvgEAALt65BF8uEMOdlVV242BA", "BAACAgEAAxkBAAMzZ7JwxRSbA8hiWCbq7_oczFiLGzQAAvkEAALt65BF2Yp31lhy6dk2BA", "BAACAgEAAxkBAAM1Z7JxUdkSnz2SiBb0v6y4SRJRGccAAvwEAALt65BFsf0LuX41W_42BA",
        "BAACAgEAAxkBAAM3Z7JyUSYg-39Y9hc1inW77HmJCZUAAv4EAALt65BFJkG5r3VWdT82BA", "BAACAgEAAxkBAAM5Z7Jy3_4KJKWNDtDjm6TLc0CjOywAAv8EAALt65BFfO21kLuVCwABNgQ", "BAACAgEAAxkBAAM9Z7J0c0n80QOPh_tJF5YUMCJfgLoAAgIFAALt65BF4R1nnjOsLOY2BA", "BAACAgEAAxkBAAM_Z7J08V6zqbmAtScQ16_cKvC3784AAgMFAALt65BFuVe2wdy4ti02BA",
        "BAACAgEAAxkBAANBZ7J1wSVKMMqROrD0n7XNIPIG2PsAAgQFAALt65BFwb5jL1Jwc802BA", "BAACAgEAAxkBAANDZ7J28ffR8NxE3Bhy6m5SPh1iLwkAAgUFAALt65BFb7_iKE-988A2BA", "BAACAgEAAxkBAANFZ7J34Gti7GZ2l0B-7LxnE59pTUMAAgYFAALt65BFOgcINOAGaig2BA", "BAACAgEAAxkBAANHZ7J4sbKXytIeeNbpiUh-ezYj4i8AAgcFAALt65BFAAF740MeOUqLNgQ"
    ],
    "الموسم 2": [
        "BAACAgEAAxkBAANJZ7J5XpbkOsAaqAHPUaUCmSY0YpYAAggFAALt65BFdu6HWrwmZ7k2BA", "BAACAgEAAxkBAANLZ7J528mKJprMyXFCiXhf8aKtGloAAgkFAALt65BFXag3xCoQlG42BA", "BAACAgEAAxkBAANLZ7J528mKJprMyXFCiXhf8aKtGloAAgkFAALt65BFXag3xCoQlG42BA", "BAACAgEAAxkBAANPZ7J7bxRLOAGGhVxdAAGGHZlspFtsAAIMBQAC7euQRWBW42JtYY_nNgQ",
        "BAACAgEAAxkBAANRZ7J73bocoOqv06aHHCKzzJtMpYEAAg0FAALt65BF1B1faODzbyI2BA", "BAACAgEAAxkBAANTZ7J8VrIERXw6gCBvrekAAQ_if_d5AAIOBQAC7euQRak7Lxff4H7mNgQ", "BAACAgEAAxkBAANVZ7J84mQLJFeX5X5-5dMYwrb6vNMAAg8FAALt65BF3cyneSLEnig2BA", "BAACAgEAAxkBAANXZ7J-E7CW-c9dDzgKwHRLGa28-b0AAhAFAALt65BFs5nHhyFql2c2BA",
        "BAACAgEAAxkBAANZZ7J-3Bmbr91egbv6kDkhVaye1m8AAhEFAALt65BFiOs4xqXzMWA2BA", "BAACAgEAAxkBAANbZ7J_ypfZNsZSuN-2HcuJMOZIdOsAAhIFAALt65BFE5SV2p_5JEE2BA", "BAACAgEAAxkBAANdZ7KAP0NqGFkQi_YYE4v3WNby0QMAAhMFAALt65BFfUX2DklFKmQ2BA", "BAACAgEAAxkBAANfZ7KAxX9PXD-uSoF4-UcZCRnloucAAhQFAALt65BFoq_T1hY3nrs2BA"
    ],
    "الموسم 3": [
        "BAACAgEAAxkBAANhZ7KpQKc0abYVSTW23MkjI3O-3owAAisFAALt65BFLSFAN3mosng2BA", "BAACAgEAAxkBAANjZ7Kp0JFp_HjKXNvpWICpnCrQ4gwAAi0FAALt65BF9YrdAx2jBk82BA", "BAACAgEAAxkBAANlZ7KqWPFtUiFyc38w1nEk4CYVEdIAAi4FAALt65BFOAI0OWmVtXk2BA", "BAACAgEAAxkBAANnZ7Kq2AYWgZLhSJlToKtsqpSIhQ4AAi8FAALt65BFhRCeFSDGnD82BA",
        "BAACAgEAAxkBAANpZ7KrXOdqw5G4U6yRHsabZHHCbh4AAjAFAALt65BF5bQkIuIqR_42BA", "BAACAgEAAxkBAANrZ7Kr4nHrFeFLgBRCIl1lRA-R0BUAAjEFAALt65BFx6THEblQTqg2BA", "BAACAgEAAxkBAANtZ7KsWVkYu-MQUKPBefqt8sBBVAcAAjIFAALt65BFlupX4SZPmFE2BA", "BAACAgEAAxkBAANvZ7Ks1BKOlOW4RQEzvVH6px13mIUAAjMFAALt65BFKAinGzdRkmc2BA",
        "BAACAgEAAxkBAANxZ7KtQXIGni0BdXC5SJ3ZIzDngQ4AAjQFAALt65BFYJ1K8y0bO8s2BA", "BAACAgEAAxkBAANzZ7Kt1tgTeeDkRDCv1HtPqOvIDN8AAjUFAALt65BFEPJo6w7yItQ2BA", "BAACAgEAAxkBAAN1Z7KuForrN5WWHAABtzD_oZKpf5OdAAK-BAAC14OYRY2tRK6FkhthNgQ", "BAACAgEAAxkBAAN3Z7KuZPCoJS7lI4OSqXDAh88tcAUAAr8EAALXg5hF7pNNrFuWOYQ2BA"
    ],
    "الموسم 4": [
        "BAACAgEAAxkBAAN5Z7KvXoFgajktRSuuDAeAi1Z8Ln0AAjYFAALt65BFcpPApiNDRHE2BA", "BAACAgEAAxkBAAN7Z7Kv4ENXXgtSM6B_V79f34CxVckAAjcFAALt65BFR_PvvqFmaB02BA", "BAACAgEAAxkBAAN9Z7KwBUSMHFzXqIwhBiKIRy6GSXoAAjgFAALt65BF43mJ-6T1UD82BA", "BAACAgEAAxkBAAN_Z7KwKWc54wABBIReAaYHhxY9sh-6AAI5BQAC7euQRRqVcAYLjEt2NgQ",
        "BAACAgEAAxkBAAOBZ7KwmU9k1OA9HTEx51wvQYAO_ncAAjoFAALt65BFoAssc2tOcXI2BA", "BAACAgEAAxkBAAODZ7KxGSoSSHmVEk8bNaqXAgV_LqQAAjsFAALt65BFD09_7azQULY2BA", "BAACAgEAAxkBAAOFZ7Kxl8IQr-K7L4NSTc-Ct5XXkH8AAjwFAALt65BFrvVlqr3RLNg2BA", "BAACAgEAAxkBAAOHZ7KyC84RhWIEeDLHBkTaSYtGcuwAAj0FAALt65BFkmKFJUJKQTI2BA",
        "BAACAgEAAxkBAAOJZ7KyhXe1AbsloQ7mLDkE0-JKInYAAgMFAALt65hFBPuBW2kbLUM2BA", "BAACAgEAAxkBAAOLZ7K0QJdTa0MbYhjBoFb3mcmLd5IAAgQFAALt65hFQzjdtX2sc2Q2BA", "BAACAgEAAxkBAAONZ7K0wO80gRnbRXfxD_JghiSCyqwAAgUFAALt65hFmewz3c_9Ufc2BA", "BAACAgEAAxkBAAOPZ7K1Yvb7luDyc-YEKhGNm40zwQcAAgcFAALt65hFtKsS9DwsNuU2BA"
    ],
    "الموسم 5": [
        "BAACAgEAAxkBAAORZ7K2ReuG3ybvAAF-OcmdcdXoWhcIAAIIBQAC7euYRVXCZpmS63FANgQ", "BAACAgEAAxkBAAOTZ7K2xhCkxE4PX48Q156xWsK5JawAAgkFAALt65hFgZ9uJh82NTI2BA", "BAACAgEAAxkBAAOVZ7K3Rm40tSvQDOvzN4B8GQS1h90AAgoFAALt65hFrgZ86D8xiY42BA", "BAACAgEAAxkBAAOXZ7K3x11ZrjX9S9pANT__Yax6fuQAAgsFAALt65hF2CchOKluW7M2BA",
        "BAACAgEAAxkBAAOZZ7K4SpXl7OGeRV2CuJRfbnLi21AAAgwFAALt65hF2q3BpIw0gx82BA", "BAACAgEAAxkBAAObZ7K4eGnD2kWRBk5O-3ywyCoNzP8AAg0FAALt65hFjMSAixiBVSc2BA", "BAACAgEAAxkBAAOdZ7K48HhXqu3D5PDyYtgTTLNAyLYAAg4FAALt65hFmfhmpA0SOmI2BA", "BAACAgEAAxkBAAOfZ7K5Ym2ahdcwTeRhEl3RSTK-YI4AAsIEAALXg5hFFWb9A8OVu4A2BA",
        "BAACAgEAAxkBAAOhZ7K50FVliKYmXBR9jdlaq6RBzeMAAg8FAALt65hFXRC2FZXvvUI2BA", "BAACAgEAAxkBAAOjZ7K6Xo69hr70R31RNifSmdwi0cwAAhAFAALt65hFYD0OAcbdcjw2BA", "BAACAgEAAxkBAAOlZ7K60M7ekAJ2f3LdnyLn7xc4LtcAAhEFAALt65hFRh7SZ1c5siI2BA", "BAACAgEAAxkBAAOnZ7K7H28Pi22uzBNBwbKwptBYFdoAAhIFAALt65hFnMMqkf4oQlM2BA"
    ],
    "الموسم 6": [
        "BAACAgEAAxkBAAOpZ7K72-rdBOozQegdyttWdiJ4h_UAAsMEAALXg5hFqMZ0tP-PH882BA", "BAACAgEAAxkBAAOrZ7K8aeRNjH-vKQtl5KOOg_2QIMIAAhMFAALt65hFdeo0yvbj-vY2BA", "BAACAgEAAxkBAAOtZ7K856MwQqt9dppgzp1ZRCFgzEAAAhQFAALt65hFja6XXLnL7Cw2BA", "BAACAgEAAxkBAAOvZ7K9Z5P0BtIH4G8dSH5NBO2YzaAAAhUFAALt65hFebMjdBoxirw2BA",
        "BAACAgEAAxkBAAOxZ7K94wJTKBRiUUzb3TA8MTPaUeoAAhYFAALt65hF4JKju6ZfqAI2BA", "BAACAgEAAxkBAAOzZ7K-mM0b9JuFejDcaq-ZOy9LZ-cAAsQEAALXg5hFzGlBt0XswpA2BA", "BAACAgEAAxkBAAO1Z7K_MwNP57ACWHRdgjWvy0kUQbgAAsUEAALXg5hFT2eJMJvolZQ2BA", "BAACAgEAAxkBAAO3Z7K_3d14jzw1S-alPhMyKEasrVIAAhgFAALt65hFmk7fc2Yptjg2BA",
        "BAACAgEAAxkBAAO5Z7LAcTGgQVXgeEIbsjg4J9ucjWkAAsYEAALXg5hFhhzpLtCH8L42BA", "BAACAgEAAxkBAAO7Z7LA-FaLSOyp1XCSds14Yg1hOkUAAhkFAALt65hFv3b7vmdG-9M2BA", "BAACAgEAAxkBAAO9Z7LBfLQgPEjqqPPt97XPuN1jnFMAAscEAALXg5hF0OkkuE6VgfM2BA", "BAACAgEAAxkBAAO_Z7LCGdpTu05kcnJnoiyKhNITueMAAhoFAALt65hF08M318_v8hY2BA",
        "BAACAgEAAxkBAAPBZ7LCslykuhAXwYWg2WFsFERNh2EAAsgEAALXg5hFjtxuNkpEj7A2BA", "BAACAgEAAxkBAAPDZ7LDQofzyS1X9gnbVezzIVbUQ0EAAhsFAALt65hFkk-ytK5NoPs2BA", "BAACAgEAAxkBAAPFZ7LD0C0iwCaHZ_1u2jd6is5vpEsAAhwFAALt65hFLvLEAUD4RTc2BA", "BAACAgEAAxkBAAPHZ7LEXiQ2MrnyqZSJT0OCpr4thCMAAsoEAALXg5hF64azoiVCgtM2BA"
    ]
}

user_data = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [KeyboardButton(season) for season in episodes.keys()]
        markup.add(*buttons)
        bot.send_message(message.chat.id, "📺 اختر الموسم:", reply_markup=markup)
    except Exception as e:
        print(f"Error in /start: {e}")

@bot.message_handler(func=lambda message: message.text in episodes.keys())
def select_season(message):
    try:
        user_data[message.chat.id] = message.text
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [KeyboardButton(f"حلقة {i+1}") for i in range(len(episodes[message.text]))]
        buttons.append(KeyboardButton("رجوع للخلف"))
        markup.add(*buttons)
        bot.send_message(message.chat.id, f"🎬 اختر الحلقة من {message.text}:", reply_markup=markup)
    except Exception as e:
        print(f"Error in select_season: {e}")

@bot.message_handler(func=lambda message: message.text.startswith("حلقة"))
def send_episode(message):
    try:
        episode_number = int(message.text.split()[1]) - 1
        season = user_data.get(message.chat.id)

        if season and 0 <= episode_number < len(episodes[season]):
            file_id = episodes[season][episode_number]
            bot.send_video(message.chat.id, file_id)
    except Exception as e:
        print(f"Error in send_episode: {e}")

@bot.message_handler(func=lambda message: message.text == "رجوع للخلف")
def go_back(message):
    try:
        user_data.pop(message.chat.id, None)
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [KeyboardButton(season) for season in episodes.keys()]
        markup.add(*buttons)
        bot.send_message(message.chat.id, "📺 اختر الموسم مرة أخرى:", reply_markup=markup)
    except Exception as e:
        print(f"Error in go_back: {e}")

bot.polling()

