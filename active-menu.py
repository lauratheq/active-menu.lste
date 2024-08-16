#!/usr/bin/python3

"""
This script provides functionality for modifying HTML content based on meta information.

The script includes the following functions:
- `register_hooks`: Registers hooks to process content before loading custom functions.
- `load_active_menu`: Updates HTML content to mark the active menu item based on meta information.

Legal Note:
    Written and maintained by Laura Herzog (laura-herzog@outlook.com)
    Licensed under the GPL license. See the project at https://github.com/lauratheq/lste
"""

from typing import Any

def register_hooks(lste: Any) -> None:
    """
    Registers hooks for processing content before loading custom functions.

    Args:
        lste: An object that supports hook registration, which will call `load_active_menu`
              when the 'pre_load_custom_functions' hook is triggered.
    """
    lste.hooks.add('pre_load_custom_functions', load_active_menu)

def load_active_menu(content: str, file: str, lste: Any) -> str:
    """
    Updates the HTML content to mark the active menu item based on meta information.

    This function searches for a menu item in the content and adds an 'active' class
    to it if the `active-menu` meta field is set for the current file.

    Args:
        content (str): The HTML content to be modified.
        file (str): The filename to look up meta information.
        lste: An object containing the content dictionary with meta fields. 

    Returns:
        str: The updated HTML content with the active menu item marked.
    """
    if 'active-menu' in lste.content[file]['meta']:
        active_menu_entry = lste.content[file]['meta']['active-menu']
        content = content.replace(f'<li id="{active_menu_entry}">', f'<li class="active" id="{active_menu_entry}">')

    return content
