import enum

from app import db


class Result(enum.Enum):
    one = "one"
    two = "two"
    draw = "draw"
    ongoing = "ongoing"


class Base(db.Model):
    __abstract__ = True

    _id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, db.FetchedValue())
    updated_at = db.Column(db.DateTime, db.FetchedValue())

    @classmethod
    def save_from_dict(cls, data):
        if "_id" in data:
            model = cls.query.filter_by(_id=data["_id"]).first()
        else:
            model = cls()
            db.session.add(model)

        for attr in data.keys() & dir(model):
            setattr(model, attr, data[attr])

        db.session.commit()

        return model


class User(Base):
    ip = db.Column(db.String)
    country = db.Column(db.String)
    countryCode = db.Column(db.String)
    region = db.Column(db.String)
    regionName = db.Column(db.String)
    city = db.Column(db.String)
    zip = db.Column(db.String)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    timezone = db.Column(db.String)
    isp = db.Column(db.String)
    org = db.Column(db.String)
    _as = db.Column(db.String)


class Comment(Base):
    user_id = db.Column(db.Integer)
    body = db.Column(db.String, db.FetchedValue())
