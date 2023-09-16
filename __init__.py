import requests, json, datetime

# import the main window object (mw) from aqt
from aqt import mw
from aqt import gui_hooks

# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect

# import all of the Qt GUI library
from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.


config = mw.addonManager.getConfig(__name__)
BEEMINDER_USERNAME = config["beeminder_username"]
BEEMINDER_PERSONAL_AUTH_TOKEN = config["beeminder_personal_auth_token"]


def get_due_cards() -> int:
    due_cards = mw.col.find_cards("is:due")
    return len(due_cards)


def post_to_beeminder(
    auth=BEEMINDER_PERSONAL_AUTH_TOKEN, user=BEEMINDER_USERNAME, goal="anki-zero"
) -> str:
    due_cards = get_due_cards()
    url = f"https://www.beeminder.com/api/v1/users/{user}/goals/{goal}/datapoints.json"

    data = {
        "auth_token": auth,
        "value": due_cards,
        "comment": "Anki Zero - {} - due cards: {}".format(
            datetime.datetime.now(), due_cards
        ),
    }

    try:
        response = requests.post(url, data=data)
        return response.text
    except requests.exceptions.RequestException as e:
        showInfo("Anki Zero error!\n\n%s" % e)
        return None


def testFunction() -> None:
    response = post_to_beeminder(BEEMINDER_PERSONAL_AUTH_TOKEN, BEEMINDER_USERNAME)

    showInfo(
        "Anki Zero success!\n\nResponse: %s"
        % json.dumps(json.loads(response), indent=4)
    )

    return None


# create a new menu item, "test"
action = QAction("Manually sync Anki Zero", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)

# Run post_to_beeminder on Anki startup.
gui_hooks.profile_did_open.append(post_to_beeminder)

# Run post_to_beeminder on Anki sync.
gui_hooks.sync_did_finish.append(post_to_beeminder)

# Run post_to_beeminder on Anki close.
gui_hooks.profile_will_close.append(post_to_beeminder)
