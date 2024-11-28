BLOG_CONTENT_TYPE = {
    "content_type": {
        "created_at": "2024-11-28T12:22:50.661Z",
        "updated_at": "2024-11-28T12:23:56.886Z",
        "title": "Blog Landing Page",
        "uid": "blog_landing_page",
        "_version": 5,
        "inbuilt_class": False,
        "schema": [
            {
                "display_name": "Title",
                "uid": "title",
                "data_type": "text",
                "mandatory": True,
                "unique": True,
                "field_metadata": {
                    "_default": True,
                    "version": 3
                },
                "multiple": False,
                "non_localizable": False
            },
            {
                "display_name": "URL",
                "uid": "url",
                "data_type": "text",
                "mandatory": False,
                "field_metadata": {
                    "_default": True,
                    "version": 3
                },
                "multiple": False,
                "unique": False,
                "non_localizable": False
            },
            {
                "data_type": "isodate",
                "display_name": "Date",
                "uid": "date",
                "startDate": None,
                "endDate": None,
                "field_metadata": {
                    "description": "Optional field that overrides the publishing date.",
                    "default_value": {
                        "custom": False,
                        "date": "",
                        "time": ""
                    },
                    "date_range": False
                },
                "mandatory": False,
                "multiple": False,
                "unique": False,
                "non_localizable": False
            },
            {
                "data_type": "file",
                "display_name": "Featured Image",
                "uid": "featured_image",
                "field_metadata": {
                    "description": "",
                    "rich_text_type": "standard",
                    "image": True
                },
                "dimension": {
                    "width": {
                        "min": None,
                        "max": None
                    },
                    "height": {
                        "min": None,
                        "max": None
                    }
                },
                "multiple": False,
                "mandatory": True,
                "unique": False,
                "non_localizable": False
            },
            {
                "data_type": "json",
                "display_name": "Body",
                "uid": "body",
                "field_metadata": {
                    "allow_json_rte": True,
                    "embed_entry": False,
                    "description": "",
                    "default_value": "",
                    "multiline": False,
                    "rich_text_type": "advanced",
                    "options": []
                },
                "format": "",
                "error_messages": {
                    "format": ""
                },
                "reference_to": ["sys_assets"],
                "multiple": False,
                "non_localizable": False,
                "unique": False,
                "mandatory": False
            },
            {
                "data_type": "reference",
                "display_name": "Related Post",
                "reference_to": ["blog_landing_page"],
                "field_metadata": {
                    "ref_multiple": True,
                    "ref_multiple_content_types": True
                },
                "uid": "related_post",
                "mandatory": False,
                "multiple": False,
                "unique": False,
                "non_localizable": False
            },
            {
                "data_type": "boolean",
                "display_name": "Is Archived?",
                "uid": "is_archived",
                "field_metadata": {
                    "description": "",
                    "default_value": False
                },
                "multiple": False,
                "mandatory": False,
                "unique": False,
                "non_localizable": False
            },
            {
                "data_type": "group",
                "display_name": "Comments",
                "field_metadata": {
                    "description": "",
                    "instruction": ""
                },
                "schema": [
                    {
                        "data_type": "text",
                        "display_name": "Leave a Reply",
                        "uid": "comment",
                        "field_metadata": {
                            "description": "",
                            "default_value": "",
                            "multiline": True,
                            "version": 3
                        },
                        "format": "",
                        "error_messages": {
                            "format": ""
                        },
                        "mandatory": False,
                        "multiple": False,
                        "non_localizable": False,
                        "unique": False
                    },
                    {
                        "data_type": "link",
                        "display_name": "Call to Action",
                        "uid": "call_to_action",
                        "field_metadata": {
                            "description": "",
                            "default_value": {
                                "title": "",
                                "url": ""
                            }
                        },
                        "mandatory": False,
                        "multiple": False,
                        "non_localizable": False,
                        "unique": False
                    }
                ],
                "uid": "comments",
                "mandatory": False,
                "multiple": False,
                "non_localizable": False,
                "unique": False
            },
            {
                "data_type": "global_field",
                "display_name": "Social Share",
                "reference_to": "social_share",
                "field_metadata": {
                    "description": ""
                },
                "uid": "social_share",
                "mandatory": False,
                "multiple": False,
                "non_localizable": False,
                "unique": False,
                "schema": [
                    {
                        "data_type": "group",
                        "display_name": "Social Media Share",
                        "field_metadata": {
                            "description": "",
                            "instruction": ""
                        },
                        "schema": [
                            {
                                "data_type": "text",
                                "display_name": "Title",
                                "uid": "title",
                                "field_metadata": {
                                    "description": "",
                                    "default_value": "",
                                    "isTitle": True,
                                    "version": 3
                                },
                                "format": "",
                                "error_messages": {
                                    "format": ""
                                },
                                "mandatory": False,
                                "multiple": False,
                                "non_localizable": False,
                                "unique": False,
                                "indexed": False,
                                "inbuilt_model": False
                            },
                            {
                                "data_type": "file",
                                "display_name": "Icon",
                                "uid": "icon",
                                "extensions": [],
                                "field_metadata": {
                                    "description": "",
                                    "rich_text_type": "standard"
                                },
                                "mandatory": False,
                                "multiple": False,
                                "non_localizable": False,
                                "unique": False,
                                "indexed": False,
                                "inbuilt_model": False
                            },
                            {
                                "data_type": "link",
                                "display_name": "url",
                                "uid": "url",
                                "field_metadata": {
                                    "description": "",
                                    "default_value": {
                                        "title": "",
                                        "url": ""
                                    }
                                },
                                "mandatory": False,
                                "multiple": False,
                                "non_localizable": False,
                                "unique": False,
                                "indexed": False,
                                "inbuilt_model": False
                            }
                        ],
                        "uid": "social_media_share",
                        "mandatory": False,
                        "multiple": True,
                        "non_localizable": False,
                        "unique": False,
                        "indexed": False,
                        "inbuilt_model": False
                    }
                ]
            },
            {
                "data_type": "global_field",
                "display_name": "SEO",
                "reference_to": "seo",
                "field_metadata": {
                    "description": ""
                },
                "uid": "seo",
                "multiple": False,
                "mandatory": False,
                "unique": False,
                "non_localizable": False,
                "schema": [
                    {
                        "data_type": "text",
                        "display_name": "Meta Title",
                        "uid": "meta_title",
                        "field_metadata": {
                            "description": "",
                            "default_value": "",
                            "version": 3
                        },
                        "format": "",
                        "error_messages": {
                            "format": ""
                        },
                        "multiple": False,
                        "mandatory": False,
                        "unique": False,
                        "non_localizable": False,
                        "indexed": False,
                        "inbuilt_model": False
                    },
                    {
                        "data_type": "text",
                        "display_name": "Meta Description",
                        "uid": "meta_description",
                        "field_metadata": {
                            "description": "",
                            "default_value": "",
                            "multiline": True,
                            "version": 3
                        },
                        "format": "",
                        "error_messages": {
                            "format": ""
                        },
                        "multiple": False,
                        "mandatory": False,
                        "unique": False,
                        "non_localizable": False,
                        "indexed": False,
                        "inbuilt_model": False
                    },
                    {
                        "data_type": "text",
                        "display_name": "Meta Keywords",
                        "uid": "keywords",
                        "field_metadata": {
                            "description": "",
                            "default_value": "",
                            "version": 3
                        },
                        "format": "",
                        "error_messages": {
                            "format": ""
                        },
                        "multiple": False,
                        "mandatory": False,
                        "unique": False,
                        "non_localizable": False,
                        "indexed": False,
                        "inbuilt_model": False
                    },
                    {
                        "data_type": "boolean",
                        "display_name": "Enable Search Indexing",
                        "uid": "enable_search_indexing",
                        "field_metadata": {
                            "description": "",
                            "default_value": True
                        },
                        "multiple": False,
                        "mandatory": False,
                        "unique": False,
                        "non_localizable": False,
                        "indexed": False,
                        "inbuilt_model": False
                    }
                ]
            }
        ],
        "maintain_revisions": True,
        "description": "Allows to design a landing page to display your blog content including entire blog posts, author details, blog release date and time, and related posts."
    }
}

