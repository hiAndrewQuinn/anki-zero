import requests, json

# import the main window object (mw) from aqt
from aqt import mw

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


def post_to_beeminder(auth, user, goal="anki-zero") -> str:
    due_cards = get_due_cards()
    url = f"https://www.beeminder.com/api/v1/users/{user}/goals/{goal}/datapoints.json"

    data = {
        "auth_token": auth,
        "value": due_cards,
        "comment": "Auto-generated from hiAndrewQuinn's Anki Zero addon.",
    }

    response = requests.post(url, data=data)

    return response.text


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
