SUMMARIZE = '''
Given a JSON, there may or may not be possible summarization in the values of the respective keys. 
Your task is to return a json that is summarized as you see fit. 
Give the output in the same json format as the question, just with the 
correct grammar inside it. While answering, make sure to return ONLY the json response
AND NOTHING ELSE.

INPUT TEXT:
{input_text}

'''

BRAINSTORM = '''
Given an input query, I want you to ideate a blog. Finally, I will give you a JSON 
and I want you to fit that blog components like title, body etc into the keys of the JSON.
Mind you, I will parsing the output in JSON format hence make sure to return ONLY the json response
AND NOTHING ELSE. Given below is an input query 

Input text : 
{input_text}

Example JSON that you have to use the structure of : 
{example_json}

'''

GRAMMAR = '''
Given a JSON, there may or may not be grammatical errors in the values of the respective keys. 
Your task is to return a json that is free of the grammatical errors. 
Give the output in the same json format as the question, just with the 
correct grammar inside it. While answering, make sure to return ONLY the json response
AND NOTHING ELSE.

{input_text}
'''

ENTRY_MAPPER = '''
Given the following Contentstack content model and a sample content entry, map the fields from the content model to the corresponding
fields in the content entry. Use the schema in the content model to define the structure, field types, and properties, ensuring that 
the output content entry aligns with the provided model structure. Generate a content entry with reasonable placeholder values if specific values are not provided.

{content_model}

Expected Content Entry Structure:

{{
    "title": "<Mapped or Placeholder Value>",
    "single_line": "hello world",
    "tags": ["<Sample Tag>"],
    "locale": "en-us",
    "uid": "<Generated or Placeholder UID>",
    "created_by": "<Placeholder User ID>",
    "updated_by": "<Placeholder User ID>",
    "created_at": "<Placeholder Date>",
    "updated_at": "<Placeholder Date>",
    "ACL": {{}},
    "_version": 1,
    "_in_progress": false,
    "publish_details": [
        {{
            "environment": "<Placeholder Environment>",
            "locale": "en-us",
            "time": "<Placeholder Publish Time>",
            "user": "<Placeholder User ID>",
            "version": 1
        }}
    ],
    "_rules": []
}}

Ensure that:

All mandatory fields are included and populated.
Field data types match the model definitions (e.g., text, number, boolean).
Constraints such as unique, mandatory, min, and max are respected.
Placeholder values are realistic and consistent with the expected data type and constraints.

Also, MAKE SURE THAT THE OUTPUT CONSIST ONLY OF JSON STRING, AS I AM GOING TO PARSE IT OUT
'''

TEMPLATE_RTE = '''
You are a creative AI assistant tasked with brainstorming ideas. You will receive input in the form of a JSON object representing a content-model structure. Your goal is to:
1. Parse the input JSON to extract the textual content and associated formatting styles.
2. Analyze the content to generate a detailed, well-structured response that aligns with the user's intent.
3. Format the response back into a similar JSON RTE structure, adhering to the following principles:
   - Ensure all text maintains its original styling (bold, italic, underline, etc.).
   - Represent your ideas in an organized manner (headings, lists, paragraphs, etc.).

Input JSON Format of content model:
{content_model}

The response JSON must maintain the structure while adapting the content. Here's an example of an output and have your idea around the `{query}` :
{{
    "uid": "<unique_id>",
    "type": "doc",
    "children": [
        {{
            "type": "h1",
            "uid": "<unique_id>",
            "attrs": {{ "style": {{}}, "redactor-attributes": {{}}, "dir": "ltr" }},
            "children": [
                {{
                    "text": "<suitable text>",
                    "bold": true
                }}
            ]
        }},
        {{
            "type": "p",
            "uid": "<unique_id>",
            "attrs": {{ "style": {{}}, "redactor-attributes": {{}}, "dir": "ltr" }},
            "children": [
                {{
                    "text": "<suitable text>"
                }}
            ]
        }},
        {{
            "type": "ul",
            "uid": "<unique_id>",
            "children": [
                {{
                    "type": "li",
                    "uid": "<unique_id>",
                    "attrs": {{ "style": {{}}, "redactor-attributes": {{}}, "dir": "ltr" }},
                    "children": [
                        {{
                            "text": "<suitable text>"
                        }}
                    ]
                }},
                {{
                    "type": "li",
                    "uid": "<unique_id>",
                    "attrs": {{ "style": {{}}, "redactor-attributes": {{}}, "dir": "ltr" }},
                    "children": [
                        {{
                            "text": "<suitable text>"
                        }}
                    ]
                }}
            ]
        }}
    ]
}}

Detailed Steps for LLM:
1. Parse the JSON to extract content and formatting.
2. Analyze and generate new ideas based on the context provided.
3. Structure the response in the specified JSON format, incorporating appropriate RTE styles for enhanced readability and organization.

**Important Instruction:** Only return the output JSON object as your response. Do not include any additional text or explanations.
'''

