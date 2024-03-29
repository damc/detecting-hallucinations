from os.path import dirname, join

from text_bridge.config import update_config


def set_text_bridge_config():
    """Set the text bridge configuration."""
    inputs_path = join(dirname(__file__), "prompts")
    config = {"inputs_path": inputs_path}
    update_config(config)


