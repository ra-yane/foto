from foto.core import logger
from foto import create_app

app = create_app()

if __name__ == '__main__':
    logger.info('Starting foto API ...')
    app.run(host='0.0.0.0', port=5000, threaded=True)
    logger.info('End of foto')
