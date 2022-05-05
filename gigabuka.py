import pyautogui as bot
bot.FAILSAFE = False
bot.moveTo(310, 1100,1)
bot.click(310, 1100,1)
bot.hotkey('Ctrl', 'T')
bot.click(950,410)
bot.typewrite('dino google')
bot.press('Enter')  
bot.moveTo(220, 290, 1)
bot.click(220, 290)
bot.press('space')
bot.PAUSE = 3
bot.press('space')