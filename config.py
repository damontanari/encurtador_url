SECRET_KEY = 'd@mont'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'postgres',
        usuario = 'cuqxqoai',
        senha = '74r06cw2r_oFJSJIrza5OSXAjNk5E9CR',
        servidor = 'motty.db.elephantsql.com',
        database = 'cuqxqoai'
    )
