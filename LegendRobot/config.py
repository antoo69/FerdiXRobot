class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 29305295
    API_HASH = "6838cc67172f18fe5f302c158ce2fbfa"

    CASH_API_KEY = "WEQNXZTREO3ZMKY1"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://u88ctvtrs3a7u9:p44d116de583f3310666af747d006125e3463d18442e981155de18669a1f99e0e@c9uss87s9bdb8n.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dfpbluemp4av3g"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://kcici715:buburayam1@cluster0.clpcyju.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/e5957d1aec17d15989b35.jpg"

    SUPPORT_CHAT = "BestieVirtual"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7152638324:AAF50JDk7SRE2jYCe5A6imkzeFQr7rilDho"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "SOCSLO0QUKHT"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7083782157  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
