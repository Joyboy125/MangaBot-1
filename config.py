env_vars = {
    # Get from my.telegram.org
    "API_HASH": "f757ca005f4a320bcea5ced947bbff5e",
    # Get from my.telegram.org
    "API_ID": "27011028",
    # Get from @BotFather
    "BOT_TOKEN": "7505997121:AAF2Wf6naoMWdEJ1VVWgDHQNgf48Jsv6_DE", 
    # Get from tembo.io
    "DATABASE_URL_PRIMARY": "postgresql://postgres:k0edUULYD0G6vZy0@fruitfully-legitimate-lemur.data-1.use1.tembo.io:5432/postgres",
    # Logs channel username without @
    "CACHE_CHANNEL": "",
    # Force subs channel username without @
    "CHANNEL": "",
    # {chap_num}: Chapter Number
    # {chap_name}: Manga Name
    # Example: Chapter {chap_num} {chap_name} @Manhwa_Arena
    "FNAME": "{chap_num}. {chap_name}",
    # Thumb Path (Optional)
    "THUMB": "thumbnail.jpg", 
    # Add authorized user IDs, separated by commas in a list
    "SUDOS": [1355560957],
    #Your repo branch
    "UPSTREAM_BRANCH": "master",
    # Your repo link
    "UPSTREAM_REPO": "https://github.com/Joyboy125/MangaBot-1.git"
}

# Determine the database URL (default to SQLite if not provided)
dbname = (
    env_vars.get("DATABASE_URL_PRIMARY") 
    or env_vars.get("DATABASE_URL") 
    or "sqlite:///test.db"
)

# Ensure compatibility with SQLAlchemy if using older Postgres URL formats
if dbname.startswith("postgres://"):
    dbname = dbname.replace("postgres://", "postgresql://", 1)
