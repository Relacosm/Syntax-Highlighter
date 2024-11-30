import sys
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def syntax_highlighter(code, language, theme='colorful'):
    try:
        # Get the lexer for the specified language
        lexer = get_lexer_by_name(language)
    except Exception as e:
        print(f"Error: {e}")
        return

    # Create a formatter with the selected theme
    formatter = HtmlFormatter(style=theme)

    # Highlight the code
    highlighted_code = highlight(code, lexer, formatter)

    # Generate the final HTML
    full_html = f"""
    <html>
    <head>
        <title>Highlighted Code</title>
        <style>{formatter.get_style_defs()}</style>
    </head>
    <body>
        <h2>Highlighted Code in {language}:</h2>
        <div class="highlight">{highlighted_code}</div>
    </body>
    </html>
    """
    return full_html

if __name__ == "__main__":
    # Example usage: Customize these variables as needed
    code_snippet = """
def hello_world():
    print("Hello, World!")
"""
    language = "python"  # Specify the programming language
    theme = "colorful"    # Specify the theme (changeable)

    # Generate highlighted HTML
    html_output = syntax_highlighter(code_snippet, language, theme)

    if html_output:
        with open("highlighted_code.html", "w") as f:
            f.write(html_output)
        print("HTML file generated: highlighted_code.html")