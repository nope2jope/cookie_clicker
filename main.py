from cookie_monster import Puppet
import time
import os

DRIVER_PATH = os.environ['ENV_DRIVER_PATH']
GAME_LINK = 'https://orteil.dashnet.org/experiments/cookie/'
SHORT_WAIT = 5
TOTAL_RUNTIME = 20

monster = Puppet(path=DRIVER_PATH, link=GAME_LINK, wait_time=SHORT_WAIT)

game_on = True

# runtime here represents the total runtime (20 seconds) of the app for testing purposes
# with this variable removed the while loop would not terminate
runtime = time.time() + TOTAL_RUNTIME
cooldown = monster.set_timer()

while game_on:
    monster.slam_cookie()

    # checks to see if twenty seconds have elapsed
    if runtime < time.time():
        print("time's up!")
        print(monster.check_wallet())
        monster.driver.close()
        game_on = False
    elif cooldown < time.time():
        try:
            monster.pause_n_click()
            cooldown = monster.set_timer()
        finally:
            continue
