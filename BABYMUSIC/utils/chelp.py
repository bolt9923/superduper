def first_page(_):
    first_page_menu = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["H_B_1"], callback_data="help_callback hb1"),
                InlineKeyboardButton(text=_["H_B_10"], callback_data="help_callback hb2"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_11"], callback_data="help_callback hb3"),
                InlineKeyboardButton(text=_["H_B_14"], callback_data="help_callback hb4"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_16"], callback_data="help_callback hb5"),
                InlineKeyboardButton(text=_["H_B_17"], callback_data="help_callback hb6"),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_22"], callback_data="help_callback hb7"
                ),
                InlineKeyboardButton(
                    text="More futures", url="http://t.me/YOUTUBE_RROBOT?start=help"
                ),
            ],
            #[
               # InlineKeyboardButton(
                  #  text=_["H_B_14"], callback_data="help_callback hb14"
               # ),
               # InlineKeyboardButton(
                #    text=_["H_B_15"], callback_data="help_callback hb15"
               # ),
           # ],
           # [
                #InlineKeyboardButton(
                 #   text=_["H_B_16"], callback_data="help_callback hb16"
               # ),
              #  InlineKeyboardButton(
                 #   text=_["H_B_17"], callback_data="help_callback hb17"
              #  ),
          #  ],
           # [
              #  InlineKeyboardButton(
                 #   text=_["H_B_18"], callback_data="help_callback hb18"
              #  ),
              #  InlineKeyboardButton(
                #    text=_["H_B_13"], callback_data="help_callback hb13"
              #  ),
           # ],
           # [
               # InlineKeyboardButton(
                #    text=_["H_B_20"], callback_data="help_callback hb20"
             #   ),
              #  InlineKeyboardButton(
                #    text=_["H_B_22"], callback_data="help_callback hb22"
              #  ),
          #  ],
           # [
              #  InlineKeyboardButton(
                #    text=_["H_B_21"], callback_data="help_callback hb21"
              #  )
          #  ],
        ]
    )
    return first_page_menu