GENERATE_RTE = '''
You are a creative AI assistant tasked with brainstorming ideas. You will receive input in the form of a JSON object representing a json rte structure. Your goal is to:
1. Parse the input JSON to extract the textual content and associated formatting styles.
2. Analyze the content to generate a detailed, well-structured response that aligns with the user's intent.
3. Format the response back into a similar content entry structure, adhering to the following principles:
   - Ensure all text maintains its original styling (bold, italic, underline, etc.).
   - Represent your ideas in an organized manner (headings, lists, paragraphs, etc.).

Input JSON Format of json rte:
{json_rte}

The response JSON must maintain the structure while adapting the content. Here's an example of an output :
{{
    "title": "new test",
    "single_line": "hello world",
    "tags": [
        "new"
    ],
    "locale": "en-us",
    "uid": "blt1f712182b37273e4",
    "created_by": "bltba469db7b754532e",
    "updated_by": "bltad6636d068e74e50",
    "created_at": "2024-04-30T10:30:22.505Z",
    "updated_at": "2024-10-14T16:28:33.549Z",
    "ACL": {{}},
    "_version": 10,
    "_in_progress": false,
    "publish_details": [
        {{
            "environment": "blt6b176308263ebc15",
            "locale": "en-us",
            "time": "2024-04-30T10:32:00.646Z",
            "user": "bltba469db7b754532e",
            "version": 1
        }}
    ],
    "_rules": []
}}

Detailed Steps for LLM:
1. Parse the JSON to extract content and formatting.
2. Analyze and generate new ideas based on the context provided.
3. Structure the response in the specified JSON format, incorporating appropriate RTE styles for enhanced readability and organization.

**Important Instruction:** Only return the output JSON object as your response. Do not include any additional text or explanations.
'''

GENERATE_FROM_TEMPLATE_V1 = '''
You are a highly skilled assistant with expertise in generating structured JSON data from a given content type schema and producing Rich Text Editor (RTE) output in Contentstack-compatible JSON format.

Instructions:

Content Type Schema Input (To Be Provided by User):
I will provide you with a JSON definition of a content type schema. This schema will include multiple fields (text, reference, date, group, global fields, etc.). Your primary task is to generate content data (a JSON object) that aligns with the provided schema.

Important: The content type structure JSON will be provided in the conversation. Do not assume any default schema; rely only on what is given. The schema could be similar to the previously shown "Blog Landing Page" structure, but it might be different. Use the fields and structure as specified in the schema you receive.

RTE (Rich Text Editor) Field Handling:
If the provided schema includes fields that support a JSON RTE, you must produce that field's value as a structured JSON array following Contentstack's JSON RTE format. Your RTE content should demonstrate a variety of formatting, including:

Headings (e.g., h1, h2)
Bold and italic text
One or more paragraphs
A list (ordered or unordered) with multiple items
Below is a reference snippet for the RTE format. This is just an example—adapt your output to match the schema given:

[
  {{
    "type": "doc",
    "attrs": {{}},
    "uid": "unique_doc_id",
    "children": [
      {{
        "type": "h1",
        "attrs": {{}},
        "uid": "unique_heading_id",
        "children": [
          {{
            "text": "Example Heading"
          }}
        ]
      }},
      {{
        "type": "p",
        "attrs": {{}},
        "uid": "unique_paragraph_id",
        "children": [
          {{
            "text": "Some sample text with "
          }},
          {{
            "text": "bold",
            "attrs": {{
              "style": {{
                "font-weight": "bold"
              }}
            }}
          }},
          {{
            "text": " and "
          }},
          {{
            "text": "italic",
            "attrs": {{
              "style": {{
                "font-style": "italic"
              }}
            }}
          }},
          {{
            "text": " formatting."
          }}
        ]
      }}
    ]
  }}
]

Required Output:

After I provide the content type schema JSON, you should:
Generate a single JSON object that strictly follows the schema.
Populate all fields with realistic example values (e.g., text fields with meaningful strings, URLs for image/file fields, ISO-8601 date formats for date fields, etc.).
If reference fields are present, use placeholder UIDs for referenced entries.
If a date field exists, ensure it is in a valid ISO-8601 format.
If file/image fields exist, provide a plausible placeholder URL.
If boolean fields exist, provide a relevant boolean value.
For SEO or other metadata fields, include sensible placeholder meta titles, descriptions, keywords, and boolean flags as applicable.
General Requirements:

The final answer should be a single valid JSON object that strictly follows the provided schema (once I give it to you).
Maintain proper indentation and formatting.
The examples given above (like the blog landing page schema or the RTE snippet) are for reference only. You will adapt your final output based on the actual schema I provide.
Use unique uid values for RTE nodes.
Your Task:
When I provide a content type schema JSON in this conversation, you will use the instructions above to generate a well-structured, fully populated JSON entry that matches that schema, including properly formatted RTE content (if required by the schema).

Given below is an example of the content-type 
{content_type}

and this is the query 
{query}
SINCE THIS OUTPUT IS PARSED IN FRONTEND, GIVE THE OUTPUT IN JSON ONLY STARTING WITH {{ AND ENDING WITH }}
'''

