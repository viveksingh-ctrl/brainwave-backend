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
You are a highly skilled assistant proficient in converting an entire content type schema into a single, cohesive RTE (Rich Text Editor) JSON output that must be compatible with Slate.js. The final output should look like a fully rendered, realistic webpage, integrating all fields defined in the given content type schema into one unified RTE structure. The RTE output must follow the provided RTE format guidelines and also be structured so that it can be interpreted by Slate.js-based editors.

Instructions:

Content Type Schema (To Be Provided by User):
I will give you a content type schema containing various fields (e.g., title, date, featured image, body, related posts, comments, social share, SEO fields, etc.). You must read the schema and convert all these fields into a single JSON RTE array.

Unified RTE Structure:

Do not produce a traditional JSON object with separate fields.
Combine all fields into one continuous RTE JSON structure that presents a fully realized webpage.
For example:
The title field should appear as an h1 heading.
The date might be an h2 or a paragraph below the title.
The featured image could be an image node (if supported) or a paragraph containing the image URL.
The body should appear as multiple paragraphs, possibly additional headings (h2, h3), bold and italic text inline, and maybe a list.
Related posts can appear as a list of links at the end.
Comments could appear as a comments section, maybe a heading with paragraphs or a representation of a form.
Social share might appear as a set of links or icons at the bottom.
SEO fields—usually hidden—should still be included, perhaps as a final paragraph mentioning meta info or keywords.
The result should feel like a coherent, narrative webpage that weaves all fields into one reading experience.

RTE Format & Slate.js Compatibility:

The final output must be a single JSON array starting with a doc node.
Each node should have:
A type field (e.g., "doc", "h1", "p", "ul", "li", "img", etc.).
An attrs object (even if empty).
A uid field with a unique identifier.
A children array, which can contain text nodes (with "text") or other elements.
Include various formatting features:
Headings (h1 for title, possibly h2/h3 for sections)
Bold and italic text inline
At least one list (ul or ol) with multiple items.
Ensure the structure is compatible with Slate.js.
For instance, maintain a hierarchical node structure that Slate can interpret, and keep formatting attributes on text nodes.
Realistic and Detailed Content:

Do not produce short, placeholder text.
Make the content read as if it's a genuine webpage: descriptive headings, meaningful paragraphs, contextually relevant formatting, and logically placed lists.
The final narrative should feel like a natural webpage derived from the schema rather than dummy data.
No Additional Output:

The final answer should contain only the RTE JSON array.
Do not include the schema or any explanations in the final output—just the constructed RTE JSON.
Strictness:

Follow these instructions exactly.
The final RTE should resemble a webpage that Slate.js can interpret, incorporating all fields from the schema in a cohesive manner.
Example RTE Snippet (For Reference Only):

