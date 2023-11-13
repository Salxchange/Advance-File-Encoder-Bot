import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "21288218")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6270384345:AAFvlP3FGsE4eKg62jYnDIX-xhnW9M8LFX0") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1001956303989') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://SNOWENCODER:SNOWENCODER@cluster0.hdxpxtg.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","USERDATA") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6065594762")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001971176803')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()


    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))