MANUAL = '''
{
            "created_at": "2024-05-21T06:53:54.981Z",
            "updated_at": "2024-08-19T08:45:14.809Z",
            "title": "Adwait",
            "uid": "adwait",
            "_version": 5,
            "inbuilt_class": false,
            "schema": [
                {
                    "data_type": "text",
                    "display_name": "Title",
                    "field_metadata": {
                        "_default": true,
                        "version": 3
                    },
                    "mandatory": true,
                    "uid": "title",
                    "unique": true,
                    "multiple": false,
                    "non_localizable": false,
                    "min": 1,
                    "max": 50
                },
                {
                    "data_type": "text",
                    "display_name": "Multi Line Textbox",
                    "uid": "multi_line",
                    "field_metadata": {
                        "description": "",
                        "default_value": "",
                        "multiline": true,
                        "version": 3
                    },
                    "format": "",
                    "error_messages": {
                        "format": ""
                    },
                    "mandatory": false,
                    "multiple": false,
                    "non_localizable": false,
                    "unique": false
                }
            ],
            "last_activity": {},
            "maintain_revisions": true,
            "description": "",
            "DEFAULT_ACL": {
                "others": {
                    "read": false,
                    "create": false
                },
                "users": [
                    {
                        "uid": "blt6bcf0337a4f6e8f7",
                        "read": true,
                        "sub_acl": {
                            "read": true
                        }
                    }
                ]
            },
            "SYS_ACL": {
                "roles": [
                    {
                        "uid": "blt0b47d49d8e46ec0f",
                        "read": true,
                        "sub_acl": {
                            "create": true,
                            "read": true,
                            "update": true,
                            "delete": true,
                            "publish": true
                        },
                        "update": true,
                        "delete": true
                    },
                    {
                        "uid": "blt6ad7a8acd16a5a99",
                        "read": true,
                        "sub_acl": {
                            "create": true,
                            "read": true,
                            "update": true,
                            "delete": true,
                            "publish": true
                        }
                    },
                    {
                        "uid": "blt49c557406956107c",
                        "read": true,
                        "sub_acl": {
                            "create": true,
                            "read": true,
                            "update": true,
                            "delete": true,
                            "publish": true
                        },
                        "update": true,
                        "delete": true
                    }
                ],
                "others": {
                    "read": false,
                    "create": false,
                    "update": false,
                    "delete": false,
                    "sub_acl": {
                        "read": false,
                        "create": false,
                        "update": false,
                        "delete": false,
                        "publish": false
                    }
                }
            },
            "options": {
                "is_page": false,
                "singleton": true,
                "sub_title": [],
                "title": "title"
            },
            "abilities": {
                "get_one_object": true,
                "get_all_objects": true,
                "create_object": true,
                "update_object": true,
                "delete_object": true,
                "delete_all_objects": true
            },
            "extension_uids": []
        }


THIS IS AN EXAMPLE OF WHAT CONTENT MODEL IN CONTENTSTACK WOULD LOOK LIKE. GIVEN BELOW IS AN ENTRY FOR THE SAME 

{
        "title": "new test",
        "single_line": "hello world",
        "tags": [
            "new"
        ],
        "locale": "en-us",
        "uid": "blt1f712182b37273e4",
        "created_by": "bltba469db7b754532e",
        "updated_by": "bltad6636d068e74e50",
        "created_at": "2024-04-30T10:30:22.505Z",
        "updated_at": "2024-10-14T16:28:33.549Z",
        "ACL": {},
        "_version": 10,
        "_in_progress": false,
        "publish_details": [
            {
                "environment": "blt6b176308263ebc15",
                "locale": "en-us",
                "time": "2024-04-30T10:32:00.646Z",
                "user": "bltba469db7b754532e",
                "version": 1
            }
        ],
        "_rules": []
    }

TAKING THIS EXAMPLE AS A RESPONSE, CONVERT THE GIVEN BELOW JSON TO A SUITABLE ENTRY

{content_model}


GIVE THE DATA IN JSON FORMAT ONLY, AS I AM PARSING IT OUT
'''
