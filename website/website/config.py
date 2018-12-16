class BaseConfig:
    """ 配置基类 """
    SECRET_KEY = 'makesure to set a very secret key'
    INDEX_PER_PAGE=50

class DevelopmentConfig(BaseConfig):
    """ 开发环境配置 """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='mysql://root:123456@mymysql/douban_movie'
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class ProductionConfig(BaseConfig):
    """ 生产环境配置 """
    pass


class TestingConfig(BaseConfig):
    """ 测试环境配置 """
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}


