from flask import jsonify


def get_swagger_spec():
    return {
        "openapi": "3.0.3",
        "info": {
            "title": "Simple Interest Calculator API",
            "version": "1.0.0",
            "description": "API to calculate simple interest from principal, rate, and time.",
        },
        "paths": {
            "/simple-interest": {
                "post": {
                    "summary": "Calculate simple interest",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "principal": {"type": "number"},
                                        "rate": {"type": "number"},
                                        "time": {"type": "number"},
                                    },
                                    "required": ["principal", "rate", "time"],
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Successful simple interest calculation",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "principal": {"type": "number"},
                                            "rate": {"type": "number"},
                                            "time": {"type": "number"},
                                            "simple_interest": {"type": "number"},
                                        }
                                    }
                                }
                            }
                        },
                        "400": {
                            "description": "Invalid request payload",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "error": {"type": "string"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


def swagger_ui_html(swagger_spec_url: str) -> str:
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Simple Interest Calculator API Docs</title>
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@4/swagger-ui.css" />
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist@4/swagger-ui-bundle.js"></script>
  <script>
    const ui = SwaggerUIBundle({
      url: '%s',
      dom_id: '#swagger-ui',
    });
  </script>
</body>
</html>
""" % swagger_spec_url
