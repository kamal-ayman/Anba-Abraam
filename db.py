from peewee import *

db = MySQLDatabase('anbaabram', user='root', password='toor', host='127.0.0.1', port=3306)


# -- Users -- #
class Users(Model):
    UserName = CharField(null=False, unique=True)
    Password = CharField(null=False)
    Email = CharField(null=True)

    class Meta:
        database = db


# ----------------------------------------------


class NumFamily(Model):
    NumberFamily = CharField(null=False, unique=True)

    class Meta:
        database = db


class FatherOfConfession(Model):
    FatherOfConfession = CharField(null=True, unique=True)

    class Meta:
        database = db


# ----------------------------------------------


# -- Wife -- #
class WifeData(Model):
    WifeName = CharField(null=True)
    WifeNikeName = CharField(null=True)
    WifeNationalId = CharField(null=True, unique=True)
    WifeWork = CharField(null=True)
    WifeMoney = CharField(null=True)
    WifePhoneNumber = CharField(null=True)
    WifeFatherOfConfession = ForeignKeyField(FatherOfConfession, backref="FatherOfConfession", null=True)
    NumberFamily = ForeignKeyField(NumFamily, backref="NumberFamily", null=True, unique=True)

    class Meta:
        database = db


class HusbandData(Model):
    HusbandName = CharField(null=True)
    HusbandNikeName = CharField(null=True)
    HusbandNationalId = CharField(null=True, unique=True)
    HusbandWork = CharField(null=True)
    HusbandMoney = CharField(null=True)
    HusbandPhoneNumber = CharField(null=True)
    HusbandFatherOfConfession = ForeignKeyField(FatherOfConfession, backref="FatherOfConfession", null=True)
    NumberFamily = ForeignKeyField(NumFamily, backref="NumberFamily", null=True, unique=True)

    class Meta:
        database = db


class Information(Model):
    DetailedAddress = CharField(null=False)
    Governorate = CharField(null=False)
    neighborhood = CharField(null=False)
    Region = CharField(null=False)
    SpecialMarque = CharField(null=True)
    Living = CharField(null=False)
    ChurchName = CharField(null=False)
    Address = CharField(null=False)
    Phone1 = CharField(null=True)
    Phone2 = CharField(null=True)

    class Meta:
        database = db


class Children(Model):
    ChildrenName = CharField(null=False)
    ChildrenNationalId = CharField(null=False, unique=True)
    ChildrenSocialStatus = CharField(null=False)
    ChildrenSchoolWork = CharField(null=False)
    ChildrenMonthlyIncome = CharField(null=True)
    ChildrenFatherOfConfession = ForeignKeyField(FatherOfConfession, backref="FatherOfConfession", null=True)

    class Meta:
        database = db


class AnotherHuman(Model):
    HumanName = CharField(null=False)
    HumanNationalId = CharField(null=False, unique=True)
    HumanRelativeRelation = CharField(null=False)
    HumanSocialStatus = CharField(null=False)
    HumanSchoolWork = CharField(null=False)
    HumanMonthlyIncome = CharField(null=True)
    HumanFatherOfConfession = ForeignKeyField(FatherOfConfession, backref="FatherOfConfession", null=True)

    class Meta:
        database = db


class HomeContents(Model):
    HomeContentsName = CharField(null=False)
    HomeContentsNumber = CharField(null=False)

    class Meta:
        database = db


class AnotherInfoFamily(Model):
    Diseases = CharField(null=True)
    Obstruction = CharField(null=True)
    OtherCircumstances = CharField(null=True)

    class Meta:
        database = db


class PrimarySourcesOfIncome(Model):
    SourceOfIncome = CharField(null=False)
    MonthlyIncome = CharField(null=False)

    class Meta:
        database = db


class ChurchesAidAndGoods(Model):
    MonthlyMaterialAssistance = CharField(null=True)
    CurativeHelp = CharField(null=True)
    MonthlyGood = CharField(null=True)
    OtherAid = CharField(null=True)
    Others = CharField(null=True)

    class Meta:
        database = db


db.connect()
db.create_tables([Users, NumFamily, FatherOfConfession, WifeData, HusbandData, Information, Children, AnotherHuman, HomeContents, AnotherInfoFamily, PrimarySourcesOfIncome, ChurchesAidAndGoods])