{{
    "_id": "6748e6ce8f3808b2ee51b4b8",
    "author": "Meet Makwana",
    "document": [
        {{
            "children": [
                {{
                    "attrs": {{
                        "dir": "ltr",
                        "redactor-attributes": {{
                        }},
                        "style": {{
                        }}
                    }},
                    "children": [
                        {{
                            "bold": true,
                            "text": "Exploring the World of Content Management Systems."
                        }}
                    ],
                    "type": "h1",
                    "uid": "title_uid"
                }},
                {{
                    "attrs": {{
                        "dir": "ltr",
                        "redactor-attributes": {{
                        }},
                        "style": {{
                        }}
                    }},
                    "children": [
                        {{
                            "text": ""
                        }}
                    ],
                    "type": "p",
                    "uid": "intro_uid"
                }},
                {{
                    "attrs": {{
                        "dir": "ltr",
                        "redactor-attributes": {{
                        }},
                        "style": {{
                        }}
                    }},
                    "children": [
                        {{
                            "text": "In today’s digital era, managing content efficiently has become a cornerstone of successful online strategies. Content Management Systems (CMS) are at the heart of this transformation, enabling individuals and organizations to create, organize, and publish content seamlessly. Whether you’re running a personal blog, a large e-commerce site, or a corporate website, a CMS can revolutionize how you manage and distribute content."
                        }}
                    ],
                    "type": "p",
                    "uid": "61f66e505a604b2bacede204366b3cf2"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": ""
                        }}
                    ],
                    "type": "p",
                    "uid": "5d113c287f014de0871cbcda5e2ceaf1"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "What is a CMS?"
                        }}
                    ],
                    "type": "h2",
                    "uid": "9a9656d11c154d8e9e49808610a499c1"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": ""
                        }}
                    ],
                    "type": "p",
                    "uid": "3fbf34c4555b4c7c87a84b70d5c7b47b"
                }},
                {{
                    "attrs": {{
                        "dir": "ltr",
                        "redactor-attributes": {{
                        }},
                        "style": {{
                        }}
                    }},
                    "children": [
                        {{
                            "text": "At its core, a CMS is software that allows users to create, modify, and manage digital content without requiring deep technical knowledge or coding skills. It provides a user-friendly interface that simplifies content creation and enables collaboration, making it a must-have tool for modern businesses."
                        }}
                    ],
                    "type": "p",
                    "uid": "d505666e451b43f89e8e0b8976db5281"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "Some of the most popular CMS platforms include "
                        }},
                        {{
                            "bold": true,
                            "text": "WordPress"
                        }},
                        {{
                            "text": ", "
                        }},
                        {{
                            "bold": true,
                            "text": "Drupal"
                        }},
                        {{
                            "text": ", "
                        }},
                        {{
                            "bold": true,
                            "text": "Joomla"
                        }},
                        {{
                            "text": ", and "
                        }},
                        {{
                            "bold": true,
                            "text": "Shopify"
                        }},
                        {{
                            "text": ", each catering to different needs and industries."
                        }}
                    ],
                    "type": "p",
                    "uid": "dbd7e1712f184e0ca08ab8bac6370af0"
                }},
                {{
                    "attrs": {{
                        "dir": "ltr",
                        "dirty": true,
                        "redactor-attributes": {{
                        }},
                        "style": {{
                        }}
                    }},
                    "children": [
                        {{
                            "text": ""
                        }}
                    ],
                    "type": "p",
                    "uid": "e0f72493d49f40cf927fa2a1eb335160"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": ""
                        }}
                    ],
                    "type": "p",
                    "uid": "133bc96d2ddf4ad58792e2350e5fa625"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "Key Features of a CMS"
                        }}
                    ],
                    "type": "h2",
                    "uid": "856ba508e18e4584b8ca7633a30ebef0"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": ""
                        }}
                    ],
                    "type": "p",
                    "uid": "7516615501514c509357780c2b8557b2"
                }},
                {{
                    "attrs": {{
                        "dir": "ltr",
                        "redactor-attributes": {{
                        }},
                        "style": {{
                        }}
                    }},
                    "children": [
                        {{
                            "text": "A good CMS brings a plethora of features to the table, streamlining content management and enhancing user experience."
                        }}
                    ],
                    "type": "p",
                    "uid": "1254b00cb04b406f95a5b8366b70423f"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "1. "
                        }},
                        {{
                            "bold": true,
                            "text": "User-Friendly Interface"
                        }}
                    ],
                    "type": "h3",
                    "uid": "bdfbc6ded5db438ba81a508429343239"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "A CMS simplifies content management with an intuitive interface that enables users to create, edit, and manage content effortlessly. You don’t need to be a developer to upload images, add text, or update product details."
                        }}
                    ],
                    "type": "p",
                    "uid": "7fc192a2141b49e8a7f8f7126b74a8c5"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "2. "
                        }},
                        {{
                            "bold": true,
                            "text": "SEO Optimization"
                        }}
                    ],
                    "type": "h3",
                    "uid": "f94f321e88bd4957b70d8ac7341b954b"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "Most CMS platforms come equipped with built-in SEO tools, helping users optimize their content for search engines. Features like meta tags, keyword analysis, and XML sitemap generation make it easier to improve website visibility and rankings."
                        }}
                    ],
                    "type": "p",
                    "uid": "f12ecb93018649f7bc444371170d4058"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "3. "
                        }},
                        {{
                            "bold": true,
                            "text": "Customization Options"
                        }}
                    ],
                    "type": "h3",
                    "uid": "a9b20402f8b1414d82a4631bb814a7fe"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "CMS platforms offer a wide range of customization possibilities. From choosing themes and layouts to integrating third-party plugins, you can tailor your website to reflect your brand’s unique identity and requirements."
                        }}
                    ],
                    "type": "p",
                    "uid": "e988dae2f2404e7e84a4701b1a4782dd"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "4. "
                        }},
                        {{
                            "bold": true,
                            "text": "Scalability"
                        }}
                    ],
                    "type": "h3",
                    "uid": "5291e33b699b4364ade6466d99f2c557"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "As your business grows, your CMS can scale to meet increased demands. Whether it’s handling more traffic, managing extensive content libraries, or adding new functionalities, modern CMS platforms are built to adapt and evolve."
                        }}
                    ],
                    "type": "p",
                    "uid": "3d49392f8d7147f9aacbc9334229bca7"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "5. "
                        }},
                        {{
                            "bold": true,
                            "text": "Integration Capabilities"
                        }}
                    ],
                    "type": "h3",
                    "uid": "fcbcdf5c816c42508911aca8f9bce4c4"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "A CMS often acts as the central hub of your digital ecosystem. It integrates seamlessly with tools like "
                        }},
                        {{
                            "bold": true,
                            "text": "Customer Relationship Management (CRM) systems"
                        }},
                        {{
                            "text": ", "
                        }},
                        {{
                            "bold": true,
                            "text": "email marketing platforms"
                        }},
                        {{
                            "text": ", and "
                        }},
                        {{
                            "bold": true,
                            "text": "analytics tools"
                        }},
                        {{
                            "text": ", providing a cohesive and streamlined workflow."
                        }}
                    ],
                    "type": "p",
                    "uid": "9d8953652e614162bbb59b9b4e52bbee"
                }},
                {{
                    "attrs": {{
                        "dir": "ltr",
                        "dirty": true,
                        "redactor-attributes": {{
                        }},
                        "style": {{
                        }}
                    }},
                    "children": [
                        {{
                            "text": ""
                        }}
                    ],
                    "type": "p",
                    "uid": "ea809a3d5d254c268451365132a27eae"
                }},
                {{
                    "attrs": {{
                        "dir": "ltr",
                        "redactor-attributes": {{
                        }},
                        "style": {{
                        }}
                    }},
                    "children": [
                        {{
                            "bold": true,
                            "text": ""
                        }}
                    ],
                    "type": "h2",
                    "uid": "usage_subheading_uid"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "Real-World Usage Scenarios"
                        }}
                    ],
                    "type": "h2",
                    "uid": "078744346e344102b8fd040fd12098f2"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "The versatility of CMS platforms makes them a valuable asset across various industries."
                        }}
                    ],
                    "type": "p",
                    "uid": "bab2d43f1aa249c385d53eff7d39facd"
                }},
                {{
                    "attrs": {{
                        "dir": "ltr",
                        "dirty": true,
                        "redactor-attributes": {{
                        }},
                        "style": {{
                        }}
                    }},
                    "children": [
                        {{
                            "text": "1. E-Commerce"
                        }}
                    ],
                    "type": "h3",
                    "uid": "a0d5e4d38ccd445d94761aa8d490aba7"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "For e-commerce businesses, a CMS simplifies managing thousands of product pages. Platforms like "
                        }},
                        {{
                            "bold": true,
                            "text": "Shopify"
                        }},
                        {{
                            "text": " and "
                        }},
                        {{
                            "bold": true,
                            "text": "Magento"
                        }},
                        {{
                            "text": " enable product catalog management, payment gateway integrations, and real-time inventory tracking, creating a seamless shopping experience."
                        }}
                    ],
                    "type": "p",
                    "uid": "8817f2a48614424ab925cf739f4be8d1"
                }},
                {{
                    "attrs": {{
                        "dir": "ltr",
                        "dirty": true,
                        "redactor-attributes": {{
                        }},
                        "style": {{
                        }}
                    }},
                    "children": [
                        {{
                            "text": "2. Education"
                        }}
                    ],
                    "type": "h3",
                    "uid": "97e164a67c8e4b248e36be8989e4e59c"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": "Educational institutions use CMS platforms to share course materials, event updates, and research papers. Platforms like "
                        }},
                        {{
                            "bold": true,
                            "text": "Moodle"
                        }},
                        {{
                            "text": " and "
                        }},
                        {{
                            "bold": true,
                            "text": "Canvas"
                        }},
                        {{
                            "text": " specialize in creating a collaborative learning environment."
                        }}
                    ],
                    "type": "p",
                    "uid": "47805cf82a684e869b2c55c48aa82cb4"
                }},
                {{
                    "attrs": {{
                        "dirty": true
                    }},
                    "children": [
                        {{
                            "text": ""
                        }}
                    ],
                    "type": "p",
                    "uid": "8f77b214356c4ab1a1cd691050a56679"
                }},
                {{
                    "attrs": {{
                        "dir": "ltr",
                        "dirty": true,
                        "redactor-attributes": {{
                        }},
                        "style": {{
                        }}
                    }},
                    "children": [
                        {{
                            "text": ""
                        }}
                    ],
                    "type": "p",
                    "uid": "c06bdecff3754cf8af130d5ab0120ab6"
                }}
            ],
            "type": "doc",
            "uid": "7i0hz6g308v"
        }}
    ],
    "last_updated": "2024-12-07 18:00:28.281023",
    "title": "Exploring the World of Content Management Systems",
    "uid": "csnSCPz1EMb3T8SZ"
}}
Use the above snippet as a structural guide only. Your final output should be more extensive, reflect the entire schema, and feature realistic, narrative content.

