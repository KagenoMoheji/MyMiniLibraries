

def func_warn(name, get_logger = None):
    logger = None
    if get_logger is not None:
        logger = get_logger(__name__)

    if logger is not None:
        logger.info("Run func_warn.")

    msg = "{} is dangerous.".format(name)
    print(msg)
    if logger is not None:
        logger.warn(msg)


def func_error(name, get_logger = None):
    logger = None
    if get_logger is not None:
        logger = get_logger(__name__)
    
    if logger is not None:
        logger.info("Run func_error.")
    
    msg = "Attacked by {}.".format(name)
    print(msg)
    if logger is not None:
        logger.error(msg)
