from . import group_setup, start, browser, free_rooms, debug, save_and_group, my_group, language, chat_log

routers = [
    group_setup.router,
    start.router,
    browser.router,
    free_rooms.router,
    debug.router,
    save_and_group.router,
    my_group.router,
    language.router,
    chat_log.router,
]
