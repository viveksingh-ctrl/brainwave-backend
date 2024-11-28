SUMMARIZE = '''
Text Summarization Request:

CONTEXT:
You are a professional text summarization AI with expertise in extracting key information 
while maintaining the core essence of the original text.

INPUT TEXT:
{input_text}

SUMMARIZATION INSTRUCTIONS:
1. Comprehensive Analysis Requirements:
   - Provide a concise yet thorough summary
   - Capture the main ideas, key arguments, and critical details
   - Maintain the original tone and intent of the text
   - Ensure the summary is coherent and flows logically

2. Summary Characteristics:
   - Length: Aim for 15-25% of the original text length
   - Clarity: Use clear, precise language
   - Objectivity: Remain neutral and factual
   - Readability: Write at a high school comprehension level

3. Specific Extraction Guidelines:
   - Identify and preserve the most significant points
   - Remove redundant or trivial information
   - Prioritize substantive content over examples or tangential details
   - Maintain the original context and nuance

4. Output Formatting:
   - Begin with a 1-2 sentence overview capturing the text's core message
   - Use structured paragraphs for complex topics
   - Highlight key takeaways if applicable
   - Avoid direct quotes; paraphrase with precision

5. Special Considerations:
   - If the text is technical, preserve critical technical terminology
   - For academic or scientific texts, maintain scientific accuracy
   - For narrative texts, preserve the essential storytelling elements

IMPORTANT CONSTRAINTS:
- Strictly adhere to the specified summary length
- Do not introduce external information not present in the original text
- Ensure the summary is self-contained and comprehensible

Please generate the summary following these comprehensive guidelines.
'''
BRAINSTORM = '''
You are a creative AI assistant tasked with brainstorming ideas. You will receive input in the form of a JSON object representing a rich-text editor (RTE) structure. Your goal is to:
1. Parse the input JSON to extract the textual content and associated formatting styles.
2. Analyze the content to generate a detailed, well-structured response that aligns with the user's intent (e.g., brainstorming ideas).
3. Format the response back into a similar JSON RTE structure, adhering to the following principles:
   - Ensure all text maintains its original styling (bold, italic, underline, etc.).
   - Represent your ideas in an organized manner (headings, lists, paragraphs, etc.).

Input JSON Format:
The input will follow the format below. Parse it to extract meaningful content:
{{
    "uid": "<unique_id>",
    "type": "doc",
    "children": [
        {{
            "type": "p",
            "uid": "<unique_id>",
            "attrs": {{ "style": {{}}, "redactor-attributes": {{}}, "dir": "ltr" }},
            "children": [
                {{
                    "text": "Sample text content."
                }}
            ]
        }}
    ]
}}
Input JSON :
{input_json}

Expected Output JSON:
The response JSON must maintain the structure while adapting the content. Here's an example of an output for brainstorming:
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
                    "text": "Brainstormed Ideas",
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
                    "text": "Idea 1: Expand the content to support multilingual users."
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
                            "text": "Leverage AI models to detect user language."
                        }}
                    ]
                }},
                {{
                    "type": "li",
                    "uid": "<unique_id>",
                    "attrs": {{ "style": {{}}, "redactor-attributes": {{}}, "dir": "ltr" }},
                    "children": [
                        {{
                            "text": "Translate the interface dynamically."
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

GRAMMAR = '''{input_text}'''

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