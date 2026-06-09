import re

with open('site/css/style.css', 'r') as f:
    css = f.read()

# 1. Fix iOS Auto-Zoom on inputs (16px)
target = """    input,
    select,
    textarea {
      font-family: 'DM Sans', sans-serif;
      font-size: 14px;"""
      
replacement = """    input,
    select,
    textarea {
      font-family: 'DM Sans', sans-serif;
      font-size: 16px;"""
      
css = css.replace(target, replacement)

# 2. Fix Tap Targets for language selector
target2 = ".lang-sel-mob a { font-size: 13px; color: var(--white); text-decoration: none; opacity: 0.5; font-weight: 500; padding: 4px 6px; border-radius: 4px; }"
replacement2 = ".lang-sel-mob a { font-size: 14px; color: var(--white); text-decoration: none; opacity: 0.5; font-weight: 500; padding: 12px 14px; border-radius: 8px; margin: 0 -4px; }"

css = css.replace(target2, replacement2)

target3 = ".lang-sel-mob { display: flex; align-items: center; gap: 6px; }"
replacement3 = ".lang-sel-mob { display: flex; align-items: center; gap: 8px; }"
css = css.replace(target3, replacement3)

# 3. Disable hover effects on mobile
hover_blocks = [
    """    nav a:hover {
      color: var(--white)
    }""",
    """    .nav-btn:hover {
      background: var(--teal)
    }""",
    """    .btn-p:hover {
      background: var(--teal)
    }""",
    """    .btn-g:hover {
      background: rgba(255, 255, 255, .1);
      border-color: rgba(255, 255, 255, .4)
    }""",
    """    .opt-check:not(.opt-disabled):hover .oci {
      border-color: var(--teal)
    }""",
    """    .f-sub:hover {
      background: var(--teal)
    }""",
    """    .flinks a:hover {
      color: var(--white)
    }"""
]

for block in hover_blocks:
    wrapped = f"    @media (hover: hover) {{\n{block}\n    }}"
    css = css.replace(block, wrapped)

with open('site/css/style.css', 'w') as f:
    f.write(css)

print("CSS UX fixes applied successfully.")
