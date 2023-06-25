import logging

log_alert = logging.getLogger()
# Setting the threshold of logger to DEBUG
log_alert.setLevel(logging.DEBUG)


# Test messages
#     logger.debug("Harmless debug Message")
#     logger.info("Just an information")
#     logger.warning("Its a Warning")
#     logger.error("Did you try to divide by zero")
#     logger.critical("Internet is down")

def LogSetup():
    # Create and configure logger
    logging.basicConfig(filename="50_States_Pandas.log",
                        format='%(asctime)s %(message)s',
                        filemode="a")