RTE_CONTENT = {
    "uid": "maximizing_sales_winter_airbnb",
    "type": "doc",
    "children": [
        {
            "type": "h1",
            "uid": "title_1",
            "attrs": { "style": {}, "redactor-attributes": {}, "dir": "ltr" },
            "children": [
                {
                    "text": "<some-text>",
                    "bold": True
                }
            ]
        },
        {
            "type": "p",
            "uid": "intro_1",
            "attrs": { "style": {}, "redactor-attributes": {}, "dir": "ltr" },
            "children": [
                {
                    "text": "<some-text>"
                }
            ]
        },
        {
            "type": "ul",
            "uid": "list_1",
            "children": [
                {
                    "type": "li",
                    "uid": "list_item_1",
                    "attrs": { "style": {}, "redactor-attributes": {}, "dir": "ltr" },
                    "children": [
                        {
                            "text": "<some-text>"
                        }
                    ]
                },
                {
                    "type": "li",
                    "uid": "list_item_2",
                    "attrs": { "style": {}, "redactor-attributes": {}, "dir": "ltr" },
                    "children": [
                        {
                            "text": "<some-text>"
                        }
                    ]
                },
                {
                    "type": "li",
                    "uid": "list_item_3",
                    "attrs": { "style": {}, "redactor-attributes": {}, "dir": "ltr" },
                    "children": [
                        {
                            "text": "<some-text>"
                        }
                    ]
                },
                {
                    "type": "li",
                    "uid": "list_item_4",
                    "attrs": { "style": {}, "redactor-attributes": {}, "dir": "ltr" },
                    "children": [
                        {
                            "text": "<some-text>"
                        }
                    ]
                }
            ]
        },
        {
            "type": "p",
            "uid": "conclusion_1",
            "attrs": { "style": {}, "redactor-attributes": {}, "dir": "ltr" },
            "children": [
                {
                    "text": "<some-text>"
                }
            ]
        }
    ]
}