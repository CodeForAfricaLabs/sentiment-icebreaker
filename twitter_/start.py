import tweepy
import logging
from logging.handlers import TimedRotatingFileHandler
from sentiment_icebreaker.twitter_ import listener


def get_logger():
    '''
    creates logger object

    :return type: <logging.Logger object>
    '''
    try:
        log_file = "logs/twitter-stream.log"
        logger = logging.getLogger(log_file)
        logger.setLevel(logging.DEBUG)
        handler = TimedRotatingFileHandler(log_file, 'midnight')
        formatter = logging.Formatter( "(asctime)s - %(name)s - %(levelname)s - %(message)s" )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    except Exception, err:
        print 'get_logger() fail - %s' % str(err)
        raise err


if __name__ == '__main__':
    logger = get_logger()
    logger.info("Initiating stream...")
    lstnr = listener.Listener(logger=logger)
    tweepy.Stream(listener.get_api(auth_only=True), lstnr).userstream()
    logger.info("Stream started.")
