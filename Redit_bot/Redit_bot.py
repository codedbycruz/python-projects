import praw
import config


praw.reddit(username =config.username,
            password=config.password,
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent = "busterronitest's dog comme nt responder v0.1")