Your Task: When I provide the content type schema, produce one single RTE JSON array representing the entire webpage. Incorporate all fields as described, ensure Slate.js compatibility, and output nothing else.
Given below is the content-type whose fields needs to be included strictly with realistic and long content in each field
{content_type}

and this is the query 
{query}

VERY IMPORTANT NOTE : 
ALL BELOW INSTRUCTIONS SHOUL BE FOLLOWED STRICTLY
AND THE OUTPUT SHOULD NOT GIVE SLATE JS INCOMPATIBLE ERROR ADD attrs WHEREVER NECESSARY TO AVOID THIS ERROR
AND I SOULD NOT SEE ANY BROKEN IMAGES OR ASSETS, USE ALL FIELDS FROM CONTENT TYPE SKIP NONE STRICTLY
AND NO TEXT OTHER THAN THE COMPLETE JSON AS OUTPUT IS THE MOST IMPORTANT THING AND GENERATE REALISTIC CONTENT FOR EACH FIELD AND TEXT CONTENT SHOULD BE BIG ENOUGH
SINCE THIS OUTPUT IS PARSED IN FRONTEND, 
GIVE THE OUTPUT IN JSON ONLY STARTING WITH {{ AND ENDING WITH }} NOTHING ELSE NO TEXT NOTHING WRITTEN EXPECT THE JSON
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
