"""
Shared configuration used by the application.
"""

APP_NAME = "Stacked PR Demo"
APP_VERSION = "2.0-child"

def get_config():
    return {
        "name": APP_NAME,
        "version": APP_VERSION,
    }