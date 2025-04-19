from marshmallow import Schema, fields, validate


class PublicationSchema(Schema):
    id = fields.Str(required=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    main_image_url = fields.Str(required=True)
    created_at = fields.DateTime(required=True)

    # Foreign keys
    author_id = fields.Str(required=True)
    company_id = fields.Str(required=True)

    # Relationships (nested schemas)
    author = fields.Nested("AuthorSchema", exclude=("publications",))
    company = fields.Nested("CompanySchema", exclude=("publications",))


class CompanySchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    image_url = fields.Str(required=True)

    # Relationships
    publications = fields.List(
        fields.Nested(PublicationSchema, exclude=("company",))
    )
    authors = fields.List(fields.Nested("AuthorSchema", exclude=("company",)))
    subscriptions = fields.List(
        fields.Nested("SubscriptionSchema", exclude=("company",))
    )


class UserBaseSchema(Schema):
    id = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    login = fields.Str(required=True)
    password = fields.Str(
        required=True, load_only=True
    )  # Пароль не должен возвращаться в ответах
    role = fields.Str(
        required=True, validate=validate.OneOf(["author", "moderator"])
    )


class AuthorSchema(UserBaseSchema):
    company_id = fields.Str(required=True)

    # Relationships
    company = fields.Nested(CompanySchema, exclude=("authors",))
    publications = fields.List(
        fields.Nested(PublicationSchema, exclude=("author",))
    )


class ModeratorSchema(UserBaseSchema):
    pass


class SubscriberSchema(Schema):
    id = fields.Int(required=True)
    telegram_id = fields.Str(required=True)

    # Relationships
    subscriptions = fields.List(
        fields.Nested("SubscriptionSchema", exclude=("subscriber",))
    )


class SubscriptionSchema(Schema):
    id = fields.Int(required=True)
    subscriber_id = fields.Int(required=True)
    company_id = fields.Str(required=True)

    # Relationships
    subscriber = fields.Nested(SubscriberSchema, exclude=("subscriptions",))
    company = fields.Nested(CompanySchema, exclude=("subscriptions",))
