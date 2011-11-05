from os.path import join, dirname, normpath

# Used to provide absolute paths.  Normally the default is fine.
LOCAL_PATH = normpath(join(dirname(__file__), '..'))

# These are the hostnames as returned by platform.node().
# If you aren't sure what to put, leave them blank and the error message should tell you which hostname Python sees.
DEVELOPMENT_HOST = 'quinella.local'
PRODUCTION_HOST = 'pealco.net'