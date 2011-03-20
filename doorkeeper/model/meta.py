"""SQLAlchemy Metadata and Session object"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.schema import MetaData

__all__ = ['Base', 'Session', "metadata"]

# SQLAlchemy session manager. Updated by model.init_model()
Session = scoped_session(sessionmaker())

# The declarative Base
Base = declarative_base()

metadata = MetaData()
Base.metadata = metadata

# constants
# dk_system SS=>System Status
# config status
SS_SERVICE_NO_KEY       = "NOKEY"
SS_SERVICE_AVAIL        = "AVAILABLE"
SS_SERVICE_NOT_AVAIL    = "N/A"
#FIXME: not sure if running status is needed.

# system roles
ROLE_SYSADMIN   = "SYSADMIN"
ROLE_USER       = "USER"

