import os

# All necessary tokens, passwords, etc.
# Your bluesky handle should include your instance, so for example handle.bsky.social if you are on the main one.
BSKY_HANDLE = "anythingbotde.bsky.social"
# Generate an app password in the settings on bluesky. DO NOT use your main password.
BSKY_PASSWORD = "burrrrrrrr"
# Your mastodon handle. Not needed for authentication, but used for making "quote posts".
MASTODON_HANDLE = ""
# The mastodon instance your account is on.
MASTODON_INSTANCE = ""
# Generate your token in the development settings on your mastodon account. Token must have the permissions to
# post statuses (write:statuses)
MASTODON_TOKEN = ""
# Get api keys and tokens from the twitter developer portal (developer.twitter.com). You need to create a project
# and make sure the access token and secret has read and write permissions.
TWITTER_APP_KEY = "KA9lbIsYK8l1JylIR4SXSsAZt"
TWITTER_APP_SECRET = "5PajZ1WxDBWvLxmuzUOB0h7ueUwHK3ZACtgWluLMaDacPhDaFM"
TWITTER_ACCESS_TOKEN = "1467409705148379137-IuCAhqejHGJLT04KiYOd1HqlCmmWWc"
TWITTER_ACCESS_TOKEN_SECRET = "1qC8o18i5ybWmNc9pbZCH988kt3snZzCKf3iE7nP97Hvk"

# Override settings with environment variables if they exist
BSKY_HANDLE = os.environ.get('BSKY_HANDLE') if os.environ.get('BSKY_HANDLE') else BSKY_HANDLE
BSKY_PASSWORD = os.environ.get('BSKY_PASSWORD') if os.environ.get('BSKY_PASSWORD') else BSKY_PASSWORD
MASTODON_INSTANCE = os.environ.get('MASTODON_INSTANCE') if os.environ.get('MASTODON_INSTANCE') else MASTODON_INSTANCE
MASTODON_HANDLE = os.environ.get('MASTODON_HANDLE') if os.environ.get('MASTODON_HANDLE') else MASTODON_HANDLE
MASTODON_TOKEN = os.environ.get('MASTODON_TOKEN') if os.environ.get('MASTODON_TOKEN') else MASTODON_TOKEN
TWITTER_APP_KEY = os.environ.get('TWITTER_APP_KEY') if os.environ.get('TWITTER_APP_KEY') else TWITTER_APP_KEY
TWITTER_APP_SECRET = os.environ.get('TWITTER_APP_SECRET') if os.environ.get('TWITTER_APP_SECRET') else TWITTER_APP_SECRET
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN') if os.environ.get('TWITTER_ACCESS_TOKEN') else TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET') if os.environ.get('TWITTER_ACCESS_TOKEN_SECRET') else TWITTER_ACCESS_TOKEN_SECRET
