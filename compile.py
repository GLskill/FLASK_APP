import sass
import os

# Path to styles.scss
scss_file = 'styles.scss'
css_file = os.path.join('static', 'styles.css')
# Compile to SCSS in CSS
css = sass.compile(filename=scss_file)

# save result
with open(css_file, 'w') as f:
    f.write(css)

print("Compile is ready")
