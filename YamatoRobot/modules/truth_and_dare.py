import random

from telegram import Update
from telegram.ext import CallbackContext

import YamatoRobot.modules.truth_and_dare_string as truth_and_dare_string
from YamatoRobot import dispatcher
from YamatoRobot.modules.disable import DisableAbleCommandHandler


def truth(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


def dare(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))
def sigma(update: Update, context: CallbackContext):
    update.effective_message.reply_video(random.choice(truth_and_dare_string.SIGMA))


def cosplay(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(random.choice(truth_and_dare_string.COSPLAY))

def onepiece(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(random.choice(truth_and_dare_string.WAIFU))

def yamato(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(random.choice(truth_and_dare_string.YAMATO))
def naruto(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(random.choice(truth_and_dare_string.NARUTO))




TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, run_async=True)
SIGMA_HANDLER = DisableAbleCommandHandler("sigma", sigma, run_async=True)
COSPLAY_HANDLER = DisableAbleCommandHandler("cosplay", cosplay, run_async=True)
WAIFU_HANDLER = DisableAbleCommandHandler("onepiece", onepiece, run_async=True)
YAMATO_HANDLER = DisableAbleCommandHandler("yamato", yamato, run_async=True)
NARUTO_HANDLER = DisableAbleCommandHandler("naruto", naruto, run_async=True)





dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(SIGMA_HANDLER)
dispatcher.add_handler(COSPLAY_HANDLER)
dispatcher.add_handler(WAIFU_HANDLER)
dispatcher.add_handler(YAMATO_HANDLER)
dispatcher.add_handler(NARUTO_HANDLER)
