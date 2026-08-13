"""
Shared configuration used by the application.
"""

APP_NAME = "Stacked PR Demo"
APP_VERSION = "1.0-parent"

def get_config():
    return {
        "name": APP_NAME,
        "version": APP_VERSION,
    }